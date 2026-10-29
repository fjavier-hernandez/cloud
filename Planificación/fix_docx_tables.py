#!/usr/bin/env python3
"""Ajusta tablas de un .docx ya generado por pandoc.

- Ninguna fila se parte entre páginas (w:cantSplit).
- La primera fila se repite como cabecera (w:tblHeader).
- Si la tabla tiene pocas filas, se procura mantenerla junta (keepNext),
  salvo el último párrafo, para que un título no se quede solo y una tabla
  corta no empiece al final de la página. Las tablas largas sí pueden
  pasar de página, con la cabecera repetida y las filas enteras.
- Algunos tipos de tabla, reconocidos por su cabecera, reciben anchos de
  columna fijos (COLUMN_WIDTHS) para que los títulos estrechos no se partan
  letra a letra y la columna con más texto sea la ancha.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
# Tablas de hasta este número de filas se intentan mantener en la misma página.
MAX_ROWS_KEEP_TOGETHER = 8

# Anchos por tipo de tabla, en porcentaje del ancho de texto.
# Clave: textos de la cabecera, en orden; valor: porcentaje de cada columna.
COLUMN_WIDTHS: dict[tuple[str, ...], tuple[int, ...]] = {
    # Resultados de aprendizaje (apartado 3).
    ("Código", "Descripción (literal)", "Peso"): (12, 76, 12),
    # Reparto de las 72 h (apartado 9).
    ("Bloque", "Horas", "Resultados de aprendizaje", "Periodo", "Instrumentos"): (18, 10, 18, 26, 28),
    # Cálculo del 28 % (apartado 12).
    ("Concepto", "Cálculo", "Horas"): (32, 52, 16),
    # Catálogo de refuerzo (apartado 12).
    ("Resultado de aprendizaje", "Actividades de refuerzo en el centro"): (28, 72),
    # Banco de instrumentos (apartado 8).
    ("Código", "Tema", "Tipo", "RA (principal)", "Estado"): (18, 12, 16, 28, 26),
    # Definición de instrumentos (apartado 8.1).
    ("Instrumento", "Código", "Qué es", "Escala"): (22, 12, 50, 16),
}


def ensure_child(parent, tag: str):
    found = parent.find(tag)
    if found is None:
        found = ET.SubElement(parent, tag)
    return found


def tr_pr(tr):
    pr = tr.find(f"{W}trPr")
    if pr is None:
        pr = ET.Element(f"{W}trPr")
        tr.insert(0, pr)
    return pr


def p_pr(p):
    pr = p.find(f"{W}pPr")
    if pr is None:
        pr = ET.Element(f"{W}pPr")
        p.insert(0, pr)
    return pr


def cell_text(tc) -> str:
    return " ".join("".join(t.text or "" for t in tc.iter(f"{W}t")).split())


def set_widths(tbl, trs) -> bool:
    if not trs:
        return False
    header = tuple(cell_text(tc) for tc in trs[0].findall(f"{W}tc"))
    widths = COLUMN_WIDTHS.get(header)
    if widths is None:
        return False
    tbl_pr = tbl.find(f"{W}tblPr")
    tbl_w = ensure_child(tbl_pr, f"{W}tblW")
    tbl_w.set(f"{W}type", "pct")
    tbl_w.set(f"{W}w", "5000")
    layout = tbl_pr.find(f"{W}tblLayout")
    if layout is None:
        layout = ET.Element(f"{W}tblLayout")
        tbl_pr.insert(list(tbl_pr).index(tbl_w) + 1, layout)
    layout.set(f"{W}type", "fixed")
    grid = tbl.find(f"{W}tblGrid")
    cols = grid.findall(f"{W}gridCol")
    total = sum(int(c.get(f"{W}w", "0")) for c in cols) or 9000
    for col, pct in zip(cols, widths):
        col.set(f"{W}w", str(round(total * pct / 100)))
    for tr in trs:
        for tc, pct in zip(tr.findall(f"{W}tc"), widths):
            tc_pr = tc.find(f"{W}tcPr")
            if tc_pr is None:
                tc_pr = ET.Element(f"{W}tcPr")
                tc.insert(0, tc_pr)
            tc_w = tc_pr.find(f"{W}tcW")
            if tc_w is None:
                tc_w = ET.Element(f"{W}tcW")
                tc_pr.insert(0, tc_w)
            tc_w.set(f"{W}type", "pct")
            tc_w.set(f"{W}w", str(pct * 50))
    return True


def fix_tree(root) -> tuple[int, int, int]:
    tables = 0
    rows = 0
    sized = 0
    for tbl in root.iter(f"{W}tbl"):
        tables += 1
        trs = list(tbl.findall(f"{W}tr"))
        if set_widths(tbl, trs):
            sized += 1
        for index, tr in enumerate(trs):
            rows += 1
            pr = tr_pr(tr)
            ensure_child(pr, f"{W}cantSplit")
            if index == 0:
                ensure_child(pr, f"{W}tblHeader")
        if 0 < len(trs) <= MAX_ROWS_KEEP_TOGETHER:
            paragraphs = []
            for tr in trs:
                for p in tr.iter(f"{W}p"):
                    paragraphs.append(p)
            for p in paragraphs[:-1]:
                ensure_child(p_pr(p), f"{W}keepNext")
                ensure_child(p_pr(p), f"{W}keepLines")
    return tables, rows, sized


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: fix_docx_tables.py archivo.docx")
    path = Path(sys.argv[1])
    with zipfile.ZipFile(path, "r") as zin:
        xml = zin.read("word/document.xml")
        others = {name: zin.read(name) for name in zin.namelist() if name != "word/document.xml"}
    root = ET.fromstring(xml)
    tables, rows, sized = fix_tree(root)
    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    tmp = path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in others.items():
            zout.writestr(name, data)
        zout.writestr("word/document.xml", new_xml)
    tmp.replace(path)
    print(f"Tablas ajustadas: {tables}. Filas: {rows}. Con anchos fijos: {sized}.")


if __name__ == "__main__":
    main()

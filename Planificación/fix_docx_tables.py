#!/usr/bin/env python3
"""Ajusta tablas de un .docx ya generado por pandoc.

- Ninguna fila se parte entre páginas (w:cantSplit).
- La primera fila se repite como cabecera (w:tblHeader).
- Si la tabla tiene pocas filas, se procura mantenerla junta (keepNext),
  salvo el último párrafo, para que un título no se quede solo y una tabla
  corta no empiece al final de la página. Las tablas largas sí pueden
  pasar de página, con la cabecera repetida y las filas enteras.
- La cabecera va en negrita y con fondo azul suave; bordes finos grises y
  relleno de celda de 0,1 cm arriba/abajo y 0,19 cm a los lados.
- El párrafo que presenta una tabla (el anterior, si acaba en «:») se
  mantiene con ella, para que la tabla no empiece en la página siguiente
  dejando la presentación sola.
- Algunos tipos de tabla, reconocidos por su cabecera, reciben anchos de
  columna fijos (COLUMN_WIDTHS) para que los títulos estrechos no se partan
  letra a letra y la columna con más texto sea la ancha.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from lxml import etree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
# Tablas de hasta este número de filas se intentan mantener en la misma página.
MAX_ROWS_KEEP_TOGETHER = 15

# …y siempre que su altura estimada no pase de un tercio de página, para que
# mantenerla entera no deje media hoja en blanco.
MAX_LINES_KEEP_TOGETHER = 18
# Las demás tablas mantienen con el título la cabecera y las primeras filas.
ROWS_WITH_HEADING = 0  # 0: no se fuerza (LibreOffice movería la tabla entera)

HEADER_FILL = "DCE6F2"  # azul suave
BORDER_COLOR = "8EA9C8"
BORDER_SIZE = "4"  # 1/2 pt
# Orden de los hijos de w:tblPr y w:tcPr según el esquema OOXML.
TBLPR_ORDER = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize", "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook"]
PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"]
TCPR_ORDER = ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"]

# Anchos por tipo de tabla, en porcentaje del ancho de texto.
# Clave: textos de la cabecera, en orden; valor: porcentaje de cada columna.
COLUMN_WIDTHS: dict[tuple[str, ...], tuple[int, ...]] = {
    # 1. Introducción.
    ("Campo", "Valor"): (24, 76),
    ("Mejora", "Aplicación en 2026-2027", "Seguimiento"): (26, 50, 24),
    # 2. Aportaciones al perfil: competencias y RA.
    ("Código", "Competencia"): (11, 89),
    ("RA", "Contribución principal a CP", "Observación breve"): (10, 45, 45),
    ("RA", "Peso en el módulo", "Horas de referencia (72 h × peso)", "Carácter"): (10, 18, 24, 48),
    # 3. Objetivos, RA y cálculo de la nota.
    ("Código", "Objetivo general"): (12, 88),
    ("OG", "CP", "RA principales"): (12, 30, 58),
    ("Código", "Descripción (literal)", "Peso"): (12, 76, 12),
    ("Paso", "Contenido"): (12, 88),
    # 4. Contenidos y temporalización.
    ("Tema", "Título", "Academy", "RA foco"): (10, 52, 16, 22),
    ("Tema", "RA1", "RA2", "RA3", "RA4"): (20, 20, 20, 20, 20),
    ("Concepto", "Valor"): (30, 70),
    ("Tramo", "Fechas", "Contenido", "Instrumentos", "Horas"): (10, 20, 36, 24, 10),
    ("Tema", "CE que se trabajan (anexo A)", "Evaluación parcial"): (12, 63, 25),
    ("Evaluación", "Periodo", "Temas"): (15, 40, 45),
    # 5 y 7. Metodología y recursos.
    ("Tipo", "Código", "Descripción", "Escala habitual"): (20, 12, 46, 22),
    ("Espacio / recurso", "Uso principal"): (30, 70),
    ("Recurso", "Uso"): (30, 70),
    # 8. Evaluación.
    ("Instrumento", "Sigla", "Descripción", "Escala"): (20, 9, 45, 26),
    ("Instrumento de calificación", "Uso en el módulo", "Valor"): (21, 54, 25),
    ("IE", "RA y CE", "Criterios de la rúbrica y puntos"): (19, 14, 67),
    ("RA", "Peso en el módulo", "Suma de sus CE (anexo A.3)"): (16, 34, 50),
    ("Código", "Tema", "Tipo", "RA", "Estado"): (24, 10, 16, 20, 30),
    # 9. Reparto de las 72 h.
    ("Bloque", "Horas", "Resultados de aprendizaje", "Periodo", "Instrumentos"): (22, 10, 20, 24, 24),
    # 11. Actividades complementarias.
    ("Actividad", "Estado", "Observación"): (42, 18, 40),
    # 12. Cálculo del 28 % y catálogo de refuerzo.
    ("Concepto", "Cálculo", "Horas"): (32, 52, 16),
    ("Resultado de aprendizaje", "Actividades de refuerzo en el centro"): (28, 72),
    # Anexo A.
    ("RA", "Nº CE del anexo", "Cobertura", "IE que puntúan"): (10, 16, 16, 58),
    ("Código CE", "Enunciado (anexo)", "RA", "Tema(s)", "IE que puntúan"): (11, 47, 8, 10, 24),
    ("IE", "Criterios de la rúbrica (puntos) y CE al que se asignan"): (11, 89),
    ("Código CE", "RA", "IE y puntos", "Puntos", "Peso"): (16, 9, 51, 11, 13),
    ("IE", "RA", "Puntos aportados al RA", "Peso dentro del RA"): (16, 14, 35, 35),
    # Anexo B.
    ("Bloque", "Horas", "Por qué esta carga"): (24, 10, 66),
    ("Periodo", "Qué ocurre"): (32, 68),
    ("Tramo", "Fechas", "Colectiva", "Individual", "Contenido", "Eval.", "Instrumentos", "Horas"): (8, 15, 11, 12, 19, 7, 21, 7),
    ("Hito", "Fecha"): (45, 55),
    ("En la tutoría y en la evaluación del módulo", "Ampliación (no sustituye el resultado de aprendizaje)"): (50, 50),
}

# Una columna de códigos cortos (letra, RA, tema…) se centra si su contenido
# no pasa de este número de caracteres y pandoc no le ha dado alineación.
MAX_CODE_CHARS = 6
# Las tablas de siete columnas o más (tramos del anexo B) van a 8 pt.
WIDE_TABLE_COLS = 7
WIDE_TABLE_SZ = "16"
# Tablas muy cortas: se mantienen enteras aunque la estimación de líneas
# supere MAX_LINES_KEEP_TOGETHER, siempre que no lleguen a media página.
MAX_ROWS_ALWAYS_TOGETHER = 6
MAX_LINES_SHORT_TABLE = 30


def ensure_child(parent, tag: str):
    found = parent.find(tag)
    if found is None:
        found = ET.SubElement(parent, tag)
    return found


def set_ordered(parent, local: str, order: list[str]):
    """Devuelve el hijo w:<local>, creándolo en su posición del esquema."""
    tag = f"{W}{local}"
    found = parent.find(tag)
    if found is not None:
        return found
    el = ET.Element(tag)
    pos = order.index(local)
    for i, child in enumerate(list(parent)):
        name = ET.QName(child).localname
        if name in order and order.index(name) > pos:
            parent.insert(i, el)
            return el
    parent.append(el)
    return el


def style_table(tbl, trs) -> None:
    tbl_pr = tbl.find(f"{W}tblPr")
    if tbl_pr is None:
        tbl_pr = ET.Element(f"{W}tblPr")
        tbl.insert(0, tbl_pr)
    borders = set_ordered(tbl_pr, "tblBorders", TBLPR_ORDER)
    for child in list(borders):
        borders.remove(child)
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = ET.SubElement(borders, f"{W}{side}")
        b.set(f"{W}val", "single")
        b.set(f"{W}sz", BORDER_SIZE)
        b.set(f"{W}space", "0")
        b.set(f"{W}color", BORDER_COLOR)
    mar = set_ordered(tbl_pr, "tblCellMar", TBLPR_ORDER)
    for child in list(mar):
        mar.remove(child)
    for side, w in (("top", "57"), ("left", "108"), ("bottom", "57"), ("right", "108")):
        m = ET.SubElement(mar, f"{W}{side}")
        m.set(f"{W}w", w)
        m.set(f"{W}type", "dxa")
    if not trs:
        return
    for tc in trs[0].findall(f"{W}tc"):
        tc_pr = tc.find(f"{W}tcPr")
        if tc_pr is None:
            tc_pr = ET.Element(f"{W}tcPr")
            tc.insert(0, tc_pr)
        shd = set_ordered(tc_pr, "shd", TCPR_ORDER)
        shd.set(f"{W}val", "clear")
        shd.set(f"{W}color", "auto")
        shd.set(f"{W}fill", HEADER_FILL)
        v = set_ordered(tc_pr, "vAlign", TCPR_ORDER)
        v.set(f"{W}val", "center")
        for r in tc.iter(f"{W}r"):
            r_pr = r.find(f"{W}rPr")
            if r_pr is None:
                r_pr = ET.Element(f"{W}rPr")
                r.insert(0, r_pr)
            # w:b va casi al principio de w:rPr (tras rStyle y rFonts).
            if r_pr.find(f"{W}b") is None:
                b = ET.Element(f"{W}b")
                idx = 0
                for i, child in enumerate(list(r_pr)):
                    if ET.QName(child).localname in ("rStyle", "rFonts"):
                        idx = i + 1
                r_pr.insert(idx, b)
                r_pr.insert(idx + 1, ET.Element(f"{W}bCs"))


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
    tbl_w = set_ordered(tbl_pr, "tblW", TBLPR_ORDER)
    tbl_w.set(f"{W}type", "pct")
    tbl_w.set(f"{W}w", "5000")
    layout = tbl_pr.find(f"{W}tblLayout")
    if layout is None:
        layout = set_ordered(tbl_pr, "tblLayout", TBLPR_ORDER)
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


def set_font_size(trs, size: str) -> None:
    """Fija el tamaño de letra de todas las celdas de la tabla."""
    for tr in trs:
        for r in tr.iter(f"{W}r"):
            r_pr = r.find(f"{W}rPr")
            if r_pr is None:
                r_pr = ET.Element(f"{W}rPr")
                r.insert(0, r_pr)
            for tag in ("sz", "szCs"):
                el = r_pr.find(f"{W}{tag}")
                if el is None:
                    el = ET.Element(f"{W}{tag}")
                    after = [c for c in r_pr if ET.QName(c).localname in RPR_AFTER_SZ]
                    if after:
                        after[0].addprevious(el)
                    else:
                        r_pr.append(el)
                el.set(f"{W}val", size)


def center_code_columns(trs) -> None:
    """Centra las columnas de códigos cortos sin alineación propia."""
    if len(trs) < 2:
        return
    ncols = len(trs[0].findall(f"{W}tc"))
    for ci in range(ncols):
        cells = [tr.findall(f"{W}tc")[ci] for tr in trs if len(tr.findall(f"{W}tc")) > ci]
        body = cells[1:]
        if not body or any(len(cell_text(tc)) > MAX_CODE_CHARS for tc in body):
            continue
        paras = [p for tc in cells for p in tc.iter(f"{W}p")]
        if any(p.find(f"{W}pPr/{W}jc") is not None for p in paras):
            continue
        for p in paras:
            set_ordered(p_pr(p), "jc", PPR_ORDER).set(f"{W}val", "center")


def estimate_lines(tbl, trs) -> int:
    """Altura aproximada de la tabla, en líneas de texto."""
    grid = tbl.find(f"{W}tblGrid")
    cols = [int(c.get(f"{W}w", "0")) for c in grid.findall(f"{W}gridCol")] if grid is not None else []
    total = sum(cols) or 9000
    # Ancho útil de unos 9000 twips: se reescala la rejilla a ese ancho.
    cols = [c * 9000 / total for c in cols] or [9000]
    lines = 0.0
    for tr in trs:
        row = 1
        for i, tc in enumerate(tr.findall(f"{W}tc")):
            width = cols[i] if i < len(cols) else cols[-1]
            per_line = max(8, int((width - 216) / 120))
            cell = 0
            for p in tc.iter(f"{W}p"):
                text = "".join(t.text or "" for t in p.iter(f"{W}t"))
                cell += max(1, -(-len(text) // per_line))
            row = max(row, cell)
        lines += row + 0.4
    return round(lines)


# Fichas de los temas (apartado 9): una página por tema. La ficha empieza en
# página nueva, no se parte, va a FICHA_SZ medios puntos y la primera
# columna (rótulos) lleva un fondo suave. Solo afecta a estas tablas.
FICHA_PREFIX = "Ficha del Tema"
FICHA_WIDTHS = (24, 76)
FICHA_SZ = "18"
FICHA_LABEL_FILL = "F2F5FA"
# Hijos de w:rPr que van detrás de w:sz/w:szCs en el esquema OOXML.
RPR_AFTER_SZ = {"szCs", "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath"}


# Espacio extra (twips, antes y después del texto de cada celda) para que las fichas
# más cortas llenen su página. Medido sobre el PDF de LibreOffice.
FICHA_PAD = {1: 0, 2: 120, 3: 125, 4: 125, 5: 120, 6: 125, 7: 130, 8: 80}


def ficha_number(trs) -> int:
    m = re.match(rf"{FICHA_PREFIX} (\d+)", cell_text(trs[0].find(f"{W}tc")))
    return int(m.group(1)) if m else 0


def is_ficha(trs) -> bool:
    if not trs:
        return False
    first = trs[0].find(f"{W}tc")
    return first is not None and cell_text(first).startswith(FICHA_PREFIX)


def fix_ficha(tbl, trs) -> None:
    tbl_pr = tbl.find(f"{W}tblPr")
    tbl_w = set_ordered(tbl_pr, "tblW", TBLPR_ORDER)
    tbl_w.set(f"{W}type", "pct")
    tbl_w.set(f"{W}w", "5000")
    set_ordered(tbl_pr, "tblLayout", TBLPR_ORDER).set(f"{W}type", "fixed")
    grid = tbl.find(f"{W}tblGrid")
    cols = grid.findall(f"{W}gridCol")
    total = sum(int(c.get(f"{W}w", "0")) for c in cols) or 9000
    for col, pct in zip(cols, FICHA_WIDTHS):
        col.set(f"{W}w", str(round(total * pct / 100)))
    pad = FICHA_PAD.get(ficha_number(trs), 0)
    for index, tr in enumerate(trs):
        for ci, tc in enumerate(tr.findall(f"{W}tc")):
            tc_pr = tc.find(f"{W}tcPr")
            if tc_pr is None:
                tc_pr = ET.Element(f"{W}tcPr")
                tc.insert(0, tc_pr)
            tc_w = tc_pr.find(f"{W}tcW")
            if tc_w is None:
                tc_w = ET.Element(f"{W}tcW")
                tc_pr.insert(0, tc_w)
            tc_w.set(f"{W}type", "pct")
            tc_w.set(f"{W}w", str(FICHA_WIDTHS[ci] * 50))
            if index > 0 and ci == 0:
                shd = set_ordered(tc_pr, "shd", TCPR_ORDER)
                shd.set(f"{W}val", "clear")
                shd.set(f"{W}color", "auto")
                shd.set(f"{W}fill", FICHA_LABEL_FILL)
            for r in tc.iter(f"{W}r"):
                r_pr = r.find(f"{W}rPr")
                if r_pr is None:
                    r_pr = ET.Element(f"{W}rPr")
                    r.insert(0, r_pr)
                for tag in ("sz", "szCs"):
                    el = r_pr.find(f"{W}{tag}")
                    if el is None:
                        el = ET.Element(f"{W}{tag}")
                        after = [c for c in r_pr if ET.QName(c).localname in RPR_AFTER_SZ]
                        if after:
                            after[0].addprevious(el)
                        else:
                            r_pr.append(el)
                    el.set(f"{W}val", FICHA_SZ)
            for p in tc.iter(f"{W}p"):
                if index < len(trs) - 1:
                    set_ordered(p_pr(p), "keepNext", PPR_ORDER)
                set_ordered(p_pr(p), "keepLines", PPR_ORDER)
            paras = list(tc.iter(f"{W}p"))
            if pad and paras:
                set_ordered(p_pr(paras[0]), "spacing", PPR_ORDER).set(f"{W}before", str(pad))
                set_ordered(p_pr(paras[-1]), "spacing", PPR_ORDER).set(f"{W}after", str(pad))
    # El título 9.x de la ficha abre página.
    prev = tbl.getprevious()
    if prev is not None and prev.tag == f"{W}p":
        set_ordered(p_pr(prev), "pageBreakBefore", PPR_ORDER)


def fix_tree(root) -> tuple[int, int, int]:
    tables = 0
    rows = 0
    sized = 0
    for tbl in root.iter(f"{W}tbl"):
        tables += 1
        trs = list(tbl.findall(f"{W}tr"))
        if set_widths(tbl, trs):
            sized += 1
        style_table(tbl, trs)
        # El párrafo de presentación («…:») va con la tabla.
        prev = tbl.getprevious()
        if prev is not None and prev.tag == f"{W}p":
            text = "".join(t.text or "" for t in prev.iter(f"{W}t")).strip()
            if text.endswith(":"):
                set_ordered(p_pr(prev), "keepNext", PPR_ORDER)
        for index, tr in enumerate(trs):
            rows += 1
            pr = tr_pr(tr)
            ensure_child(pr, f"{W}cantSplit")
            if index == 0:
                ensure_child(pr, f"{W}tblHeader")
        if is_ficha(trs):
            fix_ficha(tbl, trs)
            sized += 1
            continue
        center_code_columns(trs)
        if trs and len(trs[0].findall(f"{W}tc")) >= WIDE_TABLE_COLS:
            set_font_size(trs, WIDE_TABLE_SZ)
        lines = estimate_lines(tbl, trs)
        short = len(trs) <= MAX_ROWS_ALWAYS_TOGETHER and lines <= MAX_LINES_SHORT_TABLE
        if 0 < len(trs) <= MAX_ROWS_KEEP_TOGETHER and (lines <= MAX_LINES_KEEP_TOGETHER or short):
            paragraphs = []
            # La última fila no lleva keepNext: si la llevara, LibreOffice
            # uniría la tabla con lo que sigue y encadenaría saltos.
            for tr in trs[:-1]:
                for p in tr.iter(f"{W}p"):
                    paragraphs.append(p)
            for p in paragraphs:
                set_ordered(p_pr(p), "keepNext", PPR_ORDER)
                set_ordered(p_pr(p), "keepLines", PPR_ORDER)
        elif len(trs) > 4:
            # Sin huérfanas: la cabecera va con las dos primeras filas y las
            # dos últimas filas van juntas.
            for tr in trs[:2] + trs[-2:-1]:
                for p in tr.iter(f"{W}p"):
                    set_ordered(p_pr(p), "keepNext", PPR_ORDER)
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
    new_xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True, standalone=True)
    tmp = path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in others.items():
            zout.writestr(name, data)
        zout.writestr("word/document.xml", new_xml)
    tmp.replace(path)
    print(f"Tablas ajustadas: {tables}. Filas: {rows}. Con anchos fijos: {sized}.")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# Genera Planificación/DAW2_Introduccion_Nube_Publica_26-27.docx desde el Markdown.
#
# Uso, desde la raíz del repositorio o desde Planificación/:
#   bash Planificación/build_docx.sh
#
# El índice del Word lo escribe docx_format.lua después de la portada: una lista de hipervínculos
# a cada apartado. No se usa el campo TOC de Word, que queda vacío hasta
# que el editor lo actualiza. El índice manual del Markdown se omite.
#
# reference.docx mantiene los títulos con el párrafo siguiente.
# fix_docx_tables.py impide partir filas y repite la cabecera de tabla.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"
cd "$ROOT"

# El índice no usa el campo TOC de Word: ese campo queda vacío hasta que
# Word lo actualiza. El filtro Lua escribe un índice de hipervínculos que
# funciona al abrir el archivo.
pandoc "$DIR/PD_Cloud_INP_2026_27.md" \
  -o "$DIR/DAW2_Introduccion_Nube_Publica_26-27.docx" \
  --from=markdown \
  --reference-doc="$DIR/reference.docx" \
  --lua-filter="$DIR/docx_format.lua" \
  --resource-path="$DIR" \
  --metadata=lang:es

python3 "$DIR/fix_docx_tables.py" "$DIR/DAW2_Introduccion_Nube_Publica_26-27.docx"
echo "Generado: $DIR/DAW2_Introduccion_Nube_Publica_26-27.docx"

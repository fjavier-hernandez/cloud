#!/bin/bash
# Despliegue MkDocs → GitHub Pages (mismo flujo que RAL).
# Solo el site PÚBLICO del alumnado (mkdocs.yml). Nunca mkdocs.interno.yml.
# No ejecutar hasta «OK, commit» + OK de Pages.
# Uso: ./deploy.sh

set -euo pipefail

echo "Sincronizando rama gh-pages..."
git fetch origin gh-pages || true

echo "Desplegando documentación pública (mkdocs.yml)..."
mkdocs gh-deploy

echo "Despliegue completado."
echo "Sitio: https://fjavier-hernandez.github.io/cloud/"
echo "Nota: la guía interna (mkdocs.interno.yml / interno/) NO se despliega."

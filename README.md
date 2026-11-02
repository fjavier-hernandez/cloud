# Introducción a la Nube Pública (INP)

Apuntes MkDocs Material del módulo optativo **Introducción a la Nube Pública** (grupo **2.º DAW semipresencial**, IES Macià Abela). Curso **2026-2027**. La copia de trabajo es este repositorio.

El módulo dura **100 h** (Decreto 114/2025, anexo X-XVII, modificado por el Decreto 95/2026). De ellas, **72 h** se trabajan en el centro antes de la formación en empresa y **28 h** quedan vinculadas a la empresa. El cálculo está en `Planificación/PD_Cloud_INP_2026_27.md`.

Patrón de sitio: el de Redes Locales (tema Material, `exclude_docs: 90-guias/**`, carpeta `Planificación/` e índice con la evaluación).

Sitio previsto (cuando haya OK de commit + Pages): <https://fjavier-hernandez.github.io/cloud/>

## Servir en local

Dependencias (las mismas que RAL):

```bash
pip install "mkdocs-material[imaging]" mkdocs-print-site-plugin
# el extra imaging cubre las tarjetas sociales; Pillow/cairosvg si hace falta
```

Desde la raíz de este repo:

```bash
mkdocs serve
```

Abrir <http://127.0.0.1:8000>. Compilar sin servir:

```bash
mkdocs build --strict
```

Los ocho temas existen en `docs/01-…` … `docs/08-…` y **entran en el build** aunque no estén en `nav`. Nav pública actual: **Inicio** + **Acceso** + **Tema 1**. Los Temas 2–8 se irán añadiendo a `nav` al publicarlos.

`docs/90-guias/` queda fuera de la web (`exclude_docs`).

### Guía interna del profesor (no pública)

```bash
mkdocs serve -f mkdocs.interno.yml
```

Fuente: carpeta `interno/` (p. ej. checklist Academy). Sale a `site-interno/`. **No** entra en CI ni en `./deploy.sh`.

## Flujo de deploy (tipo RAL)

1. Contenido en `docs/` + `mkdocs.yml`.
2. **Commit / push / Pages solo con OK explícito** («OK, commit»).
3. Con remote GitHub `fjavier-hernandez/cloud` y Pages activo:
   - push a `main` dispara `.github/workflows/ci.yml` → `mkdocs gh-deploy --force`, **o**
   - `./deploy.sh` (equivale a `mkdocs gh-deploy` como en RAL).
4. URL: `https://fjavier-hernandez.github.io/cloud/`

Hasta ese OK no se publica nada.

## Qué no va aquí

- No volcar PPT/PDF de **AWS Academy** (Foundations ni Architecting) a `docs/` públicos.
- Material Architecting del compañero: solo matices de ampliación Practitioner, no temario paralelo. GIFT → Aules en fase C4 (no en el sitio público).

## Planificación

Justificación de pesos RA, duración (100 h) y calendario: `Planificación/`.

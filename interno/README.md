# Cloud INP — guía interna (profesor)

Esta carpeta **no** forma parte del sitio público del alumnado (`docs/` + `mkdocs.yml`).

## Cómo abrirla en local

Desde la raíz del repo:

```bash
mkdocs serve -f mkdocs.interno.yml
```

Abrir la URL que indique la consola (p. ej. <http://127.0.0.1:8001/>).

Compilar (opcional):

```bash
mkdocs build -f mkdocs.interno.yml
```

La salida va a `site-interno/` (ignorada por git). **No** uses `mkdocs.interno.yml` en CI ni en `deploy.sh` / `gh-deploy` del site público.

## Contenido

- [profesor-academy.md](profesor-academy.md) — checklist operativo Academy / Learner Lab / Skill Builder.

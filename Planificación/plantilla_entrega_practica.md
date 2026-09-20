# Plantilla de entrega de prácticas (INP)

Copia canónica para **adjuntar en Aules** (misma plantilla que ve el alumnado en Inicio → [Entrega de prácticas](../docs/index.md#entrega) del sitio MkDocs). Sustituye `PR201` y el título por el código y nombre de la práctica del enunciado.

---

## Cómo entregar (norma breve)

- Entrega en **Aules**, en el plazo del enunciado.
- Un **`.md`** con metadatos + H1 + enunciado + desarrollo.
- Capturas **dentro del desarrollo**, con ruta relativa `img/...`.
- Si hay imágenes → **ZIP** (`PRxxx.md` + carpeta `img/`); si no, solo el `.md`.
- No PDF salvo que Aules lo pida.

### Estructura ZIP (si hay capturas)

```text
PR201/
  PR201.md
  img/
    ejemplo.png
```

---

## Plantilla Markdown

```markdown
---
title: "PR201 — Título de la práctica"
author: "Nombre Apellidos"
email: "usuario@edu.gva.es"
curso: "2026-27"
modulo: "Introducción a la nube pública"
codigo: "PR201"
fecha: "YYYY-MM-DD"
---

# PR201 — Título de la práctica

## Enunciado
…

## Desarrollo
… texto …
![Qué se ve](img/ejemplo.png)
```

---

## Markdown y VS Code

- Guía de Markdown: <https://tutorialmarkdown.com/guia>
- Documentación de Visual Studio Code: <https://code.visualstudio.com/docs>

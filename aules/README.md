# Kit Aules — Cloud INP 2026-27

Fragmentos HTML (Bootstrap 4) para pegar en el curso vacío de **Aules**.  
No forman parte del sitio MkDocs (`docs/`).

## Cómo pegar cada HTML

1. En Aules, crea un recurso **Etiqueta** o **Página** (según el bloque).
2. En el editor, cambia a **HTML** (botón `</>` o «Código HTML»).
3. Abre el fichero `.html` de esta carpeta, copia **todo** el contenido y pégalo.
4. Guarda y revisa en el modo alumno: márgenes, enlaces y botones.
5. Sustituye los `BASE_URL` por la URL real del site de apuntes (ver abajo).

No hace falta subir estos ficheros al servidor de Aules: solo el HTML pegado.

## Mapa de secciones (curso vacío)

Orden sugerido en el curso:

| Sección Aules | Qué poner |
| --- | --- |
| **General** | Profesor (`00`) → Portada (`01`) → Cómo empezar (`02`) → Normas de entrega (`06`) → +1 CLF (`04`) |
| **Presentación / Acceso** | Enlace o etiqueta hacia Acceso en el site; recordatorio Academy / Lab |
| **Calendario** | Aviso de fechas (`05`) + enlace al Calendario del site |
| **Temas 1–8** | Una sección por tema; dentro, orden tipo RAL (ver `03`) |
| **Certificación / +1** | Enlace al hub Certificación + caja `04` (si no está ya en General) |

En Aules, crea además un **Diálogo** «Dudas individuales» y un **Foro** del curso (actividades Moodle; no van en estos HTML).

## Normas de entrega

Texto para el alumnado: `06-normas-entrega.html` (**policy A**).  
**Aplícala ya en el Tema 1**; el resto de temas igual, salvo que Aules diga otra cosa en un enunciado concreto.

## Portada gráfica (imagen del curso)

La imagen de cabecera del curso se sube en **ajustes del curso** (Moodle), no va dentro de estos HTML.

- Hazla en **Canva** partiendo de la plantilla RAL y cambiando el texto a Cloud.
- Título sugerido: **Introducción a la Nube Pública**.
- Ratio habitual en Moodle: aprox. **4:1** o el que use el tema del centro (revisa una portada que ya funcione bien en otro curso).

## Placeholder `BASE_URL`

En los HTML aparece `BASE_URL` como prefijo del site de apuntes (GitHub Pages).

- Ejemplo de valor cuando el site esté publicado: `https://fjavier-hernandez.github.io/cloud`
- Rutas típicas:
  - Inicio → `BASE_URL/index.html`
  - Acceso → `BASE_URL/00-acceso/acceso.html`
  - Calendario → `BASE_URL/calendario.html`
  - Certificación → `BASE_URL/99-certificacion/certificacion.html`
  - +1 → `BASE_URL/index.html#mas-uno-clf`

Antes de publicar el curso, sustituye `BASE_URL` por la URL real (sin barra final). Las fechas concretas de entrega van en cada tarea de Aules, no en este kit.

## Ficheros

| Fichero | Uso |
| --- | --- |
| [`00-profesor.html`](00-profesor.html) | Profesor / presentación (primera en General) |
| [`01-portada.html`](01-portada.html) | Bienvenida del módulo |
| [`02-como-empezar.html`](02-como-empezar.html) | Primeros pasos |
| [`03-plantilla-tema.html`](03-plantilla-tema.html) | Cabecera de cada Tema N + orden Moodle |
| [`04-caja-mas-uno.html`](04-caja-mas-uno.html) | Callout +1 CLF-C02 |
| [`05-aviso-calendario.html`](05-aviso-calendario.html) | Fechas orientativas |
| [`06-normas-entrega.html`](06-normas-entrega.html) | Policy A de entregas |
| [`gift/T1-fundamentos.gift`](gift/T1-fundamentos.gift) | Banco GIFT Tema 1 (piloto) |

## Importar GIFT

Banco de preguntas del Tema 1 (piloto), listo para cuestionarios en Aules:

1. En Aules: **Banco de preguntas** → **Importar**.
2. Formato: **GIFT**.
3. Categoría: crea o elige **Cloud INP / Tema 1** (en el fichero ya va `$CATEGORY: Cloud INP/Tema 1`).
4. Sube [`gift/T1-fundamentos.gift`](gift/T1-fundamentos.gift) y revisa la vista previa antes de confirmar.
5. Usa las preguntas en un cuestionario de la sección del Tema 1 (tras el enlace a apuntes y la tarea, si sigues el orden de `03`).

Codificación del fichero: **UTF-8**.

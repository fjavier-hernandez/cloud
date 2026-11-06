# AGENTS.md

Instrucciones para los agentes (Cursor y otros) que trabajen en este repositorio. Léelas antes de tocar nada y síguelas en cada tarea.

## Objetivo del repositorio

Este repositorio contiene los apuntes del módulo optativo **Introducción a la Nube Pública (INP)** del ciclo formativo de grado superior de **Desarrollo de Aplicaciones Web (DAW)**, segundo curso, modalidad semipresencial, curso 2026-2027. El hilo del módulo es AWS Academy Cloud Foundations, con ampliación hacia la certificación AWS Certified Cloud Practitioner (CLF-C02). Se publican con MkDocs (tema Material) en GitHub Pages: <https://fjavier-hernandez.github.io/cloud/>.

El repositorio es **público**: todo lo que se suba, aunque no aparezca en la web, puede leerlo cualquiera. Además, cada push a `main` despliega la web automáticamente (`.github/workflows/ci.yml`), así que fusionar una PR equivale a publicar.

## Estructura

| Ruta | Contenido | ¿Se publica en la web? |
| --- | --- | --- |
| `mkdocs.yml` | Configuración del sitio público y navegación (`nav`). | Define la web |
| `docs/index.md`, `docs/calendario.md` | Portada con la evaluación y calendario orientativo de tutorías. | Sí |
| `docs/00-acceso/` | Acceso a AWS Academy, al laboratorio, a Skill Builder y a los vouchers. | Sí |
| `docs/01-fundamentos-nube-aws/` … `docs/08-escalado-monitoreo-cierre/` | Un directorio por tema (`temaN.md` e `img/`), del Tema 1 al Tema 8. | Sí |
| `docs/90-soluciones/` | Índice de soluciones de autoevaluación y guías de apoyo a las prácticas (`pr/PRnNN.md`, `pr/AC802.md`). | Sí |
| `docs/99-certificacion/` | Preparación del CLF-C02. | Sí |
| `docs/90-guias/` | Guías de redacción y apoyo para el profesorado. | No (`exclude_docs`) |
| `mkdocs.interno.yml` e `interno/` | Guía interna del profesor; sale a `site-interno/`. | No (no entra en CI ni en `deploy.sh`) |
| `aules/` | Páginas HTML y bancos GIFT para Aules. | No |
| `Planificación/` | PD, programación de aula, matriz de CE, diario de sesiones y plantillas. Uso interno. | No |

Antes de crear un fichero nuevo, comprueba en qué carpeta va y si debe aparecer en la `nav` o quedar excluido.

## Compilar en local

```bash
pip install "mkdocs-material[imaging]" mkdocs-print-site-plugin
mkdocs build --strict
mkdocs serve
```

`mkdocs build --strict` no debe dar avisos de enlaces rotos. MkDocs construye **todos** los ficheros de `docs/`, aunque no estén en la `nav`: lo que no deba verse tiene que ir en `exclude_docs` o fuera de `docs/`.

## Estilo de los apuntes

Todo texto nuevo debe ser **prosa conceptual y cohesionada**: párrafos completos, con conectores que expliquen el porqué y enlacen una idea con la siguiente. Está prohibido el estilo telegráfico: no se admiten listas de fragmentos, frases sin verbo ni el formato «X: Y». Cada concepto se presenta explicando qué es, para qué sirve y cómo encaja en el conjunto antes de entrar en detalles, y el texto se centra en el tema que toca.

Cada párrafo tendrá entre **5 y 7 líneas** como máximo; si se alarga, se divide por ideas. El tono es profesional, sin coloquialismos, muletillas ni expresiones de chat. Se escribe en **castellano**. Las siglas se desarrollan la primera vez que aparecen en cada tema, por ejemplo «red de área local (LAN)». Lo que ya se explicó en otro tema se enlaza y no se repite. Se usan con mesura las admoniciones de Material (`!!! note`, `!!! tip`, `!!! warning`) y los bloques de código con el lenguaje indicado.

## Imágenes y diagramas

Las capturas que se leen mal (borrosas, pequeñas, con texto ilegible o con datos que no deben verse) se rehacen como diagramas SVG propios. Los SVG existentes no se quitan ni se sustituyen sin motivo. Las fotos reales de equipos o materiales llevan crédito (autor, fuente y licencia) en el pie de la figura. Toda imagen lleva un texto alternativo (`alt`) descriptivo. No se suben imágenes sin licencia de uso.

## Soluciones y autoevaluación

**Las soluciones y las claves de los exámenes (pruebas objetivas, PO) nunca se publican.** Las soluciones del Autocheck sí pueden publicarse como guía de estudio. De las pruebas objetivas (PO1 y PO2) no se suben al repositorio ni los enunciados con respuestas ni las claves. Las respuestas del cuestionario inicial y del Autocheck de cada tema van en el propio tema, en bloques plegables (`<details>`), y se indexan en `docs/90-soluciones/soluciones.md`. Las guías de `docs/90-soluciones/pr/` son guías de apoyo a las prácticas, no soluciones completas para copiar. Si dudas de si algo es una solución de examen o prueba, no lo publiques y pregunta.

## Datos personales: nunca

El repositorio es público y todo lo que se suba puede leerlo cualquiera. **Nunca** se escriben ni se suben horarios del profesorado o de los grupos; nombres, notas, listas o cualquier otro dato del alumnado o de sus familias; DNI, NIA, correos o teléfonos personales; firmas o documentos firmados; ni rutas locales del ordenador del profesor (OneDrive, Obsidian, Descargas, etc.), credenciales, tokens ni claves.

Si una tarea necesita esos datos, se trabaja fuera del repositorio. Si encuentras alguno ya subido, avísalo en la descripción de la PR en vez de dejarlo pasar.

## Evaluación

La evaluación es **competencial** y tiene como referentes los **resultados de aprendizaje (RA)**. La nota se calcula por RA, con los pesos que fija la programación didáctica (PD). Los **criterios de evaluación (CE)** ponderan: cada CE se vincula a los instrumentos de calificación y recibe un peso según su importancia, y el peso de cada RA es la suma de los pesos de sus CE. No se usa la palabra «criterial». Los RA y los CE se copian literalmente de la normativa del módulo; no se inventan ni se renombran.

## Forma de trabajar con Git

Trabaja siempre en una **rama nueva** con un nombre descriptivo. Nunca hagas commit directamente en `main`. Cuando termines, abre una **pull request (PR)** con un resumen claro de lo que cambia y por qué. **No fusiones** la PR: la revisa Neo (o el profesor). Fusionar en `main` despliega la web automáticamente cuando hay CI. No despliegues el sitio (`deploy.sh`, `mkdocs gh-deploy`) salvo que se pida expresamente. Antes de abrir la PR, ejecuta `mkdocs build --strict` y revisa que en el diff no haya datos personales ni soluciones que no deban publicarse.

## Word de la programación didáctica

Si existe `Planificación/build_docx.sh`, el Word de la PD se genera desde la raíz con `bash Planificación/build_docx.sh` (necesita `pandoc` y `python3` con `python-docx`). Edita siempre el Markdown de la PD y vuelve a generar el Word; no edites el `.docx` a mano. Si el script no existe, no lo crees sin que se pida.

## Específico de este repositorio

- **Módulo y ciclo**: Introducción a la Nube Pública (INP), módulo optativo de 2.º de DAW semipresencial, curso 2026-2027. De sus 100 h, 80 h se imparten en el centro (las clases acaban el 26-02-2027) y 20 h están vinculadas a la formación en empresa (FE).
- **Temas**: ocho temas; la 1.ª evaluación cubre los Temas 1 a 4 y la 2.ª, los Temas 5 a 8. Las prácticas se codifican como `PRnNN` (PR101 a PR104 en el Tema 1 y una práctica por tema del 2 al 8). Además, hay una actividad de clase, AC802.
- **Pesos de los RA**: consulta la PD en `Planificación/PD_Cloud_INP_2026_27.md`.
- **Plazos**: las entregas las marca Aules. La planificación por quincenas está en `Planificación/programacion_aula_Cloud_2026_27.md` y en `docs/calendario.md`.
- **AWS Academy**: no se vuelcan a `docs/` las presentaciones ni los PDF de AWS Academy. El material de Architecting solo se usa como matiz de ampliación.
- **Bancos GIFT**: van a Aules, no al sitio público.
- **Guía interna**: `mkdocs serve -f mkdocs.interno.yml`. No la despliegues.
- **Corrección en Aules**: Neo corrige en Aules como si fuera el profesor; en Cloud (ciclo superior) se revisa con especial cuidado y las dudas se consultan antes de publicar.

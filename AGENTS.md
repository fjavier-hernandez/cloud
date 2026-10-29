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
| `Planificación/` | PD (`PD_Cloud_INP_2026_27.md`), programación de aula, matriz de CE, diario de sesiones, checklist del +1 y plantilla de entrega. Uso interno. | No |

Antes de crear un fichero nuevo, comprueba en qué carpeta va y si debe aparecer en la `nav` o quedar excluido.

## Compilar en local

Para comprobar el sitio en local:

```bash
pip install "mkdocs-material[imaging]" mkdocs-print-site-plugin
mkdocs build --strict
mkdocs serve
```

`mkdocs build --strict` no debe dar avisos de enlaces rotos. Ten en cuenta que MkDocs construye **todos** los ficheros de `docs/`, aunque no estén en la `nav`: lo que no deba verse tiene que ir en `exclude_docs` o fuera de `docs/`.

## Estilo de los apuntes

- Escribe en **castellano**, con frases completas y bien construidas.
- **Todo bien explicado, aunque el texto crezca.** Cada concepto se presenta, se explica y, cuando ayude, se acompaña de un ejemplo. Es preferible un párrafo más largo y claro que uno corto que obligue al alumnado a buscar fuera.
- **Nada de texto telegráfico**: no se encadenan fragmentos sin verbo, flechas o listas de palabras sueltas en lugar de explicaciones.
- **Nada de tono coloquial**: registro académico, cercano pero correcto, sin muletillas, sin bromas y sin expresiones de chat.
- **Siglas**: la primera vez que aparecen en cada tema se escriben completas, con la sigla entre paréntesis, por ejemplo «red de área local (LAN)». Después se puede usar solo la sigla.
- **No repetir lo ya visto**: si un concepto se explicó en otro tema, se enlaza a ese apartado (enlace relativo con ancla) con una frase de recordatorio, en lugar de volver a explicarlo.
- Usa los elementos de Material con mesura: admoniciones (`!!! note`, `!!! tip`, `!!! warning`) para los avisos y bloques de código con el lenguaje indicado.

## Imágenes y diagramas

- Las **capturas que se leen mal** (borrosas, pequeñas, con texto ilegible o con datos que no deben verse) se **rehacen como diagramas SVG** propios y se guardan junto al tema, en su carpeta `img/`.
- Las **fotos reales** de equipos o materiales llevan **crédito** (autor, fuente y licencia) en el pie de la figura.
- Toda imagen lleva un texto alternativo (`alt`) descriptivo.
- No se suben imágenes sin licencia de uso.

## Soluciones y autoevaluación

- **Como el módulo es semipresencial, las guías de soluciones de las prácticas (PR) y las del Autocheck pueden estar visibles como guía de estudio. Las soluciones y las claves de los exámenes (pruebas objetivas, PO) nunca se publican.**
- **Las soluciones del Autocheck pueden publicarse; las de exámenes y pruebas, nunca.** Esto incluye las pruebas objetivas (PO1 y PO2): ni sus enunciados con respuestas ni sus claves se suben al repositorio.
- Las respuestas del cuestionario inicial y del Autocheck de cada tema van en el propio tema, en bloques plegables (`<details>`), y se indexan en `docs/90-soluciones/soluciones.md`.
- Las guías de `docs/90-soluciones/pr/` son **guías de apoyo** a las prácticas (recorrido orientativo, evidencias para la rúbrica, errores frecuentes y limpieza), no soluciones completas para copiar. No añadas en ellas respuestas cerradas de una práctica evaluable sin que el profesor lo pida.
- Si dudas de si algo es una solución de examen o prueba, no lo publiques y pregunta.

## Datos personales: nunca

El repositorio es público y todo lo que se suba puede leerlo cualquiera. **Nunca** se escriben ni se suben:

- horarios del profesorado o de los grupos;
- nombres, notas, listas o cualquier otro dato del **alumnado** o de sus familias;
- **DNI**, NIA, correos o teléfonos personales;
- **firmas** o documentos firmados;
- rutas locales del ordenador del profesor (OneDrive, Descargas, etc.), credenciales, tokens ni claves.

Si una tarea necesita esos datos, se trabaja fuera del repositorio. Si encuentras alguno ya subido, avísalo en la descripción de la PR en vez de dejarlo pasar.

## Evaluación

- La evaluación es **competencial** y tiene como referentes los **resultados de aprendizaje (RA)**. La nota se calcula por RA, con los pesos que fija la programación didáctica (PD).
- Los **criterios de evaluación (CE)** solo sirven para **verificar la cobertura**, es decir, para comprobar qué actividades o instrumentos evidencian cada CE. **No** llevan porcentajes ni pesos propios.
- No se usa la palabra «criterial» en ningún documento.
- Los RA y los CE se copian literalmente de la normativa del módulo; no se inventan ni se renombran.

## Forma de trabajar con Git

- Trabaja siempre en una **rama nueva** con un nombre descriptivo. Nunca hagas commit directamente en la rama por defecto.
- Cuando termines, abre una **pull request (PR)** con un resumen claro de lo que cambia y por qué.
- **No fusiones** la PR: la revisa y la acepta el profesor.
- No despliegues el sitio (`deploy.sh`, `mkdocs gh-deploy`) salvo que se pida expresamente.
- Antes de abrir la PR, ejecuta `mkdocs build --strict` y revisa que en el diff no haya datos personales ni soluciones que no deban publicarse.

## Word de la programación didáctica

Si existe `Planificación/build_docx.sh`, el Word de la PD se genera desde la raíz del repositorio con:

```bash
bash Planificación/build_docx.sh
```

Necesita `pandoc` y `python3` (con `python-docx`). El script usa `reference.docx` y los filtros de `Planificación/` para el formato, el índice con hipervínculos y las tablas. Edita siempre el Markdown de la PD y vuelve a generar el Word; no edites el `.docx` a mano. Si el script no existe en este repositorio, no lo crees sin que se pida.

## Específico de este repositorio

- **Módulo y ciclo**: Introducción a la Nube Pública (INP), módulo optativo de 2.º de DAW semipresencial, curso 2026-2027. El módulo acaba antes de la formación en empresa (FE).
- **Temas**: ocho temas; la 1.ª evaluación cubre los Temas 1 a 4 y la 2.ª, los Temas 5 a 8. Las prácticas se codifican como `PRnNN`, donde n es el número de tema: PR101 a PR104 en el Tema 1 y una práctica por tema del 2 al 8 (PR201 a PR801). Además, hay una actividad de clase, AC802.
- **Pesos de los RA**: consulta la PD en `Planificación/PD_Cloud_INP_2026_27.md`.
- **Plazos**: las entregas y sus fechas las marca Aules. La planificación por quincenas está en `Planificación/programacion_aula_Cloud_2026_27.md` y en `docs/calendario.md`.
- **AWS Academy**: no se vuelcan a `docs/` las presentaciones ni los PDF de AWS Academy (Cloud Foundations ni Architecting). El material de Architecting solo se usa como matiz de ampliación.
- **Bancos GIFT**: van a Aules, no al sitio público.
- **Guía interna**: `mkdocs serve -f mkdocs.interno.yml`. No la despliegues.

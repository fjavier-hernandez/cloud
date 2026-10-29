# Planificación INP — Cloud 2026-27

Carpeta **interna** (fuera del sitio MkDocs público). Versionada en el repo `cloud`.

## Nombre legal

**Introducción a la Nube Pública.** No hay código numérico de módulo en el anexo PDF usado. **No inventar** RA/CE ni renombrarlos.

## Ficheros C4 (canónicos en este repo)

| Rol | Ruta |
| --- | --- |
| Programación didáctica (PD) | [`PD_Cloud_INP_2026_27.md`](PD_Cloud_INP_2026_27.md) |
| Programación de aula (tramos y tutorías) | [`programacion_aula_Cloud_2026_27.md`](programacion_aula_Cloud_2026_27.md) — calendario del alumnado → [`docs/calendario.md`](../docs/calendario.md) |
| Word de la programación didáctica | [`DAW2_Introduccion_Nube_Publica_26-27.docx`](DAW2_Introduccion_Nube_Publica_26-27.docx), generado con `bash Planificación/build_docx.sh` |
| Diario de sesiones (tras cada tutoría) | [`diario_sesiones_Cloud_2026_27.md`](diario_sesiones_Cloud_2026_27.md) |
| Matriz CE × IE (cobertura) | [`matriz_CE_Cloud_2026_27.md`](matriz_CE_Cloud_2026_27.md) |
| Plantilla entrega prácticas (Aules) | [`plantilla_entrega_practica.md`](plantilla_entrega_practica.md) |
| Checklist +1 CLF (texto Aules, profesor) | [`checklist_Aules_mas_uno_CLF_2026_27.md`](checklist_Aules_mas_uno_CLF_2026_27.md) |

Tras cada tutoría, marca en el diario la fecha real, lo impartido y las mejoras; no sustituye Aules ni la programación de aula.

## Fuente de los resultados de aprendizaje y de los criterios de evaluación

Decreto 114/2025, anexo X-XVII, modificado por el Decreto 95/2026, anexo IV.

- **4 resultados de aprendizaje**, cada uno con criterios de evaluación **a–f** (literales).  
- Los resultados de aprendizaje y sus pesos van en `docs/index.md` (alumnado).  
- Los criterios de evaluación literales van dentro de cada tema y en la matriz de esta carpeta.

## Carga horaria

| Concepto | Horas |
| --- | ---: |
| Duración del módulo | **100 h** |
| Centro, antes de la formación en empresa | **72 h** |
| Vinculadas a la formación en empresa | **28 h** |

El 28 % se aplica a cada módulo del ciclo, con redondeo hacia abajo, para llegar al mínimo de 500 h de formación en empresa sin pasar del 65 % de ningún módulo. El detalle y las citas están en el apartado 12 de la programación didáctica. Las 72 h de centro son horas de trabajo del alumnado (tutorías y trabajo autónomo guiado), no tres horas presenciales cada semana.

## Pesos RA (propuesta en vigor en index)

| RA | Peso | Bloque |
| --- | ---: | --- |
| **RA1** | **20 %** | T1 — fundamentos, adopción, facturación |
| **RA2** | **25 %** | T1 infra + T2 IAM / responsabilidad compartida |
| **RA3** | **30 %** | T3 redes, T4 cómputo, T8 balanceo/ASG |
| **RA4** | **25 %** | T5–T8 almacenamiento, BD, WA, monitoreo |
| | **100 %** | |

CE = cobertura; **sin** % de boletín por CE.

## Calendario (resumen)

- Tutorías en semanas alternas (colectiva e individual, cada una con sesión de mañana y de tarde). La formación en empresa del ciclo empieza el 1 de marzo de 2027.  
- **1.ª eval.** T1–T4 · **2.ª** T5–T8.  
- Detalle: `programacion_aula_Cloud_2026_27.md`.

## Certificación / +1

Itinerario Foundations + ampliación CLF-C02.  
**+1** si certifica: detalle en checklist Aules y en [`docs/index.md#mas-uno-clf`](../docs/index.md#mas-uno-clf) (sin rúbrica en este documento).

## IE pendientes de ampliar

- **PO1** / **PO2** (enunciado, fecha, peso por RA).  
- Codificación formal de Autochecks como AC si Aules lo pide.  
- Posible PY; cruce GIFT → Aules.  
- Ver lista completa en la matriz § «Pendiente de ampliar».

Commit/push del repo solo con OK explícito. No implica desplegar Pages.

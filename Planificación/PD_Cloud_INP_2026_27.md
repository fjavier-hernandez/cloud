# PROGRAMACIÓN DIDÁCTICA

## INTRODUCCIÓN A LA NUBE PÚBLICA

**Código de módulo:** no consta en el anexo usado (PDF *Optativa - Introducción a la nube pública*). No se inventa código.  
**Duración de trabajo del curso:** **96 h** (optativa ≈ 3 h/sem en currículo CV).  
**Duración impresa en el anexo PDF:** **100 h** (constancia interna; el sitio y esta PD usan **96 h** salvo que el DOGV Informática vigente diga otra cifra).  

**CICLO FORMATIVO DE GRADO SUPERIOR**  
**DESARROLLO DE APLICACIONES WEB (DAW)**  
**Segundo curso — modalidad semipresencial (INP)**  

**Profesor:** Javier Hernández Illán  

**CURSO:** 2026/2027  

**Centro:** IES Macià Abela (Crevillent)  
**Departamento de Informática**

---

## Índice

1. Introducción  
2. Aportaciones del módulo al perfil del ciclo  
3. Objetivos y resultados de aprendizaje  
4. Contenidos y organización en unidades (temas)  
5. Metodología  
6. Fomento a la lectura  
7. Uso didáctico de las tecnologías  
8. Evaluación  
9. Desarrollo de las unidades (resumen)  
10. Atención a la diversidad  
11. Actividades complementarias  
12. Formación en la empresa (contexto del ciclo)  
13. Evaluación de la programación y de la práctica docente  
- Anexo A. Matriz de cobertura CE → `matriz_CE_Cloud_2026_27.md`  
- Anexo B. Programación de aula → `programacion_aula_Cloud_2026_27.md`  
- Anexo C. Sitio web de apuntes (MkDocs)

---

# 1. Introducción

Esta programación didáctica concreta el módulo optativo **Introducción a la Nube Pública** del CFGS **Desarrollo de Aplicaciones Web**, impartido en el **IES Macià Abela** (Crevillent) en el curso **2026/2027**, grupo **2.º DAW semipresencial (INP)**.

Cómputo de trabajo: **96 h**. El módulo se concentra **antes** de la formación en empresa (FE) del ciclo (prevista ~**principios de marzo 2027**; se comunicará al fijarse). En 2.º GS **no** hay 3.ª evaluación: 1.ª (T1–T4) y 2.ª (T5–T8).

Enfoque: referentes de calificación = **RA**. Los **CE** sirven para **verificar cobertura** (Anexo A), **sin** porcentajes de boletín por CE. Itinerario formativo: **AWS Academy Cloud Foundations** + ampliación **AWS Certified Cloud Practitioner (CLF-C02)**. No es el curso *AWS Academy Cloud Architecting*.

## 1.1. Datos identificativos

| Campo | Valor |
| --- | --- |
| Denominación | Introducción a la Nube Pública |
| Código | No consta en el anexo PDF usado |
| Familia profesional | Informática y Comunicaciones |
| Ciclo | Desarrollo de Aplicaciones Web |
| Nivel | Grado superior |
| Curso | Segundo (2.º DAW), semipresencial INP |
| Duración de trabajo | **96 h** |
| Anexo PDF (constancia) | 100 h |
| Ritmo de aula | Tutoría colectiva **quincenal** (~1 h) + trabajo autónomo |
| Curso académico | 2026/2027 |
| Profesor | Javier Hernández Illán |

Documento abierto: podrá ajustarse por evaluación inicial, evolución del grupo u organización, respetando currículo y transparencia de calificación.

## 1.2. Entorno

El centro forma técnicos superiores en desarrollo web. El módulo aporta vocabulario y práctica de **nube pública AWS** (cuenta lab, consola, servicios Foundations) alineados a apps web (API, front estático, datos, identidad, red).

## 1.3. Características del alumnado

2.º DAW semipresencial: carga autónoma alta, tutoría quincenal breve. Heterogeneidad en experiencia previa con cloud. Decisiones a partir de evaluación inicial y observación; refuerzo/ampliación **sin modificar los RA**.

## 1.4. Marco legal y fuente curricular

- Anexo del PDF: `[CURSOS]/26_27/[CLOUD]/Introducción a la Nube Pública/Optativa - Introducción a la nube pública.pdf` (ANEXO X-XVII, familia *Informática y Comunicaciones*; **RA/CE literales**). En ese anexo **no consta código numérico de módulo** ni un RD de título específico de la optativa; **no se inventa**.
- Ordenación general de la FP: [Ley Orgánica 3/2022](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-5139) y [Real Decreto 659/2023](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-16889), más normativa autonómica de evaluación FP aplicable.
- Calendario escolar CV 2026-2027 del centro.

## 1.5. Mejoras respecto a cursos previos / arranque 2026-27

| Mejora | Aplicación |
| --- | --- |
| Mapa de **8 temas** (T1 = Foundations M0–M3) | Sitio MkDocs + esta PD |
| Evaluación por **RA** (CE = cobertura) | § 8 y matriz CE |
| Nav completa (Acceso + T1–T8 + Certificación) | Ritmo de entregas = Aules / calendario |
| +1 CLF-C02 | Checklist Aules + `#mas-uno-clf` (detalle en Aules; sin rúbrica en este documento) |
| Entregas | Markdown (`.md`) vía Aules |

---

# 2. Aportaciones del módulo al perfil del ciclo

El módulo contribuye a que el alumnado de DAW comprenda y use servicios de nube pública en escenarios de aplicación web: modelos de servicio, identidad, red, cómputo, almacenamiento, datos, principios Well-Architected, escalado y observación.

No sustituye módulos de desarrollo de aplicaciones; aporta el contexto de **despliegue y operación** en AWS a nivel Foundations / Practitioner.

---

# 3. Objetivos y resultados de aprendizaje

## 3.1. Resultados de aprendizaje (literales del anexo) y pesos

| Código | Descripción (literal) | Peso |
| --- | --- | ---: |
| **RA1** | Comprende los fundamentos de la computación en la nube, sus ventajas frente a sistemas tradicionales, el marco de adopción, los principios de migración y los aspectos clave de facturación, como estimación y optimización de costos. | **20 %** |
| **RA2** | Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos. | **25 %** |
| **RA3** | Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos. | **30 %** |
| **RA4** | Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. | **25 %** |
| | **Total** | **100 %** |

**Criterio de los pesos (propuesta de departamento, ajustable):** carga práctica Foundations y alineación CLF-C02, sin convertir el módulo en Architecting. Detalle en el README de `Planificación/`.

## 3.2. Criterios de evaluación (literales)

### RA1
- **a)** Se ha comprendido los conceptos fundamentales de la computación en la nube.  
- **b)** Se ha demostrado la capacidad para explicar las ventajas de la nube frente a sistemas tradicionales.  
- **c)** Se ha participado en actividades relacionadas con el ecosistema de servicios en la nube.  
- **d)** Se han identificado los principios básicos de la facturación y costos en la nube.  
- **e)** Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos.  
- **f)** Se ha participado en actividades prácticas sobre gestión de costos.

### RA2
- **a)** Se ha adquirido conocimiento de los componentes de una infraestructura global en la nube.  
- **b)** Se ha demostrado la capacidad para explorar y describir las principales categorías de servicios disponibles.  
- **c)** Se ha realizado una evaluación del uso adecuado de servicios básicos en ejercicios prácticos.  
- **d)** Se ha comprendido el modelo de responsabilidad compartida en la nube.  
- **e)** Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso.  
- **f)** Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad.

### RA3
- **a)** Se ha realizado el diseño y configuración de redes virtuales privadas.  
- **b)** Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas.  
- **c)** Se ha participado activamente en la creación y configuración de una red funcional.  
- **d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.  
- **e)** Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático.  
- **f)** Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales.

### RA4
- **a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.  
- **b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.  
- **c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.  
- **d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.  
- **e)** Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización.  
- **f)** Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes.

## 3.3. Cómo se calcula la nota

1. **Nota de cada RA** = media ponderada de los **IE** (AC, PR, PY, PO) que evalúan ese RA.  
2. **Nota final** = RA1×20 % + RA2×25 % + RA3×30 % + RA4×25 %.  
3. Los **RA no se compensan** entre sí.  
4. **+1 CLF-C02:** puede sumar a la nota final según las condiciones publicadas en **Aules** (checklist interno + `#mas-uno-clf`). Sin rúbrica en este documento. No recupera un RA suspendido; la suma puede llevar la calificación del módulo **hasta 11**.

Los **CE** verifican cobertura (matriz); **no** llevan % de boletín.

---

# 4. Contenidos y organización en unidades

## 4.1. Contenidos de soporte (anexo, resumidos)

Introducción a la nube; facturación y economía; infraestructura global y servicios; seguridad (responsabilidad compartida, IAM); redes y entrega de contenido; cómputo y escalado; almacenamiento y bases de datos; arquitectura Well-Architected y monitoreo.

## 4.2. Mapa de temas (UP) × Academy × RA

| Tema | Título | Academy | RA foco |
| ---: | --- | --- | --- |
| **1** | Fundamentos de la nube AWS | M0–M3 | RA1 (+ arranque RA2) |
| **2** | Seguridad, IAM y responsabilidad compartida | M4 | RA2 |
| **3** | Redes, VPC y entrega de contenido | M5 | RA3 |
| **4** | Cómputo: EC2, Lambda y contenedores | M6 | RA3 |
| **5** | Almacenamiento | M7 | RA4 |
| **6** | Bases de datos | M8 | RA4 |
| **7** | Arquitectura Well-Architected | M9 | RA4 |
| **8** | Escalado, monitorización y cierre CLF-C02 | M10 | RA3, RA4 |

Antes del Tema 1: página **Acceso** (Academy, lab, Skill Builder). Prep. examen: hub **Certificación** (MkDocs).

## 4.3. Evaluaciones

| Evaluación | Periodo (orientativo) | Temas |
| --- | --- | --- |
| **1.ª** | sep → principios de diciembre | T1–T4 |
| **2.ª** | 2.ª semana de diciembre → finales feb / principios marzo (antes FE) | T5–T8 |

Temporalización quincenal: Anexo B.

---

# 5. Metodología

- Tutoría quincenal (~1 h): presentar bloque, recursos, dudas del anterior; **no** explicar el tema entero.  
- Trabajo autónomo: apuntes MkDocs, vídeos curados, labs Academy / consola.  
- Aprendizaje basado en casos de app web (API, front estático, datos).  
- Entregas en **Markdown** por Aules.  
- Ampliación Practitioner opcional respecto al núcleo Foundations evaluable.

---

# 6. Fomento a la lectura

Lectura de documentación AWS (guías de servicio), apuntes del sitio y enunciados de lab. Entregas `.md` como práctica de escritura técnica.

---

# 7. Uso didáctico de las tecnologías

- **Aules:** entregas, plazos, comunicación.  
- **AWS Academy / Learner Lab / Skill Builder:** labs y prep. CLF.  
- **Sitio MkDocs** del módulo: apuntes.  
- Uso responsable de cuentas lab (créditos, terminar recursos).

---

# 8. Evaluación

## 8.1. Principios

Referentes = **RA**. Instrumentos: **AC** (0–1), **PR** (0–10), **PY** (0–30), **PO** (0–100), según index del sitio. Codificación: prefijo + tema (ej. `PR201`).

## 8.2. Banco IE (provisional — ampliable tras verificación)

| Código | Tema | Tipo | RA (principal) | Estado |
| --- | ---: | --- | --- | --- |
| PR101–PR104 | 1 | PR | RA1 / RA2 | En temas |
| PR201 | 2 | PR | RA2 | En temas |
| PR301 | 3 | PR | RA3 | En temas |
| PR401 | 4 | PR | RA3 | En temas |
| PR501 | 5 | PR | RA4 | En temas |
| PR601 | 6 | PR | RA4 | En temas |
| PR701 | 7 | PR | RA4 | En temas |
| PR801, AC802 | 8 | PR / AC | RA3 / RA4 | En temas |
| Autocheck T1…T8 | 1–8 | AC (quiz tema) | según tema | En temas |
| Autocheck certificación | hub | AC / práctica | transversal CLF | Hub Certificación |
| **PO1** | — | PO | RA1–RA3 (T1–T4) | **Provisional** |
| **PO2** | — | PO | RA3–RA4 (T5–T8) | **Provisional** |
| PY | — | PY | — | **Pendiente** si hace falta proyecto mayor |

Detalle CE×IE: `matriz_CE_Cloud_2026_27.md`.

## 8.3. +1 Cloud Practitioner

Puede sumar **+1** a la nota final (hasta **11** en el módulo) según **Aules**. Resumen en el site: `#mas-uno-clf`. Checklist interno: `checklist_Aules_mas_uno_CLF_2026_27.md`. Sin rúbrica en este documento.

## 8.4. Recuperación y pendientes

Según normativa de evaluación FP del centro y lo publicado en Aules. Los RA no se compensan.

---

# 9. Desarrollo de las unidades (resumen)

Cada tema del sitio incluye: propuesta didáctica (RA/CE), bloque Foundations, ampliación Practitioner, videotutorial, práctica (PR/AC), autocheck y glosario. Guion de tutoría: Anexo B.

---

# 10. Atención a la diversidad

Medidas universales (claridad de enunciados, plazos visibles, refuerzo en tutoría). Adaptaciones de acceso sin alterar RA. Coordinación con orientación según normativa de inclusión.

---

# 11. Actividades complementarias

Prep. CLF (Skill Builder, serie de vídeos, tests de práctica) como ampliación; no sustituyen los RA del módulo.

---

# 12. Formación en la empresa

La FE del ciclo (~500 h de golpe, ~marzo 2027) **cierra** el periodo lectivo de este módulo en la 2.ª evaluación. Este módulo **no** despliega RA en empresa; el alumnado debe haber cerrado T1–T8 antes de la FE.

---

# 13. Evaluación de la programación y de la práctica docente

Revisión al cierre de cada evaluación y al final de curso (diario de sesiones / C4b). Ajustes documentados en departamento.

---

# Anexos

| Anexo | Fichero |
| --- | --- |
| A. Matriz CE | `matriz_CE_Cloud_2026_27.md` |
| B. Programación de aula | `programacion_aula_Cloud_2026_27.md` |
| C. Sitio | Repo `cloud` → `docs/` (nav: Inicio · Acceso · T1–T8 · Certificación) |

**Fuentes:** PDF anexo (RA/CE literales); Obsidian *Cloud — estado 2026-27*; `docs/index.md` (pesos y evaluación alumnado).

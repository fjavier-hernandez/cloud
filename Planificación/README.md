# Planificación INP — placeholders 2026-27

## Nombre legal

**Introducción a la Nube Pública.** No hay código numérico de módulo en el anexo usado (PDF *Optativa - Introducción a la nube pública*). No inventar RA/CE ni renombrarlos.

## Fuente RA/CE

Anexo del PDF:

`[CURSOS]/26_27/[CLOUD]/Introducción a la Nube Pública/Optativa - Introducción a la nube pública.pdf`

(ANEXO X-XVII, familia Informática y Comunicaciones; 4 RA, CE a–f). Los **RA** (literales + pesos) van en `docs/index.md`. Los **CE** literales van **dentro de cada tema**, no en el index.

## Carga horaria (discrepancia)

| Fuente | Horas |
| --- | ---: |
| **Horas de trabajo de este curso** (optativa **3 h/sem** CV, semipresencial) | **96 h** |
| Duración impresa en el PDF del anexo | **100 h** |

No se inventa una tercera cifra. El sitio y la nota usan **96 h**. El PDF legal dice 100: queda constancia aquí para la PD / JE.

Calendario lectivo del módulo en el centro: **22-sep-2026 → ~23-feb-2027** (el módulo acaba **antes** de la FE del ciclo, prevista ~principios de marzo 2027). Publicación de temas **quincenal**.

Mapa **8 temas** (2026-09-18): T1 = Foundations M0–M3 (Q1–Q2); T2–T8 = M4–M10 (Q3–Q9); Q10–Q11 repaso GIFT/CLF. El index público no discute 96 vs 100 ni justifica pesos.

## Pesos de los 4 RA (propuesta; ajustable)

Suma **100 %**. Criterio: horas y peso práctico de cada bloque Foundations + alineación con CLF-C02, **sin** convertir el módulo en Architecting.

| RA | Peso | Bloque Foundations | Por qué |
| --- | ---: | --- | --- |
| **RA1** | **20** | M0–M2 (Tema 1) | Fundamentos, adopción/migración y facturación. Base conceptual; menos laboratorio de consola que redes/cómputo. El dominio *Billing* del CLF-C02 es el más ligero (12 %), pero el RA legal también incluye ventajas y marco de adopción. |
| **RA2** | **25** | M3 (Tema 1) + M4 (Tema 2) | Infraestructura global + seguridad (responsabilidad compartida, IAM). El dominio *Security and Compliance* del CLF-C02 pesa **30 %**; el RA legal une infra y seguridad. |
| **RA3** | **30** | M5–M6, M10 (Temas 3, 4, 8) | Redes virtuales, cómputo (VM, contenedores, serverless), balanceo y autoescalado. Más CE de «diseña y configura» y más labs Academy. |
| **RA4** | **25** | M7–M9 + monitoreo M10 (Temas 5–8) | Almacenamiento, bases de datos, Well-Architected y monitorización. Cierra el módulo con arquitecturas resilientes. |

Javi puede ajustar estos porcentajes en la PD; el index los copia.

## Certificación

Itinerario **AWS Academy Cloud Foundations** + ampliación **AWS Certified Cloud Practitioner (CLF-C02)**.  
Si el alumnado **certifica** Practitioner, **+1** sobre la nota final del módulo (mismo criterio que NetAcad / CCNA en RAL). Ese +1 **no sustituye** ningún RA.

## Canónicos (cuando existan)

| Rol | Ruta prevista |
| --- | --- |
| PD / programación de aula | `[CURSOS]/26_27/[PDs]/` o `[CURSOS]/26_27/[CLOUD]/` (placeholder) |
| Copia versionada en este repo | `Planificación/` (este fichero + futuros md/figuras) |

Commit/push del repo `cloud` solo con OK explícito. No implica desplegar Pages.

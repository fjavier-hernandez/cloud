---
title: Checklist profesor — AWS Academy (INP)
description: Guía interna operativa para la clase Cloud Foundations del módulo INP.
---

# Checklist profesor — AWS Academy (INP)

Guía **interna** (no publicar en el site del alumnado). La UI de AWS Academy / Skill Builder **cambia**; trata las rutas como **típicas** y **verifica en el portal** actual.

Página pública del alumnado: `docs/00-acceso/acceso.md` (nav **Acceso**).

## 0. Punto de partida (este centro)

- Institución y rol **educator** ya OK (onboarding LMS hecho en cursos previos).
- Solo si **no** pudieras *Create a class*: revisar el curso *Getting started with AWS Academy* / soporte Academy. No rehacer el alta del centro «como si fuera la primera vez».

Referencias:

- [AWS Academy](https://aws.amazon.com/training/awsacademy/)
- [AWS Academy FAQ](https://aws.amazon.com/training/awsacademy/faq/)

## 1. Crear la clase Cloud Foundations

Ruta típica en el portal educator (verificar etiquetas actuales):

1. Entrar en [AWS Academy LMS](https://awsacademy.instructure.com) con la cuenta educator.
2. *Create a class* / crear clase → curso **AWS Academy Cloud Foundations** (no Architecting).
3. Definir **fechas** de la clase (alineadas al calendario INP: ~sep → feb/marzo, antes de FE).
4. Modalidad / zona horaria según el portal.
5. Si el curso/lab lo requiere: asociar o habilitar **Learner Lab** (sandbox de prácticas) para la class.

Comprobar que la class aparece en tu listado y que el enlace de invitación está disponible.

## 2. Invitar alumnado

1. Invitar con **email institucional** (el que usarán siempre).
2. Comunicar en Aules / tutoría: aceptar invitación + misma dirección en Academy y, más adelante, Builder ID.
3. **Reenvíos** si no llega el correo (spam / filtros del centro).
4. Evitar mezclar con registros espontáneos en **AWS Educate** (otro programa).

## 3. Progreso y notas en Canvas Academy

Ruta típica:

- En la class → **Grades** / libro de calificaciones de Canvas.
- Actividad de **Modules** (lecturas, *knowledge checks*, entregas del LMS si las hay).

**Qué verás en Academy LMS**

- Progreso y notas de lo que el LMS registra (módulos, quizzes del curso, etc.).

**Qué NO asumir**

- Que **todo** lo que el alumno haga en **Skill Builder** aparezca solo en Grades de Academy. Skill Builder es otra plataforma: no hay sync mágico de «todas las notas SB → Grades».
- Si quieres evidencia de SB: captura / certificado parcial / tarea en **Aules**, según el diseño del módulo.

## 4. Skill Builder — alumnado (activación)

Indicar en clase / Aules la página pública **Acceso** del site del alumnado (`docs/00-acceso/acceso.md` en este repo; en nav: *Acceso*).

Mensajes clave (alineados con la página pública):

1. Activación desde el **curso Academy** (módulo de recursos / T&C → enlace de la oferta).
2. Tras confirmar: provisión en **días laborables** (orientativo **3–14**), **no** meses.
3. Vigencia típica **~12 meses desde la activación** (caduca; no es tiempo de espera).
4. **Mismo email** Academy ↔ Builder ID.
5. **Cuándo activar:** primeras quincenas si el curso usará Skill Builder / prep. CLF.

Portal: [skillbuilder.aws](https://skillbuilder.aws).

## 5. Skill Builder — acceso educator

1. Seguir el **Quick Guide** / guía educator de Skill Builder disponible en el portal Academy o en los recursos educator (nombre y menú pueden variar → verificar).
2. Completar T&C / enlace de educator si el programa lo exige.
3. Si **no aparece** el acceso o la suscripción educator: ticket / soporte **AWS Academy** (no improvisar con Educate).

La oferta educator (p. ej. acceso complementario limitado en el tiempo) es independiente de la del alumnado; no mezclar plazos en la comunicación a clase.

## 6. Límites del Learner Lab

- **Créditos** limitados por estudiante / class (el portal muestra consumo).
- Recordar en tutoría: apagar / terminar recursos; región del enunciado.
- Al **cerrar o finalizar** la class, el lab puede dejar de estar disponible → planificar evidencias antes del fin de fechas.
- Consultar la guía educator del Learner Lab en el portal (PDF / documentación actual del programa).

## 7. Enlaces oficiales de referencia

Verificar siempre la versión vigente en el portal educator:

| Recurso | Dónde mirar |
| --- | --- |
| Learner Lab Educator Guide (PDF) | Recursos educator / documentación Academy del lab |
| Quick Guide Skill Builder (educator / student) | Portal Academy / comunicaciones del programa |
| FAQ AWS Academy | [aws.amazon.com/training/awsacademy/faq](https://aws.amazon.com/training/awsacademy/faq/) |
| FAQ formación AWS / Skill Builder | [aws.amazon.com/training/faqs](https://aws.amazon.com/training/faqs/) |
| LMS | [awsacademy.instructure.com](https://awsacademy.instructure.com) |

## 8. Relación con este módulo MkDocs

| Pieza | Dónde |
| --- | --- |
| Cómo entrar (alumnado) | Site público → **Acceso** |
| Contenido Foundations + ampliación | Temas 1–8 (`docs/…`) |
| Publicar un tema en nav | Descomentar en `mkdocs.yml` cuando toque en clase |
| GIFT → Aules | Fase posterior (C4); no en este checklist |

## Nota de estructura

Checklist inspirado en el tipo de guías «primeros pasos Academy» usadas en FP (clase, invitación, lab, Skill Builder), **adaptado** a INP 2.º DAW semipresencial. No copiar páginas enteras de terceros ni capturas de rol educator al site público.

---
title: Tema 7 — Arquitectura Well-Architected
description: Pilares del AWS Well-Architected Framework, desacoplo y resiliencia a nivel Foundations (M9).
---

# Tema 7. Arquitectura Well-Architected

Una sola EC2 con MySQL local, AMI hecha a mano y el puerto 3306 abierto al mundo **funciona** hasta el primer pico o el primer disco lleno. El **[Well-Architected Framework](#well-architected)** no es un poster: es un vocabulario para **discutir trade-offs** (coste vs AZ extra, seguridad vs comodidad). **Foundations M9.** Nivel Practitioner: pilares y patrones cortos. No seguimos el curso Academy Cloud Architecting. Ver [glosario](#glosario).

## Propuesta didáctica

> **RA4.** *Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.*

### Criterios de evaluación (RA4)

* **d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.
* **f)** Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes.

La monitorización fina es el Tema 8. Aquí CloudWatch aparece como práctica de **excelencia operativa**.

### Contenidos

* Seis pilares y tensiones entre ellos.
* Varias AZ, desacoplo ([SNS](#sns)/[SQS](#sqs)), [IaC](#iac) como idea.
* Well-Architected Tool: existe; no es un entregable de producción del instituto.

---

## Bloque Foundations (M9)

Los **seis pilares** del Well-Architected Framework son preguntas sistemáticas sobre una carga: ¿cómo operamos?, ¿quién accede a los datos?, ¿qué pasa si cae una AZ?, ¿el tamaño del recurso encaja?, ¿pagamos ociosidad?, ¿usamos energía con sentido? Para una API DAW sirven para **argumentar** un cambio («paso a Multi-AZ») sin dibujar un diagrama de cuarenta cajas.

| Pilar | Pregunta | Ejemplo en una API DAW |
| --- | --- | --- |
| **Excelencia operativa** | ¿Cómo desplegamos y qué aprendemos del incidente? | CloudFormation, alarmas, runbooks |
| **Seguridad** | ¿Datos, identidad, detección? | IAM de mínimo privilegio, TLS, SG |
| **Fiabilidad** | ¿Qué pasa si se cae una AZ? | ALB + dos AZ + RDS Multi-AZ |
| **Eficiencia de rendimiento** | ¿El tipo de recurso encaja? | Familia de instancia, caché |
| **Optimización de costes** | ¿Pagamos ociosidad? | Apagar dev de noche, Spot en batch |
| **Sostenibilidad** | ¿Energía y uso útil? | Rightsizing, regiones, menos idle |

Multi-AZ **mejora fiabilidad** y **sube coste**. Eso es evaluable. El diagrama de cuarenta cajas no.

Los pilares **se tensan** entre sí. Más AZ y más alarmas mejoran fiabilidad y operaciones; también suman factura y complejidad. Rightsizing mejora coste y sostenibilidad; mal hecho, empeora rendimiento. En el entregable no busques el diagrama perfecto: busca **justificar** el trade-off que aceptas.

**Antes / después.** Antes: una EC2 con MySQL local, AMI manual y SG abierto. Después (Foundations, no Architecting): ALB, dos AZ, RDS Multi-AZ, cola para trabajos largos y alarmas. Cada cambio se puede etiquetar con un **pilar**; ese es el ejercicio del CE f, no redibujar Netflix.

### Patrones de resiliencia

- Varias AZ en el plano de aplicación.
- **Desacoplar** con **[SQS](#sqs)** (cola: el productor no exige que el worker esté vivo) y **[SNS](#sns)** (pub/sub: varios suscriptores). Un pico de pedidos no tiene que tumbar el proceso que genera PDF.
- **[IaC](#iac)** (CloudFormation / CDK): repetible. En este módulo *conoces* la idea; no escribes plantillas de trescientas líneas.
- Sustituir instancias enfermas (puente al Tema 8) en vez de «cuidar» una mascota.

**Mini-caso.** El endpoint `POST /pedidos` responde 201 en milisegundos y encola «generar factura PDF». Si el worker cae, los mensajes esperan en SQS; el usuario ya tiene el pedido. Sin cola, el HTTP espera al PDF y el timeout tumba la UX en el pico de la demo.

<figure markdown="span">
![Patrón resiliente: ALB, EC2 en dos AZ, SQS, workers, RDS Multi-AZ y CloudWatch](../img/diagramas/arquitectura-resiliente.svg){ width="800" }
<figcaption>Varias AZ, desacoplo con cola SQS y base gestionada Multi-AZ (nivel Foundations, no Architecting).</figcaption>
</figure>

El lab de Foundations puede ser más simple. El análisis (CE f) es decir **qué pilar mejora** si pasas de una EC2+MySQL local a ALB + varias AZ + RDS.

La **Well-Architected Tool** es un cuestionario por pilares. Saber que existe basta. En la consola verás preguntas (PERF, COST, SEC…) y, en muchas, el enlace a comprobaciones de **Trusted Advisor**.

<figure markdown="span">
![AWS Well-Architected Tool con pregunta PERF y recursos de ayuda](img/capturas/wa-tool-pregunta.png){ width="800" }
<figcaption>Pregunta de un pilar en la Well-Architected Tool. Fuente: AWS Well-Architected Tool User Guide (AWS).</figcaption>
</figure>

<figure markdown="span">
![Pregunta COST 5 con pestaña Trusted Advisor checks](img/capturas/wa-tool-trusted-advisor.png){ width="800" }
<figcaption>Trusted Advisor integrado en la revisión de coste. Fuente: AWS Well-Architected Tool User Guide (AWS).</figcaption>
</figure>

### Errores frecuentes (diseño)

- Mejorar «todo» a la vez sin decir qué pilar priorizas (el entregable pide cinco cambios argumentados).
- Confundir este módulo con *Cloud Architecting* (otro curso Academy): aquí no diseñamos landing zones multi-cuenta.
- Usar SNS cuando necesitabas una cola de trabajo (o al revés): pub/sub ≠ «el worker procesará cuando pueda».
- Declarar sostenibilidad sin rightsizing (apagar idle cuenta más que un párrafo verde).

### Relación con Temas 3–6 y 8

Sin VPC multi-AZ (T3), RDS Multi-AZ (T6) y ALB/ASG (T8), el discurso Well-Architected se queda en carteles. Este tema **nombra** el trade-off; los anteriores dan las piezas.

---

## Bloque Ampliación Practitioner (CLF-C02)

Etiqueta el escenario con un **pilar** (seguridad, operaciones, coste, fiabilidad…). SNS ≠ SQS. No diseñas *landing zones*.

**Videotutorial (Practitioner).** [AWS Well Architecting Framework](https://www.youtube.com/watch?v=S9NTua9mg9k) (~1 h 52 min). Salta a los pilares. Vídeo: Profe Santos Cloud (YouTube).

**Ampliación y trucos de examen →** [Certificación § Tema 7](../99-certificacion/certificacion.md#tema-7).

---

## Videotutorial

**Principal (Foundations).** [AWS Architectura Discussions](https://www.youtube.com/watch?v=M2Diq9qCi4s) (~34 min).

<iframe src="https://www.youtube.com/embed/M2Diq9qCi4s" title="AWS Architectura Discussions — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: trade-offs (AZ, estado, coste); úsalo como vocabulario para PR701.

El M9 del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

**PR701 — Mejorar un diagrama frágil** (RA4 d, f)

Anti-patrón: una EC2 `t3.large` en una AZ, MySQL en la misma instancia, AMI manual, SG `0.0.0.0/0` en 3306, backups en `/home`.

Entrega: **cinco** cambios, cada uno con **pilar** y servicio Foundations (RDS, ALB, Multi-AZ, IAM, S3, CloudWatch…). No implementes el diagrama completo.

Opcional: knowledge check Academy M9.

**Formato de cada cambio (recomendado).** `Problema → servicio/práctica → pilar → por qué mejora / qué empeora (coste, complejidad)`.

---

### Cómo leer un anti-patrón en cinco minutos

1. Inventaría: ¿una AZ? ¿estado en el disco local? ¿secretos en la AMI? ¿SG abierto? ¿sin alarmas?
2. Prioriza **seguridad** y **fiabilidad** antes que adornos de rendimiento.
3. Propón el cambio mínimo Foundations (RDS, Multi-AZ, ALB, S3, IAM, CloudWatch).
4. Declara el coste o la complejidad que aceptas a cambio.

Eso es exactamente el espíritu de PR701 y de muchas preguntas CLF del dominio de conceptos/arquitectura ligera.

---

## Autocheck / preparación cert

1. Cifrar EBS y forzar HTTPS: ¿qué pilar primero?
2. Pasar de una AZ a dos con ALB: ¿efecto *principal* fiabilidad o sostenibilidad?
3. ¿SQS sirve para que un pico de pedidos no tumbe al worker que renderiza facturas?
4. ¿CloudFormation es un pilar o una práctica que ayuda a operaciones?
5. ¿Este módulo exige un *landing zone* multi-cuenta?

---

## Glosario

**Well-Architected**{: #well-architected}
Marco de AWS con seis pilares para revisar cargas en la nube (operaciones, seguridad, fiabilidad, rendimiento, coste, sostenibilidad). Nivel Practitioner: reconocer el pilar ante un escenario. No sustituye al curso Architecting ni exige un diagrama de cuarenta cajas.

**SQS**{: #sqs}
*Simple Queue Service*: cola de mensajes. Desacopla productor y consumidor: el productor encola aunque el worker esté caído o saturado. Encaja en «generar PDF / enviar mail» sin tumbar el checkout HTTP.

**SNS**{: #sns}
*Simple Notification Service*: publicación/suscripción. Un mensaje puede llegar a varios destinos (email, cola, Lambda…). Útil para avisos fan-out; no es la misma semántica que una cola de trabajo única.

**IaC**{: #iac}
*Infrastructure as Code*: definir infraestructura en ficheros (p. ej. CloudFormation) para desplegar de forma repetible, no solo a base de clics. En este módulo conoces la idea; no entregas plantillas de producción del instituto.

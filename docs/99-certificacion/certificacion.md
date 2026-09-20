---
title: Certificación
description: Preparación AWS Certified Cloud Practitioner (CLF-C02) del módulo INP — serie Santos, apuntes, tests, Skill Builder, notas y autochecks CLF por tema.
---

# Certificación { #certificacion }

Esta página es el **hub** de preparación del examen **AWS Certified Cloud Practitioner (CLF-C02)**. Aquí concentras notas de ampliación por tema, **autochecks estilo examen**, la serie Santos, apuntes, tests y la sección oficial de Skill Builder. Los Temas 1–8 siguen siendo el núcleo del módulo (*Academy Cloud Foundations*); el cuestionario de cada tema es de clase, y en este hub el tono es el del examen.

Va dirigida a todo el alumnado del módulo y también a quien quiera **adelantar** la preparación del examen a su ritmo (empresa, refuerzo, repaso entre quincenas…). Empieza por el [#orden](#orden), no por memorizar baterías.

Antes de Skill Builder, pasa por [Acceso](../00-acceso/acceso.md): allí solo entras en Academy y activas el Builder ID; el estudio del examen continúa aquí.

### Examen CLF, RA del módulo y +1

Tres cosas distintas; no las mezcles:

1. **Examen CLF-C02 (AWS).** La nota del examen es **global**: un dominio más flojo puede compensarse con otros, según las reglas de AWS del propio examen.
2. **Este módulo (INP).** Los **RA no se compensan**: hay que superar **cada** resultado de aprendizaje. Suspender uno no se salva con otro.
3. **El +1** por certificación (si se concede según [Evaluación](../index.md#evaluacion) / Aules) **suma** a la calificación del módulo, pero **no aprueba un RA suspendido**.

El procedimiento concreto del +1 en Aules se publica allí (no se inventa aquí).

## Serie Profe Santos Cloud { #serie-santos }

!!! tip "Serie Cloud Practitioner (Profe Santos Cloud)"

    Trilogía 2026 en orden + Bridging. Son sesiones largas: ve por bloques según lo que te falle (conceptos, seguridad, catálogo). Vídeo: Profe Santos Cloud (YouTube).

    1. [Sesión 1 Cloud Practitioner 2026](https://www.youtube.com/watch?v=Z3yNbQXz_bI) (~1 h 51 min)
    2. [Sesión 2 Cloud Practitioner 2026](https://www.youtube.com/watch?v=XfFq9lKYDPc) (~1 h 52 min)
    3. [Sesión 3 Cloud Practitioner 2026](https://www.youtube.com/watch?v=xZOD6JVFR2M) (~1 h 46 min)
    4. [AWS Bridging to Certification](https://www.youtube.com/watch?v=ZIh4xIaMyNM) (~1 h 55 min) — cierre hacia el examen; no es dump de preguntas.

## Apuntes externos { #apuntes }

Repaso rápido en inglés:

- [AWS Certified Cloud Practitioner Notes (kananinirav)](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes) — notas cortas CLF-C02 en GitHub.
- [AWS CP Notes (Kalonji Labs)](https://kalonjilabs.github.io/aws-cp-notes/) — apuntes web por módulos.

## Tests de práctica { #tests }

**No son oficiales de AWS.** Sirven para medir huecos, no para memorizar la batería.

- [SimulaDo CLF-C02](https://simuladoclf.s3.amazonaws.com/english.html) — quiz online (BASIC 35 / FULL 65).
- [Practice exams (kananinirav)](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/exams.md) — exámenes de práctica con respuestas; también en [kananinirav.com](https://kananinirav.com/practice-exam/exams.html).

## Skill Builder { #skill-builder }

- [AWS Skill Builder — Exam Prep](https://skillbuilder.aws/exam-prep) — preparación oficial.
- Portal: [skillbuilder.aws](https://skillbuilder.aws/). Activa la cuenta desde Academy / [Acceso](../00-acceso/acceso.md) (Builder ID).
- Guía del examen: [AWS Certified Cloud Practitioner (CLF-C02)](https://aws.amazon.com/certification/certified-cloud-practitioner/).

Si el centro publica un PDF de preparación en Aules, úsalo desde allí. En este sitio no hay un fichero de preparación autorizado.

## Orden sugerido { #orden }

1. **Temas 1–8** (Foundations + *Autocheck del tema* + caja *Para el CLF*).
2. **Notas + autocheck certificación** de este hub ([#tema-1](#tema-1) … [#tema-8](#tema-8)).
3. **Serie Santos** ([#serie-santos](#serie-santos)).
4. **Tests** ([#tests](#tests)) — terceros, no oficiales.
5. **Skill Builder Exam Prep** ([#skill-builder](#skill-builder)).

---

## Notas CLF por tema { #por-temas }

Lee el Foundations del tema primero; luego la prosa de aquí; luego el **Autocheck certificación**. Los quizzes de clase viven en cada tema (otro enunciado, misma idea).

### Tema 1 — Fundamentos { #tema-1 }

[Apuntes del tema](../01-fundamentos-nube-aws/tema1.md) · refuerzo vídeo: [Sesión 1](#serie-santos)

**Dominios.** *Cloud Concepts* (~24 %) y *Billing* (~12 %), más región / AZ / edge del dominio Technology.

- **Value proposition:** el examen quiere la *causa* (escala, HA, elasticidad, agilidad, OPEX), no el eslogan. Trampa: «más barato siempre».
- **CAF y 7 R:** etiquetas de migración. *Rehost* de MySQL a EC2 ≠ *replatform* a RDS.
- **Economía:** On-Demand / RI / Spot / Savings Plans, Organizations, tags, Pricing Calculator, Support. Trampa: confundir *tipo* de instancia con *modelo de precio*.
- **Región–AZ–edge:** varias AZ = edificios en la misma región; edge ≠ BD. Varias regiones = DR, latencia o soberanía.
- **Acceso:** consola, CLI, SDK/API; CloudFormation como idea. Identificar, no diseñar un *landing zone*.

#### Autocheck certificación

1. Una pyme quiere dejar de comprar servidores y pagar solo por lo que consume el mes. ¿Qué beneficio de la nube encaja mejor como respuesta de examen?  
   a) CapEx alto garantizado · b) gasto variable / OPEX · c) «siempre más barato que on-prem»
2. Un cliente mueve VMs a EC2 **sin cambiar** SO ni motor de BD. ¿Qué estrategia de las 7 R describe mejor el movimiento?
3. El equipo propone **Spot** para el checkout de pagos 24/7. ¿Cuál es el *best next step* más sensato en CLF?  
   a) Aceptar Spot sin más · b) rechazar Spot para esa carga y valorar On-Demand/RI/Savings · c) cambiar el tipo a `t3.micro`
4. «Ponemos la BD en una *edge location* para bajar latencia.» ¿Qué falla en el razonamiento?
5. Necesitas **estimar** el coste de un diseño *antes* de desplegar. ¿Qué herramienta encaja mejor: **Pricing Calculator** o **Cost Explorer**?

<details markdown="1">
<summary>Soluciones (certificación · Tema 1)</summary>

1. **b** (OPEX / pay-as-you-go). «Siempre más barato» es trampa.

2. **Rehost** (*lift-and-shift*).

3. **b** — Spot puede interrumpirse; checkout no tolera eso.

4. Edge/CloudFront cachea contenido; **no** hospeda RDS «en el borde».

5. **Pricing Calculator** (estimación previa); Cost Explorer mira gasto ya ocurrido.

</details>

Más práctica: [#tests](#tests) · [#serie-santos](#serie-santos) · [#skill-builder](#skill-builder).

### Tema 2 — Seguridad e IAM { #tema-2 }

[Apuntes del tema](../02-seguridad-iam/tema2.md) · refuerzo vídeo: [Sesión 2](#serie-santos)

Dominio más pesado (~30 %). Reconoce el logo; no montas un SOC.

| Servicio / idea | Para el examen |
| --- | --- |
| IAM Identity Center | SSO de organización |
| Secrets Manager / SSM Parameter Store | Secretos **fuera** del código |
| CloudTrail | Quién llamó a qué **API** |
| CloudWatch | Métricas/CPU/alarmas — **no** es CloudTrail |
| AWS Config | Cómo estaba configurado el recurso |
| GuardDuty / Inspector / Security Hub | Detección y hallazgos |
| Shield / WAF | DDoS / reglas HTTP en el borde |
| KMS | Claves de cifrado |
| Macie | Datos sensibles en S3 |
| Trusted Advisor | Checks (según plan) |

**Trampas.** ¿Quién parchea EC2? Tú. Root + MFA. App comprometida que lista buckets → seguridad **en** la nube.

#### Autocheck certificación

1. Una API en EC2 fue comprometida y el atacante listó objetos S3. ¿Falló sobre todo la seguridad *de* la nube o *en* la nube?
2. Un analista quiere saber **quién** llamó a `DeleteBucket` ayer a las 03:00. ¿Qué servicio miras primero?  
   a) CloudWatch Alarms · b) CloudTrail · c) Auto Scaling
3. Credenciales de acceso de larga duración aparecen en un repo público. ¿Cuál es el *best next step* más alineado con buenas prácticas?  
   a) Ignorar si el lab es de clase · b) rotar/invalidar keys y usar roles · c) subir el mismo `.env` a otro repo «privado»
4. ¿Quién es responsable de parchear el **sistema operativo** de una instancia EC2 de tu API?
5. El examen pregunta una acción que solo el **root** debería hacer. ¿Cuál encaja mejor?  
   a) Desplegar la API del TFG cada día · b) Cerrar la cuenta AWS · c) Leer un objeto S3 del lab

<details markdown="1">
<summary>Soluciones (certificación · Tema 2)</summary>

1. **En** la nube (rol/keys/SG del cliente).

2. **b** CloudTrail.

3. **b**.

4. **El cliente** (tú).

5. **b**.

</details>

Más práctica: [#tests](#tests) · [#serie-santos](#serie-santos).

### Tema 3 — Redes y entrega { #tema-3 }

[Apuntes del tema](../03-redes-entrega-contenido/tema3.md)

- **VPC:** subnet = una AZ. SG con estado; NACL sin estado.
- **NAT** vs **IGW:** salida privada vs puerta pública.
- **CloudFront + Route 53:** CDN y DNS; edge no mueve RDS.
- Publica ALB/CloudFront; BD en privada.

#### Autocheck certificación

1. Una empresa quiere que su API sobreviva al fallo de **un datacenter** en la región. ¿Qué implica para las subnets?  
   a) Una subnet enorme en una AZ · b) Recursos en **al menos dos AZ** (subnets distintas) · c) Solo NACL más estricta
2. Abrir el puerto 3306 a `0.0.0.0/0` «para probar desde casa». ¿Cuál es el problema principal en clave CLF?
3. Instancias en subnet privada necesitan `npm install` / parches. ¿Qué componente permite **salida** a internet sin publicar la instancia?  
   a) Solo Route 53 · b) NAT Gateway · c) Glacier
4. Un arquitecto dice: «CloudFront acerca la región de RDS al usuario.» ¿Qué corregirías en una frase?
5. ¿VPN Site-to-Site y Direct Connect resuelven el mismo problema de negocio a alto nivel? Señala **una** diferencia que el examen suele esperar.

<details markdown="1">
<summary>Soluciones (certificación · Tema 3)</summary>

1. **b**.

2. Expone la BD al mundo (seguridad *en* la nube); no es un atajo aceptable.

3. **b** NAT Gateway.

4. CloudFront cachea **contenido**; no reubica RDS.

5. Ambos conectan on-prem↔AWS; Direct Connect suele ser enlace dedicado/consistente; VPN va por internet cifrado (idea, no el catálogo de precios).

</details>

Más práctica: [#tests](#tests).

### Tema 4 — Cómputo { #tema-4 }

[Apuntes del tema](../04-computo-serverless/tema4.md)

| Necesitas… | Hipótesis CLF |
| --- | --- |
| SSH, SO custom | EC2 |
| Evento corto | Lambda |
| Docker sin K8s | ECS (+ Fargate) |
| K8s gestionado | EKS (reconocer) |

Tipo ≠ precio. SageMaker ≠ tipo de EC2.

#### Autocheck certificación

1. Una tienda necesita procesar miniaturas cuando se sube una foto (tarea de segundos). ¿Qué servicio encaja mejor como primera hipótesis?  
   a) EC2 24/7 · b) Lambda · c) Direct Connect
2. El enunciado dice «instancia *Spot* `m5.large`». ¿Spot describe el **tipo** o el **modelo de precio**?
3. Quieres contenedores **sin** administrar el SO de los nodos. ¿Qué modo encaja?  
   a) ECS en EC2 gestionado por ti · b) **Fargate** · c) Solo AMI manual
4. Un compañero propone **EKS** para un único contenedor de prácticas de dos semanas. ¿Cuál es la crítica más razonable en CLF/Foundations?
5. Rekognition «detecta caras en fotos». ¿Es un tipo de instancia EC2?

<details markdown="1">
<summary>Soluciones (certificación · Tema 4)</summary>

1. **b** Lambda (evento corto).

2. **Modelo de precio** (el tipo es `m5.large`).

3. **b** Fargate.

4. Sobreingeniería: EKS es K8s gestionado; para un lab corto ECS/Fargate o incluso EC2/Lambda bastan.

5. **No** — es IA aplicada (catálogo).

</details>

Más práctica: [#tests](#tests).

### Tema 5 — Almacenamiento { #tema-5 }

[Apuntes del tema](../05-almacenamiento/tema5.md)

En este bloque el examen premia elegir el **estilo** de almacén (objeto, bloque o fichero) y no olvidar la **salida de datos** en la factura. S3 no es el disco del SO; EBS no es EFS.

#### Autocheck certificación

1. Una startup sirve un SPA estático a todo el mundo. ¿Qué patrón encaja mejor?  
   a) EBS público · b) **S3 (+ CloudFront)** · c) RDS Multi-AZ
2. Dos EC2 en AZ distintas necesitan la **misma carpeta** montada. ¿EBS o EFS?
3. Un bucket sirve vídeos a alumnos desde casa **sin** CDN y la factura de red dispara. ¿Qué coste suele estar detrás?
4. «Guardamos el SO de la VM en S3 Standard porque es barato.» ¿Qué falla?
5. Migrar 80 TB una sola vez por la Wi‑Fi del instituto. ¿Qué familia de respuesta suele aparecer en CLF frente a «subir por VPN lenta»?

<details markdown="1">
<summary>Soluciones (certificación · Tema 5)</summary>

1. **b**.

2. **EFS**.

3. **Egress** (salida de datos).

4. El disco del SO es **EBS** (bloque), no un bucket de objetos.

5. **Snow Family** / transferencia offline (idea: la red del centro no escala).

</details>

Más práctica: [#tests](#tests).

### Tema 6 — Bases de datos { #tema-6 }

[Apuntes del tema](../06-bases-de-datos/tema6.md)

Aquí se distingue base **gestionada** frente a MySQL en la EC2, Multi-AZ (failover) frente a réplica de lectura, y cuándo un NoSQL va *además* del dominio relacional.

#### Autocheck certificación

1. Una app de pedidos necesita transacciones y joins. Primera hipótesis…  
   a) DynamoDB solo · b) **RDS/Aurora** · c) Kinesis
2. El negocio pide sobrevivir al fallo de una AZ **sin** usar la BD para reporting. ¿Multi-AZ o read replica como respuesta principal?
3. «Pasamos todo el dominio a DynamoDB este fin de semana porque escala.» ¿Cuál es el riesgo que el examen/Foundations subrayan?
4. En RDS, ¿quién aplica parches del **motor** MySQL/PostgreSQL en el discurso managed?
5. Un equipo quiere SQL ad hoc sobre logs en S3 (no OLTP). ¿Qué servicio del catálogo encaja mejor: **Athena** o **RDS**?

<details markdown="1">
<summary>Soluciones (certificación · Tema 6)</summary>

1. **b**.

2. **Multi-AZ** (failover).

3. Perder modelo relacional/transacciones sin necesidad; NoSQL *además*, no siempre *en lugar de*.

4. **AWS**.

5. **Athena** (SQL sobre S3); RDS es OLTP gestionado.

</details>

Más práctica: [#tests](#tests).

### Tema 7 — Well-Architected { #tema-7 }

[Apuntes del tema](../07-arquitectura-well-architected/tema7.md)

El examen pide **etiquetar** el escenario con un pilar y no confundir una cola de trabajo (SQS) con un pub/sub (SNS). No exige un *landing zone* multi-cuenta.

#### Autocheck certificación

1. «Ciframos discos y forzamos HTTPS.» ¿Qué pilar etiquetas primero?
2. Un checkout encola «generar factura PDF» para un worker. ¿**SQS** o **SNS** como pieza principal?
3. Rightsizing + Spot en un batch interrumpible. ¿Qué pilar suena más fuerte?
4. CloudFormation para desplegar igual en lab y demo. ¿Es un **pilar** o una **práctica** que ayuda a operaciones?
5. El enunciado pide un *landing zone* multi-cuenta completo. ¿Es requisito de este módulo INP?

<details markdown="1">
<summary>Soluciones (certificación · Tema 7)</summary>

1. **Seguridad**.

2. **SQS** (cola de trabajo); SNS sería fan-out/pub-sub.

3. **Coste** (también rendimiento si aplica; el eje claro es coste).

4. **Práctica / IaC**, no un pilar.

5. **No**.

</details>

Más práctica: [#tests](#tests) · [#serie-santos](#serie-santos).

### Tema 8 — Escalado, monitorización y catálogo { #tema-8 }

[Apuntes del tema](../08-escalado-monitoreo-cierre/tema8.md)

Cierra Foundations con balanceo, Auto Scaling y observación: health check, min/desired/max, y CloudWatch frente a CloudTrail. El catálogo de una frase resume *cuándo sí* / *cuándo no*:

| Servicio | Cuándo sí | Cuándo no |
| --- | --- | --- |
| SageMaker | ML construir/entrenar/desplegar | Sustituir EC2 «porque IA» |
| Rekognition, Transcribe, Polly, Lex… | IA aplicada | Tipo de instancia |
| Athena | SQL ad hoc sobre S3 | OLTP de la tienda |
| Glue | ETL | ORM de Express |
| Kinesis | Stream continuo | Cola simple de un PDF (SQS) |
| QuickSight | BI | Base transaccional |
| SNS / SQS / EventBridge / Step Functions | Eventos / orquestación | Ver Tema 7 |
| SES, CloudShell, CodePipeline, WorkSpaces, IoT Core | Reconocer in-scope | Montarlo todo en el lab |

#### Autocheck certificación

1. Una API HTTP necesita reglas por path y health checks. ¿**ALB** o **NAT Gateway**?
2. El ASG tiene min=2 y hay destinos *unhealthy*. ¿Qué pieza evita mandar tráfico a instancias rotas?
3. Quieres alarmar CPU al 80 %. ¿CloudWatch o CloudTrail?
4. «Necesito SQL sobre ficheros de log en S3 una vez al mes.» ¿Athena, RDS o EC2 con MySQL local?
5. Un enunciado describe clasificar objetos en imágenes. ¿Rekognition o un tipo `g4dn`?

<details markdown="1">
<summary>Soluciones (certificación · Tema 8)</summary>

1. **ALB**.

2. El **health check** del ALB (y el ASG sustituyendo enfermas).

3. **CloudWatch**.

4. **Athena**.

5. **Rekognition** (servicio de IA), no «un tipo de EC2».

</details>

Más práctica: [#tests](#tests) · [#serie-santos](#serie-santos) · [#skill-builder](#skill-builder).

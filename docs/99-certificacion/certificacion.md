---
title: Certificación
description: Prep. AWS Certified Cloud Practitioner (CLF-C02) del módulo INP — serie Santos, apuntes, tests, Skill Builder y notas por tema.
---

# Certificación { #certificacion }

Material de preparación para **AWS Certified Cloud Practitioner (CLF-C02)**. Esta página es el **hub** del CLF: aquí se explican las notas de ampliación por tema, la serie Santos, apuntes, tests y exam prep. Los Temas 1–8 del módulo siguen siendo el núcleo (Academy Cloud Foundations); no sustituyas el lab por un dump de preguntas.

**Para quién.** Todo el alumnado del módulo. También quien quiera **adelantar** la prep. CLF a su ritmo (empresa, refuerzo, repaso entre quincenas…): empieza por [#orden](#orden), no por memorizar baterías.

Antes de Skill Builder, entra por [Acceso](../00-acceso/acceso.md) (Academy → Builder ID).

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

Repaso rápido en inglés (no sustituyen los apuntes del módulo):

- [AWS Certified Cloud Practitioner Notes (kananinirav)](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes) — notas cortas CLF-C02 en GitHub.
- [AWS CP Notes (Kalonji Labs)](https://kalonjilabs.github.io/aws-cp-notes/) — apuntes web por módulos.

## Tests de práctica { #tests }

**No son oficiales de AWS.** Sirven para medir huecos, no para memorizar la batería.

- [SimulaDo CLF-C02](https://simuladoclf.s3.amazonaws.com/english.html) — quiz online (BASIC 35 / FULL 65).
- [Practice exams (kananinirav)](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/exams.md) — exámenes de práctica con respuestas; también en [kananinirav.com](https://kananinirav.com/practice-exam/exams.html).

## Skill Builder { #skill-builder }

- [AWS Skill Builder — Exam Prep](https://skillbuilder.aws/exam-prep) — prep. oficial.
- Portal: [skillbuilder.aws](https://skillbuilder.aws/). Activa la cuenta desde Academy / [Acceso](../00-acceso/acceso.md) (Builder ID).
- Guía del examen: [AWS Certified Cloud Practitioner (CLF-C02)](https://aws.amazon.com/certification/certified-cloud-practitioner/).

PDF de prep. del centro / Aules: cuando se publique allí. No hay fichero autorizado en este sitio.

## Orden sugerido { #orden }

1. **Temas 1–8** del módulo (Foundations + el puente Practitioner de cada tema).
2. **Notas de este hub** por tema ([#tema-1](#tema-1) … [#tema-8](#tema-8)).
3. **Serie Santos** ([#serie-santos](#serie-santos)).
4. **Tests** ([#tests](#tests)) — terceros, no oficiales.
5. **Skill Builder Exam Prep** ([#skill-builder](#skill-builder)).

---

## Notas CLF por tema { #por-temas }

Cada sección amplía lo que en el tema solo se apunta. Lee el Foundations del tema primero; luego vuelve aquí.

### Tema 1 — Fundamentos { #tema-1 }

[Apuntes del tema](../01-fundamentos-nube-aws/tema1.md) · refuerzo vídeo: [Sesión 1](#serie-santos)

**Dominios que tocas aquí.** *Cloud Concepts* (~24 %) y *Billing* (~12 %), más la parte de infra global (región / AZ / edge) del dominio Technology.

- **Value proposition:** el examen quiere la *causa* (escala, HA, elasticidad, agilidad, OPEX), no el eslogan. Trampa: elegir «más barato siempre» — a veces Spot ahorra y a veces tumba el checkout.
- **CAF y 7 R:** etiquetas de migración (rehost, replatform…). No diseñas un plan de empresa; sí sabes decir por qué *rehost* de MySQL a EC2 no es lo mismo que *replatform* a RDS.
- **Economía:** On-Demand / RI / Spot / Savings Plans, Organizations y factura consolidada, tags, Pricing Calculator, planes de Support. Trampa: confundir *tipo* de instancia (`t3.micro`) con *modelo de precio* (Spot).
- **Región–AZ–edge:** varias AZ = edificio distinto en la misma región; edge/CloudFront ≠ «poner la base de datos en el borde». Varias regiones = DR, latencia o soberanía — no «porque mola».
- **Acceso a AWS:** consola, CLI, SDK/API; CloudFormation como *idea* de IaC. El examen pide **identificar**, no programar un *landing zone*.

Preguntas en voz alta: ¿OPEX frente a comprar torres? ¿rehost o replatform de la base? ¿por qué dos AZ y no una VM más gorda?

### Tema 2 — Seguridad e IAM { #tema-2 }

[Apuntes del tema](../02-seguridad-iam/tema2.md) · refuerzo vídeo: [Sesión 2](#serie-santos)

Dominio más pesado del CLF (~30 %). No montas un SOC; **reconoces** el logo correcto.

| Servicio / idea | Para el examen |
| --- | --- |
| IAM Identity Center | SSO de organización |
| Secrets Manager / SSM Parameter Store | Secretos **fuera** del código |
| CloudTrail | Quién llamó a qué **API** (auditoría) |
| CloudWatch | Métricas/CPU/alarmas — **no** es CloudTrail |
| AWS Config | Cómo estaba configurado el recurso |
| GuardDuty / Inspector / Security Hub | Detección y hallazgos (reconocer) |
| Shield / WAF | DDoS / reglas HTTP en el borde |
| KMS | Claves de cifrado |
| Macie | Datos sensibles en S3 |
| Trusted Advisor | Checks (según plan de Support) |

**Trampas típicas.** ¿Quién parchea el SO de EC2? Tú (salvo servicios gestionados). ¿Qué solo puede el root? Cerrar la cuenta, cambiar ciertas cosas de facturación… MFA en root. Shared responsibility: app comprometida que lista buckets → casi siempre seguridad **en** la nube (rol amplio, keys, SG), no «AWS dejó el datacenter abierto».

### Tema 3 — Redes y entrega { #tema-3 }

[Apuntes del tema](../03-redes-entrega-contenido/tema3.md)

- **VPC:** subnet, IGW, NAT, SG, NACL. Una subnet = **una** AZ. `/16` da margen; `/28` se queda corto en lab con muchas ENI.
- **SG vs NACL:** SG con estado (recuerda conexiones); NACL sin estado (hay que abrir ida y vuelta). Trampa: abrir 3306 a `0.0.0.0/0` «para probar».
- **Conectividad:** internet (IGW), VPN, Direct Connect (híbrido dedicado). No diseñamos el CPD del instituto.
- **API Gateway:** *front* HTTP hacia Lambda u otros orígenes; no montas OpenAPI en el lab.
- **CloudFront + Route 53:** CDN y DNS. Edge cachea contenido; **no** mueve RDS a la esquina del mundo.

Decisión de examen/proyecto: front público + API + RDS → publica ALB/CloudFront; la base en privada. «Todo público para simplificar» aprueba el lab corto y suspende el sentido común.

### Tema 4 — Cómputo { #tema-4 }

[Apuntes del tema](../04-computo-serverless/tema4.md)

| Necesitas… | Hipótesis CLF |
| --- | --- |
| SSH, SO custom, legado | EC2 |
| Evento corto, sin puerto fijo | Lambda |
| Docker sin montar K8s | ECS (+ Fargate si no quieres nodos) |
| K8s gestionado | EKS (**reconocer**; no montar en el lab) |

- **Tipo vs precio:** `m5.large` no es «Spot»; Spot/RI/On-Demand es **cómo** pagas.
- **Lambda / Fargate:** menos operación de SO; no sustituyen automáticamente una API con estado en memoria y puerto fijo.
- **Auto Scaling:** elasticidad de **grupos** de EC2 (detalle Tema 8); no es un tipo de instancia.
- **SageMaker / Rekognition:** IA — **no** son «un tipo de EC2». Van al catálogo del Tema 8.

### Tema 5 — Almacenamiento { #tema-5 }

[Apuntes del tema](../05-almacenamiento/tema5.md)

- **S3:** objetos por API/HTTP; no es un disco POSIX del SO (salvo montajes que el examen casi no premia como respuesta por defecto).
- **EBS vs EFS:** EBS = disco de **una** instancia (suele una AZ); EFS = carpeta compartida NFS entre varias EC2.
- **Glacier / clases:** archivo / clases de S3, no un «tercer disco mágico» aparte del modelo de objetos.
- **Coste:** GB-mes + peticiones + **egress** (salida). Trampa: subir 50 GB de vídeo sin CDN ni clase fría y sorprenderse de la factura.

Mini-caso: SPA de 5 MB en S3 + CloudFront ≈ barato; el mismo bucket sirviendo vídeos a casa sin borde ≈ egress.

### Tema 6 — Bases de datos { #tema-6 }

[Apuntes del tema](../06-bases-de-datos/tema6.md)

- **EC2-hosted vs managed:** MySQL en EC2 lo parcheas tú; en RDS parchea AWS el motor (tú sigues con esquemas, datos y accesos).
- **Relacional vs NoSQL vs in-memory vs warehouse:** pedidos con joins → RDS/Aurora; clave-valor / documento con picos → DynamoDB; caché → ElastiCache; analítica masiva → Redshift (no el OLTP de la tienda).
- **Multi-AZ vs read replica:** Multi-AZ = **failover**; réplica = escala de **lectura**. No son lo mismo.
- **Cifrado at rest / backups point-in-time:** reconocer que existen en managed; no configurar KMS a bajo nivel en el lab.

Trampa de moda: migrar todo el dominio a NoSQL «porque escala» en un fin de semana. En examen y en sprint DAW: DynamoDB *además* del checkout SQL, no *en lugar de*, si el dominio es relacional.

### Tema 7 — Well-Architected { #tema-7 }

[Apuntes del tema](../07-arquitectura-well-architected/tema7.md)

- **Etiquetar el escenario (task 1.2):** cifrar discos → **seguridad**; alarmas/runbook → **operaciones**; Spot + rightsizing → **coste**; dos AZ + ALB → **fiabilidad**.
- **SNS vs SQS:** SNS = pub/sub (varios destinos); SQS = cola de trabajo (el worker puede ir retrasado). Trampa: usar SNS cuando necesitabas que el PDF se procesara sin tumbar el HTTP.
- **IaC (CloudFormation):** ayuda a operaciones/repetibilidad; **no** es un «pilar» en sí.
- No diseñas *landing zones* multi-cuenta en este módulo.

Si no puedes etiquetar el cambio con un pilar, el argumento de examen (y el PR701) aún no está listo.

### Tema 8 — Escalado, monitorización y catálogo { #tema-8 }

[Apuntes del tema](../08-escalado-monitoreo-cierre/tema8.md)

- **ALB / ASG / CloudWatch:** capa 7 + health check; ASG min/desired/max; métrica ≠ CloudTrail (API). Trampa: ASG min=2 en lab y olvidar bajarlo.
- **Catálogo de una frase** (reconocer, no entrenar modelos):

| Servicio | Cuándo sí | Cuándo no |
| --- | --- | --- |
| SageMaker | Construir/entrenar/desplegar ML | Sustituir EC2 «porque IA» |
| Rekognition, Transcribe, Polly, Lex… | IA aplicada al dato | Un tipo de instancia |
| Athena | SQL ad hoc sobre S3 | OLTP de la tienda |
| Glue | ETL | El ORM de Express |
| Kinesis | Stream continuo | Cola simple de un PDF (ahí SQS) |
| QuickSight | BI / dashboards | Base transaccional |
| SNS / SQS / EventBridge / Step Functions | Eventos y orquestación | Ver Tema 7 |
| SES, CloudShell, CodePipeline, WorkSpaces, IoT Core | Reconocer el logo in-scope | Montarlos todos en el lab |

Mapa dominio ↔ temas del módulo: Concepts → T1/T7; Security → T2 (+ red T3); Technology → T1 infra + T3–T8; Billing → T1.

Estudia el catálogo con *cuándo sí / cuándo no*, no con una wiki de 200 nombres. Ocho tarjetas bien hechas superan un dump.

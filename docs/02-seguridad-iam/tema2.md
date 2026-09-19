---
title: Tema 2 — Seguridad, IAM y responsabilidad compartida
description: Shared responsibility, IAM, MFA, protección de datos y servicios de seguridad a nivel Practitioner (Foundations M4).
---

# Tema 2. Seguridad, IAM y responsabilidad compartida

Una API en la nube no «hereda» la seguridad del proveedor. AWS protege los edificios y el hipervisor; **tú** decides quién llama a `s3:GetObject`, si el [root](#root) tiene [MFA](#mfa) y si el secreto del JWT vive en el código. Este tema es **Foundations M4** y el bloque que más se parece al dominio más pesado del CLF-C02 (*Security and Compliance*). Los términos clave están en el [glosario](#glosario).

## Propuesta didáctica

> **RA2.** *Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos.*

### Criterios de evaluación (RA2)

* **d)** Se ha comprendido el modelo de responsabilidad compartida en la nube.
* **e)** Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso.
* **f)** Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad.

### Contenidos

* Seguridad **de** la nube frente a seguridad **en** la nube; el límite cambia con IaaS/PaaS/SaaS.
* [IAM](#iam): root, usuarios, grupos, roles, policies; mínimo privilegio; MFA.
* Cifrado en tránsito y en reposo; Artifact y conformidad (RGPD no es automático).
* Servicios de detección y auditoría a nivel de reconocimiento (CloudTrail, GuardDuty, WAF…).

---

## Bloque Foundations (M4)

### Responsabilidad compartida

El modelo de **[responsabilidad compartida](#responsabilidad-compartida)** reparte quién asegura qué. AWS es responsable de la seguridad **de** la nube (instalaciones, hardware, hipervisor, lo que opera en un servicio gestionado). El cliente es responsable de la seguridad **en** la nube (cuentas, datos, configuración, red que tú abres, cifrado que activas, parches del SO en **EC2**).

El límite **se mueve** con el modelo de servicio. En una app DAW no es lo mismo una API en EC2 (tú parcheas Node) que una función Lambda (AWS opera el runtime) o una base RDS (AWS parchea el motor; tú sigues siendo dueño de usuarios y datos):

| Recurso | Parchear SO huésped | Identidades de la app / IAM | Hardware |
| --- | --- | --- | --- |
| EC2 (IaaS) | Tú (Node, Java, nginx) | Tú | AWS |
| RDS | AWS (motor gestionado) | Tú (usuarios de BD + IAM) | AWS |
| Lambda | AWS | Tú (rol de ejecución, código, datos) | AWS |

<figure markdown="span">
![Responsabilidad compartida en EC2, RDS y Lambda: qué parcheas tú y qué gestiona AWS](../img/diagramas/responsabilidad-compartida.svg){ width="800" }
<figcaption>El límite se mueve con el modelo de servicio: en rojo lo que asumes tú; en azul lo que opera AWS.</figcaption>
</figure>

Si subes un `.env` con la clave de Stripe a un repo público, eso no es «fallo de AWS». Si alguien entra en el datacenter, sí.

**Antes / después.** Antes: API + MySQL en la misma EC2; tú parcheas SO, Node y MySQL. Después: API en EC2 (o Lambda) y MySQL en RDS; AWS parchea el motor, pero **tú** sigues siendo dueño de usuarios de BD, datos, cifrado que activas y del security group que abre el puerto. El «pasé a gestionado» no te quita la responsabilidad del secreto en GitHub.

### Cuándo NO echar la culpa a AWS

- Access keys en un repo o en un capturas de pantalla del lab.
- Bucket público «para que se vea la foto del ejercicio».
- Root compartido por el grupo de clase.
- Abrir SSH/`0.0.0.0/0` «solo un rato» y olvidarlo.

### IAM en la práctica

**[IAM](#iam)** (*Identity and Access Management*) es el servicio con el que decides **quién** puede hacer **qué** sobre **qué recurso**. Sin IAM bien pensado, o dejas la cuenta abierta o bloqueas al equipo. Las piezas básicas:

- **[Root](#root):** dueño de la cuenta. No se usa para desarrollar. MFA. No se comparte en el grupo de clase.
- **Usuarios IAM** (o federación / Identity Center en empresas): personas.
- **Grupos:** el mismo juego de permisos (`alumnos-labs`).
- **[Roles](#rol):** identidad que **asume** un servicio o una persona; la instancia EC2 no debería llevar access keys en un fichero.
- **[Policies](#policy):** JSON *allow/deny* sobre acciones y recursos. **[Mínimo privilegio](#minimo-privilegio):** `s3:GetObject` sobre *un* bucket, no `AdministratorAccess`.

Nunca subas **access keys** a GitHub. En labs, evita admin global si el ejercicio no lo exige.

Para una API web el patrón sano es: la instancia o la función **asume un rol** con permiso concreto (`s3:GetObject` sobre *un* bucket de uploads). El desarrollador usa un usuario/federación con MFA; el root queda en la caja fuerte. Si pegas `AKIA…` en el `.env` del front, cualquier fork del repo hereda la factura.

En la consola, un **rol** se define con una *trust policy* (quién puede asumirlo) y políticas de permisos (qué puede hacer). Fíjate en el `Principal` del JSON: ahí está el servicio o la cuenta de confianza, no el listado de `s3:*`.

<figure markdown="span">
![Editor de trust policy JSON al crear un rol IAM](img/capturas/iam-trust-policy.png){ width="800" }
<figcaption>Trust policy de un rol: quién puede hacer sts:AssumeRole. Fuente: AWS Well-Architected Tool User Guide (AWS).</figcaption>
</figure>

El cortafuegos de la instancia (security group) no es IAM, pero en clase suele ir junto: IAM decide *quién* llama a la API de AWS; el SG decide *qué tráfico* entra a la ENI.

<figure markdown="span">
![Diagrama de security groups asociados a instancias EC2](img/capturas/ec2-security-groups.png){ width="800" }
<figcaption>Security groups a nivel de instancia/ENI. Fuente: Amazon EC2 User Guide (AWS).</figcaption>
</figure>

### Errores frecuentes (IAM)

- Dar `AdministratorAccess` «para que el lab funcione» y no retirarlo.
- Confundir **usuario** (persona) con **rol** (lo que asume EC2/Lambda).
- Pensar que un grupo «hereda» magia: el grupo solo agrupa policies.
- Olvidar que *deny* explícito gana a *allow* en la evaluación de policies.

### Cuentas, datos y red

- **[MFA](#mfa)** en humanos: un segundo factor además de la contraseña.
- TLS de cara al usuario (**cifrado en tránsito**); cifrado **en reposo** (KMS se nombra; el detalle de CMK queda para más adelante).
- **Security groups** (estado, a nivel de ENI) y **NACL** (sin estado, subnet): la red es control de acceso. Se profundizan en el Tema 3.

**Artifact** sirve para descargar informes de cumplimiento. Elegir `eu-west-1` no «cumple RGPD» solo: hay que configurar quién accede y dónde se replica.

TLS en el ALB o en CloudFront protege el tramo usuario↔borde; el cifrado en reposo protege el disco o el objeto en S3. Son capas distintas: una API «con HTTPS» puede seguir guardando PII en claro en un volumen sin cifrar. En Foundations basta reconocer la diferencia; el detalle de KMS/CMK es vocabulario de examen, no un lab de crypto.

### Relación con otros temas

La red (SG/NACL) se profundiza en el Tema 3: aquí solo anclas que **abrir puertos** es decisión tuya. El cómputo (Tema 4) decide *dónde* corre el código que asume el rol. Well-Architected (Tema 7) pone la seguridad como **pilar**, no como checklist suelto.

---

## Bloque Ampliación Practitioner (CLF-C02)

Más allá del IAM de aula: reconocer logos (CloudTrail ≠ CloudWatch), responsabilidad compartida y qué hace solo el **root**.

**Videotutorial (Practitioner).** [Sesión 2 Cloud Practitioner 2026](https://www.youtube.com/watch?v=XfFq9lKYDPc) (~1 h 53 min). Prioriza seguridad / IAM. Vídeo: Profe Santos Cloud (YouTube).

**Ampliación y trucos de examen →** [Certificación § Tema 2](../99-certificacion/certificacion.md#tema-2) · [serie Santos](../99-certificacion/certificacion.md#serie-santos).

---

## Videotutorial

**Principal (Foundations).** [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo) (~9 min).

<iframe src="https://www.youtube.com/embed/rEnenbxjOGo" title="IAM en Academy — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: usuarios/grupos/policies en el entorno Academy; contrasta con el rol que asume un servicio.

**Extra (opcional).** [IAM Cloud9](https://www.youtube.com/watch?v=M-TKRBYHWHA) (~24 min) — rol y entorno de desarrollo. Vídeo: Profe Santos Cloud (YouTube).

El M4 del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

**PR201 — Usuarios y políticas** (RA2 d, e, f)

Lab de IAM de Academy M4: usuario o grupo, policy gestionada, probar una denegación. Si el lab no está disponible: en la cuenta learner, con supervisión, un usuario **sin** facturación, `ReadOnlyAccess` o la policy del enunciado, MFA si el entorno lo permite, y **borrar** al terminar.

No uses el root para el trabajo cotidiano.

**Checklist de lab Academy (IAM).**

1. Confirma que no estás en la cuenta root (o no la uses si el lab lo permite).
2. Crea solo lo que pide el enunciado; anota nombres de usuario/rol.
3. Prueba una acción denegada (evidencia de mínimo privilegio).
4. Activa MFA si el entorno learner lo permite.
5. **Borra** usuarios/roles/policies de lab al terminar; quita access keys temporales.

---

### En la práctica de desarrollo web

Cuando tu API en Node usa el SDK de AWS (S3, SES, etc.), las credenciales **no** van en el front ni en el repositorio. En EC2/Lambda el SDK toma el **rol** de la instancia/función. En el portátil de desarrollo usas un perfil local o variables de entorno **fuera de Git**. Si el lab Academy te da un usuario IAM, trátalo como material sensible: no lo captures en el PDF ni en el chat del grupo.

Un `AccessDenied` en consola no es «AWS roto»: es la policy haciendo su trabajo. Lee el mensaje (acción + recurso) antes de pedir `AdministratorAccess`.

---

## Autocheck / preparación cert

1. ¿Quién parchea el SO de una EC2 donde corre tu API? ¿Y el motor de RDS?
2. Diferencia usuario / grupo / rol / policy. ¿Dónde pondrías el permiso de la instancia para leer un bucket?
3. Cita dos acciones que el examen asocia al **root**.
4. ¿CloudTrail sirve para métricas de CPU o para auditoría de API?
5. ¿El modelo compartido es idéntico en EC2 y en Lambda? ¿Por qué cambia el riesgo de un `.env` mal subido?

---

## Glosario

**responsabilidad compartida**{: #responsabilidad-compartida}
Reparto de deberes de seguridad entre AWS (seguridad *de* la nube) y el cliente (seguridad *en* la nube). El límite cambia según uses EC2, RDS, Lambda, etc. En una app DAW: AWS no revisa tu `.env`; tú no proteges el edificio del datacenter.

**IAM**{: #iam}
*Identity and Access Management*: servicio para gestionar identidades y permisos sobre recursos AWS (usuarios, grupos, roles y policies). Es el control de acceso de casi todo lo que harás en Foundations: sin IAM coherente, o abres demasiado o bloqueas el lab.

**root**{: #root}
Cuenta propietaria de la suscripción AWS. Tiene privilegios totales; no debe usarse para el trabajo diario y debe protegerse con MFA. El examen suele asociarla a acciones de cuenta (p. ej. cambiar plan de soporte, cerrar la cuenta), no a desplegar la API del TFG.

**rol**{: #rol}
Identidad IAM que se *asume* temporalmente (por una persona, una instancia EC2 o un servicio). Evita pegar access keys permanentes en el disco. En desarrollo web es la forma correcta de que la API lea un bucket o escriba logs.

**policy**{: #policy}
Documento (suele ser JSON) que permite o deniega acciones sobre recursos. Se adjunta a usuarios, grupos o roles. Una policy mal acotada (`*` sobre `*`) convierte un lab en un incidente.

**mínimo privilegio**{: #minimo-privilegio}
Principio de dar solo los permisos necesarios para la tarea, ni más. Reduce el daño si se compromete una identidad. En clase: empieza por denegación y añade lo mínimo para que el lab pase.

**MFA**{: #mfa}
*Multi-factor authentication*: segundo factor (app, hardware…) además de usuario y contraseña. Obligatoria en root; muy recomendable en cualquier humano que pueda crear recursos de pago.

**CloudTrail**{: #cloudtrail}
Servicio que registra llamadas a la API de AWS (quién hizo qué, cuándo). Es auditoría, no un monitor de CPU. Si necesitas latencia o uso de CPU, miras CloudWatch (Tema 8), no CloudTrail.

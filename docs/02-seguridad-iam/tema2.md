---
title: Tema 2 — Seguridad, IAM y responsabilidad compartida
description: Shared responsibility, IAM, MFA, protección de datos y servicios de seguridad a nivel Practitioner (Foundations M4).
---

# Tema 2. Seguridad, IAM y responsabilidad compartida

Una API en la nube no «hereda» la seguridad del proveedor. AWS protege los edificios y el hipervisor; **tú** decides quién llama a `s3:GetObject`, si el [root](#root) tiene [MFA](#mfa) y si el secreto del JWT vive en el código. Este tema es **Foundations M4** y el bloque que más se parece al dominio más pesado del CLF-C02 (*Security and Compliance*). Los términos clave están en el [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). Si vienes del Tema 1, confirma Acceso y región del lab: aquí el eje es **quién puede hacer qué** (IAM y responsabilidad compartida).

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

### Programación de aula (orientativa)

| Quincena | En tutoría | Trabajo autónomo / evidencias |
| --- | --- | --- |
| **Q3** | Responsabilidad compartida + IAM | **PR201**; Autocheck del tema |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Responde con lo que sepas"
    1. En una API en **EC2** con MySQL en la misma máquina, ¿quién parchea el SO de la VM? ¿Y si pasas el motor a **RDS**?
    2. ¿Para qué sirve el usuario **root** de la cuenta AWS y por qué no lo usarías a diario?
    3. ¿Qué aporta el **MFA** frente a solo usuario y contraseña?
    4. ¿Por qué es mala idea pegar **access keys** en el repositorio de una app Node?
    5. Da un ejemplo de **mínimo privilegio**: una acción permitida sobre un recurso concreto (no «AdministratorAccess»).

Este cuestionario es solo para ti: te ayuda a ver qué dominas ya y qué te falta antes o mientras lees el tema. No se entrega en Aules; respóndelo con lo que sepas y, cuando quieras contrastar, abre el bloque **Soluciones (autoevaluación)** debajo o el índice en [Soluciones](../90-soluciones/soluciones.md).

<details markdown="1">
<summary>Soluciones (autoevaluación)</summary>

1. En **EC2**, **tú** parcheas el SO de la VM. Si el motor pasa a **RDS**, AWS parchea el motor; tú sigues con usuarios, datos, cifrado y el security group.

2. El **root** es la identidad de la cuenta (facturación, cierre, Support…). No lo uses a diario: crea usuarios/roles con mínimo privilegio.

3. El **MFA** añade un segundo factor: aunque filtren la contraseña, hace falta el dispositivo/código.

4. Las **access keys** en el repo se filtran (GitHub, forks, capturas); quien las tenga actúa como tu cuenta. Mejor rol de instancia/función o credenciales fuera de Git.

5. Ejemplo: `s3:GetObject` solo sobre `arn:aws:s3:::mi-bucket-lab/*` para un rol de la API — no `AdministratorAccess`.

</details>

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

<figure markdown="span">
![Modelo AWS: seguridad EN la nube (cliente) frente a seguridad DE la nube (AWS)](img/salvador/responsabilidad_compartida.png){ width="720" }
<figcaption>Misma idea en el diagrama oficial de AWS: datos e identidades son tuyos; regiones, AZ y hardware son del proveedor.</figcaption>
</figure>

Si subes un `.env` con la clave de Stripe a un repo público, eso no es «fallo de AWS». Si alguien entra en el datacenter, sí.

**Antes / después.** Antes: API + MySQL en la misma EC2; tú parcheas SO, Node y MySQL. Después: API en EC2 (o Lambda) y MySQL en RDS; AWS parchea el motor, pero **tú** sigues siendo dueño de usuarios de BD, datos, cifrado que activas y del security group que abre el puerto. El «pasé a gestionado» no te quita la responsabilidad del secreto en GitHub.

### Cuándo NO echar la culpa a AWS

- Access keys en un repo o en unas capturas de pantalla del lab.
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

En una API Node el patrón sano es: la persona usa un usuario o federación con MFA; la instancia o la función **asume un rol** con la policy justa. Si pegas access keys en el repo, has saltado IAM y has creado un incidente.

!!! tip "Ideas de policy (S3) que conviene reconocer"
    - Lectura solo para un **usuario IAM** concreto (`s3:GetObject` sobre `arn:aws:s3:::mi-bucket/*`).
    - Lectura/escritura para un **rol** de la app (`GetObject` + `PutObject`).
    - **Deny** si la IP de origen no es la del aula/oficina (`NotIpAddress`).
    - Condicionar por **etiqueta** del objeto (p. ej. solo `Access=public`).
    - Limitar a tráfico que entra por un **VPC endpoint** (`aws:SourceVpce`).

    En Foundations no memorizas el JSON entero: sí reconoces *Principal*, *Action*, *Resource* y *Condition*. El lab Academy te hace probar un allow/deny real.

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

En Foundations practicas IAM en el lab; el examen te pide **reconocer** el modelo de responsabilidad compartida, el papel del **root** y qué audita cada logo (CloudTrail no es CloudWatch).

!!! tip "Para el CLF"
    Si una app comprometida lista buckets, la falla suele ser *en* la nube (tu cuenta), no del edificio de AWS. El root lleva MFA; CloudTrail registra llamadas a la API y no mide CPU. Ampliación, tabla de logos y **autocheck certificación** en [Certificación § Tema 2](../99-certificacion/certificacion.md#tema-2).

**Videotutorial (Practitioner).** [Sesión 2 Cloud Practitioner 2026](https://www.youtube.com/watch?v=XfFq9lKYDPc) (~1 h 53 min). Prioriza seguridad / IAM. Vídeo: Profe Santos Cloud (YouTube).

---

## Videotutorial

**Principal (Foundations).** [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo) (~9 min).

<iframe src="https://www.youtube.com/embed/rEnenbxjOGo" title="IAM en Academy — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: usuarios/grupos/policies en el entorno Academy; contrasta con el rol que asume un servicio.

**Extra (opcional).** [IAM Cloud9](https://www.youtube.com/watch?v=M-TKRBYHWHA) (~24 min) — rol y entorno de desarrollo. Vídeo: Profe Santos Cloud (YouTube).

El M4 del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

### PR201 — Usuarios y políticas

* :simple-neutralinojs: **PR201**. (RA2 // d, e, f // **PR 0–10**). Practicas IAM con mínimo privilegio: un usuario o grupo, una policy y la evidencia de una denegación, sin usar el root a diario.

  - Preferente: lab de IAM de Academy M4.
  - Alternativa (si el lab no está disponible): en la cuenta learner, con supervisión, un usuario **sin** facturación, `ReadOnlyAccess` o la policy del enunciado, MFA si el entorno lo permite, y **borrar** al terminar.

  **Tareas:** confirma que no trabajas como root; crea solo lo que pide el enunciado y anota nombres; prueba una acción denegada; activa MFA si el learner lo permite; borra usuarios/roles/policies y access keys temporales al cerrar.

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR201.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo (no sustituye el enunciado): [Soluciones · PR201](../90-soluciones/pr/PR201.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Lab / usuario | Recurso creado según enunciado | 0–3 |
| Mínimo privilegio | Evidencia de denegación | 0–3 |
| MFA / buenas prácticas | MFA si aplica; sin root diario | 0–2 |
| Limpieza | Borrado de recursos de lab | 0–2 |
| **Total** | | **/10** |

---

### En la práctica de desarrollo web

Cuando tu API en Node usa el SDK de AWS (S3, SES, etc.), las credenciales **no** van en el front ni en el repositorio. En EC2/Lambda el SDK toma el **rol** de la instancia/función. En el portátil de desarrollo usas un perfil local o variables de entorno **fuera de Git**. Si el lab Academy te da un usuario IAM, trátalo como material sensible: no pegues claves ni capturas con secretos en el `.md` de la práctica, ni en el chat del grupo.

Un `AccessDenied` en consola no es «AWS roto»: es la policy haciendo su trabajo. Lee el mensaje (acción + recurso) antes de pedir `AdministratorAccess`.

---

## Autocheck del tema

Comprueba IAM y responsabilidad compartida de este tema. CLF: [Certificación § Tema 2](../99-certificacion/certificacion.md#tema-2).

1. ¿Quién parchea el SO de una **EC2** donde corre tu API Node?
2. ¿Dónde encaja mejor el permiso «leer el bucket S3» de la API: **usuario** largo en el disco, o **rol** de la instancia/función?
3. **V/F.** CloudTrail te dice la CPU de la instancia.
4. Elige dos acciones típicas del **root** (no del trabajo diario de despliegue):  
   a) `s3:GetObject` en un bucket de lab · b) cerrar la cuenta · c) cambiar el plan de Support · d) lanzar un `t3.micro`
5. Empareja: **policy** · **grupo** · **MFA** con: (a) documento JSON de permisos · (b) segundo factor · (c) conjunto de usuarios con políticas comunes.

<details markdown="1">
<summary>Soluciones</summary>

1. **Tú** (cliente) en EC2.

2. **Rol** asumido (evita keys permanentes en disco).

3. **Falso** — CloudTrail audita llamadas API; CPU → CloudWatch.

4. **b** y **c** (el examen asocia root a cuenta/billing/support, no al deploy rutinario).

5. La **policy** es (a) el documento JSON de permisos; el **MFA**, (b) el segundo factor; el **grupo**, (c) el conjunto de usuarios con políticas comunes.

</details>

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

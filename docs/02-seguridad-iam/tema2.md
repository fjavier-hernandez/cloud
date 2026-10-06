---
title: Tema 2 — Seguridad, IAM y responsabilidad compartida
description: Shared responsibility, IAM, MFA, protección de datos y servicios de seguridad a nivel Practitioner (Foundations Módulo 4).
---

# Tema 2. Seguridad, IAM y responsabilidad compartida

Una API en la nube no «hereda» la seguridad del proveedor. AWS protege los centros de datos y el hipervisor; **tú** decides quién puede llamar a `s3:GetObject`, si el [usuario raíz](#usuario-raiz) tiene [MFA](#mfa) y si el secreto del JWT vive en el código o fuera de Git. Este tema corresponde al **Módulo 4** de *AWS Academy Cloud Foundations* y es el bloque que más se parece al dominio más pesado del CLF-C02 (*Security and Compliance*). Los términos clave están en el [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). Si vienes del Tema 1, confirma [Acceso](../00-acceso/acceso.md) y la región del Learner Lab: aquí el eje es **quién puede hacer qué** ([IAM](#iam) y [responsabilidad compartida](#responsabilidad-compartida)).

## Propuesta didáctica

> **RA2.** *Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos.*

### Criterios de evaluación (RA2)

* **d)** Se ha comprendido el modelo de responsabilidad compartida en la nube.
* **e)** Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso.
* **f)** Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad.

### Contenidos

* Seguridad **de** la nube frente a seguridad **en** la nube; el límite cambia con IaaS, PaaS y SaaS.
* [IAM](#iam): usuario raíz, usuarios, grupos, roles, políticas; [mínimo privilegio](#minimo-privilegio); [MFA](#mfa).
* Cifrado en tránsito y en reposo; Artifact y conformidad (el RGPD no se cumple solo eligiendo región).
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

## Bloque Foundations (Módulo 4)

### Responsabilidad compartida

El modelo de **[responsabilidad compartida](#responsabilidad-compartida)** reparte quién asegura qué. AWS es responsable de la seguridad **de** la nube: instalaciones, hardware, red global del proveedor e hipervisor, y también de lo que opera en un servicio gestionado. Tú eres responsable de la seguridad **en** la nube: identidades, datos, configuración, puertos que abres, cifrado que activas y parches del sistema operativo cuando corres una máquina virtual.

Esa frontera **no es fija**: se mueve con el modelo de servicio que vimos en el Tema 1 ([IaaS](../01-fundamentos-nube-aws/tema1.md#iaas), [PaaS](../01-fundamentos-nube-aws/tema1.md#paas), [SaaS](../01-fundamentos-nube-aws/tema1.md#saas)). En un proyecto DAW no es lo mismo una API Node en [EC2](../01-fundamentos-nube-aws/tema1.md#ec2) que una base en [RDS](../01-fundamentos-nube-aws/tema1.md#rds) o un correo SaaS del centro.

#### En IaaS (API en EC2 con tu stack)

**Qué es en este caso.** Alquilas la máquina virtual y montas tú el sistema operativo, nginx, Node y, a veces, MySQL en el mismo disco.

**En la práctica.** AWS garantiza que el hipervisor y el centro de datos están protegidos; **tú** parcheas el SO, endureces la instancia, gestionas usuarios del sistema, eliges el [security group](#security-group) y cuidas de que el `.env` no acabe en un repo público. Si alguien compromete tu API porque dejaste el puerto 22 abierto a `0.0.0.0/0`, la falla es **en** la nube (tu configuración), no del edificio de AWS.

#### En PaaS (motor en RDS)

**Qué es en este caso.** Mueves MySQL a un motor gestionado: AWS opera y parchea el motor de base de datos.

**En la práctica.** Dejas de parchear MySQL a mano, pero **sigues** siendo dueño de los usuarios de la base, de los datos, del cifrado que actives y del security group que deja entrar a la API. «Pasé a gestionado» no te quita la responsabilidad si alguien obtiene la contraseña del usuario `app` porque la pegaste en Discord.

#### En SaaS (correo o CRM del centro)

**Qué es en este caso.** Consumes una aplicación completa: correo, wiki, CRM.

**En la práctica.** AWS (o el proveedor del SaaS) opera casi toda la pila; tú configuras cuentas, permisos de buzón y qué datos metes. En un TFG el SaaS suele ser dependencia (auth, correo), no el sitio donde despliegas tu API —pero si compartes la contraseña del correo del proyecto, el incidente sigue siendo tuyo.

| Recurso / modelo | Parchear SO o motor | Identidades y datos de la app | Hardware y centros de datos |
| --- | --- | --- | --- |
| EC2 + tu stack (IaaS) | Tú (SO, Node, nginx…) | Tú | AWS |
| RDS (plataforma gestionada) | AWS (motor) | Tú (usuarios de BD, datos, cifrado, SG) | AWS |
| Lambda (runtime gestionado) | AWS | Tú (rol de ejecución, código, datos) | AWS |
| Correo / CRM (SaaS) | Proveedor | Tú (cuentas y configuración) | Proveedor |

<figure markdown="span">
![Responsabilidad compartida en EC2, RDS y Lambda: qué parcheas tú y qué gestiona AWS](../img/diagramas/responsabilidad-compartida.svg){ width="800" }
<figcaption>El límite se mueve con el modelo de servicio: en rojo lo que asumes tú; en azul lo que opera AWS.</figcaption>
</figure>

<figure markdown="span">
![Modelo AWS: seguridad EN la nube (cliente) frente a seguridad DE la nube (AWS)](img/salvador/responsabilidad_compartida.png){ width="720" }
<figcaption>Misma idea en el diagrama oficial de AWS: datos e identidades son tuyos; regiones, AZ y hardware son del proveedor.</figcaption>
</figure>

**Antes / después.** Antes: API y MySQL en la misma EC2; tú parcheas SO, Node y MySQL. Después: API en EC2 (o Lambda) y MySQL en RDS; AWS parchea el motor, pero **tú** sigues siendo dueño de usuarios de BD, datos, cifrado y del security group que abre el puerto. Si subes un `.env` con la clave de Stripe a un repo público, eso no es «fallo de AWS». Si alguien entra físicamente en el centro de datos del proveedor, sí entra en su lado del modelo.

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| Distinguir seguridad *de* la nube (AWS) frente a *en* la nube (cliente) | Justificar, en un incidente, si falló parche, IAM, SG o el proveedor |
| Reconocer que el límite cambia con EC2 / RDS / Lambda / SaaS | En el lab: no echar la culpa a AWS por keys en GitHub o bucket público |

### Cuándo NO echar la culpa a AWS

Cada uno de estos fallos es seguridad **en** la nube: configuración o hábitos tuyos (o del equipo).

**Access keys en un repo o en capturas del lab.** Quien encuentre la clave puede llamar a la API como si fueras tú. Evítalo: no pegues `AKIA…` en el `.md`, en el chat ni en el front; usa un [rol](#rol) o credenciales fuera de Git y bórralas al terminar el lab.

**Bucket público «para que se vea la foto del ejercicio».** Abres el objeto al mundo: scrapers y bots lo indexan. Evítalo: URL firmada, política mínima o solo lectura desde la API; no marques el bucket entero como público «un rato».

**Usuario raíz compartido por el grupo de clase.** Cualquiera del grupo puede cerrar la cuenta, cambiar facturación o borrar recursos. Evítalo: cada persona con su identidad de trabajo; el root queda con MFA y fuera del día a día.

**SSH o `0.0.0.0/0` «solo un rato» y olvido.** Dejas la instancia expuesta a internet. Evítalo: restringe el [security group](#security-group) a la IP del lab o del aula, y ciérralo al terminar.

### IAM: quién puede hacer qué

**[IAM](#iam)** (*Identity and Access Management*) es el servicio con el que decides **quién** puede hacer **qué** sobre **qué recurso**. Sin IAM bien pensado, o dejas la cuenta abierta o bloqueas al equipo. En una API Node el patrón sano es: la persona usa un usuario o federación con MFA; la instancia o la función **asume un rol** con la política justa. Si pegas [access keys](#access-key) en el repo, has saltado ese diseño y has creado un incidente.

#### Usuario raíz (root)

**Qué es en este caso.** El [usuario raíz](#usuario-raiz) es la identidad propietaria de la cuenta AWS: facturación, cierre de cuenta, cambio de plan de Support y otras acciones de cuenta.

**En la práctica.** No lo uses para desarrollar ni para el lab diario. Activa [MFA](#mfa), guarda las credenciales fuera del grupo de clase y trabaja con un usuario o con el rol que te dé Academy. El examen asocia el root a acciones de cuenta, no a desplegar la API del TFG.

#### Usuario IAM

**Qué es en este caso.** Un [usuario IAM](#usuario-iam) es una identidad permanente pensada para una persona (o, a veces, para una aplicación antigua). Tiene contraseña de consola y, si las creas, access keys.

**En la práctica.** En empresas suele sustituirse por federación o Identity Center; en Foundations creas usuarios de lab para practicar políticas. Dale solo lo necesario y bórralo al cerrar la práctica. No es lo mismo que un **rol**: el usuario es «alguien con credenciales largas»; el rol se **asume** un rato.

#### Grupo IAM

**Qué es en este caso.** Un [grupo](#grupo-iam) agrupa usuarios para aplicarles las mismas [políticas](#politica). Por ejemplo, `alumnos-labs` con lectura en un bucket de enunciados.

**En la práctica.** El grupo no «hereda magia»: solo es un atajo para adjuntar las mismas policies a varias personas. Si cambias la policy del grupo, cambia el permiso de todos sus miembros.

#### Rol IAM

**Qué es en este caso.** Un [rol](#rol) es una identidad que **se asume** temporalmente: una instancia EC2, una función Lambda, otro servicio o una persona con permiso para *AssumeRole*. Lleva una *trust policy* (quién puede asumirlo) y políticas de permisos (qué puede hacer después).

**En la práctica.** Es la forma correcta de que tu API lea un bucket de uploads sin llevar `AKIA…` en el disco. En la consola, al crear el rol, fíjate en el `Principal` del JSON de confianza: ahí está el servicio (por ejemplo `ec2.amazonaws.com`), no el listado de acciones `s3:*`.

<figure markdown="span">
![Editor de trust policy JSON al crear un rol IAM](img/capturas/iam-trust-policy.png){ width="800" }
<figcaption>Trust policy de un rol: quién puede hacer sts:AssumeRole. Fuente: AWS Well-Architected Tool User Guide (AWS).</figcaption>
</figure>

#### El Learner Lab: rol y restricciones

En el **Learner Lab** de Academy no trabajas como en una cuenta AWS personal con tarjeta. Entras con la identidad del lab y, para crear recursos, sueles **asumir un rol** que el propio laboratorio define (en la documentación del Student Guide aparece con nombres del estilo *LabRole* o equivalentes). Ese rol ya trae permisos acotados: puedes hacer lo que el lab necesita y, a la vez, el entorno te impide operaciones peligrosas o fuera de guion (por ejemplo, ciertas acciones de facturación o de cuenta).

Por eso el lab «a veces no te deja» lo que un tutorial de internet hace con `AdministratorAccess`: no es que IAM esté roto; es que Academy te obliga a practicar con **mínimo privilegio** y con la región que permite el lab. En una cuenta propia tendrías más libertad —y más riesgo de dejar la factura abierta.

#### Política (policy)

**Qué es en este caso.** Una [política](#politica) es el documento (casi siempre JSON) que **permite o deniega** acciones sobre recursos. Se adjunta a usuarios, grupos o roles.

**En la práctica.** El [principio de mínimo privilegio](#minimo-privilegio) dice: solo lo necesario para la tarea. `s3:GetObject` sobre *un* bucket de lab, no `AdministratorAccess` «para que funcione». Hay políticas **gestionadas** por AWS (p. ej. `ReadOnlyAccess`) y políticas **insertadas** (*inline*) pegadas a una sola identidad; en Foundations reconoces ambas y eliges la que pida el enunciado.

##### Ejemplo de política JSON (línea a línea)

Imagina que tu API solo debe **leer** objetos de un bucket de imágenes del lab:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LeerImagenesLab",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::mi-bucket-lab/*"
    }
  ]
}
```

- **`Version`:** formato del lenguaje de políticas que espera IAM (en Foundations lo dejas como en el ejemplo del lab o de la documentación).
- **`Statement`:** lista de reglas; aquí hay una.
- **`Sid`:** etiqueta opcional para reconocer la regla en consola.
- **`Effect`:** `Allow` permite; `Deny` deniega. Un *deny* explícito gana a un *allow* cuando se evalúan varias políticas.
- **`Action`:** la operación de la API de AWS (`s3:GetObject`). Sin esto, no hay permiso concreto.
- **`Resource`:** sobre qué recurso aplica, en forma de [ARN](#arn) (`arn:aws:s3:::mi-bucket-lab/*` = objetos dentro del bucket). Un `*` sobre todos los buckets sería lo contrario del mínimo privilegio.

En Foundations no memorizas el JSON entero; sí reconoces *Effect*, *Action*, *Resource* y, cuando aparezca, *Condition* (por ejemplo limitar por IP). El lab del Módulo 4 te hace probar un allow/deny real.

!!! tip "Ideas de policy (S3) que conviene reconocer"
    - Lectura solo para un **usuario IAM** concreto (`s3:GetObject` sobre `arn:aws:s3:::mi-bucket/*`).
    - Lectura/escritura para un **rol** de la app (`GetObject` + `PutObject`).
    - **Deny** si la IP de origen no es la del aula u oficina (`NotIpAddress`).
    - Condicionar por **etiqueta** del objeto (p. ej. solo `Access=public`).
    - Limitar a tráfico que entra por un **VPC endpoint** (`aws:SourceVpce`).

#### Access keys y por qué no van a GitHub

Las [access keys](#access-key) son un par de credenciales de larga duración asociadas a un usuario IAM (identificador que suele empezar por `AKIA…` más un secreto). Quien las tenga puede firmar llamadas a la API **como ese usuario**, desde cualquier sitio con red.

Si las pegas en el repositorio de una app Node —en el `.env` subido, en un commit «temporal» o en una captura del `.md`—, GitHub, forks, bots y compañeros del grupo pueden acabar usándolas. La factura y los borrados corren a nombre de tu cuenta (o del lab). El patrón sano es:

- En **EC2** o **Lambda**, el SDK asume el **rol** de la instancia o de la función (credenciales temporales).
- En el **portátil**, un perfil local o variables de entorno **fuera de Git**.
- En el lab Academy, trata cualquier clave como material sensible: no la pegues en Aules ni en el chat.

Un `AccessDenied` en consola no es «AWS roto»: es la política haciendo su trabajo. Lee el mensaje (acción + recurso) antes de pedir `AdministratorAccess`.

#### Security group frente a IAM

El cortafuegos de la instancia ([security group](#security-group)) **no es IAM**, pero en clase suele ir junto: IAM decide *quién* llama a la API de AWS; el SG decide *qué tráfico de red* entra a la interfaz de la instancia. Abrir el puerto 3306 al mundo es un fallo de red; dar `s3:*` sobre `*` es un fallo de IAM. Los dos pueden tumbar un TFG.

<figure markdown="span">
![Diagrama de security groups asociados a instancias EC2](img/capturas/ec2-security-groups.png){ width="800" }
<figcaption>Security groups a nivel de instancia/ENI. Fuente: Amazon EC2 User Guide (AWS).</figcaption>
</figure>

### Errores frecuentes (IAM)

**Dar `AdministratorAccess` «para que el lab funcione» y no retirarlo.** El lab pasa, pero cualquier filtración de esa identidad puede hacerlo todo en la cuenta. Evítalo: policy mínima, prueba la denegación y limpia al terminar ([PR201](#pr201-usuarios-y-politicas)).

**Confundir usuario con rol.** El usuario es persona (o identidad larga); el rol lo asume EC2, Lambda u otra cuenta un rato. Si pones access keys de usuario en la instancia «porque el rol es complicado», vuelves al antipatrón.

**Pensar que el grupo hereda permisos mágicos.** El grupo solo agrupa políticas. Si el usuario no está en el grupo o la policy no está adjunta, no hay permiso.

**Olvidar que *deny* explícito gana a *allow*.** Puedes tener una managed policy amplia y un deny por IP o por etiqueta que te bloquea: lee el mensaje de error antes de ensanchar permisos a ciegas.

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| Root + MFA; mínimo privilegio; rol frente a access keys | En el lab: no root diario; evidence de AccessDenied; borrar usuarios y keys |
| App comprometida que lista buckets → falla *en* la nube | Revisar rol de la API y policy S3 antes de culpar al proveedor |

### Cuentas, datos y red

**[MFA](#mfa)** (*multi-factor authentication*) añade un segundo factor (app o dispositivo) además de la contraseña. En el usuario raíz es obligatorio en la práctica seria; en cualquier humano que pueda crear recursos de pago, muy recomendable. Aunque filtren la contraseña, falta el código del dispositivo.

**Cifrado en tránsito** protege los datos mientras viajan (TLS hacia el usuario, hacia el ALB o hacia CloudFront). **Cifrado en reposo** protege lo que está parado en disco u objeto (volumen, bucket S3). Son capas distintas: una API «con HTTPS» puede seguir guardando datos personales en claro en un volumen sin cifrar. [KMS](#kms) (*Key Management Service*) es el servicio que gestiona claves de cifrado; en Foundations basta reconocerlo; el detalle de CMK no es un lab de criptografía.

**Security groups** (con estado, a nivel de interfaz de la instancia) y **NACL** (sin estado, a nivel de subred) son control de acceso de **red**. Se profundizan en el Tema 3; aquí solo anclas que **abrir puertos** es decisión tuya, no de AWS.

**Artifact** sirve para descargar informes de cumplimiento del proveedor. Elegir una región europea no «cumple el RGPD» solo: hay que configurar quién accede, qué datos guardas y dónde se replican.

### Relación con otros temas

La red (SG/NACL) se profundiza en el Tema 3: aquí solo anclas que abrir puertos es decisión tuya. El cómputo (Tema 4) decide *dónde* corre el código que asume el rol. Well-Architected (Tema 7) pone la seguridad como **pilar**, no como checklist suelto.

---

## Bloque Ampliación Practitioner (CLF-C02)

En Foundations practicas IAM en el lab; el examen te pide **reconocer** el modelo de responsabilidad compartida, el papel del usuario raíz y qué audita cada servicio. [CloudTrail](#cloudtrail) registra llamadas a la API (quién hizo qué); no mide la CPU de la instancia —eso es CloudWatch (Tema 8).

!!! tip "Para el CLF"
    Si una app comprometida lista buckets, la falla suele ser *en* la nube (tu cuenta), no del centro de datos de AWS. El root lleva MFA; CloudTrail no es CloudWatch. Ampliación, tabla de logos y **autocheck certificación** en [Certificación § Tema 2](../99-certificacion/certificacion.md#tema-2).

**Videotutorial (Practitioner).** [Sesión 2 Cloud Practitioner 2026](https://www.youtube.com/watch?v=XfFq9lKYDPc) (~1 h 53 min). Prioriza seguridad / IAM. Vídeo: Profe Santos Cloud (YouTube).

---

## Videotutorial

**Principal (Foundations).** [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo) (~9 min).

<iframe src="https://www.youtube.com/embed/rEnenbxjOGo" title="IAM en Academy — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Conviene fijarte en usuarios, grupos y políticas en el entorno Academy, y contrastarlo con el rol que asume un servicio.

**Extra (opcional).** [IAM Cloud9](https://www.youtube.com/watch?v=M-TKRBYHWHA) (~24 min) — rol y entorno de desarrollo. Vídeo: Profe Santos Cloud (YouTube).

El **Módulo 4** del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

### PR201 — Usuarios y políticas

* :simple-neutralinojs: **PR201**. (RA2 // d, e, f // **PR 0–10**). Practicas IAM con mínimo privilegio: un usuario o grupo, una policy y la evidencia de una denegación, sin usar el root a diario.

  - Preferente: lab de IAM de Academy (**Módulo 4**).
  - Alternativa (si el lab no está disponible): en la cuenta learner, con supervisión, un usuario **sin** facturación, `ReadOnlyAccess` o la policy del enunciado, MFA si el entorno lo permite, y **borrar** al terminar.

  **Tareas:** confirma que no trabajas como root; crea solo lo que pide el enunciado y anota nombres; prueba una acción denegada; activa MFA si el learner lo permite; borra usuarios/roles/policies y access keys temporales al cerrar.

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR201.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo: [Soluciones · PR201](../90-soluciones/pr/PR201.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Lab / usuario | Recurso creado según enunciado | 0–3 |
| Mínimo privilegio | Evidencia de denegación | 0–3 |
| MFA / buenas prácticas | MFA si aplica; sin root diario | 0–2 |
| Limpieza | Borrado de recursos de lab | 0–2 |
| **Total** | | **/10** |

---

### En la práctica de desarrollo web

Cuando tu API en Node usa el SDK de AWS (S3, SES, etc.), las credenciales **no** van en el front ni en el repositorio. En EC2 o Lambda el SDK toma el **rol** de la instancia o de la función. En el portátil de desarrollo usas un perfil local o variables de entorno **fuera de Git**. Si el lab Academy te da un usuario IAM, trátalo como material sensible: no pegues claves ni capturas con secretos en el `.md` de la práctica, ni en el chat del grupo.

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
Reparto de deberes de seguridad entre AWS (seguridad *de* la nube) y el cliente (seguridad *en* la nube). El límite cambia según uses EC2, RDS, Lambda, etc. En una app DAW: AWS no revisa tu `.env`; tú no proteges el edificio del centro de datos.

**IAM**{: #iam}
*Identity and Access Management*: servicio para gestionar identidades y permisos sobre recursos AWS (usuarios, grupos, roles y políticas). Es el control de acceso de casi todo lo que harás en Foundations: sin IAM coherente, o abres demasiado o bloqueas el lab.

**usuario raíz**{: #usuario-raiz}
También llamado *root*: identidad propietaria de la cuenta AWS. Tiene privilegios totales; no debe usarse para el trabajo diario y debe protegerse con MFA. El examen suele asociarla a acciones de cuenta (cambiar plan de soporte, cerrar la cuenta), no a desplegar la API del TFG.

**root**{: #root}
Sinónimo de [usuario raíz](#usuario-raiz) en la documentación y en el examen. Misma idea: dueño de la cuenta, no identidad de desarrollo diario.

**usuario IAM**{: #usuario-iam}
Identidad IAM pensada para una persona (contraseña de consola y, si se crean, access keys). En labs se usa para practicar políticas; en empresas a menudo se sustituye por federación.

**grupo IAM**{: #grupo-iam}
Conjunto de usuarios IAM que comparten las mismas políticas. No concede permisos por sí solo: hay que adjuntarle policies.

**rol**{: #rol}
Identidad IAM que se *asume* temporalmente (por una persona, una instancia EC2 o un servicio). Evita pegar access keys permanentes en el disco. En desarrollo web es la forma correcta de que la API lea un bucket o escriba logs.

**política**{: #politica}
Documento (suele ser JSON) que permite o deniega acciones sobre recursos (`Effect`, `Action`, `Resource`). Se adjunta a usuarios, grupos o roles. Una policy mal acotada (`*` sobre `*`) convierte un lab en un incidente.

**policy**{: #policy}
Nombre en inglés de [política](#politica). En consola y en el examen verás *policy* / *policies*.

**mínimo privilegio**{: #minimo-privilegio}
Principio de dar solo los permisos necesarios para la tarea, ni más. Reduce el daño si se compromete una identidad. En clase: empieza por denegación y añade lo mínimo para que el lab pase.

**MFA**{: #mfa}
*Multi-factor authentication*: segundo factor (app, hardware…) además de usuario y contraseña. Obligatoria en la práctica seria para el usuario raíz; muy recomendable en cualquier humano que pueda crear recursos de pago.

**access key**{: #access-key}
Par de credenciales de larga duración de un usuario IAM (identificador + secreto) para firmar llamadas a la API. No deben subirse a GitHub ni pegarse en entregas; preferible rol con credenciales temporales.

**ARN**{: #arn}
*Amazon Resource Name*: identificador único de un recurso AWS (por ejemplo `arn:aws:s3:::mi-bucket-lab/*`). Las políticas lo usan en el campo `Resource`.

**política gestionada**{: #politica-gestionada}
Policy creada y mantenida por AWS (o por ti como *customer managed*) que puedes adjuntar a varias identidades. Ejemplo habitual en labs: `ReadOnlyAccess`.

**política insertada**{: #politica-insertada}
Policy *inline* pegada a un solo usuario, grupo o rol. Sirve para permisos muy concretos de esa identidad; si borras la identidad, suele irse con ella.

**cifrado en tránsito**{: #cifrado-en-transito}
Protección de los datos mientras viajan por la red (típicamente TLS/HTTPS). No implica por sí solo que el dato esté cifrado en disco.

**cifrado en reposo**{: #cifrado-en-reposo}
Protección de los datos almacenados (volumen, objeto S3, etc.). Complementa el cifrado en tránsito; son capas distintas.

**security group**{: #security-group}
Cortafuegos con estado asociado a la interfaz de red de una instancia (u otro recurso). Controla qué tráfico de red entra o sale; es otra capa distinta de IAM.

**KMS**{: #kms}
*Key Management Service*: servicio de AWS para crear y controlar claves de cifrado. En Foundations basta reconocerlo; el diseño fino de CMK queda fuera del primer lab.

**CloudTrail**{: #cloudtrail}
Servicio que registra llamadas a la API de AWS (quién hizo qué, cuándo). Es auditoría, no un monitor de CPU. Si necesitas latencia o uso de CPU, miras CloudWatch (Tema 8), no CloudTrail.

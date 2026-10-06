---
title: Tema 4 — Cómputo: EC2, Lambda y contenedores
description: EC2, AMI, tipos de instancia, Lambda, ECS/EKS/Fargate y elección de servicio (Foundations M6).
---

# Tema 4. Cómputo: EC2, Lambda y contenedores

Tres maneras de «correr código» en AWS: **máquina virtual** ([EC2](#ec2) —*Elastic Compute Cloud*, nube elástica de cómputo—), **contenedor** ([ECS](#ecs) / [Fargate](#fargate)) y **función** ([Lambda](#lambda)). El error típico en un proyecto de DAW no es desconocer los logos; es meter una API con WebSocket persistente en Lambda «porque es serverless» o dejar un `t3.large` 24/7 para un cron de treinta segundos. Este tema corresponde al **Módulo 6** de *AWS Academy Cloud Foundations*. Los términos clave están en el [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). La red del Tema 3 ya sitúa la instancia; aquí eliges **dónde corre** el proceso y cuánto pagas por dejarlo encendido.

## Propuesta didáctica

> **RA3.** *Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos.*

### Criterios de evaluación (RA3)

* **d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.
* **f)** Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales.

Balanceo y Auto Scaling: Tema 8. Aquí se *nombra* el ASG como pareja natural de EC2.

### Contenidos

* [EC2](#ec2): [AMI](#ami), familia de instancia, red, compra (On-Demand, Spot, Savings Plans).
* Lambda: evento, duración, coste por invocación.
* ECS, EKS, Fargate: contenedores con o sin nodos cuyo SO tú parcheas.
* Elastic Beanstalk, Lightsail: nombres; cuándo simplifican.

### Programación de aula (orientativa)

| Quincena | En tutoría | Trabajo autónomo / evidencias |
| --- | --- | --- |
| **Q5** | EC2 + AMI + elección VM/Lambda | **PR401**; Autocheck del tema |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Responde con lo que sepas"
    1. Nombra un caso en el que **EC2** encaje mejor que **Lambda** (pista: estado o conexión larga).
    2. ¿Qué es una **AMI** y para qué la usarías al clonar un lab?
    3. ¿**Spot** es un tamaño de instancia (`t3.micro`) o un **modelo de compra**?
    4. ¿Por qué conviene **terminate** (o min=0) al acabar el lab aunque «la dejes para mañana»?
    5. En una frase: ¿qué diferencia hay entre una **VM** y un **contenedor** en quién mantiene el SO?

Este cuestionario es solo para ti: te ayuda a ver qué dominas ya y qué te falta antes o mientras lees el tema. No se entrega en Aules; respóndelo con lo que sepas y, cuando quieras contrastar, abre el bloque **Soluciones (autoevaluación)** debajo o el índice en [Soluciones](../90-soluciones/soluciones.md).

<details markdown="1">
<summary>Soluciones (autoevaluación)</summary>

1. API con **WebSocket** o proceso largo con estado en memoria / puerto persistente: mejor **EC2** (o contenedor) que Lambda «porque es serverless».

2. Una **AMI** es la **plantilla** (SO + software) para lanzar instancias iguales; sirve para clonar el lab sin reinstalar a mano.

3. **Spot** es un **modelo de compra** (capacidad interrumpible más barata), no un tamaño `t3.micro`.

4. Si no **terminate** (o min=0), el lab **sigue facturando** horas, discos y balancers olvidados.

5. En una **VM** gestionas (más) el SO y el proceso; en un **contenedor** empaquetas la app y, con Fargate, dejas de parchear nodos EC2 del clúster.

</details>

---

## Bloque Foundations (Módulo 6)

Imagina la misma **API** de tu proyecto de DAW (Node o PHP, front aparte, base de datos en RDS): puedes desplegarla en una **instancia EC2**, invocarla como **función Lambda** (con adaptaciones) o empaquetarla en **Docker** y correrla en **ECS con Fargate**. Las tres opciones ejecutan código; cambian quién mantiene y actualiza qué, cómo pagas, los límites de duración y si puedes guardar estado en un proceso que escucha un puerto todo el día.

### Amazon EC2

**Qué es en este caso.** **[Amazon EC2](#ec2)** es el servicio de **instancias** (máquinas virtuales) en AWS. Eliges una plantilla (**[AMI](#ami)**, *Amazon Machine Image*, imagen de máquina de Amazon), un **[tipo de instancia](#tipo-de-instancia)** (combinación de **vCPU** —*virtual CPU*, procesador virtual—, RAM y red), la **[VPC](../03-redes-entrega-contenido/tema3.md#vpc)** y la subred, el disco (**[EBS](#ebs)**, *Elastic Block Store*, almacenamiento en bloques elástico, Tema 5) y el [security group](../03-redes-entrega-contenido/tema3.md#security-group). La instancia es un servidor Linux o Windows donde instalas Node, PHP, nginx o Apache y dejas un proceso escuchando un puerto.

**En la práctica.** Es la opción más directa para una API clásica con `listen(3000)`, sesiones en memoria o WebSockets largos. Tú aplicas los **parches del SO**; tú mantienes y actualizas el runtime y las dependencias. Pagas mientras la instancia está en estado *running* (más el disco EBS asociado). En el lab del **Módulo 6** sueles lanzar una instancia con AMI y tipo pequeños; en el **Learner Lab**, si la EC2 debe llamar a S3 u otros servicios, asignas **LabRole** con **LabInstanceProfile** (rol para el servicio, no para tu sesión de consola).

La **[AMI](#ami)** no es la instancia encendida: es la receta (SO + software base). Si cada despliegue reinstala Node a mano, pierdes tiempo además de pagar horas de VM. Cuando la instancia ya está bien configurada, puedes crear una AMI propia y clonar el entorno.

<figure markdown="span">
![Selección de AMI Quick Start en la consola EC2](img/salvador/ec2_1.png){ width="720" }
<figcaption>AMI Quick Start al lanzar una instancia.</figcaption>
</figure>

!!! tip "Crear tu propia AMI (idea Foundations)"
    Cuando la instancia ya tiene el SO y el software «bien», puedes **Actions → Image and templates → Create image**. Así lanzas clones iguales sin reinstalar a mano. En el formulario conviene dejar el *reboot* para snapshot coherente.

<figure markdown="span">
![Menú Actions: Create image desde una instancia en ejecución](img/salvador/ami_create_menu.png){ width="720" }
<figcaption>Crear AMI desde una EC2 que ya está lista.</figcaption>
</figure>

<figure markdown="span">
![Formulario Create image: nombre, reboot y volúmenes](img/salvador/ami_create_form.png){ width="720" }
<figcaption>Nombre de la AMI, reboot para consistencia y volúmenes incluidos.</figcaption>
</figure>

!!! note "Características EC2 (Foundations)"
    - Genera **máquinas virtuales** en la nube (web, correo, ficheros…).
    - El coste depende de RAM, vCPU, disco e [IP elástica](../03-redes-entrega-contenido/tema3.md#ip-elastica) si la usas.
    - Escalable: puedes cambiar tipo (con límites) según necesidad — y **apagando** cuando no hace falta.

#### Tipo de instancia y familia

Un **[tipo de instancia](#tipo-de-instancia)** (por ejemplo `t3.micro`) fija vCPU, memoria y rendimiento de red de plantilla. Las **[familias](#familia-de-instancia)** agrupan perfiles: propósito general (`t`), cómputo (`c`), memoria (`m`), almacenamiento, GPU… **Rightsizing** significa no coger un `2xlarge` porque el tutorial lo traía: para una API de prácticas con poco tráfico, un tipo pequeño suele bastar si el código no es un cuello de botella.

<figure markdown="span">
![Familias y tipos de instancia EC2](img/salvador/ec2_8.png){ width="720" }
<figcaption>Familia / tipo: plantilla de hardware, no el modelo de precio.</figcaption>
</figure>

El **modelo de compra** (On-Demand, Reserved, Savings Plans, Spot) **no** es una familia: Spot puede aplicarse a un `t3.micro` interrumpible.

#### Disco: EBS frente a instance store

**[EBS](#ebs)** es disco en red persistente: sobrevive al *stop* de la instancia si lo configuras así. **[Instance store](#instance-store)** es almacenamiento local ligado al host: más rápido en algunos casos, pero **se pierde** si la instancia termina o falla el hardware subyacente. Para la API del proyecto de DAW y los logs, en Foundations casi siempre piensa en **EBS**; el instance store es un detalle de examen y de cargas muy concretas.

#### Par de claves y user data

El **[par de claves](#par-de-claves)** (*key pair*) sirve para entrar por **[SSH](#ssh)** (*Secure Shell*, acceso remoto cifrado) en Linux si no usas solo Instance Connect. Si generas tu propia clave, **descárgala en el momento**: es la única oportunidad. En Academy a menudo usas `vockey` / `labsuser.pem` según el lab.

<figure markdown="span">
![Descarga / uso del par de claves](img/salvador/ec2_9.png){ width="640" }
<figcaption>Par de claves: sin `.pem` no entras por SSH.</figcaption>
</figure>

**[User data](#user-data)** es un script o cloud-init que la instancia ejecuta al **primer arranque** (instalar paquetes, clonar repo, arrancar servicio). No sustituye a una AMI bien hecha, pero en el lab acelera el «primer boot».

#### Cómo pagas EC2: On-Demand, Reserved, Savings Plans y Spot

| Modelo | Idea | Cuándo tiene sentido |
| --- | --- | --- |
| **On-Demand** | Pagas por hora/segundo sin compromiso | Labs, picos imprevisibles, primer despliegue |
| **Reserved Instances** / compromiso | Descuento a cambio de plazo (1 o 3 años) | Carga estable 24/7 en producción |
| **Savings Plans** | Compromiso de gasto ($/h) flexible entre familias/regiones | Empresa con mix de tipos pero uso predecible |
| **Spot** | Capacidad sobrante, **puede interrumpirse** con aviso | Batch tolerante a fallos, no checkout en vivo |

En un **lab** y en muchas prácticas de DAW usas **On-Demand** y **apagas o terminate** al terminar. **Spot** ahorra, pero AWS puede recuperar la instancia: no es la hipótesis seria para una demo de evaluación que no tolera corte. **Reserved** y **Savings Plans** son decisiones de empresa con uso medido meses, no del ejercicio de un fin de semana.

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| Spot = modelo de precio, no `t3.micro` | No usar Spot para la demo que no puede caerse |
| Distinguir tipo/familia de modelo de compra | Rightsizing antes de Reserved |
| EC2 = tú parcheas el SO | En el `.md`, justificar On-Demand + terminate en labs |

Un `t3.large` 24/7 «porque así va holgado» para una API con pico a las 11:00 factura ociosidad. Tipo más pequeño, apagado fuera de horario (o [Auto Scaling](#auto-scaling) a cero en el Tema 8) y, si el workload es un cron corto, valorar Lambda. El ahorro viene de dejar de pagar lo que no usas.

Al **parar** (*stop*) una instancia dejas de pagar cómputo de esa VM, pero el volumen **EBS** sigue facturando si no lo borras. Al **terminar** (*terminate*) liberas la instancia; los volúmenes *delete on termination* desaparecen con ella según cómo lanzaras el disco. En el lab, **terminate** al cerrar evita sorpresas el lunes.

Conectar por consola con **EC2 Instance Connect** evita pelear con el `.pem` en el portátil del aula: el usuario (`ubuntu`, `ec2-user`…) lo marca la AMI. Si entras por **SSH** con par de claves, el security group debe permitir el puerto 22 **solo** desde tu IP o bastión, no desde todo internet.

### AWS Lambda

**Qué es en este caso.** **[AWS Lambda](#lambda)** ejecuta una **[función](#funcion-lambda)** cuando llega un **[evento](#evento-lambda)** (HTTP vía API Gateway, subida a S3, mensaje en cola, regla de EventBridge…). No gestionas una VM encendida: AWS prepara un entorno efímero, ejecuta tu handler y factura por **invocaciones** y por **GB-segundo** de duración.

**En la práctica.** Encaja en webhooks, transformaciones de imagen, tareas tras un upload o un cron que dura segundos. No encaja en un `listen(3000)` eterno, jobs de horas ni estado en memoria de proceso entre peticiones no relacionadas. Cada invocación tiene un **[timeout](#timeout-lambda)** configurable; en la documentación oficial de Lambda el **tiempo máximo de ejecución por invocación es 15 minutos**. Por encima de ese tope necesitas otro servicio (EC2, contenedor, Step Functions que encadene Lambdas…).

El **[arranque en frío](#cold-start)** (*cold start*) es la latencia extra cuando no hay entorno caliente: importa en APIs muy sensibles al milisegundo; importa menos en un batch nocturno. Mantener y actualizar el runtime lo hace AWS; **tú** mantienes y actualiza el código, las dependencias empaquetadas y el rol de ejecución (permisos IAM).

**Cuándo no usar Lambda para la API del proyecto de DAW.** WebSockets largos, transcodificación de vídeo de horas, depuración con SSH al host o una app Express «tal cual» con sesión en RAM y puerto fijo suelen ir mejor en EC2 o en contenedor.

### Contenedores: Docker, ECR, ECS, EKS y Fargate

**Qué es en este caso.** Un **[contenedor](#contenedor)** empaqueta la aplicación y sus dependencias en una **[imagen](#imagen-contenedor)** (capas de sistema de ficheros). **[Docker](#docker)** es la herramienta habitual para construir y probar esa imagen en local. En AWS guardas imágenes en **[ECR](#ecr)** (*Elastic Container Registry*, registro de contenedores elástico) y las ejecutas con un orquestador.

**En la práctica.** Si en clase ya dockerizas la API, el salto natural es **ECS** (*Elastic Container Service*, servicio de contenedores elástico) con **[Fargate](#fargate)** (AWS gestiona los nodos; tú defines CPU/memoria del *task*). **EKS** (*Elastic Kubernetes Service*, Kubernetes gestionado) tiene sentido cuando el equipo ya estandariza en Kubernetes; para un único contenedor de prácticas suele ser exceso. Con Fargate **no** parcheas el SO de cada nodo EC2 del clúster; sí mantienes y actualiza la imagen de tu app.

| Servicio | Qué aporta | Trade-off didáctico |
| --- | --- | --- |
| **ECR** | Repositorio de imágenes privado en AWS | Hay que publicar imagen antes del despliegue |
| **ECS** | Orquestación propia de AWS | Menos portable que K8s puro |
| **EKS** | Kubernetes gestionado | Más control, más piezas |
| **Fargate** | Cómputo serverless para contenedores | Sin SSH al nodo; menos «tocar el hierro» |

No montamos un clúster de producción en Foundations. Sí debes poder razonar: «esta API ya va en Docker → ECS/Fargate; este script de 20 s → Lambda; este legado con licencia de SO concreta → EC2».

<figure markdown="span">
![Opciones de cómputo: EC2, Lambda, ECS y Fargate](../img/diagramas/computo-opciones.svg){ width="800" }
<figcaption>Misma carga, distinto nivel de gestión: VM, función o contenedor (con o sin nodos).</figcaption>
</figure>

En EC2 el camino del módulo es el de siempre: lanzar en una AZ, security group y conectar. En Lambda no hay `listen`: editas el handler, **Deploy** y **Test**.

<figure markdown="span">
![Diagrama Get started de Amazon EC2](img/capturas/ec2-get-started.png){ width="800" }
<figcaption>Flujo Get started de EC2. Fuente: Amazon EC2 User Guide (AWS).</figcaption>
</figure>

<figure markdown="span">
![Editor de código de AWS Lambda con handler Node.js](img/capturas/lambda-code-editor.png){ width="800" }
<figcaption>Editor de la función: Deploy / Test en la propia consola. Fuente: AWS Lambda Developer Guide (AWS).</figcaption>
</figure>

<figure markdown="span">
![Diálogo de evento de prueba en Lambda](img/capturas/lambda-test-event.png){ width="800" }
<figcaption>Evento de prueba: invocas sin montar API Gateway todavía. Fuente: AWS Lambda Developer Guide (AWS).</figcaption>
</figure>

### Elastic Beanstalk y Lightsail

**Elastic Beanstalk** subes código o artefacto y AWS provisiona EC2, balanceador y despliegue con menos pasos manuales: PaaS (*Platform as a Service*, plataforma como servicio) sobre EC2. **Lightsail** ofrece VPS simplificados con precio plano para sitios pequeños. En un proyecto de DAW con VPC, ALB y RDS diseñados a mano sueles usar EC2 o contenedores; Beanstalk/Lightsail aparecen en el CLF como «acortar camino» cuando no necesitas control fino de red.

### EC2, Lambda y contenedor: la misma API, tres formas

| Dimensión | EC2 | Lambda | ECS + Fargate |
| --- | --- | --- | --- |
| Quién parchea el SO | Tú (instancia) | AWS (entorno gestionado) | AWS (nodo); tú la imagen de app |
| Cómo pagas | Tiempo *running* + EBS | Invocaciones + duración | vCPU/memoria del task + tiempo |
| Estado / puerto | Proceso `listen`, disco local | Efímero por invocación; sin `listen` clásico | Proceso en contenedor; puerto del task |
| Límites didácticos | Disco, tipo, tú escalas (ASG T8) | Timeout máx. 15 min/invocación; cold start | Definición de task; no SSH al nodo |
| Cuándo elegir | API persistente, WebSocket, legado | Eventos cortos, cron, webhook | App ya dockerizada, sin administrar nodos |

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| Lambda no sustituye todo «por moderno» | PR401: comparar estado, duración, coste 24/7 |
| Fargate ≠ gestionar SO del nodo | Docker en clase → ECS/Fargate razonable |
| Beanstalk/Rekognition/SageMaker ≠ «tipo EC2» | Nombrar el servicio correcto en el enunciado |

### Errores frecuentes (cómputo)

Dejar la instancia del lab encendida el fin de semana **sigue facturando** horas y disco aunque nadie entre por SSH, porque el estado *running* consume cómputo. Al terminar, **terminate** (o *stop* si el lab lo pide y entiendes que el EBS puede seguir costando) y deja captura de lista vacía.

Elegir **Spot** para el checkout o una demo en directo **puede interrumpir** la instancia cuando AWS recupera capacidad; el usuario ve caída aunque «ayer funcionaba». Para labs de evaluación usa On-Demand salvo que el enunciado pida Spot y acepte interrupción.

Meter en Lambda una API Express «tal cual» con estado en memoria y puerto fijo **choca** con el modelo por invocación: no hay un proceso eterno escuchando. Hay que reescribir a handler por evento o mover a EC2/contenedor.

Montar **EKS** para un único contenedor de prácticas **añade** plano de control, nodos y curva de aprendizaje que no aportan si ECS/Fargate basta. Reserva EKS para escenarios que ya exigen Kubernetes.

Confundir **tipo** `t3.micro` con **Spot**: el primero es tamaño de hardware; el segundo es forma de compra interrumpible.

### Relación con red y almacenamiento

EC2 sin VPC y security group claros (Tema 3) es un servidor expuesto. El disco principal de la VM suele ser **EBS** (Tema 5); los uploads compartidos entre instancias no se improvisan en el directorio raíz efímero. **[Auto Scaling](#auto-scaling)** (*ASG*, grupo de autoescalado) en el Tema 8 escala **grupos** de instancias EC2; no sustituye elegir bien tipo y modelo de compra.

### Lab del Módulo 6

En *Cloud Foundations*, el **Módulo 6** centra el lanzamiento de **EC2**: AMI, tipo pequeño, red del lab, par de claves o Instance Connect y, a menudo, crear o usar una AMI. Sigue el enunciado del LMS en la **región del lab**. La práctica **PR401** pide además **comparar** ese mismo workload mental con Lambda aunque el lab solo lance la VM. Si practicas en el **Learner Lab**, recuerda **LabRole** / **LabInstanceProfile** cuando la instancia o una Lambda deba llamar a la API de AWS sin access keys en disco.

### Conectar Lambda a HTTP (idea Foundations)

Una API REST en EC2 expone un puerto; en Lambda el patrón habitual es **API Gateway** (u otro disparador) delante de la función. API Gateway recibe HTTPS, valida la ruta y **invoca** la función con un evento JSON; la función devuelve status y cuerpo. No hay un proceso Node eterno: cada petición es una invocación (con posible *cold start*). Para el CLF basta reconocer la pareja «API HTTP → API Gateway → Lambda» frente a «ALB → EC2 con `listen`». En un proyecto intermodular puedes mezclar: front estático en S3, rutas dinámicas en Lambda y sesiones largas en EC2 si el diseño lo exige.

### Lightsail en una frase útil

**Lightsail** agrupa instancia, red simple y precio predecible para sitios pequeños. Si ya diseñaste VPC, subredes privadas, ALB y RDS en el Tema 3, Lightsail no sustituye ese diseño: es atajo para un WordPress o un servidor único sin practicar el mapa completo de red.


---

## Bloque Ampliación Practitioner (CLF-C02)

En el CLF-C02 no basta con nombrar EC2 o Lambda: hay que separar **tipo de instancia** de **modelo de precio** y elegir servicio según estado, duración y quién mantiene el entorno (ECS/Fargate, EKS…). Preguntas trampa mezclan **SageMaker** o **Rekognition** con «un EC2 más grande»: son servicios gestionados de ML, no familias de instancia. Otra trampa es creer que **Auto Scaling** elige por ti Lambda frente a EC2: solo ajusta **cuántas** instancias de un tipo ya elegido hay en el grupo.

Si el enunciado describe **carga interrumpible** y tolerancia a aviso de terminación, piensa **Spot**. Si describe **compromiso a 1–3 años** con uso estable, piensa **Reserved** o **Savings Plans**. Si describe **función ante evento S3**, piensa **Lambda**, no una VM encendida «por si acaso».

!!! tip "Para el CLF"
    Spot es un modelo de compra, no un tamaño `t3.micro`. SageMaker o Rekognition no son «un tipo de EC2». Auto Scaling escala **grupos** de instancias, no sustituye elegir bien el cómputo. Ampliación y **autocheck certificación** en [Certificación § Tema 4](../99-certificacion/certificacion.md#tema-4).

---

## Videotutorial

**Principal (Foundations).** [ATTA AWS Academy 03 EC2 Linux](https://www.youtube.com/watch?v=vdSKZxOVX1A) (~25 min).

<iframe src="https://www.youtube.com/embed/vdSKZxOVX1A" title="ATTA AWS Academy 03 EC2 Linux — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: AMI, tipo pequeño, SG y cómo apagar/terminar; eso es lo que facturas en el lab.

**Extra (opcional).** [Lambda 101](https://www.youtube.com/watch?v=TIeUbq4bCOU) (~14 min) — contraste serverless frente a EC2 24/7. Vídeo: Profe Santos Cloud (YouTube).

**Extra.** [Creación y gestión de EC2](https://www.youtube.com/watch?v=ts9izrtvrqg) — lanzar instancia: AMI, tipo, par de claves y acceso.

<iframe src="https://www.youtube.com/embed/ts9izrtvrqg" title="Creación y gestión de EC2" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

<figure markdown="span">
![Pares de claves al crear una EC2](img/salvador/ec2_4.png){ width="640" }
<figcaption>Par de claves al lanzar la instancia.</figcaption>
</figure>

<figure markdown="span">
![EC2 Instance Connect: usuario de la AMI y botón Connect](img/salvador/ec2_12.png){ width="720" }
<figcaption>Conectar desde consola (Instance Connect): el usuario suele venir de la AMI (`ubuntu`, `ec2-user`…).</figcaption>
</figure>

<figure markdown="span">
![Instancia EC2 en ejecución / consola](img/salvador/ec2_11.png){ width="640" }
<figcaption>Instancia en consola tras el lanzamiento.</figcaption>
</figure>

Abre el **Módulo 6** en tu clase de *Cloud Foundations* y sigue el lab que indique Aules. Usa la región del lab.

---

## Actividad / práctica

### PR401 — Lanzar y comparar cómputo

* :simple-neutralinojs: **PR401**. (RA3 // d, f // **PR 0–10**). Lanzas el lab Academy del **Módulo 6** (EC2 / AMI) y argumentas si ese mismo workload encajaría en **Lambda**, mirando estado, duración y coste 24/7.

  **Tareas:** sigue AMI/región del enunciado con tipo pequeño y SG mínimo; documenta evidencias del lanzamiento; en el `.md`, compara EC2 frente a Lambda (estado, tiempo, puerto persistente, coste); **terminate** las instancias y deja evidencia de lista vacía o parada.

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR401.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo (no sustituye el enunciado): [Soluciones · PR401](../90-soluciones/pr/PR401.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Lab EC2/AMI | Lanzamiento según enunciado | 0–3 |
| Comparación Lambda | Estado, duración, coste 24/7 | 0–4 |
| Limpieza | Terminate / evidencias | 0–2 |
| Claridad del `.md` | Sin quedarse solo en el logo | 0–1 |
| **Total** | | **/10** |

---

### Despliegue: de `npm start` al servicio

En tu portátil de clase, `node server.js` abre el puerto 3000 y el navegador en `localhost` habla con ese proceso. Llevar la **misma API** a AWS no es copiar el comando: cambia quién proporciona la máquina, la red y el ciclo de vida del proceso.

Si eliges **EC2**, primero defines la red (subred y security group del Tema 3) y lanzas una instancia con una **AMI** que ya traiga Linux. Instalas Node o PHP, clonas el repo y arrancas la app. El security group debe permitir tráfico al puerto de la API **solo** desde el ALB o desde el origen que hayas diseñado, no desde todo internet si puedes evitarlo. Necesitas que el proceso sobreviva al cierre de la sesión SSH: **systemd**, **PM2** o similar. Si la instancia tiene IP pública efímera, el front o el DNS deben apuntar al ALB, no a una IP que cambia en cada *stop*.

Si eliges **Lambda**, no exportas un servidor que hace `listen`. Empaquetas un **handler** que recibe evento y contexto, despliegas la función y conectas un disparador (API Gateway, S3, cron…). Cada petición HTTP pasa por API Gateway, que invoca la función; cuando termina, no queda un demonio escuchando el 3000. Adaptas rutas y estado: lo que guardabas en RAM entre peticiones pasa a RDS, ElastiCache o desaparece.

Si eliges **ECS con Fargate**, construyes una **imagen Docker** de la API, la subes a **ECR**, defines un *task* con CPU y memoria y un servicio que mantiene N tareas en marcha. El balanceador (ALB) registra esas tareas como destinos. Mantienes y actualiza la imagen cuando cambia el código; no entras a parchear el SO del nodo.

El criterio del proyecto de DAW no es «cuál suena más moderno», sino **estado**, **duración**, **quién mantiene qué** y **coste** (sobre todo EC2 24/7 frente a invocaciones sueltas). Anótalo en **PR401** aunque el lab del Módulo 6 solo te haga lanzar EC2.

---

## Autocheck del tema

Comprueba cómputo de esta quincena. CLF: [Certificación § Tema 4](../99-certificacion/certificacion.md#tema-4).

1. Una **AMI** es…  
   a) la instancia encendida · b) la plantilla para lanzar instancias · c) un tipo de precio
2. **V/F.** Spot es un tipo de instancia (`t3.micro`).
3. Un cron de 30 s cada hora: hipótesis más razonable en Foundations…  
   a) EC2 24/7 · b) Lambda · c) EKS obligatorio
4. **V/F.** Con Fargate administras tú el SO de cada nodo EC2 del clúster.
5. Empareja: **EC2** · **Lambda** · **ECS+Fargate** con: (a) handler sin `listen` · (b) SSH y SO custom · (c) contenedor sin gestionar nodos

<details markdown="1">
<summary>Soluciones</summary>

1. **b**.

2. **Falso** — Spot es **modelo de precio**, no familia/tipo.

3. **b** (evento corto; EC2 24/7 suele sobrar).

4. **Falso** — Fargate quita la gestión del nodo.

5. **EC2** encaja con (b) SSH y SO a medida; **Lambda**, con (a) handler sin `listen`; **ECS+Fargate**, con (c) contenedor sin gestionar nodos.

</details>

---


## Glosario

**EC2**{: #ec2}
*Elastic Compute Cloud* (nube elástica de cómputo): servicio de **instancias** (máquinas virtuales) en AWS. Tú eliges AMI, tipo, red y almacenamiento; sueles parchear el sistema operativo. Es el análogo más cercano a «tengo un Linux donde instalo Node/Java», con factura por tiempo de vida de la instancia.

**instancia**{: #instancia}
Máquina virtual EC2 en ejecución o parada, creada a partir de una AMI y un tipo concreto. No confundir la instancia con la AMI ni con el tipo de instancia.

**AMI**{: #ami}
*Amazon Machine Image* (imagen de máquina de Amazon): plantilla (SO + software) a partir de la cual se lanzan instancias EC2. No es la instancia en ejecución. Si la «buena» AMI solo vive en el disco de un compañero, el despliegue no es repetible.

**tipo de instancia**{: #tipo-de-instancia}
Combinación publicada de vCPU, RAM y red (p. ej. `t3.micro`). Es hardware de plantilla, no modelo de precio.

**familia de instancia**{: #familia-de-instancia}
Letra inicial del tipo (`t`, `m`, `c`…): perfil de uso (general, memoria, cómputo…). El rightsizing elige familia y tamaño acorde a la carga.

**vCPU**{: #vcpu}
*virtual CPU* (procesador virtual): unidad de cómputo asignada a la instancia según el tipo elegido.

**EBS**{: #ebs}
*Elastic Block Store* (almacenamiento en bloques elástico): volumen de disco en red asociado a EC2, persistente según configuración. Tema 5 profundiza tipos y copias.

**instance store**{: #instance-store}
Almacenamiento local en el host físico: alto rendimiento en algunos tipos, pero los datos se pierden si la instancia termina o falla el hardware.

**par de claves**{: #par-de-claves}
*Key pair*: credencial SSH pública/privada para acceder a instancias Linux. La privada (`.pem`) solo se descarga al crearla si la generas tú.

**SSH**{: #ssh}
*Secure Shell* (acceso remoto cifrado): protocolo habitual para administrar instancias Linux desde terminal. Requiere par de claves o método alternativo (Instance Connect).

**user data**{: #user-data}
Datos de arranque (script cloud-init) que la instancia ejecuta en el primer boot; sirve para bootstrap sin rebakear AMI.

**On-Demand**{: #on-demand}
Modelo de compra EC2 sin compromiso: pagas por tiempo de uso. Habitual en labs.

**Reserved Instances**{: #reserved-instances}
Compromiso de uso (plazo) a cambio de descuento sobre instancias con perfil estable.

**Savings Plans**{: #savings-plans}
Compromiso de gasto en $/h con flexibilidad entre familias y regiones; descuento frente a On-Demand.

**Spot**{: #spot}
Modelo de compra de capacidad sobrante interrumpible; no es un tipo de instancia.

**Lambda**{: #lambda}
Servicio de funciones *serverless*: ejecuta código ante eventos sin mantener una VM encendida. Se factura por invocaciones y duración.

**función Lambda**{: #funcion-lambda}
Unidad desplegada (código + runtime + configuración) que AWS invoca ante un evento.

**evento Lambda**{: #evento-lambda}
Disparador (API Gateway, S3, cola, cron…) que provoca una invocación de la función.

**cold start**{: #cold-start}
Latencia extra al arrancar un entorno nuevo para atender una invocación tras periodo inactivo.

**timeout Lambda**{: #timeout-lambda}
Tiempo máximo de una invocación; en la documentación oficial de AWS el límite configurable llega a **15 minutos** por invocación.

**contenedor**{: #contenedor}
Proceso aislado empaquetado con dependencias; en DAW suele ser la API dockerizada.

**imagen de contenedor**{: #imagen-contenedor}
Plantilla inmutable de capas a partir de la cual se crean contenedores (p. ej. `mi-api:1.0`).

**Docker**{: #docker}
Herramienta para construir, probar y publicar imágenes de contenedor en local y en CI.

**ECR**{: #ecr}
*Elastic Container Registry*: registro privado de imágenes Docker en AWS.

**ECS**{: #ecs}
*Elastic Container Service*: orquestación de contenedores gestionada por AWS (no Kubernetes nativo).

**EKS**{: #eks}
*Elastic Kubernetes Service*: Kubernetes gestionado en AWS; más piezas que ECS para un solo contenedor de prácticas.

**Fargate**{: #fargate}
Modo de ejecución serverless para contenedores en ECS/EKS: AWS gestiona nodos; tú defines task/pods.

**Elastic Beanstalk**{: #elastic-beanstalk}
PaaS de AWS que despliega aplicaciones sobre EC2 gestionadas con menos pasos manuales.

**Auto Scaling**{: #auto-scaling}
Servicio que ajusta el número de instancias EC2 (u otros recursos) según demanda; detalle en Tema 8.

**Lightsail**{: #lightsail}
Servicio de VPS simplificados con precio plano; atajo para sitios pequeños, no sustituto del diseño VPC+ALB+RDS del módulo de redes.


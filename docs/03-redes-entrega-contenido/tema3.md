---
title: Tema 3 — Redes, VPC y entrega de contenido
description: VPC, subredes, rutas, seguridad de red, CloudFront y Route 53 (Foundations Módulo 5).
---

# Tema 3. Redes, VPC y entrega de contenido

Tu front y tu API (interfaz de programación de aplicaciones) no «salen a internet» solos: viven en una **[VPC](#vpc)** (*Virtual Private Cloud*, nube virtual privada), en **[subredes](#subnet)** ligadas cada una a una zona de disponibilidad (**AZ**, *Availability Zone*), con tablas de rutas y cortafuegos. Este tema corresponde al **Módulo 5** de *AWS Academy Cloud Foundations*: el mínimo para publicar un servidor web sin abrir SSH al mundo. No sustituye a un módulo de redes locales; aquí el rango de direcciones cabe en un esquema sencillo y el trade-off es **qué expones** frente a **cómo sales a internet**. Los términos clave están en el [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). Trae claro el mapa región/AZ del Tema 1: aquí decides dónde queda el balanceador, la API y la base de datos (BD), y qué tráfico entra o sale.

## Propuesta didáctica

> **RA3.** *Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos.*

### Criterios de evaluación (RA3)

* **a)** Se ha realizado el diseño y configuración de redes virtuales privadas.
* **b)** Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas.
* **c)** Se ha participado activamente en la creación y configuración de una red funcional.

Cómputo (tipos de instancia, Lambda) es el Tema 4. Balanceo y autoescalado: Tema 8.

### Contenidos

* VPC, CIDR, subredes (una AZ cada una), tablas de rutas, puerta de enlace a internet y NAT.
* Security groups frente a NACL; subred pública frente a privada.
* Route 53 y CloudFront: DNS y CDN.
* VPN frente a Direct Connect (cuándo merece un enlace dedicado).

### Programación de aula (orientativa)

| Quincena | En tutoría | Trabajo autónomo / evidencias |
| --- | --- | --- |
| **Q4** | VPC pública/privada + SG | **PR301**; Autocheck del tema |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Responde con lo que sepas"
    1. ¿Qué es una **VPC** en una frase, sin inventar CIDR todavía?
    2. ¿En qué se diferencia una subred **pública** de una **privada** (ruta a internet)?
    3. ¿Security group o NACL: cuál usas casi siempre en el lab de una API web, y por qué?
    4. ¿Por qué abrir **3306** o **22** a `0.0.0.0/0` es un anti-patrón aunque «así conectas desde casa»?
    5. ¿CloudFront acerca el **contenido** al usuario o replica tu base de datos al borde?

Este cuestionario es solo para ti: te ayuda a ver qué dominas ya y qué te falta antes o mientras lees el tema. No se entrega en Aules; respóndelo con lo que sepas y, cuando quieras contrastar, abre el bloque **Soluciones (autoevaluación)** debajo o el índice en [Soluciones](../90-soluciones/soluciones.md).

<details markdown="1">
<summary>Soluciones (autoevaluación)</summary>

1. Una **VPC** es tu red virtual aislada lógica en **una** región de AWS: el espacio donde colocas front, API y datos.

2. **Pública:** tiene ruta hacia el Internet Gateway (puede recibir o enviar tráfico a internet según el diseño). **Privada:** no tiene esa ruta directa; si necesita salir, usa un NAT Gateway, sin aceptar entradas no solicitadas desde internet.

3. Casi siempre el **security group** (cortafuegos con estado, ligado a la interfaz de la instancia). La NACL filtra a nivel de subred, no guarda estado y es más fácil de romper en el lab.

4. Expone SSH o el motor de la BD a **todo internet**: escaneo, fuerza bruta e incidentes. Mejor un bastión, una VPN o un security group que solo acepte desde el security group de la API.

5. CloudFront acerca **contenido** cacheable (estáticos, respuestas cacheables); **no** replica tu base de datos a las ubicaciones de borde.

</details>

---

## Bloque Foundations (Módulo 5)

### VPC: tu red virtual en una región

Una **[VPC](#vpc)** (*Virtual Private Cloud*, nube virtual privada) es una red virtual **aislada lógicamente** dentro de **una** región de AWS. En ella defines el rango de direcciones **IP** (*Internet Protocol*, protocolo de internet), partes ese rango en **[subredes](#subnet)**, decides las **[tablas de rutas](#tabla-de-rutas)** y conectas (o no) la red a internet. No es un edificio físico: es el espacio de direcciones y de rutas donde AWS coloca tus interfaces de red. Para un proyecto de DAW (front en S3, API Node o PHP en EC2, base en RDS), la VPC es el sitio donde viven el balanceador, las instancias de la API y la base de datos. Sin diseñarla, o publicas de más o la app no llega a internet cuando debe.

Eliges un bloque **[CIDR](#cidr)** (*Classless Inter-Domain Routing*, enrutamiento entre dominios sin clases): una notación que dice «desde esta IP, cuántas direcciones caben». Un ejemplo habitual en labs es `10.0.0.0/16`. El prefijo `/16` significa que los primeros 16 bits identifican la red y el resto (16 bits) quedan para hosts: sobre el papel son 65 536 direcciones. Ese margen te permite crear varias subredes sin pelearte por el espacio. Dentro de ese bloque, una subred `10.0.1.0/24` usa 256 direcciones (menos las que AWS reserva). El `/24` es más pequeño, cabe cómodo en una sola AZ y deja claro el límite de esa pieza. El `/16` de la VPC agrupa todos esos `/24` bajo el mismo bloque. Si eligieras un `/28` minúsculo «porque solo tengo dos instancias», te quedarías sin IPs en cuanto añadas el ALB, el NAT y otra AZ.

!!! note "IPs que AWS se reserva en cada subred"
    En el CIDR de una subred, AWS reserva **cinco** direcciones (no las asignes a una EC2): la de red, la de la puerta de enlace virtual, la del DNS de la VPC, una reservada y la de *broadcast*. Ejemplo en `10.0.0.0/24`: `.0`, `.1`, `.2`, `.3` y `.255` no son tuyas para instancias. Por eso un `/24` no te deja 256 EC2 útiles: resta esas cinco y planifica.

Cada **[subred](#subnet)** vive en **una** AZ (*Availability Zone*, zona de disponibilidad). Por eso la alta disponibilidad implica al menos dos subredes (en dos AZ), no un único `/24` enorme «para ahorrar». Si una AZ cae y toda tu API estaba en una sola subred, no hay magia de «HA» que te salve.

#### Subred pública

**Qué es en este caso.** Una subred cuya **tabla de rutas** envía el tráfico destinado a internet (`0.0.0.0/0`) hacia un **[Internet Gateway](#igw)** (*IGW*, puerta de enlace a internet). Los recursos que deban ser alcanzables desde internet (o salir con IP pública) suelen ir aquí, con [IP pública](#ip-publica) o [elástica](#ip-elastica) según el diseño. «Pública» no significa «sin seguridad»: significa que *puede* hablar con internet según las rutas y los cortafuegos.

**En la práctica.** En un proyecto de DAW típico colocas aquí el **ALB** (*Application Load Balancer*, balanceador de carga de aplicación; familia **ELB**, *Elastic Load Balancing*) o, en labs más simples, una EC2 que sirve **HTTP** / **HTTPS** (*Hypertext Transfer Protocol* / *Hypertext Transfer Protocol Secure*). El usuario llega por HTTPS a ese punto; no debería llegar directo al puerto de la API (3000, 8080…) ni al de MySQL (3306) o PostgreSQL (5432).

#### Subred privada

**Qué es en este caso.** Una subred **sin** ruta directa al Internet Gateway. Los recursos no reciben conexiones no solicitadas desde internet. Si necesitan salir (aplicar parches del SO, `npm install`, llamar a una API externa), usan un **[NAT Gateway](#nat-gateway)** (*Network Address Translation*, traducción de direcciones de red) colocado en una subred pública. La salida la inicia la instancia privada; internet no «entra a llamar» por ese camino.

**En la práctica.** Aquí van la API en EC2 y la base en RDS. El ALB (en pública) habla con el security group de la API; la API habla con el security group de RDS. Nadie desde internet abre el 22 o el 3306 «porque así conecto desde casa». Si necesitas administrar la instancia, usas un bastión, una VPN o Session Manager —no un agujero permanente a `0.0.0.0/0`.

#### Tabla de rutas, Internet Gateway y NAT Gateway

**Qué es en este caso — tabla de rutas.** Es el conjunto de reglas que decide el siguiente salto de cada destino: tráfico local dentro de la VPC, hacia el IGW o hacia el NAT. Sin mirar la tabla de rutas, el dibujo de «subred privada» es solo un nombre en la consola.

**En la práctica — tabla de rutas.** El error típico es llamar «privada» a una subred que aún tiene ruta `0.0.0.0/0 → IGW`. Otro error es crear el IGW y olvidar asociar la tabla a la subred correcta. Comprueba siempre **Subnet → Route table**.

**Qué es en este caso — Internet Gateway (IGW).** Es la puerta de la VPC hacia internet para recursos con ruta e IP pública. Sin IGW (y sin la ruta), la subred no es pública aunque el diagrama diga otra cosa.

**En la práctica — IGW.** Adjuntas un IGW a la VPC y apuntas la ruta por defecto de las subredes públicas a ese IGW. El ALB o la EC2 pública salen y entran por ahí. La BD no debería tener IP pública ni ruta al IGW.

**Qué es en este caso — NAT Gateway.** Permite que instancias en subred **privada** inicien conexiones **salientes** a internet (parches del SO, descarga de paquetes) sin aceptar entradas no solicitadas. No es un balanceador: no publica tu API al mundo.

**En la práctica — NAT.** El NAT vive en una subred **pública** (necesita llegar al IGW) y la tabla de rutas de la subred privada apunta `0.0.0.0/0` al NAT. Así la API puede hacer `apt update` o `npm install` sin exponer el puerto 22. Si el lab no monta NAT, anótalo: o no hay salida, o la instancia está en pública «para simplificar».

#### Caso DAW: ALB pública, API y RDS privadas

Un diseño didáctico sólido (y el que conviene tener en la cabeza aunque el lab simplifique) es este:

1. Subredes públicas en dos AZ: **ALB** (y el NAT, si hace falta salida).
2. Subredes privadas en esas mismas AZ: **EC2** con la API Node o PHP, y **RDS** con MySQL o PostgreSQL.
3. Security group del ALB: 443 desde internet (y 80 solo si rediriges a HTTPS).
4. Security group de la API: solo tráfico desde el security group del ALB (puerto de la app).
5. Security group de RDS: solo desde el security group de la API (puerto 3306 o 5432).

El primer lab de Academy a menudo deja un único servidor HTTP en subred pública: vale para aprender rutas y security groups. En el `.md` debes saber **qué simplificaste** respecto a este patrón. Si en el lab solo hay una AZ, di que es simplificación didáctica, no el diseño de un proyecto intermodular en producción.

<figure markdown="span">
![VPC con IGW, subnet pública (ALB y NAT) y subnet privada (EC2 y RDS)](../img/diagramas/vpc-subredes.svg){ width="800" }
<figcaption>Patrón didáctico Foundations: exposición controlada en pública; API y datos en privada.</figcaption>
</figure>

<figure markdown="span">
![Ejemplo oficial de VPC con subnets privadas](img/capturas/vpc-subnets-privadas.png){ width="800" }
<figcaption>VPC con subnets privadas (patrón de la guía). Fuente: Amazon VPC User Guide (AWS).</figcaption>
</figure>

| Pieza | Para qué sirve | Error típico |
| --- | --- | --- |
| **Subred** | Trozo del CIDR en una sola AZ | Pensar que una subred cruza dos AZ |
| **Tabla de rutas** | Decide el siguiente salto (local, IGW, NAT) | Subred «privada» con ruta al IGW |
| **Internet Gateway** | Entrada y salida a internet con IP pública | Poner la BD con IP pública «para conectar desde casa» |
| **NAT Gateway** | Salida desde subred privada sin inbound desde internet | Confundirlo con un balanceador de carga |
| **Security group** | Cortafuegos con estado en la interfaz de red | Abrir el puerto 22 a `0.0.0.0/0` |
| **NACL** | Cortafuegos sin estado en la subred | Olvidar la regla de retorno |

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| Subred = una AZ; pública tiene ruta al IGW; privada sale con NAT | Dibujar ALB en pública y API/RDS en privada antes de abrir el lab |
| Reconocer IGW frente a NAT | En el entregable, justificar por qué la BD no tiene IP pública |
| CIDR coherente VPC / subred | Explicar por qué `10.0.0.0/16` y `10.0.1.0/24` (espacio y tamaño) |

### Security groups frente a NACL

El **[security group](#security-group)** (SG) es un cortafuegos **con estado** (*stateful*, «con estado») asociado a la interfaz de red de la instancia (**ENI**, *elastic network interface*, interfaz de red elástica). Si permites una conexión entrante (por ejemplo **TCP** —*Transmission Control Protocol*— puerto 443), el tráfico de retorno de esa misma conexión se permite sin otra regla. Es la herramienta habitual en Foundations: puerto 443 desde internet hacia el ALB; desde el SG del ALB hacia el SG de la API.

La **[NACL](#nacl)** (*network access control list*, lista de control de acceso de red) es un cortafuegos **sin estado** (*stateless*) a nivel de **subred**. Hay que permitir explícitamente la ida y la vuelta (puertos efímeros incluidos). Sirve como capa extra; en el lab es fácil romperla si editas reglas «por completar» sin plan.

**Qué es en este caso — security group.** Reglas *allow* sobre quién puede hablar con la ENI. Lo que no permites, queda denegado. Puedes referenciar otro security group como origen: «acepta solo desde el SG del ALB» es más limpio que pegar CIDR de IPs que cambian.

**En la práctica — security group.** En el lab del servidor web, 80/443 hacia quien deba (internet o el balanceador). Administración (22/3389) restringida a tu IP o a un bastión si el lab lo permite. Abrir `0.0.0.0/0` en 22 «un rato» suele acabar en olvido y en escaneo desde internet.

**Qué es en este caso — NACL.** Filtro de la subred entera, evaluado por número de regla, sin memoria de la conexión. Si permites el 443 de entrada, también tienes que permitir el retorno por los puertos efímeros; si no, «no carga la web» y pierdes media hora.

**En la práctica — NACL.** Si el enunciado del Módulo 5 no pide tocar la NACL, deja la por defecto y trabaja con security groups. En el examen CLF sí debes reconocer la diferencia de estado.

| | Security group | NACL |
| --- | --- | --- |
| Dónde actúa | Interfaz de red (instancia u otro recurso) | Subred entera |
| Estado | Con estado: el retorno de una conexión permitida pasa | Sin estado: ida y vuelta van en reglas distintas |
| Uso habitual en el módulo | Casi todo el control de 80/443/SSH/BD | Solo si el enunciado lo pide |
| Error típico | `0.0.0.0/0` en administración | Olvidar el puerto de retorno |

<figure markdown="span">
![Diagrama de security groups en EC2](img/capturas/ec2-security-groups.png){ width="800" }
<figcaption>SG a nivel de ENI: allow explícito, resto denegado. Fuente: Amazon EC2 User Guide (AWS).</figcaption>
</figure>

En la práctica diaria del módulo casi todo se decide con security groups. Si el enunciado no pide NACL, no inventes reglas simétricas «por relleno».

Una sola EC2 con IP pública, Node en el puerto 3000 abierto al mundo y MySQL en el mismo host suele «funcionar» en el aula y fallar en cuanto alguien escanea internet. Con ALB en pública y API más RDS en privada, el usuario sigue llegando por HTTPS y tú dejas de exponer SSH y el puerto del motor. Ese cambio no es cosmética: es el mismo criterio de mínimo privilegio que viste en IAM, aplicado a puertos y orígenes.

### DNS y entrega de contenido

Cuando alguien escribe `midominio.es` en el navegador, hace falta traducir el nombre a una dirección o a un balanceador. **[Route 53](#route-53)** es el servicio de **DNS** (*Domain Name System*, sistema de nombres de dominio) de AWS: zonas autoritativas, comprobaciones de salud (*health checks*) y políticas básicas de enrutamiento. Route 53 no sustituye al ALB ni a CloudFront: resuelve el nombre hacia ellos.

**[CloudFront](#cloudfront)** es la **CDN** (*content delivery network*, red de entrega de contenido) de AWS: guarda copias cacheables cerca del usuario en **[ubicaciones de borde](#edge-location)** (*edge locations*). Acerca HTML, JS, CSS e imágenes; **no** replica tu base de datos transaccional a otra región ni a Tokio. El origen suele ser un bucket S3 (front estático del proyecto de DAW) o un ALB / origen HTTP.

En Foundations el flujo habitual es: el dominio en Route 53 apunta a un ALB o a CloudFront; CloudFront toma el origen en S3 o en el balanceador y reduce la latencia de lo cacheable. *Global Accelerator* (IPs anycast) aparece como nombre de examen; no lo necesitas para el lab del Módulo 5.

**Qué es en este caso — Route 53.** El registro DNS que hace que `api.midominio.es` apunte al ALB (o a CloudFront delante del front).

**En la práctica — Route 53.** En el lab a menudo usas la URL del ALB o de la instancia sin dominio propio. En un proyecto intermodular sí tendrás dominio: el registro A/ALIAS o CNAME debe apuntar al recurso correcto, no «a la IP de la EC2 de esta semana» si esa IP cambia.

**Qué es en este caso — CloudFront.** Capa de caché y terminación en el borde para contenido que se puede servir muchas veces igual.

**En la práctica — CloudFront.** Encaja con el front estático en S3 y con assets. No encaja cuando cada petición es una consulta con datos personales al origen: la CDN no sustituye a la API ni mueve RDS. El checkout dinámico sigue golpeando el origen; los CSS del tema, no.

### Flujo de una petición HTTP

Imagina que un usuario abre `https://midominio.es/productos` en un proyecto de DAW con front en S3 detrás de CloudFront, API en EC2 detrás de un ALB y datos en RDS. El lab del Módulo 5 a veces lo reduce a un solo servidor web; igual debes poder contar el camino completo.

Primero el navegador pregunta al DNS (Route 53 u otro resolutor) qué destino tiene ese nombre. La respuesta puede ser la distribución de CloudFront o, si no hay CDN, el nombre del ALB. Con eso el cliente ya sabe a quién hablar por HTTPS.

Si hay CloudFront, la petición llega a una ubicación de borde. Si el objeto está en caché y la política de TTL lo permite, CloudFront responde desde ahí y el origen (S3 o el ALB) no se entera. Si no hay caché o la petición no es cacheable, CloudFront pide el contenido al origen y, según la configuración, puede guardarlo para la siguiente.

Cuando el origen es el ALB (o cuando no hay CDN), el balanceador vive en subredes públicas y acepta HTTPS según su security group (443 desde internet, o desde CloudFront si el origen está restringido). El ALB elige un destino sano del grupo de destinos —las instancias de la API en subred privada— y reenvía la petición. Eso solo funciona si el security group de la API permite tráfico **desde el security group del ALB** en el puerto de la aplicación. Si el SG de la API solo acepta tu IP de casa, el ALB recibe fallos de *health check* y ves *502* o destinos no sanos.

La API (Node o PHP) ejecuta la lógica. Si necesita datos, abre una conexión **TCP** al puerto del motor en RDS. El security group de RDS debe aceptar ese puerto **solo** desde el security group de la API (o desde la subred privada de la API, según diseño). Abrir 3306 a `0.0.0.0/0` «para probar con DBeaver desde el instituto» rompe el patrón entero: cualquier escáner de internet puede intentar fuerza bruta contra el motor.

La respuesta JSON o HTML vuelve por el mismo camino: RDS → API → ALB → (CloudFront si aplica) → navegador. Si en algún tramo falta la regla de retorno en una NACL (sin estado), o bloqueaste el SG, el fallo se ve como timeout aunque «la instancia esté en marcha».

En un lab corto a veces se simplifica a una EC2 pública con 80 abierto. En el `.md` debes poder decir qué simplificaste y por qué: la rúbrica premia que sepas la diferencia, no que copies un diagrama vacío.

| Examen CLF | Clase DAW / empresa |
| --- | --- |
| CloudFront acerca contenido cacheable; no mueve RDS | Front en S3 + CloudFront; API detrás del ALB |
| Route 53 resuelve nombres; no sustituye al balanceador | Apuntar el dominio al ALB o a CloudFront según el diseño |
| SG con estado frente a NACL sin estado | Preferir SG; justificar NACL solo si el enunciado lo pide |

### Enlace híbrido: VPN y Direct Connect

Si el backend del instituto o del cliente sigue en un CPD (centro de proceso de datos) y la API nueva está en AWS, hace falta un enlace entre ambos mundos. No todo vive «solo en la nube» desde el día uno.

**Qué es en este caso — VPN.** Una **[VPN](#vpn)** (*virtual private network*, red privada virtual) sitio a sitio cifra el tráfico, a menudo por internet, entre tu red on-premises y la VPC. Montas un túnel IPsec (u otra tecnología que indique el escenario) y las redes se ven a través de ese túnel.

**En la práctica — VPN.** Encaja para pruebas, para conectar el CPD del cliente con un caudal moderado y para escenarios donde importa cifrar sin esperar a un circuito dedicado. En Foundations no configuras la VPN del lab típico del Módulo 5; sí la reconoces en el CLF-C02 cuando el enunciado habla de un enlace cifrado por internet.

**Qué es en este caso — Direct Connect.** Un **[Direct Connect](#direct-connect)** es un enlace de red **dedicado** (no el internet genérico de casa) entre tu ubicación y AWS. El tráfico no viaja por la misma ruta genérica que el resto de internet público de la misma forma que una VPN sobre ADSL.

**En la práctica — Direct Connect.** Tiene sentido cuando el caudal estable y la previsibilidad importan más que un lab de aula: sincronizaciones grandes, aplicaciones sensibles a la variación del camino público, contratos donde el enlace dedicado es requisito. En Foundations solo debes **reconocer** el escenario del examen: mucho tráfico estable al CPD → Direct Connect; prueba rápida y cifrada → VPN. No inventamos precios ni latencias aquí: eso lo marca el contrato y la ubicación.

En un proyecto de DAW casi nunca montarás Direct Connect; sí debes saber nombrarlo cuando el enunciado del CLF-C02 lo describa. Un [VPC endpoint](#vpc-endpoint) es otra pieza distinta: permite alcanzar servicios de AWS (por ejemplo S3) desde la VPC sin salir por internet público; no sustituye a Direct Connect hacia el CPD del cliente.

### Relación con cómputo y balanceo

La VPC fija el mapa de red; EC2 y Lambda (Tema 4) son los recursos que ejecutan código; el ALB y el Auto Scaling (Tema 8) reparte y escala *dentro* de esa red. Sin CIDR y subredes claras, el resto de labs falla con timeouts, sin ruta al IGW o con un security group que no cuadra. Cuando en el Tema 4 lances una instancia, la pregunta no es solo «¿qué AMI?» sino «¿en qué subred y con qué security group?». Cuando en el Tema 8 montes un ALB, la pregunta es «¿en qué subredes públicas van los nodos del balanceador y hacia qué destinos privados reenvían?».

### Qué suele pedir el lab del Módulo 5 (sin inventar pasos)

En Academy el lab del **Módulo 5** trabaja VPC, subredes, rutas y un servidor web alcanzable. El detalle exacto (asistente *VPC and more*, una sola AZ, nombre de cada recurso, si hay NAT o no) lo marca el LMS de tu clase: **no inventamos aquí capturas ni clics que no hayamos verificado**. Lo que sí debes llevar al `.md` es siempre el mismo criterio: CIDR y AZ de cada subred, qué subred tiene ruta al IGW, qué reglas tiene el security group y que la administración no quede abierta a todo internet. Usa la **región que permita el lab**. Si el lab simplifica a una sola subred pública, anota la simplificación y relaciona el resultado con el patrón ALB / API / RDS del apartado anterior.

---

## Bloque Ampliación Practitioner (CLF-C02)

El examen insiste en **dónde** publicas (ALB o CloudFront frente a base en privada), qué hace una CDN y la diferencia de estado entre security group y NACL. VPN y Direct Connect solo hay que reconocerlos: si el escenario describe un enlace dedicado al CPD, Direct Connect; si describe un túnel cifrado por internet para conectar redes, VPN.

!!! tip "Para el CLF"
    Publica el tráfico en el borde o en el balanceador; deja la base en subred privada. CloudFront acerca contenido cacheable: no «mueve» RDS al borde. El security group lleva estado; la NACL, no. Ampliación y **autocheck certificación** en [Certificación § Tema 3](../99-certificacion/certificacion.md#tema-3).

**Videotutorial (CDN / DNS).** [CloudFront - S3 - Route 53 (Static Web)](https://www.youtube.com/watch?v=DgQroj70CJ0) (~19 min). Vídeo: Profe Santos Cloud (YouTube).

---

## Videotutorial

**Principal (Foundations).** [VPC](https://www.youtube.com/watch?v=u0Kh0JRK4zk) (~16 min).

<iframe src="https://www.youtube.com/embed/u0Kh0JRK4zk" title="VPC — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Conviene fijarte en el CIDR, las subredes y la salida a internet, y anotar qué queda público y qué privado.

**Extra (opcional).** [VPC EC2 RDS](https://www.youtube.com/watch?v=I0nL0NX4qZc) (~40 min) — demo de red con cómputo y base; útil antes del lab del Módulo 5. Vídeo: Profe Santos Cloud (YouTube).

En tu clase de *Cloud Foundations* de Academy, abre el **Módulo 5** (redes / VPC) y sigue el lab que indique el LMS (sistema de gestión del aprendizaje). Usa la región que permita ese lab.

---

## Actividad / práctica

### PR301 — VPC y servidor web

* :simple-neutralinojs: **PR301**. (RA3 // a, b, c // **PR 0–10**). Montas (o completas) el lab Academy del **Módulo 5** de VPC y servidor web: subredes, rutas y security group coherentes con una API publicada sin abrir administración al mundo.

  **Tareas:** anota el CIDR de la VPC y el de cada subred con su AZ; verifica la ruta al IGW solo en la subred pública; captura el security group (puertos 80/443 y administración restringida si el lab lo permite); termina los recursos en el orden que indique el lab (suele ser instancia → volúmenes o ENI → IGW → subredes → VPC).

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR301.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo: [Soluciones · PR301](../90-soluciones/pr/PR301.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| VPC / subredes | CIDR y AZ documentados | 0–3 |
| Rutas e IGW | Pública frente a privada coherente | 0–2 |
| Security group | Puertos justificados; sin `0.0.0.0/0` innecesario | 0–3 |
| Limpieza | Recursos de lab terminados | 0–2 |
| **Total** | | **/10** |

---

## Autocheck del tema

Comprueba VPC y entrega de este tema. CLF: [Certificación § Tema 3](../99-certificacion/certificacion.md#tema-3).

1. **V/F.** Una subred puede cruzar dos AZ «para tener alta disponibilidad gratis».
2. El **security group**…  
   a) no tiene estado · b) recuerda conexiones establecidas · c) sustituye al IGW
3. ¿Para qué sirve un **NAT Gateway** si ya hay IGW?
4. Empareja: **IGW** · **NACL** · **CloudFront** con: (a) puerta a internet de la VPC · (b) filtro a nivel de subred (sin estado) · (c) CDN en el borde
5. **V/F.** CloudFront «mueve» RDS a la ubicación de borde más cercana al alumno.

<details markdown="1">
<summary>Soluciones</summary>

1. **Falso** — una subred = una AZ.

2. **b**.

3. Salida a internet desde subredes **privadas** sin aceptar entradas no solicitadas (parches del SO, `npm`…).

4. El **IGW** es (a) la puerta a internet de la VPC; la **NACL**, (b) el filtro a nivel de subred sin estado; **CloudFront**, (c) la CDN en el borde.

5. **Falso** — cachea contenido; no traslada la base de datos.

</details>

---


## Glosario

**VPC**{: #vpc}
*Virtual Private Cloud* (nube virtual privada): red virtual aislada lógicamente en una región AWS donde colocas subredes, rutas y recursos (EC2, bases de datos, etc.). Es el espacio de red de tu app web: sin VPC bien planteada, publicas de más o no sales a internet cuando toca.

**subnet**{: #subnet}
Subred: trozo del CIDR de la VPC asociado a **una** zona de disponibilidad. No cruza dos AZ. Por eso la alta disponibilidad implica al menos dos subredes (y suele implicar dos AZ).

**CIDR**{: #cidr}
*Classless Inter-Domain Routing*: notación de rango de direcciones IP (p. ej. `10.0.0.0/16` para la VPC y `10.0.1.0/24` para una subred). Define el tamaño del bloque.

**IGW**{: #igw}
*Internet Gateway* (puerta de enlace a internet): puerta de la VPC hacia internet para recursos con ruta e IP pública. Sin IGW (y sin ruta), una subred «pública» no lo es.

**NAT Gateway**{: #nat-gateway}
*Network Address Translation Gateway*: permite que recursos en una subred **privada** inicien conexiones salientes a internet (parches del SO, `npm`) sin aceptar entradas no solicitadas. No es un balanceador ni sustituye al IGW para publicar un front.

**security group**{: #security-group}
Cortafuegos **con estado** a nivel de interfaz de red (instancia). Si permites una conexión, el tráfico de retorno asociado se permite. Es la herramienta habitual para controlar 80/443/SSH en labs Foundations.

**NACL**{: #nacl}
*Network ACL* (lista de control de acceso de red): cortafuegos **sin estado** a nivel de subred. Hay que permitir explícitamente ida y vuelta. Útil como capa extra; fácil de romper si se edita sin plan.

**CloudFront**{: #cloudfront}
CDN (*content delivery network*) de AWS: cachea contenido en ubicaciones de borde cerca de los usuarios. Origina típicamente en S3 o en un balanceador. Acerca estáticos; no mueve tu base de datos transaccional al borde.

**tabla de rutas**{: #tabla-de-rutas}
Conjunto de reglas que decide el siguiente salto de cada destino (local, IGW, NAT, peering…). Define si una subred es pública o privada en la práctica.

**IP pública**{: #ip-publica}
Dirección alcanzable desde internet, asociada a un recurso en subred con ruta al IGW. Distinta de la IP privada dentro de la VPC.

**IP elástica**{: #ip-elastica}
*Elastic IP*: dirección pública fija que puedes asociar o mover entre recursos en la cuenta (según cuotas). Útil cuando necesitas una IP estable; en muchos diseños el ALB evita pegar una EIP a cada instancia.

**VPC endpoint**{: #vpc-endpoint}
Punto de enlace que permite alcanzar servicios de AWS (por ejemplo S3) desde la VPC sin salir por internet público. Aparece en políticas IAM como condición (`aws:SourceVpce`).

**Route 53**{: #route-53}
Servicio DNS de AWS: traduce nombres de dominio a direcciones o a recursos (ALB, CloudFront…). No sustituye al balanceador ni a la CDN.

**edge location**{: #edge-location}
Ubicación de borde de la red de AWS donde CloudFront (y otros servicios de borde) cachea o termina tráfico cerca del usuario. No es una AZ de cómputo de tu VPC.

**VPN**{: #vpn}
*Virtual private network* (red privada virtual): enlace cifrado, a menudo por internet, entre tu red on-premises y la VPC (sitio a sitio) u otros escenarios.

**Direct Connect**{: #direct-connect}
Enlace de red dedicado entre tu ubicación y AWS. Se reconoce en el examen cuando el escenario pide caudal estable hacia el CPD; no se configura en el lab típico de Foundations.

**ALB**{: #alb}
*Application Load Balancer*: balanceador de carga de aplicación (capa HTTP/HTTPS) que reparte tráfico hacia destinos en la VPC. Suele ir en subred pública.

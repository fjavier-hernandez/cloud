---
title: Preparación para el AWS GameDay 2026
description: Guía de un día para la clasificación virtual del AWS GameDay 2026. Equipos IESMADAWS (DAW) e IESMAWSMIR (SMR).
status: new
---

# Preparación para el AWS GameDay 2026

El jueves 26 de noviembre de 2026, de 9:30 a 12:30, se juega la clasificación virtual del AWS GameDay. En el instituto salen dos equipos: **IESMADAWS**, de Desarrollo de Aplicaciones Web (DAW), con cuatro personas, e **IESMAWSMIR**, de Sistemas Microinformáticos y Redes (SMR), con dos. Esta página es la preparación de ese día. Quien todavía no ha cursado Amazon Web Services (AWS) puede seguirla igual, y con ella basta.

Los vídeos del canal [Profe Santos Cloud](https://www.youtube.com/@ProfeSantosCloud) acompañan la lectura. Quien más adelante curse el módulo de nube puede abrir el tema enlazado cuando quiera el desarrollo largo. Para la clasificación, con esta página abierta es suficiente.

Si la lees la tarde anterior, empieza por los [vídeos](#videos-de-apoyo) y sigue por el rol que te toque. Si la abres el jueves, entra por [los diez primeros minutos](#los-diez-primeros-minutos) y ten a mano la [tabla](#si-te-piden-esto-mira-aqui) y las [consultas](#consultas-y-politica-para-copiar). Para llevarla en papel, imprime solo esta página desde el navegador o guárdala como PDF.

## Qué es un GameDay y cómo se juega

Un GameDay es una competición por equipos dentro de una cuenta de AWS preparada para la ocasión. El trabajo son retos. Cada reto vale puntos, y la plataforma ofrece pistas cuando un reto se atasca. En el formato habitual, usar una pista resta parte de la puntuación de ese reto, así que compensa releer el enunciado antes de abrirla. La clasificación la gana el equipo que más puntos suma entre las 9:30 y las 12:30.

Cada reto hay que leerlo hasta el final y contestar exactamente lo que pregunta. A veces pide un dato (una dirección IP, un nombre, un código) y a veces pide dejar un recurso en un estado concreto. Si la pregunta pide el dato, el dato es la entrega. Si pide dejar el servicio bien cerrado, el cierre es la entrega. Arreglar cosas que el enunciado no pregunta consume el reloj del equipo y, con frecuencia, estropea lo que otro reto ya daba por bueno.

La consola de AWS es el sitio donde se resuelve casi todo. Ahí se tocan los grupos de seguridad, el balanceador, los registros, la política de un bucket y las reglas de un cortafuegos de aplicación. El código de la aplicación se deja como está, salvo que el enunciado hable de un fichero, de una función o de un dato guardado en el repositorio.

El editor del navegador (un Cloud IDE) y el Gitea del equipo, que es el servidor Git compartido, se abren solo en ese caso. Todo el equipo usa la misma cuenta y, si aparecen, el mismo IDE y el mismo Gitea. Lo que cambia una persona lo ven las demás.

Hay una condición que manda sobre el resto. Lo que al empezar responde bien tiene que seguir respondiendo al terminar. Un cambio que anota un reto y tira la web abajo deja al equipo sin la base sobre la que se apoyan los demás retos. Antes de dar por cerrado un cambio, alguien carga la página en el navegador.

## Los diez primeros minutos

Esos minutos deciden cómo se pasa el resto de la mañana. Durante ese rato el equipo entra, mira dónde está cada cosa y reparte el trabajo. Los cambios llegan después.

1. Entra con el acceso que den al equipo esa mañana y comprueba que la sesión es la del equipo. Si tenías otra cuenta de AWS abierta en el navegador, ciérrala antes, porque es fácil cambiar recursos en el sitio equivocado. Las credenciales se quedan dentro del equipo. No se reenvían por el móvil, no se pegan en un repositorio y no se capturan para un grupo distinto del equipo.
2. Mira la región en la barra superior derecha de la consola. Los recursos del evento viven en una región, y la consola solo enseña los de la región seleccionada. Si la barra marca otra, la cuenta parece vacía y se pierde un buen rato. En el [Tema 1](../01-fundamentos-nube-aws/tema1.md#el-error-clasico-de-la-region) está explicado por qué lo que creas en una región no aparece en otra.
3. Lee todos los retos antes de que nadie modifique un recurso. Anota, con las palabras del enunciado, qué hay que entregar en cada uno y cuántos puntos vale. Esa lista la guarda quien lleve la lectura en ese momento. Muchos fallos de la mañana salen de contestar una pregunta distinta de la que estaba escrita.
4. Reparte un reto principal a cada persona, según los roles de más abajo. Quien termina el suyo avisa y coge el siguiente. Si todo el equipo se mete en el mismo reto difícil, se quedan sin hacer los que se resolvían en pocos minutos.
5. Empieza por lo que se entiende al leerlo. Los puntos que están claros entran primero. Si un reto lleva un cuarto de hora sin avanzar, se anota dónde se ha quedado el equipo y se pasa a otro. La pista, cuando haga falta, se abre al terminar ese cuarto de hora.

A partir de ahí se trabaja en la misma región durante toda la mañana. Si un reto no pide un recurso nuevo, se corrige el que ya existe. Crear balanceadores, máquinas o buckets para probar llena la cuenta de recursos ajenos al evento y hace más difícil reconocer los que ya estaban.

## Roles de cada equipo

IESMADAWS va de cuatro personas, una por rol, y el capitán puede cambiar el reparto después de leer los retos. Si en ese equipo falta alguien, el capitán se queda con la lectura y la persona siguiente junta dos roles afines. IESMAWSMIR va de dos, y más abajo está cómo se parten el trabajo. Quien mira los registros y quien toca la red o el cortafuegos de la web tienen que poder hablarse, porque uno encuentra la petición y el otro coloca la regla.

La consola del evento suele estar en inglés. La primera vez que salga un menú, va el nombre en español y, entre paréntesis, el nombre que verás en pantalla.

### Capitán y lector

En IESMADAWS este rol lo lleva una persona durante toda la mañana. Lee cada reto entero, en voz alta si el equipo está junto, antes de que nadie pulse un cambio. Mientras lee, apunta la pregunta literal y el tipo de respuesta que pide. También lleva el reloj: de 9:30 a 12:30 dan tres horas, y se van en cuanto dos personas se quedan atascadas en lo mismo.

El otro trabajo del capitán es la hoja compartida del equipo. Cada cambio se anota con la hora, quién lo ha hecho, cómo estaba el recurso y cómo ha quedado. Esa hoja es la que permite deshacer. Cuando alguien va a borrar una regla, un objeto o una instancia, lo dice antes en esa hoja y espera a que el resto lo haya visto. Después del cambio, una persona carga la web y dice si sigue en pie.

En IESMAWSMIR esa lectura y esa hoja no tienen una persona solo para ellas. Las hacen los dos, turnándose, como está descrito en su apartado.

### IESMADAWS (DAW)

#### Detective de registros

Tu pieza son los registros. CloudWatch guarda métricas y registros de los servicios. Logs Insights es el buscador que hay dentro, en CloudWatch, menú *Logs*, *Logs Insights*. Eliges el grupo de registros del balanceador, ajustas el rango de tiempo de la parte superior y lanzas una consulta de [las de más abajo](#consultas-de-logs-insights).

El registro de acceso de un balanceador de carga de aplicación (*Application Load Balancer*, ALB) deja una línea por petición. En esa línea están la IP del cliente, el código de estado que devolvió el balanceador y la URL, con sus parámetros. De ahí se saca el dato que el reto pide copiar.

Una inyección SQL es una petición que esconde una orden de base de datos dentro de un parámetro, para que la aplicación consulte algo que su autor no tenía previsto. En la línea del registro se reconoce por una comilla, por un `OR 1=1`, por un `UNION SELECT` o por un comentario `--`. A menudo el espacio llega escrito como `%20` y la comilla como `%27`, porque así viaja en la URL.

La aplicación se queda como está. Tú marcas la petición, le pasas a quien lleva la web el nombre del balanceador y copias el dato que pide el reto tal como aparece, sin espacios de más.

CloudWatch responde a qué peticiones han llegado. CloudTrail responde a quién ha llamado a la API de AWS, por ejemplo quién ha cambiado un grupo de seguridad. Si buscas una IP de un visitante dentro de CloudTrail, no va a estar ahí. La diferencia está en la [monitorización del Tema 8](../08-escalado-monitoreo-cierre/tema8.md#monitorizacion).

#### Web y cortafuegos de aplicación

Tu pieza es el tráfico HTTP que entra por el balanceador. AWS WAF (*Web Application Firewall*, cortafuegos de aplicaciones web) inspecciona la petición antes de que llegue a los servidores. Va asociado a un balanceador concreto. Si lo asocias a otro, las reglas no ven las visitas de la web y el reto sigue igual.

En la consola abres *WAF & Shield*, luego *Web ACLs*, y compruebas que en los recursos asociados (*Associated AWS resources*) figura el ALB que sirve la página. Añades un grupo de reglas gestionadas. El conjunto básico (*Core rule set*) cubre ataques web habituales y el de base de datos SQL (*SQL database*) cubre la inyección que el detective haya visto en los registros.

La acción por defecto de la ACL se queda en permitir, de modo que las visitas normales siguen pasando y solo se bloquea lo que coincide con una regla. En cuanto guardes, carga la web. Si la portada deja de abrir, deshaz ese cambio antes de probar otro. El balanceador, el grupo de destino y la comprobación de estado están explicados en el [Tema 8](../08-escalado-monitoreo-cierre/tema8.md#elastic-load-balancing).

#### Código y datos

Tu pieza entra cuando el enunciado habla de un fichero, de una función o de objetos que han desaparecido. El resto de la mañana se resuelve desde la consola, sin abrir el código. Amazon S3 (*Simple Storage Service*, almacenamiento de objetos) guarda ficheros como objetos dentro de un bucket. Si faltan objetos, miras la política del bucket y si el versionado está activo; la plantilla para denegar el borrado está [más abajo](#politica-que-deniega-borrados). El desarrollo está en el [Tema 5](../05-almacenamiento/tema5.md#amazon-s3).

Si el evento deja un Cloud IDE, es un editor en el navegador, compartido por el equipo. El Gitea es el sitio donde está el repositorio Git. Antes de editar, en la terminal del IDE, ejecutas `git pull` para traer lo que haya subido otra persona. Dices en la hoja del equipo qué fichero tienes abierto, porque dos personas escribiendo el mismo fichero a la vez se sobrescriben.

Cuando toque subir el cambio, un commit con una frase clara de lo que ha hecho el equipo, y sin credenciales dentro del fichero.

AWS Lambda ejecuta una función cuando ocurre algo, como una petición, un fichero que llega o una hora programada, y no deja una máquina encendida. Si el reto habla de una función o de una API hecha así, es tuyo. La función actúa con un rol de IAM (*Identity and Access Management*, gestión de identidades y accesos), que es el permiso del servicio. Lambda está en el [Tema 4](../04-computo-serverless/tema4.md#aws-lambda) y los roles, en el [Tema 2](../02-seguridad-iam/tema2.md#rol-iam).

### IESMAWSMIR (SMR)

En este equipo sois dos. El trabajo de red, de máquinas, de registros y de almacenamiento sigue estando, pero no cabe un puesto por cabeza. Uno lleva la seguridad y la red. El otro lleva la monitorización y los registros. La lectura de los retos y la hoja de cambios se turnan, porque no hay una tercera persona que se quede solo de capitán.

#### Seguridad y red

Tu puesto es quién puede hablar con quién, y si las máquinas siguen sirviendo la web. Una VPC (*Virtual Private Cloud*, nube virtual privada) es la red de la cuenta dentro de una región, partida en subredes. Un grupo de seguridad (*security group*) es el cortafuegos de cada recurso. Las reglas de entrada deciden el puerto y el origen que pueden entrar, y lo que no está escrito ahí se queda fuera.

La visión de conjunto está en el [Tema 3](../03-redes-entrega-contenido/tema3.md#vpc-tu-red-virtual-en-una-region), con las [subredes](../03-redes-entrega-contenido/tema3.md#subred-publica) y la comparación entre [grupos de seguridad y listas de control de acceso de red (NACL)](../03-redes-entrega-contenido/tema3.md#security-groups-frente-a-nacl).

En la base de datos, el puerto del motor (3306 en MySQL o MariaDB, 5432 en PostgreSQL) acepta solo el grupo de seguridad de los servidores web. El origen de esa regla es un identificador que empieza por `sg-`. El rango `0.0.0.0/0` significa cualquier dirección IPv4 de internet y publica el motor. Una IP pública suelta en esa regla también se sale del patrón.

Si en las reglas de entrada aparece una IP así y el tráfico legítimo ya entra por el balanceador o por el grupo de los servidores, esa IP es lo primero que hay que cuestionar. Anotas la regla entera, se la enseñas a tu compañero, la quitas y uno de los dos carga la web. Cómo se encadenan balanceador, servidores y base está en la [seguridad por capas del Tema 3](../03-redes-entrega-contenido/tema3.md#seguridad-por-capas) y en la [red de RDS del Tema 6](../06-bases-de-datos/tema6.md#instantaneas-y-red).

Amazon EC2 (*Elastic Compute Cloud*) son las máquinas virtuales, y también entran en tu puesto. Compruebas que las que sirven la web están en ejecución (*running*). Parar o terminar una instancia se avisa antes, y si el reto no lo pide, se deja la máquina como está. El detalle está en el [Tema 4](../04-computo-serverless/tema4.md#amazon-ec2).

El balanceador de carga de aplicación (*Application Load Balancer*, ALB) reparte hacia un grupo de destino (*target group*). La comprobación de estado (*health check*) decide si un destino está sano. Un destino *unhealthy* deja de recibir visitas, y si no queda ninguno sano la web cae, muchas veces con un 502. Miras el puerto, la ruta y el código esperado, y los comparas con lo que la aplicación contesta. El [Tema 8](../08-escalado-monitoreo-cierre/tema8.md#grupo-de-destino-y-comprobacion-de-estado) lo desarrolla.

Para entrar a una máquina, Session Manager abre un shell desde la consola y mantiene cerrado el puerto 22. El camino es EC2, la instancia, *Connect*, *Session Manager*. Si el botón no está disponible, se lo dices a tu compañero y el puerto 22 sigue cerrado a internet. Si el reto es de ataques a la web, el cortafuegos de aplicación (WAF) lo asocias tú al balanceador, con el dato que te pase quien lleva los registros.

#### Monitorización y registros

Tu puesto es averiguar qué ha pasado y dejar constancia. CloudWatch guarda métricas y registros. Logs Insights es el buscador, en CloudWatch, menú *Logs*, *Logs Insights*. Eliges el grupo de registros del balanceador, ajustas el rango de tiempo de la parte superior y lanzas una consulta de [las de más abajo](#consultas-de-logs-insights).

El registro de acceso del balanceador deja una línea por petición, con la IP del cliente, el código de estado y la URL, parámetros incluidos. Una inyección SQL se reconoce ahí por una comilla, un `OR 1=1`, un `UNION SELECT` o un comentario `--`. A menudo el espacio llega como `%20` y la comilla como `%27`. La aplicación se queda como está: marcas la petición, le pasas el nombre del balanceador a quien lleva la seguridad y copias el dato tal como aparece.

CloudWatch responde a qué peticiones han llegado. CloudTrail responde a quién ha llamado a la API de AWS. Una IP de un visitante se busca en CloudWatch, no en CloudTrail. La diferencia está en la [monitorización del Tema 8](../08-escalado-monitoreo-cierre/tema8.md#monitorizacion).

Si faltan objetos de un bucket, también miras tú. En Amazon S3 los ficheros son objetos dentro de un bucket, y la política de bucket es el JSON que permite o deniega acciones sobre él. Un *Deny* explícito de `s3:DeleteObject` gana a un permiso de borrado que hubiera en otra política. La plantilla está [más abajo](#politica-que-deniega-borrados). Si el bucket ya tiene una política, se añade la regla dentro de `Statement`. Sustituir el documento entero puede quitar un permiso que la web necesita.

Si el versionado está activo, un objeto borrado a veces sigue ahí, tapado por un marcador de borrado. Si el versionado está apagado, hay que volver a subir el objeto desde la copia que tenga el equipo. El [Tema 5](../05-almacenamiento/tema5.md#seguridad-en-s3-enlace-con-el-tema-2) explica la política y el [versionado](../05-almacenamiento/tema5.md#versionado-y-borrados-por-que-importa-en-un-proyecto-de-daw).

Mientras tu compañero está dentro de un grupo de seguridad o de una máquina, la hoja la sostienes tú: la regla se copia entera antes de tocarla. Cuando el cambio es una política de bucket, la copia la hace tu compañero antes de que guardes. Cada anotación lleva la hora, qué se ha tocado y cómo estaba, de forma que el otro pueda devolver el recurso al estado anterior sin preguntar.

#### Cómo os cubrís

Cada reto nuevo lo lee en voz alta quien en ese momento no tiene la consola abierta. Al reto siguiente cambiáis de lector. Quien lee apunta la pregunta literal y los puntos, y deja el ratón quieto hasta que el otro ha oído qué hay que entregar.

Si uno lleva un cuarto de hora atascado, el otro mira el mismo síntoma desde su puesto y luego vuelve a su lista. Una IP rara en un grupo de seguridad se busca también en los registros, y un 502 de los registros se contrasta con el grupo de destino y la comprobación de estado. El recurso lo toca una sola persona. La otra recarga la web y dice si sigue en pie.

Hacia las once podéis cambiar de puesto si uno va ahogado y el otro ya ha cerrado lo que tenía claro. La hoja tiene que bastar para continuar. Los dos a la vez en la misma política o en el mismo grupo de seguridad se sobrescriben. Uno guarda el cambio y el otro comprueba la web.

## Si te piden esto, mira aquí { #si-te-piden-esto-mira-aqui }

La tabla no sustituye la lectura del reto. Sirve para no abrir un servicio al azar cuando el enunciado ya está señalando el sitio. Después de la tabla, cada fila está explicada para poder aplicarla sin haber dado el tema.

| Qué está pasando | Dónde mirar | Qué conviene dejar |
| --- | --- | --- |
| La base de datos acepta conexiones que no deberían llegar | Grupo de seguridad de la base, reglas de entrada | El puerto del motor solo desde el grupo de seguridad de los servidores web |
| Una IP suelta figura en una regla de entrada | Grupo de seguridad del recurso afectado | Esa regla anotada y retirada, y la web sigue abriendo |
| Alguien borra objetos de un bucket | Política del bucket, en S3, *Permissions* | Un *Deny* de `s3:DeleteObject` y los objetos otra vez en su sitio |
| Llegan ataques web o una inyección SQL | AWS WAF asociado al balanceador de la web | Reglas gestionadas en el ALB correcto, con la portada todavía en pie |
| La web no carga, o el balanceador responde 502 | Grupos de seguridad, grupo de destino y comprobación de estado | El balanceador llega al puerto de la aplicación y hay destinos sanos |
| Hay que encontrar un dato en los registros | CloudWatch Logs Insights, sobre el grupo de registros adecuado | La consulta filtrada por código, por IP o por parámetro, en el rango de tiempo correcto |

### La base de datos queda abierta

El grupo de seguridad de la base es el que decide quién puede abrir una conexión al motor. La regla de entrada cita el puerto del motor y, como origen, el grupo de seguridad de los servidores web. Si mañana se sustituye una máquina y la nueva lleva el mismo grupo, la base la sigue aceptando.

Una IP cualquiera de internet se queda sin camino. Pegar la IP de una máquina concreta en esa regla deja de valer en cuanto la máquina cambia, y abrir `0.0.0.0/0` publica el motor. El patrón está en el [Tema 3](../03-redes-entrega-contenido/tema3.md#seguridad-por-capas) y en el [Tema 6](../06-bases-de-datos/tema6.md#relacionales-rds-y-aurora).

### Una IP de origen desconocido

Recorres las reglas de entrada del grupo que protege la web, las máquinas o la base. El tráfico de los usuarios entra por el balanceador, y el de la base entra desde el grupo de los servidores. Una regla cuyo origen es una sola IP pública, con máscara `/32`, y que nadie del equipo reconoce, es una candidata a quitarse.

La copias entera en la hoja, con protocolo, puerto, origen y descripción. Luego la eliminas y cargas la web. Si la web cae, la restauras con lo que habías copiado y avisas a quien lleve la lectura, porque esa regla estaba haciendo algo que el equipo todavía no ha entendido.

### Borrados en S3

Alguien con permiso, o una política demasiado abierta, puede borrar objetos. La defensa habitual es una política de bucket que deniegue `s3:DeleteObject`. Un denegado explícito gana a un permiso, como en las políticas de IAM del [Tema 2](../02-seguridad-iam/tema2.md#politica-policy). La política corta los borrados nuevos.

Los objetos que ya no están hay que devolverlos. Con el versionado, se quita el marcador de borrado o se recupera la versión anterior. Sin versionado, se sube otra vez el fichero. Denegar y reponer van juntas. Con solo la política, el bucket queda protegido y vacío.

### Ataques web e inyección SQL

El detective encuentra la petición en los registros y quien lleva la web coloca el WAF delante del balanceador que de verdad recibe el tráfico. En IESMAWSMIR quien lleva los registros encuentra la petición y quien lleva la seguridad asocia el WAF. La asociación y las reglas van juntas. Un grupo de reglas en el balanceador equivocado no ve el ataque, y un balanceador bien elegido sin reglas tampoco lo para.

Después de asociar la ACL, la portada tiene que seguir cargando. Si el WAF bloquea también las visitas normales, la regla ha quedado demasiado amplia y se revisa antes de seguir.

### La web cae o responde 502

Conviene separar dos síntomas. Si el navegador se queda colgado y no llega respuesta, mira las reglas de entrada del propio balanceador: el puerto 80 o el 443 tienen que admitir a los usuarios. Si el balanceador contesta 502, la petición sí le ha llegado y él no ha conseguido una respuesta válida del destino. Entonces se miran tres sitios, en este orden.

El grupo de seguridad de las máquinas permite el puerto de la aplicación con origen el grupo de seguridad del balanceador. El grupo de destino tiene esas máquinas registradas, en el puerto en el que la aplicación escucha. La comprobación de estado pide una ruta que exista, por ejemplo `/`, y espera el código que esa ruta devuelve.

Un destino en *unhealthy* deja de recibir tráfico. Si todos están así, el balanceador responde 502 aunque las máquinas sigan encendidas. El [Tema 8](../08-escalado-monitoreo-cierre/tema8.md#grupo-de-destino-y-comprobacion-de-estado) detalla el grupo de destino y la comprobación.

### Un dato escondido en los registros

Abres Logs Insights, seleccionas el grupo de registros del balanceador o de la aplicación, y pones el rango de tiempo en el que ha pasado el hecho. Un rango de cinco minutos, cuando la petición es de hace una hora, devuelve cero líneas y parece que la consulta está mal. Amplía el rango antes de reescribir la consulta. Las cuatro consultas siguientes se pegan y se adaptan.

## Consultas y política para copiar

Los textos de esta sección se copian y se modifican los marcadores. Un marcador en mayúsculas, como `NOMBRE-DEL-BUCKET`, se sustituye por el nombre real del recurso, con las mismas mayúsculas y guiones. La dirección `203.0.113.50` y el código `502` son ejemplos de relleno, y también se cambian. Son valores de esta guía. En el evento se sustituyen por los que pida el reto.

### Consultas de Logs Insights

En CloudWatch, entra en *Logs* y luego en *Logs Insights*. Arriba se elige el grupo de registros y el rango de tiempo. Pegas la consulta y pulsas *Run query*. `filter @message like` busca un texto dentro de la línea completa, así que sirve aunque el registro no esté partido en campos. `sort` ordena y `limit` corta la lista para que se pueda leer.

La primera consulta deja las líneas en las que aparece un código de estado. El `502` se cambia por el código que pida el reto o por el que esté devolviendo la web. En el registro del balanceador suelen convivir el código que ve el usuario y el que contestó el servidor. Si el balanceador dice 502 y el servidor no llega a contestar, el fallo está en el camino entre los dos (grupo de seguridad, registro en el grupo de destino o comprobación). Si los dos dicen 500, la aplicación ha respondido un error.

```text
fields @timestamp, @message
| filter @message like / 502 /
| sort @timestamp desc
| limit 40
```

La segunda filtra por una dirección IP. Sustituye `203.0.113.50` por la IP que indique el reto o por la que ya hayas visto en otra línea. Ese valor de ejemplo pertenece a un rango reservado para documentación: si lo buscas tal cual, no vas a encontrar el tráfico del evento.

```text
fields @timestamp, @message
| filter @message like /203.0.113.50/
| sort @timestamp desc
| limit 40
```

La tercera busca un parámetro de la URL. El nombre va justo antes del signo `=`. Cambia `id` por el parámetro que nombre el enunciado o por el que veas al leer una línea. Detrás del igual está el valor, que muchas veces es justo lo que hay que entregar.

```text
fields @timestamp, @message
| filter @message like /id=/
| sort @timestamp desc
| limit 40
```

La cuarta filtra peticiones que parecen inyección SQL, cuando todavía no sabes el nombre del parámetro. `union` caza un `UNION SELECT` en cualquier combinación de mayúsculas. `or%201` caza un «or 1» con el espacio codificado, y `%27` es una comilla codificada. Cada línea que salga se lee, y te quedas con la que trae el parámetro manipulado.

```text
fields @timestamp, @message
| filter @message like /(?i)union/ or @message like /(?i)or%201/ or @message like /%27/
| sort @timestamp desc
| limit 40
```

### Política que deniega borrados

Esta política de bucket deniega borrar objetos. `Effect` en `Deny` gana a cualquier `Allow` de otra política, con el mismo criterio que en IAM. `s3:DeleteObject` es el borrado normal. `s3:DeleteObjectVersion` cubre el versionado, para que nadie vaya eliminando las versiones una a una.

El recurso termina en `/*` porque los objetos viven dentro del bucket. `Principal` con asterisco aplica el denegado a todo el mundo, también a los roles de la aplicación. La web puede seguir leyendo y subiendo, y el borrado queda cerrado.

Sustituye `NOMBRE-DEL-BUCKET` por el nombre exacto del bucket. Si el nombre no coincide, la política se guarda igual y no protege nada.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenegarBorradoDeObjetos",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:DeleteObject",
        "s3:DeleteObjectVersion"
      ],
      "Resource": "arn:aws:s3:::NOMBRE-DEL-BUCKET/*"
    }
  ]
}
```

!!! warning "Si el bucket ya tiene política"
    Copia el JSON anterior en la hoja del equipo y, en la consola, abre el bucket, *Permissions*, *Bucket policy*. Si el cuadro está vacío, pega la plantilla entera. Si ya hay un documento, no lo sustituyas: añade este objeto dentro de la lista `Statement`, separado por una coma del que ya estaba. Sustituir el documento borra los permisos anteriores y puede tirar la web. Guarda también el JSON viejo, para poder volver a él.

Cuando la política ya está puesta, repón los objetos que falten. Con versionado, en la lista de versiones se puede quitar el marcador de borrado o restaurar la versión previa. Sin versionado, se sube de nuevo el fichero. Al terminar, intenta borrar un objeto de prueba que haya subido el equipo. El borrado tiene que fallar, y la web tiene que seguir abriendo.

## Reglas de oro

Cualquier borrado se avisa antes en la hoja del equipo. Antes de quitar una regla de un grupo de seguridad, un objeto de S3, una instancia, una política o una ACL del WAF, se escribe cómo está el recurso. Quien va a borrar espera a que lo vea el capitán, en DAW, o su compañero, en SMIR, y solo entonces guarda el cambio. Con esa copia se puede volver atrás.

Después de cada cambio, alguien carga la web y lo dice en alto. Sirve tanto si el cambio era de red como si era del WAF o del bucket. Un reto anotado con la portada caída deja al equipo peor de lo que estaba. Si la web ha caído, se deshace el último cambio con la nota de la hoja y se vuelve a probar desde ese estado.

En el IDE compartido, `git pull` va antes de editar. Si Git dice que tu copia y la del repositorio han divergido, paras y hablas con quien haya editado antes. El envío se hace con un push normal. `git push --force` reescribe el historial que el resto del equipo tiene por bueno. Un commit lleva una frase que explica el cambio, y el fichero va sin secretos.

Las credenciales del evento se quedan en el equipo. Un chat de clase, un repositorio o una captura las sacan de ahí. IAM decide quién puede llamar a la API de AWS, y el grupo de seguridad decide qué tráfico de red entra. Son capas distintas. Ensanchar las dos para salir del paso deja la cuenta abierta.

Si un botón responde *AccessDenied*, se lee la acción que ha denegado y se le pasa a quien lleve la lectura en ese momento. La salida es entender esa denegación. Pedir más permisos, o pegar una clave de acceso en el código, abre un incidente. Esa separación está en el [Tema 2](../02-seguridad-iam/tema2.md#security-group-frente-a-iam).

<div class="imprimir-enlaces" markdown="1">

## Vídeos de apoyo { #videos-de-apoyo }

Están en el canal [Profe Santos Cloud](https://www.youtube.com/@ProfeSantosCloud). Con los dos primeros y el de tu rol se llega al jueves. El resto es para la tarde en la que sobre tiempo. Al imprimir la página o guardarla como PDF, la dirección de cada vídeo sale junto al título.

### Los dos equipos, antes que nada

Quien vaya a jugar, en DAW y en SMR, ve primero cómo se entra en AWS Academy y cómo se mueve uno por la consola. Es el vídeo de [introducción a AWS Academy](https://www.youtube.com/watch?v=dxWV4pvGZmU). El segundo, también para todos, es [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo). Ahí se ven usuarios, roles y el motivo por el que una denegación se lee antes de pedir permiso de administrador. Con esos dos ya se entiende la sesión con la que van a recibir al equipo.

### Red y web

Quien lleve la seguridad y la red en IESMAWSMIR, y quien en IESMADAWS vaya a tocar subredes o grupos de seguridad, ve la [VPC](https://www.youtube.com/watch?v=u0Kh0JRK4zk). Quien lleve la web en DAW, y también quien lleve la seguridad y la red en SMR, ve el [balanceador de aplicación](https://www.youtube.com/watch?v=GqRMAwo6QRA), porque el 502 y la comprobación de estado se entienden mejor después de ver cómo se registra un destino.

### Sistemas

En IESMAWSMIR, quien lleva la seguridad y la red ve el de [EC2 con Linux](https://www.youtube.com/watch?v=vdSKZxOVX1A), donde se lanza una máquina, se revisa el grupo de seguridad y se entra a la instancia. Conviene verlo antes que el del balanceador, porque el balanceador necesita una máquina clara a la que enviar el tráfico.

### Base de datos

Quien vaya a cerrar el acceso a la base, en cualquiera de los dos equipos, ve primero [RDS en una subred privada](https://www.youtube.com/watch?v=4X1f23RpBG0). Ahí se ve por qué el motor no se publica a internet y cómo el grupo de seguridad de la base cita al de los servidores. Si la tarde da de sí, el segundo es el de [RDS](https://www.youtube.com/watch?v=43jYEiZvOsw), más general.

### Registros

El detective de registros de IESMADAWS, y quien lleve la monitorización en IESMAWSMIR, ven [CloudWatch, CloudTrail y EventBridge](https://www.youtube.com/watch?v=T_Pz1ksb9ng). Ahí se distingue el registro de una petición HTTP del registro de quién ha llamado a la API de AWS. Las consultas de esta guía se pegan igual si el vídeo no llega al detalle de Logs Insights.

### Almacenamiento

Quien lleve el código y los datos en DAW, y quien lleve la monitorización en SMR, ven el de [S3](https://www.youtube.com/watch?v=OkGNAHtVCq8). Trata el bucket, los objetos y los permisos, que es lo que hay que tocar si desaparecen ficheros.

### Extra para DAW

Estos dos quedan para cuando la tarde da de sí, y solo en IESMADAWS. Primero [Lambda](https://www.youtube.com/watch?v=TIeUbq4bCOU), por si un reto habla de una función. Después [DynamoDB](https://www.youtube.com/watch?v=j1VL7ctuerw), por si aparece una tabla no relacional. En el módulo, DynamoDB se sitúa en el [Tema 6](../06-bases-de-datos/tema6.md#nosql-y-analitica), junto al resto de opciones distintas de RDS. El recorrido de la mañana sigue siendo el de los apartados anteriores.

### Orden para una tarde

El equipo ve juntos los dos primeros. Después cada persona sigue con el de su rol, y los dos últimos solo si aún queda tiempo. La tabla es el orden de esa tarde.

| Momento | Quién lo ve | Vídeo |
| --- | --- | --- |
| 1. Todos juntos | DAW y SMR | [Introducción a AWS Academy](https://www.youtube.com/watch?v=dxWV4pvGZmU) |
| 2. Todos juntos | DAW y SMR | [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo) |
| 3. Cada rol | Seguridad y red, en SMR, y quien vaya a tocar la VPC | [VPC](https://www.youtube.com/watch?v=u0Kh0JRK4zk) |
| 3. Cada rol | Seguridad y red, en SMR, antes del balanceador | [EC2 Linux](https://www.youtube.com/watch?v=vdSKZxOVX1A) |
| 3. Cada rol | Web, en DAW, y seguridad y red, en SMR | [Balanceador de aplicación](https://www.youtube.com/watch?v=GqRMAwo6QRA) |
| 3. Cada rol | Quien vaya a cerrar la base | [RDS en una subred privada](https://www.youtube.com/watch?v=4X1f23RpBG0) |
| 3. Cada rol | Registros, en DAW, y monitorización, en SMR | [CloudWatch, CloudTrail y EventBridge](https://www.youtube.com/watch?v=T_Pz1ksb9ng) |
| 3. Cada rol | Código y datos, en DAW, y monitorización, en SMR | [S3](https://www.youtube.com/watch?v=OkGNAHtVCq8) |
| 4. Si sobra la tarde | DAW | [Lambda](https://www.youtube.com/watch?v=TIeUbq4bCOU) y, después, [DynamoDB](https://www.youtube.com/watch?v=j1VL7ctuerw) |
| 4. Si sobra la tarde | Seguridad y red, en SMR | [RDS](https://www.youtube.com/watch?v=43jYEiZvOsw), o el balanceador si todavía no lo ha visto |

Con esa tanda y una lectura del rol propio se llega al jueves. El resto de vídeos puede esperar a después de la clasificación.

</div>

## Si te sobra tiempo

Esta práctica es voluntaria y queda fuera de la evaluación del módulo. El jueves se puede jugar sin haberla hecho. Sirve para ver, una vez, un balanceador con dos máquinas y una comprobación de estado en verde. Hace falta el Learner Lab de AWS Academy. Quien no lo tenga se queda con lo anterior, porque el jueves no depende de este laboratorio. Cómo se arranca está en [Acceso](../00-acceso/acceso.md#2-entrar-al-learner-lab-desde-el-curso).

El objetivo es dejar un ALB de cara a internet, con dos instancias EC2 pequeñas de Amazon Linux que sirven una página, y comprobar que el grupo de destino las marca sanas. La página escribe el nombre de la máquina, así que al recargar el nombre DNS del balanceador se ve que no siempre contesta la misma.

El grupo de seguridad de las máquinas solo admite el tráfico web que viene del grupo del balanceador. Abrir la IP de una máquina en el navegador tiene que fallar, y abrir el nombre del balanceador tiene que funcionar. Es el mismo encadenado que el equipo va a revisar el jueves.

Trabaja en la región que marca el laboratorio cuando el indicador de AWS está en verde. En este módulo suele ser Norte de Virginia (`us-east-1`). Usa la VPC predeterminada y dos subredes de zonas de disponibilidad distintas. Si el asistente exige un par de claves, elige `vockey` y conserva ese par. La comprobación se hace en el navegador, con el nombre DNS del balanceador.

1. Crea el grupo `sg-gameday-alb` con una regla de entrada HTTP, puerto 80, origen `0.0.0.0/0`. Crea el grupo `sg-gameday-web` con una regla de entrada HTTP, puerto 80, y elige como origen el grupo `sg-gameday-alb`.
2. Lanza dos instancias, `gameday-web-a` y `gameday-web-b`, con Amazon Linux 2023 y tipo `t3.micro` (o `t2.micro` si el laboratorio no ofrece el primero). Ponlas en dos subredes de zonas distintas, asígnales `sg-gameday-web` y pega este *user data*, que es el script del primer arranque:

    ```bash
    #!/bin/bash
    dnf install -y httpd
    systemctl enable httpd
    systemctl start httpd
    echo "<h1>Hola desde $(hostname)</h1>" > /var/www/html/index.html
    ```

3. Crea un grupo de destino de tipo instancia, HTTP, puerto 80, en la VPC predeterminada. La comprobación de estado usa la ruta `/` y espera un 200. Registra las dos instancias en el puerto 80.
4. Crea un *Application Load Balancer* de cara a internet, en la VPC predeterminada, con al menos dos subredes en zonas distintas y con el grupo `sg-gameday-alb`. El *listener* HTTP del puerto 80 reenvía al grupo de destino que acabas de crear.
5. Espera a que las dos instancias pasen a *healthy*. El script puede tardar unos minutos. Si se quedan en *unhealthy*, revisa el grupo de seguridad y, en la instancia, *Monitor and troubleshoot*, *Get system log*, para ver si el script ha llegado a instalar Apache. Cuando estén sanas, abre `http://` seguido del nombre DNS del balanceador. Recarga varias veces.
6. Al acabar, borra en este orden el balanceador, el grupo de destino y las dos instancias. Las instancias se terminan (*terminate*). Pararlas (*stop*) deja el disco y el crédito sigue contando mientras existan recursos encendidos. Cuando ya no los use nadie, borra también los dos grupos de seguridad.

!!! warning "Límites del Learner Lab"
    En el Learner Lab no se pueden crear usuarios, grupos ni roles de IAM. El rol que ya trae el entorno se llama **LabRole** y se asigna a una instancia o a una función mediante **LabInstanceProfile**, para que ese recurso llame a otros servicios de AWS. No amplía los botones de tu sesión en la consola. Esta práctica no lo necesita, porque las máquinas solo sirven una página. Session Manager puede no estar disponible por la misma razón. El detalle de los dos entornos de Academy está en el [Tema 2](../02-seguridad-iam/tema2.md#dos-entornos-de-academy-lab-del-modulo-4-y-learner-lab).

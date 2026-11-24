---
title: Preparación para el AWS GameDay 2026
description: Guía breve de la clasificación virtual del AWS GameDay 2026. Equipos IESMADAWS (DAW) e IESMAWSMIR (SMR).
status: new
---

# Preparación para el AWS GameDay 2026

El jueves 26 de noviembre de 2026, de 9:30 a 12:30, se juega la clasificación virtual del AWS GameDay. En el instituto salen dos equipos: **IESMADAWS**, de Desarrollo de Aplicaciones Web (DAW), con cuatro personas, e **IESMAWSMIR**, de Sistemas Microinformáticos y Redes (SMR), con dos. Esta página es la preparación de ese día. Quien todavía no ha cursado Amazon Web Services (AWS) puede seguirla igual: con ella basta.

Los vídeos del canal [Profe Santos Cloud](https://www.youtube.com/@ProfeSantosCloud) acompañan la lectura. Si la lees la tarde anterior, empieza por los [vídeos](#videos-de-apoyo) y sigue por el rol que te toque. Si la abres el jueves, entra por [los diez primeros minutos](#los-diez-primeros-minutos) y ten a mano la [tabla](#si-te-piden-esto-mira-aqui). Para llevarla en papel, imprime esta página o guárdala como PDF.

## Qué es un GameDay y cómo se juega

Un GameDay es una competición por equipos dentro de una cuenta de AWS preparada para la ocasión. El trabajo son retos. Cada uno vale puntos, y la plataforma ofrece pistas cuando uno se atasca. En el formato habitual, usar una pista resta parte de la puntuación de ese reto, así que compensa releer el enunciado antes de abrirla. Gana el equipo que más puntos suma entre las 9:30 y las 12:30.

Cada reto hay que leerlo hasta el final y contestar exactamente lo que pregunta. A veces pide un dato (una dirección IP, un nombre, un código) y a veces pide dejar un recurso en un estado concreto. Si la pregunta pide el dato, el dato es la entrega. Si pide dejar el servicio bien cerrado, el cierre es la entrega. Arreglar cosas que el enunciado no pregunta consume el reloj y, con frecuencia, estropea lo que otro reto ya daba por bueno.

La consola de AWS es el sitio donde se resuelve casi todo. El código de la aplicación se deja como está, salvo que el enunciado hable de un fichero, de una función o de un dato del repositorio. El editor del navegador (un Cloud IDE) y el Gitea del equipo, que es el servidor Git compartido, se abren solo en ese caso. Todo el equipo usa la misma cuenta. Lo que al empezar responde bien tiene que seguir respondiendo al terminar: un cambio que anota un reto y tira la web abajo deja al equipo sin la base sobre la que se apoyan los demás. Antes de dar por cerrado un cambio, alguien carga la página en el navegador.

## Los diez primeros minutos

Esos minutos deciden cómo se pasa el resto de la mañana. Durante ese rato el equipo entra, mira dónde está cada cosa y reparte el trabajo. Los cambios llegan después.

1. Entra con el acceso que den al equipo esa mañana y comprueba que la sesión es la del equipo. Si tenías otra cuenta de AWS abierta, ciérrala antes. Las credenciales se quedan dentro del equipo: no se reenvían por el móvil, no se pegan en un repositorio y no se capturan para un grupo distinto.
2. Mira la región en la barra superior derecha de la consola. Los recursos del evento viven en una región, y la consola solo enseña los de la región seleccionada. Si la barra marca otra, la cuenta parece vacía. En el [Tema 1](../01-fundamentos-nube-aws/tema1.md#el-error-clasico-de-la-region) está explicado por qué.
3. Lee todos los retos antes de que nadie modifique un recurso. Anota, con las palabras del enunciado, qué hay que entregar en cada uno y cuántos puntos vale. Muchos fallos salen de contestar una pregunta distinta de la que estaba escrita.
4. Reparte un reto principal a cada persona, según los roles de más abajo. Quien termina el suyo avisa y coge el siguiente. Si todo el equipo se mete en el mismo reto difícil, se quedan sin hacer los que se resolvían en pocos minutos.
5. Empieza por lo que se entiende al leerlo. Los puntos claros entran primero. Si un reto lleva un cuarto de hora sin avanzar, se anota dónde se ha quedado y se pasa a otro. La pista, cuando haga falta, se abre al terminar ese cuarto de hora.

A partir de ahí se trabaja en la misma región durante toda la mañana. Si un reto no pide un recurso nuevo, se corrige el que ya existe. Crear máquinas o buckets para probar llena la cuenta y hace más difícil reconocer lo que ya estaba.

## Roles de cada equipo

Los roles son orientativos: sirven para arrancar sin pisaros, pero cada equipo los adapta según los retos que salgan. IESMADAWS va de cuatro personas, una por rol, y el capitán puede cambiar el reparto después de leer los retos. IESMAWSMIR va de dos: una persona lleva la seguridad y la red, y la otra, la monitorización y los registros. Quien mira los registros y quien toca la red o el cortafuegos tienen que poder hablarse, porque uno encuentra la petición y el otro coloca la regla. La consola del evento suele estar en inglés: la primera vez que salga un menú, va el nombre en español y, entre paréntesis, el que verás en pantalla.

### IESMADAWS (DAW)

El capitán lee cada reto entero antes de que nadie pulse un cambio, apunta la pregunta literal y lleva el reloj. También lleva la hoja compartida del equipo: cada cambio se anota con la hora, quién lo ha hecho, cómo estaba el recurso y cómo ha quedado. Cuando alguien va a borrar una regla, un objeto o una instancia, lo dice antes en esa hoja. Después del cambio, una persona carga la web y dice si sigue en pie.

El detective de registros trabaja en CloudWatch. Logs Insights es el buscador, en CloudWatch, menú *Logs*, *Logs Insights*. Eliges el grupo de registros del balanceador, ajustas el rango de tiempo y lanzas la [consulta](#consulta-y-politica) de más abajo. El registro de un balanceador de carga de aplicación (*Application Load Balancer*, ALB) deja una línea por petición, con la IP del cliente, el código de estado y la URL. Una inyección SQL se reconoce por una comilla, un `OR 1=1`, un `UNION SELECT` o un comentario `--`; a menudo el espacio llega como `%20` y la comilla como `%27`. CloudWatch responde a qué peticiones han llegado. CloudTrail responde a quién ha llamado a la API de AWS. Una IP de un visitante se busca en CloudWatch, no en CloudTrail.

Quien lleva la web y el cortafuegos trabaja el tráfico HTTP que entra por el balanceador. AWS WAF (*Web Application Firewall*, cortafuegos de aplicaciones web) inspecciona la petición antes de que llegue a los servidores, y va asociado a un balanceador concreto. En *WAF & Shield*, *Web ACLs*, compruebas que en los recursos asociados (*Associated AWS resources*) figura el ALB que sirve la página, y añades reglas gestionadas: el conjunto básico (*Core rule set*) y el de base de datos SQL (*SQL database*). La acción por defecto de la ACL se queda en permitir. En cuanto guardes, carga la web; si la portada deja de abrir, deshaz ese cambio.

Quien lleva el código y los datos entra cuando el enunciado habla de un fichero, de una función o de objetos que han desaparecido. El resto se resuelve desde la consola. Si faltan objetos en Amazon S3 (*Simple Storage Service*, almacenamiento de objetos), miras la política del bucket y si el versionado está activo. Si el evento deja un Cloud IDE y un Gitea, ejecutas `git pull` antes de editar, dices en la hoja qué fichero tienes abierto y subes un commit con una frase clara, sin credenciales en el fichero. Si el reto habla de una función, AWS Lambda ejecuta código cuando ocurre un evento y actúa con un rol de IAM (*Identity and Access Management*, gestión de identidades y accesos).

### IESMAWSMIR (SMR)

En este equipo sois dos. Uno lleva la seguridad y la red. El otro lleva la monitorización y los registros. La lectura de los retos y la hoja de cambios se turnan: cada reto nuevo lo lee en voz alta quien no tiene la consola abierta, y al siguiente cambiáis de lector. Si uno lleva un cuarto de hora atascado, el otro le echa una mano y luego vuelve a su lista. El recurso lo toca una sola persona. La otra recarga la web.

Quien lleva la seguridad y la red decide quién puede hablar con quién. La red de la cuenta es una VPC (*Virtual Private Cloud*, nube virtual privada). Un grupo de seguridad (*security group*) es el cortafuegos de cada recurso: las reglas de entrada deciden el puerto y el origen, y lo que no está escrito se queda fuera. En la base de datos, el puerto del motor (3306 en MySQL o MariaDB, 5432 en PostgreSQL) acepta solo el grupo de seguridad de los servidores web, un identificador que empieza por `sg-`. El rango `0.0.0.0/0` publica el motor a internet. Compruebas que las máquinas EC2 (*Elastic Compute Cloud*) que sirven la web están en ejecución (*running*) y, si el reto no pide pararlas, las dejas como están. El ALB reparte hacia un grupo de destino (*target group*); si no queda ningún destino sano (*healthy*), la web cae, muchas veces con un 502. Si el reto es de ataques a la web, asocias tú el WAF al balanceador, con el dato que te pase quien lleva los registros.

Quien lleva la monitorización y los registros averigua qué ha pasado y deja constancia. Trabaja en Logs Insights igual que el detective de DAW, marca la petición y le pasa el nombre del balanceador a quien lleva la seguridad. Si faltan objetos de un bucket, también miras tú: un *Deny* explícito de `s3:DeleteObject` gana a un permiso de borrado, y si el bucket ya tiene política se añade la regla dentro de `Statement`, sin sustituir el documento entero. Mientras tu compañero toca un grupo de seguridad o una máquina, la hoja la sostienes tú, con la hora y cómo estaba el recurso, de forma que se pueda volver atrás.

## Si te piden esto, mira aquí { #si-te-piden-esto-mira-aqui }

La tabla no sustituye la lectura del reto. Sirve para no abrir un servicio al azar cuando el enunciado ya está señalando el sitio.

| Qué está pasando | Dónde mirar | Qué conviene dejar |
| --- | --- | --- |
| La base de datos acepta conexiones que no deberían llegar | Grupo de seguridad de la base, reglas de entrada | El puerto del motor solo desde el grupo de seguridad de los servidores web |
| Una IP suelta figura en una regla de entrada | Grupo de seguridad del recurso afectado | Esa regla anotada y retirada, y la web sigue abriendo |
| Alguien borra objetos de un bucket | Política del bucket, en S3, *Permissions* | Un *Deny* de `s3:DeleteObject` y los objetos otra vez en su sitio |
| Llegan ataques web o una inyección SQL | AWS WAF asociado al balanceador de la web | Reglas gestionadas en el ALB correcto, con la portada todavía en pie |
| La web no carga, o el balanceador responde 502 | Grupos de seguridad, grupo de destino y comprobación de estado | El balanceador llega al puerto de la aplicación y hay destinos sanos |
| Hay que encontrar un dato en los registros | CloudWatch Logs Insights, sobre el grupo de registros adecuado | La consulta filtrada por código, por IP o por parámetro, en el rango de tiempo correcto |

Si el navegador se queda colgado, mira primero las reglas de entrada del balanceador: el puerto 80 o el 443 tienen que admitir a los usuarios. Si el balanceador contesta 502, la petición sí le ha llegado y él no ha conseguido una respuesta válida del destino. Entonces se miran el grupo de seguridad de las máquinas, el grupo de destino y la comprobación de estado. En Logs Insights, el rango de tiempo importa tanto como la consulta: un rango de cinco minutos, cuando la petición es de hace una hora, devuelve cero líneas y parece que la consulta está mal.

## Consulta y política { #consulta-y-politica }

En CloudWatch, entra en *Logs* y luego en *Logs Insights*. Arriba se elige el grupo de registros y el rango de tiempo. Pegas la consulta, pulsas *Run query* y cambias el `502` por el código, la IP o el fragmento de URL que pida el reto. `filter @message like` busca un texto dentro de la línea completa.

```text
fields @timestamp, @message
| filter @message like / 502 /
| sort @timestamp desc
| limit 40
```

Para cortar los borrados en un bucket, la defensa habitual es una política que deniegue `s3:DeleteObject`. Un *Deny* explícito gana a cualquier permiso de borrado. Sustituye `NOMBRE-DEL-BUCKET` por el nombre exacto del bucket. Si el cuadro de la política ya tiene un documento, no lo sustituyas: añade este objeto dentro de la lista `Statement` y guarda antes el JSON viejo. La política corta los borrados nuevos; los objetos que ya no están hay que reponerlos, quitando el marcador de borrado si hay versionado o volviendo a subir el fichero si no lo hay.

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

## Reglas de oro

Cualquier borrado se avisa antes en la hoja del equipo. Antes de quitar una regla, un objeto, una instancia, una política o una ACL del WAF, se escribe cómo está el recurso. Quien va a borrar espera a que lo vea el capitán, en DAW, o su compañero, en SMR, y solo entonces guarda el cambio. Después de cada cambio, alguien carga la web y lo dice en alto. Si la web ha caído, se deshace el último cambio con la nota de la hoja. Un reto anotado con la portada caída deja al equipo peor de lo que estaba.

En el IDE compartido, `git pull` va antes de editar. Si Git dice que tu copia y la del repositorio han divergido, paras y hablas con quien haya editado antes. `git push --force` reescribe el historial que el resto del equipo tiene por bueno. Un commit lleva una frase que explica el cambio, y el fichero va sin secretos. Las credenciales del evento se quedan en el equipo. IAM decide quién puede llamar a la API de AWS, y el grupo de seguridad decide qué tráfico de red entra: son capas distintas. Si un botón responde *AccessDenied*, se lee la acción que ha denegado y se le pasa a quien lleve la lectura. Pedir más permisos, o pegar una clave de acceso en el código, no es la salida.

<div class="imprimir-enlaces" markdown="1">

## Vídeos de apoyo { #videos-de-apoyo }

Están en el canal [Profe Santos Cloud](https://www.youtube.com/@ProfeSantosCloud), en este orden. El equipo ve juntos los dos primeros; después cada persona sigue con el de su rol. Al imprimir, la dirección de cada vídeo sale junto al título.

1. DAW y SMR, todos juntos: [Introducción a AWS Academy](https://www.youtube.com/watch?v=dxWV4pvGZmU).
2. DAW y SMR, todos juntos: [IAM en Academy](https://www.youtube.com/watch?v=rEnenbxjOGo).
3. Seguridad y red, en SMR, y quien vaya a tocar la VPC: [VPC](https://www.youtube.com/watch?v=u0Kh0JRK4zk).
4. Seguridad y red, en SMR, antes del balanceador: [EC2 Linux](https://www.youtube.com/watch?v=vdSKZxOVX1A).
5. Web, en DAW, y seguridad y red, en SMR: [Balanceador de aplicación](https://www.youtube.com/watch?v=GqRMAwo6QRA).
6. Quien vaya a cerrar la base: [RDS en una subred privada](https://www.youtube.com/watch?v=4X1f23RpBG0).
7. Registros, en DAW, y monitorización, en SMR: [CloudWatch, CloudTrail y EventBridge](https://www.youtube.com/watch?v=T_Pz1ksb9ng).
8. Código y datos, en DAW, y monitorización, en SMR: [S3](https://www.youtube.com/watch?v=OkGNAHtVCq8).
9. Si sobra tiempo, DAW: [Lambda](https://www.youtube.com/watch?v=TIeUbq4bCOU) y, después, [DynamoDB](https://www.youtube.com/watch?v=j1VL7ctuerw).
10. Si sobra tiempo, seguridad y red en SMR: [RDS](https://www.youtube.com/watch?v=43jYEiZvOsw).

</div>

## Si te sobra tiempo

Si quieres ver una vez un balanceador con dos máquinas y una comprobación de estado en verde, puedes montarlo en el Learner Lab de AWS Academy. Es voluntario y el jueves se puede jugar sin haberlo hecho. Cómo se arranca está en [Acceso](../00-acceso/acceso.md#2-entrar-al-learner-lab-desde-el-curso). En ese laboratorio no se pueden crear usuarios, grupos ni roles de IAM: el rol que ya trae el entorno se llama **LabRole** y se asigna a una instancia o a una función mediante **LabInstanceProfile**, para que ese recurso llame a otros servicios; no amplía los botones de tu sesión. Al acabar, termina las instancias (*terminate*) y borra el balanceador, porque pararlas (*stop*) deja el crédito corriendo.

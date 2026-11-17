---
title: "Práctica orientativa: examen de la 1.ª evaluación"
description: Práctica guiada en el Learner Lab para preparar la parte práctica del examen de la 1.ª evaluación (EC2, grupo de seguridad, user data, EBS y limpieza).
---

# Práctica orientativa: examen de la 1.ª evaluación

!!! info "Datos de la práctica"
    - **Módulo:** Introducción a la Nube Pública (INP) · 2.º DAW semipresencial · Curso 2026-2027
    - **Entorno:** AWS Academy Learner Lab · Región *Norte de Virginia* (`us-east-1`)
    - **Puntuación:** 10 puntos

Esta práctica sirve para ensayar, con guía, la parte práctica de la prueba objetiva 1 (PO1), el examen de la 1.ª evaluación. Repasa lo que has visto en los temas [3](../03-redes-entrega-contenido/tema3.md) y [4](../04-computo-serverless/tema4.md): el lanzamiento de una instancia de Amazon EC2 en la VPC predeterminada, el grupo de seguridad, los datos de usuario, un volumen de Amazon EBS, la conexión al servidor y la limpieza del laboratorio. El enunciado del día del examen será distinto y tendrá algo más de dificultad, pero se apoyará en las mismas destrezas.

Trabajarás en el Learner Lab del curso de AWS Academy. Entra en el curso, abre el contenido y pulsa el enlace de lanzamiento del laboratorio para el alumnado. Espera a que el indicador de AWS pase a verde y confirma, en la barra superior de la consola, que estás administrando recursos en la región Norte de Virginia (`us-east-1`). Si la consola está en otra región, cámbiala antes de crear nada: los recursos no aparecen de una región a otra y podrías dejar capacidad encendida sin verla.

La entrega es un único documento PDF, llamado `PO1_practica_orientativa.pdf`, con las capturas que se piden en cada ejercicio. En cada imagen debe leerse con claridad lo que se solicita (nombres, tipo, región, reglas o la barra de direcciones del navegador). Al terminar, deja el laboratorio limpio: una instancia que sigue en ejecución factura cómputo y, si no se borra, también el volumen.

!!! warning "Sin credenciales en la entrega"
    No incluyas claves, ficheros `.pem` ni capturas con credenciales.

## Antes de empezar

1. Inicia el Learner Lab y espera a que el círculo junto a AWS esté en verde.
2. Abre la consola de EC2 y comprueba que la región es **Norte de Virginia (`us-east-1`)**.
3. Comprueba que en la lista de pares de claves aparece **vockey**, que es el que proporciona el laboratorio. En esta práctica la conexión se hace desde la propia consola (EC2 Instance Connect), así que no necesitas el fichero `.pem` en tu portátil, aunque el par de claves sí debe quedar asociado a la instancia.
4. Prepara un editor o un procesador de texto para ir pegando las capturas a medida que avanzas, no al final, cuando ya hayas terminado la instancia.

## Datos comunes del laboratorio

| Campo | Valor |
| --- | --- |
| Región | Norte de Virginia (`us-east-1`) |
| Nombre de la instancia | `web-po1-practica` |
| AMI | Amazon Linux 2023 (la versión actual del catálogo *Quick Start*) |
| Tipo de instancia | `t3.micro` (si no estuviera disponible en el laboratorio, usa `t2.micro` y déjalo indicado en la captura) |
| Par de claves | `vockey` |
| Red | VPC predeterminada y una subred de esa VPC que asigne automáticamente una dirección IPv4 pública |
| Grupo de seguridad | Nombre `sg-web-po1`. Descripción: `Grupo de seguridad de la práctica orientativa PO1` |

La VPC predeterminada suele usar el bloque `172.31.0.0/16`, pero no hace falta escribir un CIDR concreto: elige la VPC que la consola marca como *default* y una de sus subredes con asignación automática de IPv4 pública.

## Ejercicio 1. Lanzar la instancia con datos de usuario (2,5 puntos)

El objetivo es dejar en ejecución un servidor web instalado en el primer arranque, todavía sin reglas de entrada en el grupo de seguridad. Así comprobarás más adelante qué ocurre cuando el tráfico no está permitido.

1. En la consola de EC2, pulsa **Launch instance**.
2. Asigna el nombre `web-po1-practica`.
3. En *Application and OS Images*, elige **Amazon Linux 2023**. No hace falta buscar una compilación concreta del kernel: sirve la AMI actual de *Quick Start*.
4. En *Instance type*, elige **t3.micro** (o **t2.micro**, si *t3.micro* no aparece).
5. En *Key pair*, selecciona **vockey**. No crees un par nuevo.
6. En *Network settings*, pulsa **Edit** para ver todas las opciones. Elige la **VPC predeterminada** y una de sus subredes, y comprueba que *Auto-assign public IP* queda en *Enable*. Marca la opción de crear un grupo de seguridad y nómbralo `sg-web-po1`, con la descripción indicada en la tabla. **Elimina o desactiva cualquier regla de entrada** que el asistente haya añadido por defecto (SSH, HTTP o HTTPS). El grupo debe quedar sin reglas de entrada al lanzar.
7. En *Configure storage* deja el volumen raíz que propone la AMI; lo modificarás en un ejercicio posterior.
8. Despliega **Advanced details**. Activa la **protección frente a la terminación** (*Termination protection*). En **User data** pega exactamente este script:

    ```bash
    #!/bin/bash
    dnf install -y httpd
    systemctl enable httpd
    systemctl start httpd
    echo '<html><h1>Practica orientativa PO1</h1></html>' > /var/www/html/index.html
    ```

9. Lanza la instancia y espera a que pase a estado *running* y a que las comprobaciones de estado queden en 2/2. El script de datos de usuario puede tardar un par de minutos en terminar; no adelantes el ejercicio 2 hasta ver la instancia en buen estado.

**Entrega (tres capturas):**

- El apartado *Name and tags*, la AMI y el tipo de instancia, tomados del asistente antes de lanzar o del resumen equivalente.
- El apartado *Network settings*, donde se vean la VPC predeterminada, la subred y el grupo de seguridad `sg-web-po1` sin reglas de entrada.
- El apartado *Advanced details*, donde se vean la protección frente a la terminación activada y el script de *User data*.

## Ejercicio 2. Publicar la página web (2 puntos)

Cuando lanzaste la instancia, el script instaló Apache HTTP Server y dejó una página sencilla. Si ahora abres en el navegador la dirección IPv4 pública, la conexión no debería entrar: el grupo de seguridad aún no permite el puerto 80. El fallo, en este caso, no es de la nube, sino de la configuración *en* la nube.

1. Localiza el grupo de seguridad `sg-web-po1` (desde la instancia, pestaña *Security*, o desde *Network & Security → Security Groups*).
2. Añade una regla de **entrada** de tipo HTTP, protocolo TCP, puerto **80**, origen `0.0.0.0/0`, con una descripción breve (por ejemplo, `HTTP de la practica`).
3. Copia la **dirección IPv4 pública** de la instancia y ábrela en el navegador con `http://` seguido de esa IP (sin puerto, porque HTTP usa el 80). Debes ver el mensaje *Practica orientativa PO1*. No uses el enlace *open address* de la consola, porque abre la dirección con `https://` y el servidor no escucha en el puerto 443, de modo que la página no cargaría.
4. Si la página no carga, espera un poco más a que termine el *user data*, confirma que la instancia tiene IP pública y que la regla quedó guardada, y vuelve a intentarlo. No abras todavía el puerto 22: la conexión SSH llega en el ejercicio 4.

**Entrega (dos capturas):**

- Las reglas de entrada del grupo `sg-web-po1`, donde se vea la regla HTTP del puerto 80.
- El navegador mostrando el mensaje de la página y, en la barra de direcciones, la IPv4 pública de la instancia.

## Ejercicio 3. Cambiar el tipo de instancia y el tamaño del volumen (2 puntos)

Vas a distinguir dos cambios que se hacen de manera distinta. El tipo de instancia (la plantilla de procesador y memoria) exige parar la máquina. El volumen de EBS sí se puede ampliar con la instancia en ejecución, aunque en esta práctica basta con dejar constancia del cambio en la consola: no se pide redimensionar el sistema de ficheros desde Linux.

1. Selecciona la instancia `web-po1-practica` y **párala** (*Stop instance*). Espera al estado *stopped*.
2. En *Actions → Instance settings → Change instance type*, cambia el tipo a **t3.small** (o **t2.small**, si en el ejercicio 1 usaste *t2.micro*). Aplica el cambio y **vuelve a iniciar** la instancia.
3. Cuando esté otra vez en *running*, abre **Elastic Block Store → Volumes**, localiza el volumen raíz asociado a la instancia y pulsa *Actions → Modify volume*. Fija el tamaño en **12 GiB**. Si el volumen ya midiera 12 GiB o más, no lo reduzcas: captura el tamaño actual y explícalo en una línea junto a la imagen.
4. Espera a que la modificación del volumen pase a *optimizing* o *completed* y a que el nuevo tamaño se vea en la lista. El volumen seguirá en estado *in-use*, porque continúa conectado a la instancia. Comprueba también que, tras el arranque, la instancia sigue teniendo una IPv4 pública. Al parar y volver a iniciar una instancia sin IP elástica, AWS le asigna una IPv4 pública distinta; no pasa nada, usarás la nueva en el ejercicio siguiente.

**Entrega (dos capturas):**

- Los detalles de la instancia, donde se lea el nuevo tipo (`t3.small` o `t2.small`).
- El panel *Modify volume* (o el detalle del volumen ya modificado) donde se vea el tamaño de 12 GiB, o el tamaño actual si ya era mayor.

## Ejercicio 4. Conectarte y personalizar la página (2 puntos)

Ahora entrarás en la instancia desde la propia consola de AWS y cambiarás el mensaje de la página para que incluya tu nombre y apellidos. Después de editar el fichero hay que reiniciar Apache para que el navegador muestre el contenido nuevo.

1. Añade al grupo `sg-web-po1` una regla de **entrada** SSH, protocolo TCP, puerto **22**, origen `0.0.0.0/0`. En un entorno profesional restringirías el origen.

    !!! note "Por qué no basta con *My IP*"
        En este laboratorio, la conexión **EC2 Instance Connect sale desde rangos de AWS, no desde la IP de tu casa**, de modo que una regla limitada a *My IP* hace que la conexión falle.

2. Selecciona la instancia, pulsa **Connect** y usa la pestaña **EC2 Instance Connect**. El usuario de Amazon Linux 2023 es `ec2-user`. Conecta.
3. Edita `/var/www/html/index.html` para que la página muestre exactamente este mensaje, con tu nombre y tus apellidos: `Esta es mi web. Mi nombre es: Nombre Apellidos`. Puedes usar, por ejemplo:

    ```bash
    sudo tee /var/www/html/index.html >/dev/null << 'EOF'
    <html><h1>Esta es mi web. Mi nombre es: Nombre Apellidos</h1></html>
    EOF
    sudo systemctl restart httpd
    ```

4. Sustituye `Nombre Apellidos` por los tuyos. Comprueba con `systemctl is-active httpd` que el servicio sigue activo y abre de nuevo en el navegador la IPv4 pública actual.

**Entrega (dos capturas):**

- La sesión de EC2 Instance Connect (o la terminal SSH equivalente) en la que se vea la edición del fichero `index.html` y el reinicio de `httpd`.
- El navegador con el nuevo mensaje, tu nombre legible y la IPv4 pública en la barra de direcciones.

## Ejercicio 5. Terminar la instancia y dejar el laboratorio limpio (1,5 puntos)

La protección frente a la terminación, que activaste al lanzar, impide un *terminate* accidental. Antes de eliminar la instancia hay que desactivarla. Al terminar, confirma que no queda la máquina en ejecución ni un volumen huérfano que siga facturando.

1. Con la instancia seleccionada, abre *Actions → Instance settings → Change termination protection* y **desactiva** la protección.
2. Pulsa *Instance state → Terminate instance* y confirma. El estado pasará a *shutting-down* y después a *terminated*.
3. Revisa **Volumes**. Si el volumen raíz tenía marcada la opción de borrado al terminar, desaparecerá solo; si quedara alguno de esta práctica, elimínalo.
4. Si quieres, borra también el grupo de seguridad `sg-web-po1`. Es posible que la consola no te deje hacerlo durante unos segundos, mientras la instancia recién terminada sigue apareciendo en la lista; en ese caso, inténtalo al final y, si continúa asociado, déjalo indicado en el documento. No se penaliza que quede el grupo, porque lo importante es que no quede cómputo encendido ni volúmenes facturando.

**Entrega (dos capturas):**

- La lista de instancias (o el detalle de `web-po1-practica`) donde se vea el estado **terminated**, o la lista sin instancias en ejecución en la región `us-east-1`.
- La lista de **Volumes** de `us-east-1`, donde se vea que no queda ningún volumen de esta práctica.

## Resumen de la puntuación

| Ejercicio | Contenido | Puntos |
| --- | --- | --- |
| 1 | Lanzamiento en `us-east-1` con AMI, tipo, *vockey*, VPC predeterminada, grupo sin entradas, protección frente a la terminación y *user data* | 2,5 |
| 2 | Regla HTTP y página visible por la IPv4 pública | 2,0 |
| 3 | Cambio de tipo (con la instancia parada) y ampliación del volumen de EBS a 12 GiB | 2,0 |
| 4 | Regla SSH, conexión desde la consola y página personalizada con reinicio de `httpd` | 2,0 |
| 5 | Desactivación de la protección, terminación y laboratorio sin cómputo encendido | 1,5 |
| **Total** | | **10** |

## Consejos finales

!!! tip "Antes de entregar"
    Una captura ilegible, recortada o de otra región no acredita el paso. Si en el ejercicio 1 usaste `t2.micro` porque no aparecía `t3.micro`, mantén la misma familia al pasar a *small* y déjalo escrito junto a la imagen. Si la página del ejercicio 2 no carga, no abras puertos al azar: revisa la regla 80, la IP pública y que el *user data* haya terminado. Cuando acabes, comprueba una última vez que en `us-east-1` no queda ninguna instancia en *running* ni *stopped*.

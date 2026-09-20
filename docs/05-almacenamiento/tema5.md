---
title: Tema 5 — Almacenamiento
description: S3, EBS, EFS, FSx, clases de almacenamiento y backup (Foundations M7).
---

# Tema 5. Almacenamiento

En una app web hay **tres** estilos de almacenamiento que la gente mezcla: el disco de la VM, una carpeta de red compartida y un **objeto** al que se llega por HTTP. Subir el `uploads/` de Express a [S3](#s3) no es lo mismo que montar un [EBS](#ebs). **Foundations M7.** Ver [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). Si tu API ya corre en EC2 o Lambda, aquí decides **dónde viven los ficheros** y qué pasa si borras la instancia.

## Propuesta didáctica

> **RA4.** *Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.*

### Criterios de evaluación (RA4)

* **a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.
* **c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.

Bases de datos: Tema 6.

### Contenidos

* Objeto (S3), bloque (EBS), fichero (EFS / FSx).
* Clases S3, lifecycle, versionado, *block public access*.
* Snapshots, instance store, backup y movimiento de datos (Snow, Gateway).

### Programación de aula (orientativa)

| Quincena | En tutoría | Trabajo autónomo / evidencias |
| --- | --- | --- |
| **Q7** | S3 vs EBS/EFS + lifecycle | **PR501**; Autocheck del tema |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Responde con lo que sepas"
    1. ¿**S3** es el disco del sistema operativo de la EC2, o un almacén de **objetos** por API/HTTP?
    2. ¿Cuándo usarías **EBS** frente a subir ficheros a un bucket?
    3. Dos EC2 en AZ distintas necesitan la **misma carpeta** montada: ¿EBS o **EFS**?
    4. Si terminas la instancia, ¿qué suele pasar con los datos solo en el disco raíz si no hiciste snapshot?
    5. ¿Por qué la **salida de datos** (egress) puede disparar la factura aunque el almacenamiento «parezca barato»?

Este cuestionario es solo para ti: te ayuda a ver qué dominas ya y qué te falta antes o mientras lees el tema. No se entrega en Aules; respóndelo con lo que sepas y, cuando quieras contrastar, abre el bloque **Soluciones (autoevaluación)** debajo o el índice en [Soluciones](../90-soluciones/soluciones.md).

<details markdown="1">
<summary>Soluciones (autoevaluación)</summary>

1. **S3** es almacén de **objetos** (API/HTTP), no el disco del SO de la EC2.

2. **EBS** cuando el SO o la app necesitan un **volumen de bloque** montado en esa VM (disco del sistema, datos de una sola instancia).

3. **EFS** (fichero de red montable en varias EC2). EBS es de una instancia (salvo patrones avanzados fuera de este módulo).

4. Los datos del disco raíz **se pierden** al terminate si no hay snapshot/AMI que los preserve (salvo volúmenes que el enunciado diga conservar).

5. El **egress** factura el tráfico que sale hacia internet/clientes; un bucket «barato» sirviendo mucho sin CDN puede salir caro en red.

</details>

---

## Bloque Foundations (M7)

Antes de memorizar logos, fija el **estilo de acceso**. En desarrollo web decides: ¿guardo un fichero con una URL/API (foto de perfil, ZIP, front estático)? ¿necesito un disco que el SO vea como `/dev/xvdf` (sistema de la VM)? ¿varias instancias deben montar la **misma** carpeta a la vez (`uploads/` compartido)? Esas tres preguntas apuntan a objeto, bloque o fichero —y casi nunca al mismo servicio.

| Estilo | Unidad | Servicio | ¿Se monta en el SO? | Caso web |
| --- | --- | --- | --- | --- |
| **Objeto** | Objeto + metadatos, HTTP | **S3** | No (API / SDK) | Imágenes, zips, front estático |
| **Bloque** | Volumen | **EBS** | Sí (disco de EC2) | Disco del sistema, datos de una sola VM |
| **Fichero** | NFS/SMB | **EFS**, **FSx** | Sí (carpeta de red) | Varias instancias leyendo el mismo `uploads/` |

<figure markdown="span">
![Comparativa de estilos de almacenamiento en AWS](img/salvador/s3_1.jpg){ width="720" }
<figcaption>Bloque / fichero / objeto: elige por cómo accede la app.</figcaption>
</figure>

!!! tip "Ventajas por estilo (resumen)"
    - **Bloque (EBS):** más rendimiento para el disco de una VM.
    - **Objeto (S3):** sencillo de integrar por API y suele ser más barato para ficheros/front.
    - **Fichero (EFS):** varias EC2 montan la misma carpeta.

<figure markdown="span">
![Almacenamiento: S3 (objeto), EBS (bloque) y EFS (archivo)](../img/diagramas/almacenamiento-opciones.svg){ width="800" }
<figcaption>Tres estilos de acceso: API de objetos, disco de la VM o carpeta NFS compartida.</figcaption>
</figure>

**Antes / después.** Antes: fotos de perfil en `public/uploads` dentro de la EC2 (se pierden al terminar la instancia; no escalan a dos nodos). Después: subida con SDK a S3 y URL firmada o CloudFront. El código deja de tratar el disco local como almacén duradero de usuario.

### Amazon S3

**[Amazon S3](#s3)** (*Simple Storage Service*) es almacenamiento de **objetos**: guardas bytes con una clave dentro de un *bucket*, y hablas con él por API/SDK (o URL firmada), no como si fuera la unidad `C:`. Buckets (nombre globalmente único), objetos, prefijos. **Clases** (Standard, IA, Glacier…): precio frente a tiempo de acceso. **Lifecycle** para enfriar lo que nadie pide. Versionado. *Block public access* por defecto: un 403 en la URL es el resultado **correcto** si el objeto no debe ser público.

<figure markdown="span">
![Clases de almacenamiento S3 / ciclo de vida (visión de consola)](img/salvador/s3_20.png){ width="640" }
<figcaption>Clases y ciclo de vida: Standard es lo habitual; Glacier no es «disco barato con acceso inmediato».</figcaption>
</figure>

En código DAW suele verse así: el controlador recibe el multipart, el SDK hace `PutObject`, y la base solo guarda la clave o la URL. El navegador no necesita NFS. Si mañana hay dos instancias detrás del ALB, **ambas** hablan con el mismo bucket: no hay divergencia de `uploads/` locales.

Tras un `PutObject` correcto, una lectura inmediata del mismo objeto debe ver los datos nuevos: S3 ofrece consistencia fuerte de lectura tras escritura. En clase: no inventes «espera unos segundos» como si fuera 2015.

<figure markdown="span">
![Diagrama de consistencia fuerte de lectura tras escritura en Amazon S3](img/capturas/s3-consistency1.png){ width="800" }
<figcaption>Lectura tras escritura en el mismo objeto. Fuente: Amazon S3 User Guide (AWS).</figcaption>
</figure>

Web estática en S3 (HTML/JS): patrón útil para un SPA. El API sigue en otro sitio (Gateway + Lambda, o EC2). No es un CMS.

**Cuándo NO usar S3 como «disco».** No montes S3 como si fuera `/var/lib/mysql` ni esperes bloqueos POSIX de fichero para una base embebida. Tampoco abras el bucket al mundo para «que se vea el lab»: usa URLs firmadas o un origen CloudFront con política clara.

Si el acceso a S3 sale «por internet» desde una EC2 en VPC privada, en arquitecturas avanzadas aparece el endpoint/PrivateLink. Nivel Foundations: entiende que S3 es un servicio *regional* con API, no un disco montado.

<figure markdown="span">
![Arquitectura de acceso a S3 desde VPC con endpoints](img/capturas/s3-acceso-privado-arquitectura.png){ width="800" }
<figcaption>Acceso a S3 desde una VPC (patrón de la guía de consola). Fuente: AWS Management Console Getting Started Guide (AWS).</figcaption>
</figure>

### Amazon EBS

**[Amazon EBS](#ebs)** (*Elastic Block Store*) es el **disco de bloque** de una instancia EC2: se monta en el sistema operativo como un volumen. Vive en **una** AZ. Snapshots hacia S3. Tipos gp/io (IOPS). **Instance store:** disco del host, efímero; no lo uses como única copia del TFG.

<figure markdown="span">
![Volumen EBS asociado a una instancia](img/salvador/s3_2.jpg){ width="720" }
<figcaption>EBS: volumen de bloque ligado a EC2 (misma AZ).</figcaption>
</figure>

!!! success "Ventajas EBS"
    - Replicación dentro de la AZ; persistencia aunque pares la instancia (según configuración).
    - Cifrado sencillo; se puede **aumentar** el tamaño (no reducir).
    - Un volumen EBS solo se asocia a una instancia de **su misma AZ**.

<figure markdown="span">
![Crear volumen EBS: tipo gp3, tamaño, AZ y etiqueta](img/salvador/s3_3.png){ width="720" }
<figcaption>Volumen EBS: tipo, GiB, IOPS y **misma AZ** que la instancia a la que lo vas a asociar.</figcaption>
</figure>

Multi-attach avanzado queda fuera. La regla Foundations: un volumen ≈ una instancia.

Si terminas la EC2 y dejas el volumen, **sigue facturando**. El snapshot es la copia durable hacia S3; el volumen huérfano es un clásico de lab caro.

### EFS / FSx y movimiento

**[Amazon EFS](#efs)** ofrece un sistema de ficheros **NFS** elástico: **varias** EC2 pueden montar el mismo directorio a la vez (incluso en AZ distintas de la región). **FSx:** Windows / Lustre / NetApp (nombres de examen).

<figure markdown="span">
![Amazon EFS montado desde varias instancias](img/salvador/s3_9.png){ width="720" }
<figcaption>EFS: carpeta compartida entre EC2.</figcaption>
</figure>

!!! note "Características EFS (resumen)"
    - NFS gestionado; crece y decrece sin dimensionar a ojo el LUN.
    - Varias EC2 (incluso en AZ distintas de la región) montan el **mismo** sistema de ficheros.
    - Encaja en `uploads/` compartidos; no sustituye a S3 para objetos servidos por HTTP a escala.

<figure markdown="span">
![Montaje / acceso EFS desde instancias](img/salvador/s3_11.png){ width="720" }
<figcaption>Varias instancias montan el mismo EFS (idea de práctica).</figcaption>
</figure>

<figure markdown="span">
![Políticas / acceso a objetos (contexto S3)](img/salvador/s3_17.png){ width="640" }
<figcaption>Acceso a objetos: política y *block public access* van juntos.</figcaption>
</figure>

**Storage Gateway**, familia **Snow** (dispositivo físico para muchos TB), **AWS Backup**, DataSync: reconocer *cuándo* un VPN no basta para 80 TB.

### Errores frecuentes (almacenamiento)

- Guardar uploads solo en el EBS de una instancia detrás de un ASG (cada nodo ve un disco distinto).
- Confundir Glacier «barato» con «acceso inmediato».
- Medir solo GB-mes y olvidar **egress** al servir ficheros grandes a internet.

### Relación con otros temas

S3 + CloudFront (Tema 3) para estáticos. EBS nace con EC2 (Tema 4). Las bases (Tema 6) no se sustituyen por un bucket: el bucket guarda objetos, no transacciones SQL.

---

## Bloque Ampliación Practitioner (CLF-C02)

El examen premia elegir el **estilo** de almacén (objeto, bloque o fichero) y no olvidar la **salida de datos** en la factura. Glacier es una clase o archivo de S3, no un disco de SO.

!!! tip "Para el CLF"
    S3 no sustituye el EBS del sistema operativo; EFS no es lo mismo que un volumen de una sola VM. Si sirves mucho tráfico desde un bucket sin CDN, el coste que dispara suele ser el egress. Ampliación y **autocheck certificación** en [Certificación § Tema 5](../99-certificacion/certificacion.md#tema-5).

---

## Videotutorial

**Principal (Foundations).** [ATTA AWS Academy 02 S3](https://www.youtube.com/watch?v=OkGNAHtVCq8) (~12 min).

<iframe src="https://www.youtube.com/embed/OkGNAHtVCq8" title="ATTA AWS Academy 02 S3 — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: subida de objeto y *block public access*; el 403 es evidencia, no un fallo del lab.

**Extra (opcional).** [S3 Static Web](https://www.youtube.com/watch?v=GMsD5XIfRLc) (~8 min) — hosting estático mínimo. Vídeo: Profe Santos Cloud (YouTube).

**Extra.** [Web estática en S3](https://www.youtube.com/watch?v=HTmkUgp3XdY) — bucket, *static website hosting* y prueba del endpoint.

<iframe src="https://www.youtube.com/embed/HTmkUgp3XdY" title="Web estática en S3" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

<figure markdown="span">
![Consola S3 / bucket](img/salvador/s3_18.png){ width="640" }
<figcaption>Trabajo con buckets S3 en consola.</figcaption>
</figure>

<figure markdown="span">
![Hosting estático / web en S3](img/salvador/s3_21.png){ width="640" }
<figcaption>Web estática sobre S3 (paso de práctica).</figcaption>
</figure>

El M7 del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

### PR501 — Objetos y bloques

* :simple-neutralinojs: **PR501**. (RA4 // a, c // **PR 0–10**). Distingues almacén de objetos y de bloque con **una** evidencia del lab Academy M7 (S3 o EBS), sin dejar recursos vivos.

  Completa **una** de estas vías:

  - Sube un fichero a S3, deja *block public access*, prueba la URL y explica el 403.
  - O: volumen EBS, montaje, snapshot y borrado del volumen (e instancia) de lab.

  **Tareas:** documenta la vía elegida con capturas en el desarrollo; anota la clase S3 si el lab la pide; al terminar, *delete* de lo creado.

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR501.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo (no sustituye el enunciado): [Soluciones · PR501](../90-soluciones/pr/PR501.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Evidencia S3 o EBS | Una vía completa y correcta | 0–4 |
| Concepto (objeto/bloque) | Explicación coherente (403 / snapshot) | 0–3 |
| Limpieza | Recursos de lab eliminados | 0–2 |
| Claridad | Capturas con leyenda / `.md` ordenado | 0–1 |
| **Total** | | **/10** |

---

### Versionado y borrados (por qué importa en un TFG)

Con versionado en S3, un `delete` no siempre destruye el objeto: puede dejar un *delete marker*. Eso salva un borrado accidental en prácticas… y también deja residuos que facturan. Lifecycle rules existen para pasar a clases frías o expirar versiones viejas. En Foundations basta reconocer el mecanismo; en un proyecto real, sin lifecycle, el bucket de «pruebas» crece sin control.

EBS: snapshot ≠ backup mágico de la aplicación. Es copia del volumen en un momento; la app debe estar en estado coherente (o aceptas el riesgo). Instance store desaparece al parar/terminar: no guardes ahí el único ZIP del TFG.

---

## Autocheck del tema

Comprueba almacenamiento de este tema. CLF: [Certificación § Tema 5](../99-certificacion/certificacion.md#tema-5).

1. El disco del SO de una EC2 se diseña normalmente con…  
   a) S3 Standard · b) **EBS** · c) Glacier Deep Archive
2. **V/F.** EFS puede montarse en varias EC2 (misma región) a la vez.
3. Una foto a la que casi nadie accede en un año: ¿clase/archivo **caliente** o **fría/archivo** (idea)?
4. **V/F.** Un snapshot de EBS «vive solo» en la AZ del volumen y no se puede usar para recuperar en la región.
5. Empareja: **S3** · **EBS** · **egress** con: (a) objetos por API/HTTP · (b) volumen de bloque · (c) tráfico de salida que factura

<details markdown="1">
<summary>Soluciones</summary>

1. **b** (EBS).

2. **Verdadero**.

3. **Fría/archivo** (Glacier / clase fría — idea, no el céntimo exacto).

4. **Falso** — el snapshot es recurso de región (idea Foundations: no lo trates como «solo disco local de la AZ»).

5. **S3** encaja con (a) objetos por API/HTTP; **EBS**, con (b) volumen de bloque; el **egress**, con (c) el tráfico de salida que factura.

</details>

---


## Glosario

**S3**{: #s3}
*Simple Storage Service*: almacenamiento de objetos accesible por API/HTTP. Ideal para ficheros, backups de objetos y front estático; no sustituye el disco del sistema de una VM. El acceso público es una decisión explícita (y peligrosa si se deja abierta «para la demo»).

**EBS**{: #ebs}
*Elastic Block Store*: volúmenes de bloque para instancias EC2. Se montan en el SO; suelen vivir en una sola AZ. Son el disco de la VM: sistema, swap o datos locales —no el almacén compartido de un ASG con varios nodos.

**EFS**{: #efs}
*Elastic File System*: sistema de ficheros NFS gestionado, compartible por varias instancias a la vez en la región. Encaja cuando varias EC2 necesitan la misma carpeta montada; no sustituye a S3 para objetos servidos por HTTP a escala web.


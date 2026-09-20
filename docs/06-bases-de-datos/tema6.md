---
title: Tema 6 — Bases de datos
description: RDS, Aurora, DynamoDB, Redshift y elección relacional vs NoSQL (Foundations M8).
---

# Tema 6. Bases de datos

Instalar MySQL «en la misma EC2 que Express» funciona en el aula y **acopla** fallo, parche y backup. En nube la pregunta de DAW es: ¿necesito SQL transaccional, un almacén de documentos, o analítica? **Foundations M8.** Ver [glosario](#glosario).

!!! tip "Al empezar"
    Empieza por el [cuestionario inicial](#cuestionario-inicial). Distingue ya el almacenamiento de objetos (Tema 5) de los **datos estructurados**: aquí eliges motor y quién parchea.

## Propuesta didáctica

> **RA4.** *Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.*

### Criterios de evaluación (RA4)

* **b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.
* **c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.

### Contenidos

* BD en EC2 frente a [RDS](#rds) / Aurora (quién parchea el motor).
* Relacional: [Multi-AZ](#multi-az) vs [*read replica*](#read-replica).
* DynamoDB, ElastiCache, Redshift: cuándo no es RDS.
* DMS / SCT: migración de datos (enlace con las 7 R del Tema 1).

### Programación de aula (orientativa)

| Quincena | En tutoría | Trabajo autónomo / evidencias |
| --- | --- | --- |
| **Q8** | RDS Multi-AZ vs réplica + DynamoDB | **PR601**; Autocheck del tema |

---

<a id="cuestionario-inicial"></a>

## Cuestionario inicial

!!! question "Responde con lo que sepas"
    1. MySQL en la misma EC2 que Express frente a **RDS**: ¿quién aplica parches del **motor** en cada caso?
    2. ¿**Multi-AZ** responde sobre todo a failover de escritura o a escalar lecturas de reporting?
    3. ¿Para qué sirve una **réplica de lectura** que Multi-AZ no cubre igual?
    4. ¿Cuándo tendría sentido **DynamoDB** *además* de un checkout SQL, y cuándo es un error sustituirlo «por moda»?
    5. ¿Por qué abrir **3306** al mundo desde RDS es un anti-patrón aunque «así conectas el cliente SQL del portátil»?

Este cuestionario es solo para ti: te ayuda a ver qué dominas ya y qué te falta antes o mientras lees el tema. No se entrega en Aules; respóndelo con lo que sepas y, cuando quieras contrastar, abre el bloque **Soluciones (autoevaluación)** debajo o el índice en [Soluciones](../90-soluciones/soluciones.md).

<details markdown="1">
<summary>Soluciones (autoevaluación)</summary>

1. MySQL en EC2: **tú** parcheas el motor (y el SO). En **RDS**, **AWS** aplica parches del motor.

2. **Multi-AZ** responde sobre todo al **failover** de la escritura (otra AZ), no a escalar SELECT de reporting.

3. La **réplica de lectura** escala lecturas / reporting de forma asíncrona; no es el mismo mecanismo que el failover Multi-AZ.

4. **Además:** p. ej. catálogo o sesión NoSQL junto a un checkout SQL. **Error:** tirar el dominio relacional/transaccional «porque DynamoDB escala» sin necesidad.

5. Expone el motor a internet entero; el SG debe aceptar el SG de la API (o bastion), no `0.0.0.0/0` en 3306.

</details>

---

## Bloque Foundations (M8)

### ¿Gestionada o «en la VM»?

MySQL en EC2: control total y **tú** haces alta disponibilidad, parches y copias. **[Amazon RDS](#rds)** (*Relational Database Service*) es una base de datos **relacional gestionada**: AWS asume parches del motor, snapshots y Multi-AZ opcional. El examen (y una app de clase bien hecha) premian el servicio gestionado salvo motor raro o licencia que lo impida. Para un desarrollador web: sigues hablando SQL; dejas de ser el DBA del SO.

<figure markdown="span">
![Visión de RDS como servicio gestionado](img/salvador/rds_1.png){ width="640" }
<figcaption>RDS: motor gestionado (PaaS de datos), no solo una EC2 con MySQL.</figcaption>
</figure>

!!! note "Por qué RDS y no MySQL «a pelo» en EC2"
    Puedes instalar el SGBD en EC2, sí. Con RDS te ahorras parches del motor, backups y buena parte de la HA. A cambio, menos control del SO. Por seguridad suele ir en **subnets privadas** y solo acepta el SG de la API.

<figure markdown="span">
![Bases de datos gestionadas: RDS/Aurora y DynamoDB](../img/diagramas/bases-datos-opciones.svg){ width="800" }
<figcaption>Relacional gestionado frente a NoSQL serverless: elige por el modelo de datos, no por el logo.</figcaption>
</figure>

Al crear RDS, mira motor, plantilla (Free tier / Dev) e identificador **antes** de pulsar Create: ahí se decide buena parte de la factura del lab.

<figure markdown="span">
![Asistente Create database de Amazon RDS con MySQL y Free tier](img/capturas/rds-create-mysql.png){ width="800" }
<figcaption>Create database: motor MySQL y plantilla Free tier. Fuente: Amazon RDS User Guide (AWS).</figcaption>
</figure>

**Antes / después.** Antes: MySQL en la misma EC2 que Express; un `terminate` se lleva API y datos; el parche del SO afecta a ambos. Después: API en cómputo y RDS en subnet privada; snapshots y Multi-AZ los activa el servicio gestionado, pero **tú** sigues diseñando esquema, usuarios y SG.

### Relacionales

**RDS:** MySQL, PostgreSQL, MariaDB, SQL Server, Oracle… (el lab dirá el motor).

**Aurora:** compatible MySQL/PostgreSQL, almacenamiento distribuido, réplicas. Nivel Foundations: «RDS con más margen de HA/rendimiento», no el whitepaper interno.

Para el desarrollador web la sensación es la misma conexión SQL; cambia quién aplica el parche del motor y cómo pides Multi-AZ. Si tu framework ya habla PostgreSQL, Aurora PostgreSQL-compatible encaja sin reescribir el dominio —eso es *replatform* ligero, no *refactor*.

Dos mecanismos que se confunden:

- **[Multi-AZ](#multi-az):** disponibilidad (failover a otra AZ). No es un *speedup* de lecturas.
- **[Read replica](#read-replica):** escala de **lectura** (reporting). No es el mismo mecanismo que Multi-AZ.

<figure markdown="span">
![Esquema Multi-AZ en RDS](img/salvador/rds_4.png){ width="640" }
<figcaption>Multi-AZ: copia síncrona para failover.</figcaption>
</figure>

!!! tip "Multi-AZ frente a réplica de lectura"
    - **Multi-AZ:** escritura síncrona al standby; ante fallo, el standby toma el relevo (comercio, finanzas…).
    - **Réplica de lectura:** replicación asíncrona; escala SELECT / reporting; el failover manual no es el mismo mecanismo.

<figure markdown="span">
![Esquema de réplica de lectura en RDS](img/salvador/rds_3.png){ width="640" }
<figcaption>Réplica de lectura: escala SELECT; no es el mismo mecanismo que Multi-AZ.</figcaption>
</figure>

Security group: el puerto del motor **no** se abre a `0.0.0.0/0`. La API en subnet privada habla con RDS; tú no expones 3306 a internet «para DBeaver desde casa» si hay alternativas (bastion, VPN).

<figure markdown="span">
![RDS: VPC, subnet group y acceso público = No](img/salvador/rds_2.png){ width="720" }
<figcaption>Conectividad: VPC + subnet group; **acceso público = No** en lab serio.</figcaption>
</figure>

Si el lab pide WordPress+RDS, identifica en el `.md` qué es IaaS (EC2) y qué es gestionado (RDS): es exactamente el límite de responsabilidad del Tema 2 aplicado a datos.

### NoSQL y analítica

No todo dato de una app web es «tablas con FK». A veces el dominio es un documento JSON con picos imprevisibles; a veces necesitas caché; a veces informes analíticos. La tabla sitúa servicios: **no** elijas DynamoDB solo porque «suena a nube».

En un mismo producto puedes combinar: RDS para pedidos, ElastiCache para sesiones calientes, S3 para facturas PDF. Eso no es «multicloud»: es usar el servicio adecuado por patrón de acceso. El examen premia reconocer el patrón; el proyecto DAW premia no meterlo todo en una sola EC2.

| Servicio | Modelo | Caso |
| --- | --- | --- |
| **[DynamoDB](#dynamodb)** | Clave-valor / documentos, serverless | Sesiones, catálogo simple, picos imprevisibles |
| **ElastiCache** | Caché en memoria | No es el sistema de registro |
| **Redshift** | Analítica columnar | Informes; no el [OLTP](#oltp) de la tienda |
| DocumentDB / Neptune / Keyspaces | Nombres | Una línea en el examen |

DynamoDB no es «MySQL más rápido». Si tu dominio es relacional (pedidos, stock, FKs), RDS sigue siendo la hipótesis seria.

Al crear una tabla, lo primero que pide la consola es la **partition key** (y opcionalmente sort key). Sin eso no hay tabla: no es un «CREATE TABLE» SQL libre.

<figure markdown="span">
![Pantalla Create table de Amazon DynamoDB con partition key y sort key](img/capturas/dynamodb-create-table.png){ width="800" }
<figcaption>Create table: partition key (y sort key opcional). Fuente: Amazon DynamoDB Developer Guide (AWS).</figcaption>
</figure>

**Cuándo NO usar DynamoDB.** Pedidos con joins y transacciones clásicas, reporting ad hoc con SQL libre, o un equipo que solo conoce Sequelize/JPA sobre tablas normalizadas. Forzar NoSQL «porque es serverless» suele acabar en un modelo a medias y consultas dolorosas.

### Migración

**DMS** replica datos; **SCT** ayuda a convertir esquemas. Encaja con *replatform* (Tema 1): Oracle on-prem → Aurora, por ejemplo.

En Foundations no montas un proyecto DMS completo: reconoces la herramienta cuando el escenario es «mover datos con poco downtime» frente a «rediseñar la app» (*refactor*).

### Errores frecuentes (datos)

- Abrir 3306/5432 al mundo para «probar desde el portátil».
- Confundir Multi-AZ (failover) con read replica (escala de lectura).
- Dejar la instancia RDS del lab encendida tras la entrega.
- Guardar la contraseña del master en el README público del repo.

### Relación con otros temas

El disco y los objetos del Tema 5 no sustituyen una base transaccional: S3 guarda ficheros; aquí eliges motor y quién parchea. La API sigue viviendo en el cómputo del Tema 4, idealmente en subnet privada (Tema 3), y Multi-AZ o réplicas se entienden mejor cuando el Tema 7 pide justificar el trade-off.

---

## Bloque Ampliación Practitioner (CLF-C02)

Aquí el examen contrapone base **gestionada** frente a MySQL en la EC2, relacional frente a NoSQL, y Multi-AZ frente a réplica de lectura: no son sinónimos.

!!! tip "Para el CLF"
    Multi-AZ responde al **failover** de la escritura; la réplica de lectura escala SELECT o reporting. DynamoDB puede ir *además* de un checkout SQL si el dominio sigue siendo relacional; no lo sustituyas «por moda». Ampliación y **autocheck certificación** en [Certificación § Tema 6](../99-certificacion/certificacion.md#tema-6).

**Videotutorial (Practitioner / NoSQL).** [DynamoDB](https://www.youtube.com/watch?v=j1VL7ctuerw) (~10 min). Vídeo: Profe Santos Cloud (YouTube).

---

## Videotutorial

**Principal (Foundations).** [ATTA AWS Academy RDS 05](https://www.youtube.com/watch?v=43jYEiZvOsw) (~19 min).

<iframe src="https://www.youtube.com/embed/43jYEiZvOsw" title="ATTA AWS Academy RDS 05 — Profe Santos Cloud" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

Vídeo: Profe Santos Cloud (YouTube). Qué mirar: clase pequeña, SG del motor y borrar la instancia al acabar.

**Extra (opcional).** [RDSPrivateSubnet EC2Linux](https://www.youtube.com/watch?v=4X1f23RpBG0) (~21 min) — RDS en privada con EC2; refuerza el Tema 3. Vídeo: Profe Santos Cloud (YouTube).

**Extra.** [WordPress con RDS](https://www.youtube.com/watch?v=WUHzjhrS8tg) — app web en EC2 y base MySQL gestionada en RDS.

<iframe src="https://www.youtube.com/embed/WUHzjhrS8tg" title="WordPress con RDS" style="width:100%;max-width:840px;aspect-ratio:16/9;border:0;display:block;margin:0.8em auto" allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen loading="lazy"></iframe>

<figure markdown="span">
![WordPress / app conectada a RDS](img/salvador/rds_5.png){ width="640" }
<figcaption>App + RDS: la BD fuera de la EC2.</figcaption>
</figure>

<figure markdown="span">
![Pasos de práctica WordPress con RDS](img/salvador/rds_8.png){ width="640" }
<figcaption>Práctica: app en cómputo y credenciales apuntando al endpoint RDS.</figcaption>
</figure>

El M8 del LMS Academy se indica en clase / Aules.

---

## Actividad / práctica

### PR601 — RDS mínimo

* :simple-neutralinojs: **PR601**. (RA4 // b, c // **PR 0–10**). Configuras un RDS de lab (Academy M8) con tamaño mínimo, red restringida y secretos fuera del markdown público; borras la instancia al acabar.

  **Tareas:** elige clase/tamaño mínimo; restringe el SG (sin 3306/5432 al mundo); documenta el endpoint y la separación IaaS (EC2) / gestionado (RDS) si el lab enlaza WordPress+RDS (cinco líneas bastan); deja secretos fuera del `.md` público; **delete** RDS (y snapshots de lab si el enunciado lo pide).

  **Entrega:** según [Cómo entregar las prácticas](../index.md#entrega) — fichero `PR601.md` (o ZIP + `img/` si hay capturas).

  Guía de apoyo (no sustituye el enunciado): [Soluciones · PR601](../90-soluciones/pr/PR601.md).

| Criterio | Descripción | Puntos |
| --- | --- | --- |
| Instancia RDS | Creada según lab / tamaño mínimo | 0–3 |
| Seguridad de red | SG sin motor abierto al mundo | 0–3 |
| Secretos y claridad | Fuera del markdown público; IaaS vs managed si aplica | 0–2 |
| Limpieza | Delete RDS / snapshots de lab | 0–2 |
| **Total** | | **/10** |

---

### Conexión desde la app (detalle que el lab a veces oculta)

La URL JDBC/`DATABASE_URL` apunta al *endpoint* de RDS, no a una base en tu portátil. El security group de RDS acepta el SG de la API (o un bastion), no tu IP pública del instituto de forma permanente. Secretos: Parameter Store / Secrets Manager en el discurso Practitioner; en el lab, al menos **fuera** del markdown entregado en claro si el enunciado lo permite.

En el asistente verás la opción de conectar EC2↔RDS con los SG coherentes: úsala como checklist, no como excusa para abrir 3306 al mundo.

<figure markdown="span">
![Ajustes de red al conectar EC2 con Amazon RDS](img/capturas/rds-ec2-conexion.png){ width="800" }
<figcaption>Conexión EC2–RDS: SG y subnets, no IP pública del aula. Fuente: Amazon RDS User Guide (AWS).</figcaption>
</figure>

Si usas un ORM (Sequelize, JPA, Entity Framework), Multi-AZ no cambia tu código SQL: cambia la disponibilidad del endpoint. Read replicas sí pueden exigir un connection string de solo lectura para reporting.

---

## Autocheck del tema

Comprueba bases de datos de este tema. CLF: [Certificación § Tema 6](../99-certificacion/certificacion.md#tema-6).

1. **Multi-AZ** en RDS sirve sobre todo para…  
   a) acelerar SELECT de reporting · b) **failover** si cae una AZ · c) sustituir backups
2. Checkout con transacciones SQL: primera hipótesis…  
   a) DynamoDB · b) **RDS/Aurora** · c) Redshift
3. ¿Quién parchea el **motor** en RDS?
4. **V/F.** Redshift es la opción típica de OLTP de la tienda online.
5. Empareja: **DynamoDB** · **ElastiCache** · **read replica** con: (a) NoSQL clave-valor · (b) caché en memoria · (c) escala de lectura

<details markdown="1">
<summary>Soluciones</summary>

1. **b**.

2. **b**.

3. **AWS** (managed); tú esquemas/datos/accesos.

4. **Falso** — Redshift ≈ analítica/warehouse; OLTP → RDS/Aurora.

5. **DynamoDB** encaja con (a) NoSQL clave-valor; **ElastiCache**, con (b) caché en memoria; la **read replica**, con (c) escala de lectura.

</details>

---


## Glosario

**RDS**{: #rds}
*Relational Database Service*: bases de datos relacionales gestionadas (MySQL, PostgreSQL…). AWS opera el motor y la infraestructura; tú gestionas esquemas, datos y accesos. Para una API DAW es la hipótesis habitual cuando el dominio es SQL transaccional.

**Multi-AZ**{: #multi-az}
Despliegue de RDS (u otros servicios) en más de una zona de disponibilidad para **failover** y mayor disponibilidad. No sustituye a las réplicas de lectura ni acelera por sí solo las consultas SELECT de reporting.

**read replica**{: #read-replica}
Copia de solo lectura de una base relacional para repartir consultas de lectura. No es el mecanismo principal de failover Multi-AZ. Útil cuando el cuello de botella es lectura, no la caída de una AZ.

**DynamoDB**{: #dynamodb}
Base NoSQL gestionada (clave-valor / documentos), serverless y de baja latencia. Encaja con modelos no relacionales y picos variables; no es un sustituto automático de SQL transaccional con joins y FKs.

**OLTP**{: #oltp}
*Online Transaction Processing*: cargas transaccionales del día a día (pedidos, stock). Se distingue de la analítica / reporting (p. ej. Redshift). Mezclar ambos en el mismo motor sin criterio suele degradar la tienda o el informe.


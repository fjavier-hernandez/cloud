# PROGRAMACIÓN DIDÁCTICA

## INTRODUCCIÓN A LA NUBE PÚBLICA

**Duración:** **100 h** (módulo optativo; Decreto 114/2025, anexo X-XVII, modificado por el Decreto 95/2026, anexo IV). En semipresencial rigen las mismas 100 h (Orden 30/2022, art. 3). De ellas, **72 h (72 %)** se trabajan en el centro antes de la formación en empresa y **28 h (28 %)** quedan vinculadas a la empresa.

**CICLO FORMATIVO DE GRADO SUPERIOR**  
**DESARROLLO DE APLICACIONES WEB (DAW)**  
**Segundo curso — modalidad semipresencial (INP)**  

**Profesor:** Javier Hernández Illán  

**CURSO:** 2026/2027  

**Centro:** IES Macià Abela (Crevillent)  
**Departamento de Informática**

::: manual-index

## Índice

El documento Word lleva un índice de hipervínculos, escrito por `Planificación/docx_format.lua` al ejecutar `Planificación/build_docx.sh`. Esta lista sirve para leer el archivo Markdown y no se copia al Word.

1. Introducción  
2. Aportaciones del módulo al desarrollo de competencias  
3. Objetivos  
4. Contenidos y organización en unidades de programación  
5. Metodología  
6. Fomento a la lectura  
7. Uso didáctico y profesional de las tecnologías  
8. Evaluación  
9. Desarrollo de las unidades de programación  
10. Medidas de atención a la diversidad  
11. Actividades complementarias y extraescolares  
12. Formación en la empresa  
13. Evaluación de la programación y de la práctica docente (remisión al apartado 8.15)  
- Referencias  
- Anexo A. Verificación de la cobertura y ponderación de los criterios de evaluación  
- Anexo B. Programación de aula  
- Anexo C. Sitio web de apuntes

:::

# 1. Introducción

Esta programación didáctica (PD) concreta la planificación del módulo optativo **Introducción a la Nube Pública** (INP) del ciclo formativo de grado superior **Desarrollo de Aplicaciones Web** (DAW), impartido en el **IES Macià Abela** (Crevillent) durante el curso **2026/2027** al grupo de **segundo curso en régimen semipresencial**.

El módulo dura **100 h**. De ellas, **72 h (72 %)** se trabajan en el centro antes de la formación en empresa (FE), que empieza el **1 de marzo de 2027**, y **28 h (28 %)** quedan vinculadas a la FE sin asignarle resultados de aprendizaje concretos (apartado 12). Las horas de centro combinan las tutorías y el trabajo autónomo guiado del alumnado; no son clases presenciales semanales. El periodo de centro va del 22 de septiembre de 2026 al 26 de febrero de 2027 y se organiza en dos evaluaciones: la primera abarca los Temas 1 a 4 y la segunda, los Temas 5 a 8. El detalle está en el apartado 4.4 y en el anexo B.

La evaluación es competencial y toma como referentes los **resultados de aprendizaje (RA)**. Los **criterios de evaluación (CE)** se vinculan a los **instrumentos de evaluación (IE)** con los que se trabajan en el aula, y cada uno recibe una ponderación según su importancia. Una vez verificado que todos se trabajan y se evalúan, esa ponderación se expresa en porcentaje en el anexo A.3, calculada a partir de las rúbricas de las actividades que se califican, y el peso de cada RA es la suma de las ponderaciones de sus CE: 20 % el RA1, 25 % el RA2, 30 % el RA3 y 25 % el RA4. La nota de cada RA es la media ponderada de los IE que lo evalúan y la nota final del módulo es la media ponderada de los RA. Los RA no son compensables entre sí. Así, la calificación del boletín refleja lo que se imparte y se evalúa en el aula.

El itinerario formativo es el curso **AWS Academy Cloud Foundations** de Amazon Web Services (AWS), con una ampliación hacia la certificación **AWS Certified Cloud Practitioner (CLF-C02)**. El módulo aporta al perfil de DAW el contexto de despliegue y operación de aplicaciones web en una nube pública: identidad y seguridad, redes virtuales, cómputo, almacenamiento, bases de datos, arquitectura, escalado y observación.

## 1.1. Características del módulo y concepto de programación didáctica

Introducción a la Nube Pública es un módulo optativo del currículo valenciano. No sustituye a los módulos de desarrollo del ciclo: los completa con el entorno en el que esas aplicaciones se publican y se mantienen. Su enfoque es práctico y se apoya en los laboratorios de AWS Academy, en la consola de AWS y en la calculadora de precios pública.

La PD es el nivel de concreción curricular del departamento: establece qué RA se deben alcanzar, cómo se organiza el aprendizaje, con qué recursos, cómo se atiende a la diversidad y cómo se evalúa. Estos son sus datos identificativos:

| Campo | Valor |
| --- | --- |
| Denominación | Introducción a la Nube Pública |
| Código | El anexo del módulo no le asigna código numérico. |
| Carácter | Módulo optativo (Decreto 114/2025, anexo X-XVII) |
| Familia profesional | Informática y Comunicaciones |
| Ciclo formativo | Desarrollo de Aplicaciones Web |
| Nivel | Ciclo formativo de grado superior |
| Curso | Segundo (2.º DAW), régimen semipresencial |
| Duración | **100 h**: 72 h en el centro y 28 h vinculadas a la FE |
| Ritmo de tutorías | Tutoría colectiva e individual en semanas alternas, cada una con sesión de mañana y de tarde y el mismo contenido. El resto es trabajo autónomo guiado. |
| Curso académico | 2026/2027 |
| Profesor | Javier Hernández Illán |

La PD es un documento abierto. Podrá ajustarse a partir de la evaluación inicial, de la evolución del grupo, de la FE o de cambios organizativos, respetando el currículo y la transparencia de la calificación, y los ajustes se registrarán en el departamento.

## 1.2. Entorno

Conforme al Real Decreto 659/2023, el currículo debe atender al entorno socioproductivo. El IES Macià Abela está en Crevillent (Baix Vinalopó), cerca de Elche y de Alicante, en un tejido de pequeñas y medianas empresas industriales y de servicios que se está digitalizando. Muchas de ellas publican sus aplicaciones y sus tiendas en línea en servicios de nube pública, o están valorando hacerlo.

Ese entorno justifica que el módulo trabaje casos de aplicación web reconocibles: una API (interfaz de programación de aplicaciones) de un proyecto de DAW, un front estático, una base de datos gestionada, una cuenta con usuarios y permisos, y la factura que todo ello genera. El objetivo es que el alumnado llegue a la FE sabiendo leer y explicar la parte de nube del proyecto en el que participe.

## 1.3. Características del alumnado

El alumnado de 2.º DAW semipresencial es heterogéneo en edad, vía de acceso y experiencia previa con la nube. Una parte compagina los estudios con el trabajo, y por eso el régimen semipresencial descansa en el trabajo autónomo y en tutorías de semanas alternas. La carga autónoma es alta y exige organización: los apuntes, los vídeos y los laboratorios están disponibles desde el inicio, pero los plazos los marcan Aules y el calendario de evaluaciones.

Las decisiones didácticas se toman a partir de la evaluación inicial (el cuestionario inicial de cada tema), de la observación en las tutorías y, cuando procede, de la información del departamento de orientación. La respuesta combina actividades graduadas, práctica guiada y autónoma, refuerzo o ampliación y adaptaciones de acceso, **sin modificar los RA**.

## 1.4. Marco legal

La programación se ajusta a la normativa estatal y autonómica aplicable al módulo.

En el ámbito estatal se tienen en cuenta la Ley Orgánica 2/2006, de Educación, en la redacción dada por la Ley Orgánica 3/2020, y la Ley Orgánica 3/2022, de ordenación e integración de la Formación Profesional (FP). El título de Técnico Superior en Desarrollo de Aplicaciones Web se cita por el Real Decreto 686/2010, de 20 de mayo, actualizado por el Real Decreto 405/2023, de 29 de mayo, y por el Real Decreto 500/2024, de 21 de mayo. La ordenación de la FP se toma del Real Decreto 659/2023, de 18 de julio.

En el ámbito autonómico se tienen en cuenta el Decreto 114/2025, de 29 de julio, de currículos de FP, cuyo anexo X-XVII establece este módulo optativo, modificado por el Decreto 95/2026, de 19 de junio, que fija su duración en 100 h; la Orden 8/2025, de evaluación en FP; la Orden 30/2022, de 12 de mayo, que regula el régimen semipresencial (artículos 3 y 28.2, este último modificado por la Orden 9/2025, de 5 de junio); la Resolución de 16 de julio de 2026, de la Secretaría Autonómica de Educación, con las instrucciones para los grados D y E en el curso 2026-2027; la Resolución de 15 de junio de 2026, de la Dirección General de Centros Docentes, que fija el calendario escolar 2026-2027; el Decreto 104/2018 y la Orden 20/2019, de inclusión educativa; y el Decreto 252/2019, de organización de los centros.

La relación completa de normas y de fuentes está en el apartado de referencias, al final del documento. La temporalización se alinea con el calendario del centro y con la programación de aula del anexo B.

## 1.5. Mejoras y decisiones de arranque del curso 2026-2027

El módulo se reorganiza este curso alrededor de los apuntes publicados y del itinerario de AWS Academy. Las decisiones principales son estas:

| Mejora | Aplicación en 2026-2027 | Seguimiento |
| --- | --- | --- |
| Mapa de ocho temas | El Tema 1 reúne los módulos 0 a 3 de Cloud Foundations y los Temas 2 a 8 siguen los módulos 4 a 10, uno por tema. | Apartado 4 y anexo C |
| Evaluación competencial | Los referentes son los RA. Cada CE se vincula a los IE del aula y se pondera según su importancia; el peso de cada RA es la suma de sus CE. | Apartado 8 y anexo A.3 |
| Ponderación de los CE | Los porcentajes salen de las rúbricas de las prácticas y de la actividad de clase que se califican. | Anexo A.3 |
| Certificación CLF-C02 | La certificación suma 1 punto a la nota final, hasta 11, sin recuperar ni sustituir ningún RA. | Apartado 8.7.3 |
| Entregas | Las prácticas se entregan en Markdown (`.md`) por Aules, con capturas propias y sin datos de la cuenta. | Apartados 6, 7 y 8.5 |
| Calendario semipresencial | Veintiuna tutorías en semanas alternas y cierre del periodo de centro el 26 de febrero de 2027, antes de la FE. | Anexo B |

---

# 2. Aportaciones del módulo al desarrollo de competencias

## 2.1. Relación con el desarrollo de la competencia general

Según el artículo 4 del Real Decreto 686/2010, la **competencia general** del título consiste en:

> Desarrollar, implantar, y mantener aplicaciones web, con independencia del modelo empleado y utilizando tecnologías específicas, garantizando el acceso a los datos de forma segura y cumpliendo los criterios de accesibilidad, usabilidad y calidad exigidas en los estándares establecidos.

El módulo contribuye a la parte de **implantar y mantener** de esa competencia. Enseña a elegir dónde y cómo se ejecuta una aplicación web en una nube pública, a protegerla con identidades y permisos, a conectar sus datos de forma segura y a mantenerla con escalado, monitorización y control de costes. No sustituye a los módulos de desarrollo: aporta el contexto de despliegue y operación al nivel de Cloud Foundations y Cloud Practitioner.

## 2.2. Relación con las competencias profesionales, personales y sociales

El anexo del módulo optativo solo fija la duración, los RA, los CE y los contenidos orientativos; no lo relaciona con competencias concretas del título. La relación siguiente es, por tanto, una propuesta del departamento a partir de los contenidos y de los RA. El módulo contribuye sobre todo a estas competencias profesionales, personales y sociales (CP) del artículo 5 del Real Decreto 686/2010:

| Código | Competencia |
| --- | --- |
| **a** | Configurar y explotar sistemas informáticos, adaptando la configuración lógica del sistema según las necesidades de uso y los criterios establecidos. |
| **b** | Aplicar técnicas y procedimientos relacionados con la seguridad en sistemas, servicios y aplicaciones, cumpliendo el plan de seguridad. |
| **c** | Gestionar servidores de aplicaciones adaptando su configuración en cada caso para permitir el despliegue de aplicaciones web. |
| **d** | Gestionar bases de datos, interpretando su diseño lógico y verificando integridad, consistencia, seguridad y accesibilidad de los datos. |
| **ñ** | Desplegar y distribuir aplicaciones web en distintos ámbitos de implantación, verificando su comportamiento y realizando modificaciones. |
| **o** | Gestionar y/o realizar el mantenimiento de los recursos de su área en función de las cargas de trabajo y el plan de mantenimiento. |
| **p** | Adaptarse a las nuevas situaciones laborales, manteniendo actualizados los conocimientos científicos, técnicos y tecnológicos relativos a su entorno profesional, gestionando su formación y los recursos existentes en el aprendizaje a lo largo de la vida y utilizando las tecnologías de la información y la comunicación. |

Además, el módulo refuerza la documentación técnica, el uso responsable de cuentas y recursos de pago y la autonomía en el aprendizaje, que en el régimen semipresencial son condiciones del propio trabajo.

## 2.3. Contribución a las competencias para la empleabilidad

### Unidad de competencia asociada

El módulo es optativo y el Real Decreto 686/2010 no lo asocia a ninguna unidad de competencia (UC) del Catálogo Nacional de Cualificaciones Profesionales. Sus contenidos se relacionan con las UC del título que tratan la implantación y la explotación de sistemas, como la UC0223_3 («Configurar y explotar sistemas informáticos»), pero esa relación es orientativa y no supone una acreditación.

### Empleabilidad

Las competencias para la empleabilidad tienen carácter transversal. Se integran en las actividades y en los IE vinculados a los RA y no reciben una calificación separada. En este módulo se trabajan, sobre todo, la comunicación técnica escrita (entregas en Markdown con supuestos y capturas comentadas), la lectura de documentación técnica en inglés, la resolución de problemas a partir de un caso y el uso ético y seguro de la tecnología (mínimo privilegio, secretos fuera de las entregas y control del gasto).

Las fuentes consultadas no recogen qué competencias para la empleabilidad, con su referencia, asigna el Proyecto Curricular del ciclo de DAW a este módulo. Cuando el departamento las concrete, se añadirán aquí con su referencia, sin cambiar la calificación.

Los casos del módulo acercan al alumnado a ocupaciones de desarrollo y despliegue web, de soporte de plataformas en la nube y de operación de aplicaciones en pequeñas y medianas empresas.

## 2.4. Contribución de los resultados de aprendizaje a las competencias

| RA | Contribución principal a CP | Observación breve |
| :---: | --- | --- |
| RA1 | a, p | Conceptos, modelos de servicio y de despliegue, adopción, migración y facturación |
| RA2 | a, b | Infraestructura global, categorías de servicios, responsabilidad compartida y gestión de identidades y accesos |
| RA3 | a, b, c, ñ, o | Redes virtuales, seguridad de red, cómputo, balanceo de carga y escalado automático |
| RA4 | d, ñ, o | Almacenamiento, bases de datos gestionadas, arquitectura resiliente y monitorización |

El peso de cada RA es el del apartado 8.4. Las horas de referencia reparten las 72 h de centro en la misma proporción que el peso del RA. Son una distribución de referencia, no una temporalización nueva: el reparto real por temas y tutorías está en el apartado 4.4 y en el anexo B. Las 28 h vinculadas a la FE no se asignan a ningún RA (apartado 12). El apartado 8.7.4 considera necesarios todos los RA, con umbral de 5 y sin compensación entre ellos; por eso todos figuran como esenciales.

| RA | Peso en el módulo | Horas de referencia (72 h × peso) | Carácter |
| :---: | ---: | ---: | --- |
| RA1 | 20 % | 14,40 h | Esencial |
| RA2 | 25 % | 18,00 h | Esencial |
| RA3 | 30 % | 21,60 h | Esencial |
| RA4 | 25 % | 18,00 h | Esencial |
| **Total** | **100 %** | **72,00 h** | — |

---

# 3. Objetivos

## 3.1. Objetivos generales del ciclo vinculados al módulo

Como en el apartado 2.2, el anexo del módulo no fija su relación con los objetivos generales (OG) del ciclo. El departamento propone que la formación del módulo contribuya a alcanzar, entre otros, estos objetivos generales del artículo 9 del Real Decreto 686/2010:

| Código | Objetivo general |
| --- | --- |
| **a** | Ajustar la configuración lógica analizando las necesidades y criterios establecidos para configurar y explotar sistemas informáticos. |
| **b** | Identificar las necesidades de seguridad verificando el plan preestablecido para aplicar técnicas y procedimientos relacionados. |
| **d** | Ajustar parámetros analizando la configuración para gestionar servidores de aplicaciones. |
| **e** | Interpretar el diseño lógico, verificando los parámetros establecidos para gestionar bases de datos. |
| **p** | Establecer procedimientos, verificando su funcionalidad, para desplegar y distribuir aplicaciones. |
| **q** | Programar y realizar actividades para gestionar el mantenimiento de los recursos informáticos. |
| **r** | Analizar y utilizar los recursos y oportunidades de aprendizaje relacionadas con la evolución científica, tecnológica y organizativa del sector y las tecnologías de la información y la comunicación, para mantener el espíritu de actualización y adaptarse a nuevas situaciones laborales y personales. |

## 3.2. Relación entre objetivos, competencias y resultados de aprendizaje

| OG | CP | RA principales |
| :---: | :---: | :---: |
| a | a | RA1, RA2, RA3 |
| b | b | RA2, RA3 |
| d | c | RA3 |
| e | d | RA4 |
| p | ñ | RA3, RA4 |
| q | o | RA3, RA4 |
| r | p | RA1 |

## 3.3. Resultados de aprendizaje

Los RA del módulo son los del anexo X-XVII del Decreto 114/2025, modificado por el Decreto 95/2026, y se reproducen de forma literal. Sus pesos en la calificación del curso 2026-2027 son estos:

| Código | Descripción (literal) | Peso |
| --- | --- | ---: |
| **RA1** | Comprende los fundamentos de la computación en la nube, sus ventajas frente a sistemas tradicionales, el marco de adopción, los principios de migración y los aspectos clave de facturación, como estimación y optimización de costos. | **20 %** |
| **RA2** | Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos. | **25 %** |
| **RA3** | Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos. | **30 %** |
| **RA4** | Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. | **25 %** |
| | **Total** | **100 %** |

Los pesos son una propuesta del departamento. Reflejan la carga práctica de cada bloque de Cloud Foundations: el RA3 reúne redes, cómputo y escalado, y es el de mayor peso; el RA1 es el más conceptual. Cada peso coincide con la suma de las ponderaciones de los CE de su RA, calculadas en el anexo A.3.

Los CE de cada RA, también literales, son los siguientes. Su código une el número del RA y la letra del criterio: CE1a es el criterio a) del RA1.

### Criterios de evaluación del RA1

- **a)** Se ha comprendido los conceptos fundamentales de la computación en la nube.
- **b)** Se ha demostrado la capacidad para explicar las ventajas de la nube frente a sistemas tradicionales.
- **c)** Se ha participado en actividades relacionadas con el ecosistema de servicios en la nube.
- **d)** Se han identificado los principios básicos de la facturación y costos en la nube.
- **e)** Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos.
- **f)** Se ha participado en actividades prácticas sobre gestión de costos.

### Criterios de evaluación del RA2

- **a)** Se ha adquirido conocimiento de los componentes de una infraestructura global en la nube.
- **b)** Se ha demostrado la capacidad para explorar y describir las principales categorías de servicios disponibles.
- **c)** Se ha realizado una evaluación del uso adecuado de servicios básicos en ejercicios prácticos.
- **d)** Se ha comprendido el modelo de responsabilidad compartida en la nube.
- **e)** Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso.
- **f)** Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad.

### Criterios de evaluación del RA3

- **a)** Se ha realizado el diseño y configuración de redes virtuales privadas.
- **b)** Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas.
- **c)** Se ha participado activamente en la creación y configuración de una red funcional.
- **d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.
- **e)** Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático.
- **f)** Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales.

### Criterios de evaluación del RA4

- **a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.
- **b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.
- **c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.
- **d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.
- **e)** Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización.
- **f)** Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes.

### Nota metodológica de evaluación

Los referentes de la calificación son los RA, no los instrumentos aislados ni las evaluaciones parciales. La nota de cada RA es la media ponderada de los IE que lo evalúan: actividad de clase (AC), práctica (PR), proyecto (PY) y prueba objetiva (PO). La nota final del módulo es la media ponderada de los cuatro RA, con pesos **20 / 25 / 30 / 25**. Los CE permiten verificar que el alumnado ha alcanzado el RA: se trabajan y se comprueban todos (anexo A) y cada uno se pondera según su importancia, a través de los IE con los que se trabaja en el aula. Esa ponderación se expresa en porcentaje en el anexo A.3 y la suma de los CE de cada RA da su peso. El peso de cada IE dentro del RA depende de los CE que evidencia y de los puntos que su rúbrica les dedica. Este diseño procedimental de los instrumentos no reparte la nota en una parte conceptual, otra procedimental y otra actitudinal. Las referencias que sustentan este criterio están en el apartado 8.1.

### Cómo se calcula la nota

| Paso | Contenido |
| --- | --- |
| **1** | Se califican los instrumentos AC, PR, PY y PO, cada uno en su escala (apartado 8.3.1). |
| **2** | La nota de cada RA es la media ponderada de los IE de ese RA (apartado 8.7.2). |
| **3** | La nota final es RA1 × 20 % + RA2 × 25 % + RA3 × 30 % + RA4 × 25 % (apartado 8.7.3). |
| Extra | La certificación CLF-C02 suma 1 punto a la nota final, que puede llegar a 11. Ese punto no recupera ni sustituye ningún RA. |

## 3.4. Objetivos transversales y concreción didáctica

Además de los objetivos del título, el módulo trabaja de forma transversal:

- La comunicación técnica escrita: supuestos, desgloses y justificaciones en las entregas en Markdown.
- El uso ético y seguro de las tecnologías de la información y la comunicación (TIC): mínimo privilegio, protección de credenciales y respeto a los datos personales.
- La responsabilidad económica: apagar y eliminar los recursos de los laboratorios y leer qué dispara una factura.
- La autonomía y la gestión del propio aprendizaje, propias del régimen semipresencial y de la preparación de una certificación.
- La sostenibilidad: dimensionar los recursos según la carga real en lugar de sobredimensionarlos.

---

# 4. Contenidos y organización en unidades de programación

Conforme al Decreto 114/2025, el módulo se organiza en unidades de programación. En esta PD las unidades coinciden con los **ocho temas** de los apuntes (anexo C).

## 4.1. Contenidos curriculares de soporte

El anexo X-XVII del Decreto 114/2025 recoge estos contenidos orientativos, que la programación desarrolla en los ocho temas:

1. **Introducción a la nube:** qué es la computación en la nube, ventajas frente a sistemas tradicionales, ecosistema de la nube y principios de migración.
2. **Facturación y economía de la nube:** aspectos fundamentales de los precios, calculadora de costes, modelos de soporte técnico y herramientas de gestión y cálculo de costes.
3. **Infraestructura global y servicios principales:** infraestructura global, categorías de servicios, consola de administración y navegación por la infraestructura y los servicios.
4. **Seguridad en la nube:** modelo de responsabilidad compartida, identidad y gestión de acceso, protección de cuentas y datos, conformidad y buenas prácticas de seguridad.
5. **Redes y entrega de contenido:** conceptos básicos de redes, red virtual, seguridad en redes y diseño de arquitecturas, enrutamiento y distribución de contenido; creación de una red virtual y lanzamiento de un servidor web.
6. **Informática y escalado automático:** servicios de cómputo, máquinas virtuales y funciones sin servidor, balanceo de carga y escalado automático.
7. **Almacenamiento y bases de datos:** almacenamiento en bloques, de objetos y de ficheros; bases de datos relacionales, no relacionales y otros servicios; creación y gestión de una base de datos; selección de tecnologías.
8. **Arquitectura y monitoreo:** marco Well-Architected, herramientas de monitorización y asistentes de infraestructura, arquitecturas resilientes y escalables, e interpretación de recomendaciones de optimización.

El módulo dura 100 h, según el Decreto 95/2026, que modificó el anexo del Decreto 114/2025. Esa duración es la misma en régimen semipresencial (Orden 30/2022, artículo 3).

## 4.2. Criterios de organización y secuenciación

La secuenciación responde a estos criterios:

1. **Itinerario de AWS Academy.** Los temas siguen los módulos de Cloud Foundations, de modo que los laboratorios de la plataforma encajan con las prácticas evaluables.
2. **De lo conceptual a lo operativo.** Primero se construye el mapa (conceptos, coste e infraestructura global), después se protege la cuenta (identidades y permisos) y a continuación se despliega: red, cómputo, almacenamiento y datos. El curso cierra con la arquitectura, el escalado y la observación.
3. **Integración de teoría y práctica.** Cada tema combina apuntes, vídeo, laboratorio y una práctica con rúbrica; las pruebas objetivas cierran cada evaluación.
4. **Ritmo semipresencial.** La tutoría colectiva presenta el bloque y la individual sigue las prácticas. El trabajo autónomo ocupa la mayor parte de las 72 h.
5. **Cierre antes de la FE.** Los ocho temas, las dos pruebas y el cierre terminan el 26 de febrero de 2027, porque la FE empieza el 1 de marzo de 2027.

## 4.3. Bloques de contenido

| Tema | Título | Academy | RA foco |
| ---: | --- | --- | --- |
| **1** | Fundamentos de la nube AWS | M0–M3 | RA1 y RA2 |
| **2** | Seguridad, IAM y responsabilidad compartida | M4 | RA2 |
| **3** | Redes, VPC y entrega de contenido | M5 | RA3 |
| **4** | Cómputo: EC2, Lambda y contenedores | M6 | RA3 |
| **5** | Almacenamiento | M7 | RA4 |
| **6** | Bases de datos | M8 | RA4 |
| **7** | Arquitectura Well-Architected | M9 | RA4 |
| **8** | Escalado, monitorización y cierre CLF-C02 | M10 | RA3 y RA4 |

La columna «Academy» indica el módulo de Cloud Foundations (M0 a M10) que acompaña a cada tema. Antes del Tema 1, la página de acceso de los apuntes explica cómo entrar en AWS Academy, en el laboratorio de prácticas y en Skill Builder. La preparación del examen CLF-C02 está en la página de certificación.

### Mapa tema × RA

| Tema | RA1 | RA2 | RA3 | RA4 |
| --- | :---: | :---: | :---: | :---: |
| T1 | X | X | | |
| T2 | | X | | |
| T3 | | | X | |
| T4 | | | X | |
| T5 | | | | X |
| T6 | | | | X |
| T7 | | | | X |
| T8 | | | X | X |
| **Peso** | 20 % | 25 % | 30 % | 25 % |

## 4.4. Distribución temporal y unidades de programación

Fuente: programación de aula (anexo B). Las siglas de los instrumentos se explican en el apartado 8.3.1.

| Concepto | Valor |
| --- | --- |
| Duración del módulo | 100 h: 72 h de centro y 28 h vinculadas a la FE. |
| Naturaleza de las 72 h | Son horas de trabajo del alumnado: tutorías y trabajo autónomo guiado con apuntes, vídeos, laboratorios y entregas. No equivalen a tres horas presenciales cada semana. |
| Tutorías | Semanas alternas: tutoría colectiva y, la semana siguiente, tutoría individual. Cada una tiene sesión de mañana y sesión de tarde con el mismo contenido. |
| Primera tutoría colectiva | 22 de septiembre de 2026. |
| Número de tutorías | 11 colectivas y 10 individuales hasta el 26 de febrero de 2027. |
| Fin del periodo de centro | 26 de febrero de 2027. |
| Inicio de la FE | 1 de marzo de 2027. |
| Evaluaciones | Primera: Temas 1 a 4 y PO1. Segunda: Temas 5 a 8, PO2 y cierre. No hay tercera evaluación. |

El calendario se organiza en once tramos de dos semanas, salvo los tramos 7 y 11, que duran una. La fecha de cada tutoría es el martes de esa semana, el mismo día que la primera tutoría colectiva.

| Tramo | Fechas | Contenido | Instrumentos | Horas |
| ---: | --- | --- | --- | ---: |
| 1 | 22-sep – 02-oct-2026 | Tema 1, parte 1: acceso, conceptos y modelos | PR101, PR102 | 7 |
| 2 | 05-oct – 16-oct-2026 | Tema 1, parte 2: facturación e infraestructura global | PR103, PR104 | 7 |
| 3 | 19-oct – 30-oct-2026 | Tema 2. Seguridad e IAM | PR201 | 6 |
| 4 | 02-nov – 13-nov-2026 | Tema 3. Redes y VPC | PR301 | 7 |
| 5 | 16-nov – 27-nov-2026 | Tema 4. Cómputo | PR401 | 7 |
| 6 | 30-nov – 11-dic-2026 | PO1 y arranque del Tema 5 | PO1 (3 h), inicio de PR501 (3 h) | 6 |
| 7 | 14-dic – 18-dic-2026 | Tema 5. Almacenamiento | PR501 | 3 |
| 8 | 11-ene – 22-ene-2027 | Tema 6. Bases de datos | PR601 | 6 |
| 9 | 25-ene – 05-feb-2027 | Tema 7. Well-Architected | PR701 | 6 |
| 10 | 08-feb – 19-feb-2027 | Tema 8. Escalado y monitorización | PR801, AC802 | 9 |
| 11 | 22-feb – 26-feb-2027 | PO2 y cierre del módulo | PO2 (4 h), cierre (4 h) | 8 |
| | | | **Total** | **72** |

Cada tramo incluye además el autocheck del tema, que es autoevaluación y no se califica (apartado 8.3.2). La PO1 está propuesta para el jueves 3 de diciembre de 2026 a las 10:00, pendiente de publicarse en la web del centro, y la PO2 se celebra en la semana del 22 al 26 de febrero de 2027. Las vacaciones de Navidad van del 22 de diciembre de 2026 al 6 de enero de 2027, y las semanas del 21 de diciembre y del 4 de enero no tienen tutoría. Los festivos locales de Crevillent están pendientes de confirmar; si coinciden con una tutoría, esta se traslada al día lectivo más cercano de la misma semana sin cambiar las horas del tramo.

La tabla siguiente recoge los CE que se trabajan en cada tema, tomados del anexo A. Si un CE se trabaja en dos temas, figura en ambos, pero su ponderación es única (anexo A.3).

| Tema | CE que se trabajan (anexo A) | Evaluación parcial |
| --- | --- | --- |
| T1 | CE1a, CE1b, CE1c, CE1d, CE1e, CE1f, CE2a, CE2b, CE2c | 1.ª |
| T2 | CE2d, CE2e, CE2f | 1.ª |
| T3 | CE3a, CE3b, CE3c | 1.ª |
| T4 | CE3d, CE3f | 1.ª (hasta la PO1) |
| T5 | CE4a, CE4c | 2.ª |
| T6 | CE4b, CE4c | 2.ª |
| T7 | CE4d, CE4f | 2.ª |
| T8 | CE3e, CE3f, CE4e, CE4f | 2.ª (hasta la PO2) |

## 4.5. Evaluaciones

| Evaluación | Periodo | Temas |
| --- | --- | --- |
| **1.ª** | Del 22 de septiembre a la semana del 1 de diciembre de 2026 | Temas 1 a 4 y PO1, propuesta para el jueves 3 de diciembre de 2026 a las 10:00 |
| **2.ª** | De la semana del 1 de diciembre de 2026 al 26 de febrero de 2027 | Temas 5 a 8, PO2 y cierre |

La fecha de la PO1 la ha propuesto la coordinación del ciclo y está pendiente de publicarse en la web del centro. El Tema 5 empieza en la misma semana de la PO1, de modo que las dos evaluaciones comparten ese tramo.

---

# 5. Metodología

## 5.1. Principios metodológicos aplicables a la enseñanza en la formación profesional

La metodología busca un aprendizaje significativo y aplicado: el alumnado trabaja con servicios reales de la nube, en un entorno de laboratorio, sobre casos de aplicación web. Las prioridades son aprender haciendo, avanzar de la práctica guiada a la autónoma, documentar lo que se hace y trabajar con seguridad y control de costes. En régimen semipresencial, el material está pensado para estudiarse sin el profesor delante, y la tutoría se reserva para orientar, resolver dudas y revisar el trabajo.

## 5.2. Metodologías activas

Se combinan los laboratorios guiados de AWS Academy, el aprendizaje basado en casos (una API, un front estático, una agenda con base de datos o un diseño frágil que hay que mejorar), la clase invertida que permite el sitio de apuntes, con vídeo y glosario en cada tema, y la autoevaluación con el autocheck. La preparación de la certificación CLF-C02 es una ampliación voluntaria que refuerza lo trabajado.

## 5.3. Estrategias de enseñanza-aprendizaje y secuencia didáctica

Cada tema sigue una secuencia estable:

1. **Activación:** cuestionario inicial del tema, con finalidad diagnóstica.
2. **Presentación:** tutoría colectiva con el mapa del tema, los recursos y una demostración breve.
3. **Estudio autónomo:** apuntes del bloque de Cloud Foundations y videotutorial.
4. **Práctica:** laboratorio de AWS Academy o de la consola y entrega de la práctica en Aules.
5. **Seguimiento:** tutoría individual sobre las prácticas y los laboratorios.
6. **Síntesis:** autocheck del tema, retroalimentación en Aules y enlace con la prueba objetiva de la evaluación.

## 5.4. Tipo de actividades

| Tipo | Código | Descripción | Escala habitual |
| --- | :---: | --- | --- |
| Actividad de clase | **AC** | Microevidencia de aula o de AWS Academy | 0–1 |
| Práctica | **PR** | Laboratorio de AWS Academy o de la consola, con rúbrica | 0–10 |
| Proyecto | **PY** | Entregable mayor con rúbrica, solo si llega a ser necesario | 0–30 |
| Prueba objetiva | **PO** | Examen escrito o en el ordenador | 0–100 |

El cuestionario inicial y el autocheck de cada tema son actividades de diagnóstico y de autoevaluación y no se califican. La codificación de los IE sigue el patrón tipo, tema y orden: PR301 es la práctica 01 del Tema 3.

## 5.5. Organización del aula, agrupamientos y roles

- **Tutoría colectiva:** presenta el bloque, indica los recursos y resuelve las dudas del tramo anterior. No explica el tema entero.
- **Tutoría individual:** seguimiento de las prácticas y de los laboratorios de cada alumno o alumna.
- **Trabajo autónomo:** individual, con los apuntes, los vídeos y el laboratorio. Las prácticas se entregan de forma individual.
- **Comunicación:** los avisos, las entregas y la retroalimentación pasan por Aules.

## 5.6. Coordinación intermodular, Proyecto Intermodular y formación en empresa

Se coordina con el equipo docente de 2.º DAW, en especial con los módulos de despliegue y de desarrollo en entorno servidor, para que los casos de la nube encajen con las aplicaciones que el alumnado construye. Si el Proyecto Intermodular incluye un despliegue en la nube, el módulo puede servir de apoyo, sin duplicar entregas ni calificaciones. El Proyecto Intermodular no se dualiza (artículo 5.6 del Decreto 114/2025). La FE se desarrolla en el apartado 12 y empieza el 1 de marzo de 2027.

## 5.7. Materiales y recursos didácticos

- Sitio web de apuntes: <https://fjavier-hernandez.github.io/cloud/> (anexo C), con un videotutorial, un cuestionario inicial, un autocheck y un glosario por tema.
- AWS Academy Cloud Foundations, con sus laboratorios y el laboratorio de prácticas (Learner Lab).
- AWS Skill Builder y la guía oficial del examen CLF-C02.
- La consola de AWS y la calculadora de precios pública (AWS Pricing Calculator).
- Aules, para las entregas, las calificaciones y los avisos.
- Visual Studio Code con Markdown y la plantilla de entrega de prácticas.

## 5.8. Planificación del uso de espacios y equipamientos

| Espacio / recurso | Uso principal |
| --- | --- |
| Aula del ciclo | Tutorías colectivas e individuales y, cuando proceda, las pruebas objetivas |
| Equipo del alumnado | Estudio, laboratorios y redacción de entregas `.md` |
| AWS Academy y Learner Lab | Laboratorios de cada tema y práctica en la consola con créditos de laboratorio |
| Skill Builder | Preparación voluntaria de la certificación CLF-C02 |
| Aules | Entregas, calificaciones y avisos |

---

# 6. Fomento a la lectura

## 6.1. Actividades de lectura y comunicación técnica

Se fomenta la lectura comprensiva de:

- Los apuntes de cada tema y los enunciados de los laboratorios.
- La documentación oficial de AWS, en su mayor parte en inglés, que los apuntes enlazan en cada práctica.
- La guía del examen CLF-C02 y las páginas de preparación.

La producción escrita se canaliza con las entregas en Markdown en Aules: supuestos de un presupuesto, explicación de una política de permisos o propuesta razonada de mejoras de una arquitectura. Las rúbricas valoran la claridad del texto, y PR701 exige expresamente prosa en párrafos y no una fórmula fija.

## 6.2. Seguimiento, evaluación e inclusión

El seguimiento se hace a través de las prácticas que exigen leer documentación y redactar. Se ofrecen la plantilla de entrega, ejemplos y rúbricas visibles. Cuando sea necesario se adapta el formato de acceso, por ejemplo con más tiempo o con apoyos de lectura, sin reducir la exigencia del RA evaluado.

---

# 7. Uso didáctico y profesional de las tecnologías

## 7.1. Finalidad y criterios generales de utilización

En este módulo las tecnologías son el propio objeto de trabajo. Se usan como en un entorno profesional: una cuenta de laboratorio con límites, servicios reales y documentación técnica. Se priorizan las herramientas que el alumnado encontrará en un despliegue web real.

## 7.2. Búsqueda, selección y gestión de información técnica

El alumnado busca y contrasta información en la documentación oficial, en los apuntes y en las guías de laboratorio, y aprende a distinguir una fuente fiable de un contenido no verificado. En la preparación de la certificación se evitan los bancos de preguntas filtradas.

## 7.3. Comunicación, entrega y colaboración mediante canales digitales

- **Aules** es el canal oficial de entregas, calificaciones y avisos.
- La comunicación es respetuosa y queda registrada.
- Las tutorías individuales permiten revisar el trabajo de cada alumno o alumna.

## 7.4. Software y entornos digitales del módulo

| Recurso | Uso |
| --- | --- |
| Aules | Entorno virtual de aprendizaje del centro |
| AWS Academy y Learner Lab | Laboratorios y práctica en la consola |
| AWS Pricing Calculator | Estimación de costes (PR103) |
| Skill Builder | Preparación de la certificación |
| Visual Studio Code y Markdown | Redacción de entregas |
| Sitio de apuntes (MkDocs) | Apuntes, calendario y planificación visible |

## 7.5. Uso responsable, seguro, ético y accesible

Se exige:

- No usar el usuario raíz para el trabajo diario y aplicar el mínimo privilegio.
- No mostrar en las capturas el identificador de la cuenta de AWS (Account ID), claves de acceso ni contraseñas, y dejar los secretos fuera de las entregas.
- Detener y eliminar los recursos de laboratorio al terminar, para no consumir créditos.
- Respetar la privacidad y los datos personales.
- Mantener la integridad académica (apartado 8.8).
- Preferir formatos accesibles: Markdown, contraste suficiente y estructura clara.

---

# 8. Evaluación

## 8.1. Principios y organización de la evaluación

La evaluación es continua, formativa y sumativa, y comprueba el grado de consecución de los RA. Los referentes de la evaluación son los RA. Los instrumentos —actividad de clase, práctica, proyecto y prueba objetiva— aportan las evidencias con las que se califica cada RA. No se califica la evaluación parcial ni el instrumento suelto como referente del módulo.

Se sigue el criterio de la referencia de Solbes citada debajo. Cada CE se vincula a los IE con los que se trabaja en el aula y recibe una ponderación según su importancia. Verificada la cobertura (anexo A), esa ponderación se expresa en porcentaje en el anexo A.3, calculada a partir de las rúbricas de las actividades que se califican, y la suma de los CE de cada RA da su peso. La nota de cada RA es la media ponderada de los IE que lo evalúan, y la nota final del módulo es la media ponderada de los RA, con pesos del 20, el 25, el 30 y el 25 por ciento. Los RA no son compensables entre sí. La certificación CLF-C02 suma 1 punto sobre la nota final (máximo 11) sin sustituir ningún RA.

El matiz que se recoge es el de Solbes: el RA es el referente y los CE identifican su logro y ponderan dentro de él según su importancia. Diseñar más instrumentos, o darles más peso, sobre los CE más relevantes del perfil profesional no equivale a dividir la nota en una parte conceptual, otra procedimental y otra actitudinal.

Referencias: [Los referentes para evaluar en FP](https://raulsolbes.com/2025/01/22/los-referentes-para-evaluar-en-fp/); [Programaciones didácticas para FP: evaluación](https://raulsolbes.com/2025/04/04/programaciones-didacticas-para-fp-evaluacion/); matiz en [Evaluación por competencias en FP](https://raulsolbes.com/2020/05/27/evaluacion-por-competencias-en-fp/).

## 8.2. Características de la evaluación

La evaluación inicial detecta el punto de partida al comienzo del curso y de cada tema, con el cuestionario inicial. La evaluación procesual da retroalimentación en Aules y en la tutoría individual. La evaluación final consolida cada RA y la calificación del módulo. Los criterios, las rúbricas y los plazos se publican con antelación en los apuntes y en Aules. Cuando hace falta, se aplican las adaptaciones de acceso del apartado 10, sin modificar los RA.

## 8.3. Referentes, ponderación y trazabilidad curricular

Los referentes de calificación son los cuatro RA, con pesos del 20, el 25, el 30 y el 25 por ciento. Esos pesos están en el apartado 8.4 y no se sustituyen por los instrumentos ni por las evaluaciones parciales.

Cada IE declara el RA que evalúa y los CE que permite comprobar. La matriz completa está en el anexo A. La cobertura verificada es de **24 de 24** CE. Esa matriz comprueba la cobertura y es la base del cálculo de la ponderación de cada CE en el anexo A.3.

### 8.3.1. Procedimientos e instrumentos de evaluación

Para que los apartados siguientes se entiendan, conviene distinguir tres conceptos:

- Los **procedimientos de evaluación** son las formas de obtener información sobre el aprendizaje: el análisis de las producciones entregadas en Aules, el seguimiento en las tutorías y las pruebas objetivas.
- Los **instrumentos de evaluación (IE)** son las actividades concretas que generan una evidencia calificable: la actividad de clase, la práctica, el proyecto y la prueba objetiva.
- Los **instrumentos de calificación** son las herramientas con las que el profesorado puntúa cada IE: la escala numérica y la rúbrica (apartado 8.3.2).

Los IE del módulo y sus escalas son los que figuran en la página de inicio de los apuntes (anexo C):

| Instrumento | Sigla | Descripción | Escala |
| --- | --- | --- | --- |
| Actividad de clase | AC | Microevidencia de aula o de AWS Academy. | 0–1 |
| Práctica | PR | Laboratorio de AWS Academy o de la consola. | 0–10 |
| Proyecto | PY | Entregable mayor con rúbrica, solo si llega a ser necesario (apartado 8.5). | 0–30 |
| Prueba objetiva | PO | Examen escrito o en el ordenador. | 0–100 |
| Certificación | +1 | Certificación AWS Certified Cloud Practitioner (CLF-C02). | +1 en la nota final (máximo 11) |

Cada IE se identifica con el prefijo de su tipo, el número del tema y un ordinal de dos cifras: PR201 es la práctica 01 del Tema 2 y AC802 es la actividad de clase 02 del Tema 8. Las pruebas objetivas son dos: PO1 cierra los Temas 1 a 4 y PO2 cierra los Temas 5 a 8. En los apuntes, cada actividad indica el RA y los CE que evalúa y su escala; por ejemplo, PR201 evalúa el RA2 con los CE d, e y f, en la escala de 0 a 10.

### 8.3.2. Instrumentos de calificación

| Instrumento de calificación | Uso en el módulo | Valor |
| --- | --- | --- |
| Escala numérica | Todos los IE se califican en la escala de su tipo. | AC 0–1, PR 0–10, PY 0–30 y PO 0–100 |
| Rúbrica | Cada práctica y la actividad de clase AC802 llevan en su tema una rúbrica con criterios, descripción y puntos parciales; la suma de los criterios da la nota. Sus valores están en la tabla siguiente. | PR sobre 10 y AC sobre 1 |
| Cuestionario inicial | Al empezar cada tema. Tiene finalidad diagnóstica, no se entrega y sus soluciones son visibles en los apuntes. | Sin calificación |
| Autocheck | Al final de cada tema. Sirve de autoevaluación, no se entrega y no se califica. | Sin calificación |
| Certificación | La CLF-C02 suma según las condiciones publicadas en Aules; no recupera un RA ni sustituye prácticas ni pruebas. | +1 (máximo 11) |

Las rúbricas de los instrumentos que se califican, tal como figuran en los apuntes, son estas:

| IE | RA y CE | Criterios de la rúbrica y puntos |
| --- | --- | --- |
| PR101 Consola y ecosistema | RA1 c; RA2 b, c | Acceso e introducción al curso (0–2), consola sin coste (0–2), cinco servicios (0–4) y claridad del `.md` (0–2) |
| PR102 Modelos | RA1 a, b, c | Cuatro situaciones (0–4), modelos coherentes (0–3) y justificación (0–3) |
| PR103 Estimación | RA1 d, e, f | Escenario 24/7 (0–3), escenario de 40 h semanales (0–3), lectura de coste (0–2) y laboratorio M2 o claridad (0–2) |
| PR104 Fábrica global | RA2 a, b, c | Comparación de regiones (0–3), región europea y zonas de disponibilidad (0–3), conceptos (0–2) y knowledge check o claridad (0–2) |
| PR201 Usuarios y políticas | RA2 d, e, f | Laboratorio y usuarios (0–3), mínimo privilegio (0–3), buenas prácticas (0–2) y claridad del `.md` (0–2) |
| PR301 VPC y servidor web | RA3 a, b, c | VPC y subredes (0–3), rutas y puerta de enlace (0–2), grupo de seguridad (0–3) y limpieza (0–2) |
| PR401 Lanzar y comparar cómputo | RA3 d, f | Laboratorio EC2 y AMI (0–3), comparación con Lambda (0–4), limpieza (0–2) y claridad del `.md` (0–1) |
| PR501 Objetos y bloques | RA4 a, c | Laboratorio de EBS (0–4), concepto de objeto y bloque (0–3), limpieza (0–2) y claridad (0–1) |
| PR601 RDS mínimo | RA4 b, c | Laboratorio de RDS (0–3), seguridad de red (0–3), secretos y claridad (0–2) y limpieza (0–2) |
| PR701 Mejorar un diagrama frágil | RA4 d, f | Cinco mejoras (0–4), pilares (0–3), equilibrio (0–2) y claridad (0–1) |
| PR801 Escalar y observar | RA3 e, f; RA4 e | Balanceador ALB (0–3), grupo de autoescalado (0–3), CloudWatch (0–2) y limpieza (0–2) |
| AC802 Mapa de servicios CLF | RA3 f; RA4 f | Ocho tarjetas útiles (0–1) |

La rúbrica del proyecto, si llega a ser necesario, y el desglose interno de las pruebas objetivas se concretarán cuando se cierren esos instrumentos y se publicarán en Aules. Para calcular la nota de un RA, las notas de sus IE se normalizan a la escala de 0 a 10 y se promedian con el peso que les corresponde, según los CE que evidencian (apartado 8.7.2 y anexo A.3).

## 8.4. Ponderación de los RRAA y CCEE

El título del apartado se mantiene porque así figura en la plantilla del departamento; RRAA y CCEE son los plurales abreviados de RA y CE. Primero se explica cómo se verifican y ponderan los CE y después se ponderan los RA.

### Verificación y ponderación de los criterios de evaluación

Los CE del módulo son los del anexo X-XVII del Decreto 114/2025, modificado por el Decreto 95/2026. Sirven para verificar que el RA se ha alcanzado. Se trabajan y se comprueban todos, según el anexo A, y cada uno recibe una ponderación según su importancia a través de los IE con los que se trabaja en el aula. La importancia se mide por los puntos que las rúbricas de las prácticas y de la actividad de clase dedican a cada CE. Un mismo CE puede aparecer en varias actividades: su ponderación reúne lo que aporta en cada una. El anexo A.3 expresa esa ponderación en porcentaje, y el peso de cada RA es la suma de las ponderaciones de sus CE.

El peso de cada instrumento dentro del RA depende de los CE que evidencia y de los puntos que su rúbrica les dedica. El anexo A.3 recoge también ese peso.

### Ponderación de los resultados de aprendizaje

| RA | Peso en el módulo | Suma de sus CE (anexo A.3) |
| :---: | ---: | ---: |
| RA1 | 20 % | 20,00 % |
| RA2 | 25 % | 25,00 % |
| RA3 | 30 % | 30,00 % |
| RA4 | 25 % | 25,00 % |
| **Total** | **100 %** | **100,00 %** |

## 8.5. Banco de instrumentos, guías de estudio y entregas

Las siglas de esta tabla se explican en el apartado 8.3.1.

| Código | Tema | Tipo | RA | Estado |
| --- | :---: | --- | --- | --- |
| PR101–PR104 | 1 | PR | RA1 y RA2 | Publicadas en los apuntes |
| PR201 | 2 | PR | RA2 | Publicada |
| PR301 | 3 | PR | RA3 | Publicada |
| PR401 | 4 | PR | RA3 | Publicada |
| PR501 | 5 | PR | RA4 | Publicada |
| PR601 | 6 | PR | RA4 | Publicada |
| PR701 | 7 | PR | RA4 | Publicada |
| PR801 y AC802 | 8 | PR y AC | RA3 y RA4 | Publicadas |
| PO1 | 1–4 | PO | RA1, RA2 y RA3 | Propuesta para el 3-12-2026, 10:00 |
| PO2 | 5–8 | PO | RA3 y RA4 | Semana del 22 al 26-2-2027 |
| PY | — | PY | — | Solo si hiciera falta un proyecto |

Las PO puntúan en los RA de los temas que cubren. El peso de cada PO dentro de esos RA se publicará en Aules al cerrar su enunciado. Las PO no se asignan a un CE concreto y, por eso, no entran en el reparto de los porcentajes del anexo A.3, que se calcula con las prácticas y la actividad de clase.

Como el módulo es semipresencial, las guías de solución de las prácticas y las soluciones del cuestionario inicial y del autocheck se mantienen visibles en los apuntes como guía de estudio. Las soluciones, los enunciados con respuestas y las claves de las pruebas objetivas nunca se publican ni se suben al repositorio.

Las prácticas se entregan en Aules como fichero Markdown y exigen capturas propias dentro del desarrollo como evidencia del trabajo realizado. En esas capturas no debe verse el identificador de la cuenta de AWS, ni claves de acceso, ni contraseñas. Si hay imágenes, se entregan en un ZIP junto al Markdown.

## 8.6. Plazo de realización de las convocatorias

Las convocatorias se ajustan al calendario oficial del centro y a las instrucciones de inicio del curso 2026-2027. La PO1 está propuesta para el jueves 3 de diciembre de 2026 a las 10:00, pendiente de publicarse en la web del centro, y la PO2 se celebra en la semana del 22 al 26 de febrero de 2027, antes del inicio de la FE. Los plazos de las prácticas los marca Aules: que un tema esté publicado en la web no abre su entrega. Cualquier cambio se comunicará por Aules y se reflejará en el seguimiento del departamento.

## 8.7. Cálculo de las calificaciones y condiciones de superación

### 8.7.1. Calificación de un criterio de evaluación

El apartado conserva el título de la plantilla. El CE no se califica con un instrumento aparte: pondera en la nota a través de los IE con los que se trabaja en el aula. Se comprueba que cada CE tiene al menos una evidencia en el anexo A. Si un CE se trabaja en varias actividades, su ponderación reúne lo que aporta en cada una. El anexo A.3 expresa en porcentaje la ponderación de cada CE, calculada a partir de las rúbricas, y la suma de los CE de cada RA da su peso.

### 8.7.2. Calificación de un resultado de aprendizaje

Para cada RA se hace lo siguiente:

1. Se toman los IE que lo evalúan: AC (escala de 0 a 1), PR (de 0 a 10), PY (de 0 a 30) y PO (de 0 a 100).
2. Las notas se normalizan a una escala común de 0 a 10.
3. Se calcula la media ponderada. El peso de cada práctica y de la actividad de clase es el del anexo A.3, según los CE que evidencia. Cuando un IE evidencia CE de dos RA, como PR101, PR801 y AC802, cada RA recibe la parte de la rúbrica asignada a sus CE. El peso de las PO se publica en Aules al cerrar su enunciado.
4. La nota del RA se expresa de 0 a 10.

Cada RA debe alcanzarse con una nota igual o superior a 5. Los RA no son compensables entre sí.

### 8.7.3. Calificación final del módulo

La nota final es la media ponderada de los cuatro RA:

$$N_{\mathrm{final}} = 0{,}20\,N_{\mathrm{RA1}} + 0{,}25\,N_{\mathrm{RA2}} + 0{,}30\,N_{\mathrm{RA3}} + 0{,}25\,N_{\mathrm{RA4}}$$

Si se acredita la certificación AWS Certified Cloud Practitioner (CLF-C02) en el plazo y en las condiciones publicados en Aules, se suma C = 1; si no, C = 0:

$$N_{\mathrm{módulo}} = \min(11,\ N_{\mathrm{final}} + C)$$

La nota final puede llegar a 11. Ese punto solo suma: no sustituye ningún RA, no recupera un RA inferior a 5 y no sustituye prácticas ni pruebas. Esta programación no incluye la rúbrica de ese punto, que se publica en Aules.

Condición de superación ordinaria: todos los RA con nota igual o superior a 5, y cumplimiento de los requisitos de evaluación continua que establezcan la Orden 8/2025, la Orden 30/2022 y las instrucciones del curso.

### 8.7.4. RRAA esenciales, umbrales y compensación

- Todos los RA del módulo se consideran **necesarios** para superarlo.
- **No hay compensación** entre RA.
- Umbral por RA: **5 o más**.

### 8.7.5. Calificaciones parciales y nota informativa de los temas

Las dos evaluaciones parciales tienen carácter **informativo** del progreso. Se calculan con los IE disponibles hasta la fecha y con los RA trabajados. La calificación final del módulo se determina conforme al apartado 8.7.3 cuando hay evidencias suficientes de todos los RA.

## 8.8. Autoría, integridad académica y uso de inteligencia artificial

El alumnado debe entregar trabajo propio, con capturas propias de su laboratorio. Se permite el uso de la inteligencia artificial (IA) como apoyo a la redacción o a la depuración si se declara, y nunca sustituye la comprensión ni la ejecución práctica exigida. El plagio, la copia en pruebas individuales o la entrega de evidencias no realizadas por quien las entrega podrán conllevar la calificación de insuficiente en el IE afectado y, en su caso, las medidas previstas en las normas del centro.

## 8.9. Refuerzo y recuperación durante el proceso ordinario

Durante el periodo de centro se ofrecen oportunidades de refuerzo y de recuperación de los IE y RA pendientes, con prioridad para la recuperación temprana después de la PO1 y antes del 26 de febrero de 2027, porque la FE empieza el 1 de marzo. La tutoría individual es el momento de acordar la recuperación de una práctica. Las condiciones concretas (plazos e instrumentos alternativos equivalentes) se publican en Aules, de acuerdo con la Orden 8/2025 y las instrucciones del curso 2026-2027, sin fijar porcentajes que la normativa no establece.

## 8.10. Evaluación final ordinaria y plan de recuperación para evaluación extraordinaria

Quien no supere el módulo en la evaluación final ordinaria podrá acogerse al plan de recuperación y a la convocatoria extraordinaria conforme a la normativa autonómica y a los acuerdos del centro. El plan especificará los RA pendientes y los instrumentos equivalentes, y se informará de él con antelación suficiente.

## 8.11. Alumnado con el módulo pendiente de cursos anteriores

El alumnado con el módulo pendiente seguirá el plan que establezca el departamento: calendario de entregas y pruebas, docente responsable y condiciones de superación por RA. Se mantienen como referentes los RA, la ponderación de los CE del anexo A.3 y los pesos de los RA del curso vigente, salvo decisión documentada en contra.

## 8.12. Pérdida del derecho a la evaluación continua

La pérdida del derecho a la evaluación continua se regirá por la Orden 8/2025, la Orden 30/2022 del régimen semipresencial, las instrucciones del curso 2026-2027 y las normas de organización y funcionamiento del centro. En ese caso, el alumnado será evaluado con las pruebas o los instrumentos extraordinarios que se determinen, manteniendo como referentes los RA del módulo. Esta PD no fija porcentajes de inasistencia distintos de los que establezcan la normativa o el centro.

## 8.13. Evaluación de los RRAA y formación en la empresa

En este módulo la FE no tiene RA asignados: los cuatro RA se imparten y se evalúan en el centro, en las 72 h. El profesorado del módulo califica el 100 % de la nota y la empresa emite un informe de apto o no apto. Las 28 h vinculadas a la FE completan la formación en un entorno productivo real, pero no cambian los pesos de los RA ni la ponderación de los CE. Si la empresa no permite trabajar esas horas, la evidencia se completa con el catálogo de refuerzo del apartado 12. Como la FE empieza el 1 de marzo de 2027, toda la evaluación del módulo se cierra antes de esa fecha.

## 8.14. Información, comunicación, revisión y reclamación

Las calificaciones y los criterios se comunican por los canales oficiales: Aules y los procedimientos del centro. El alumnado puede pedir aclaraciones en la tutoría individual o por Aules. Las reclamaciones se tramitan según el procedimiento que establecen la normativa y el IES Macià Abela.

## 8.15. Evaluación de la programación y de la práctica docente

La programación y la práctica docente se revisan durante el curso. Después de cada evaluación se analizan los resultados por RA, el cumplimiento de la temporalización (72 h de centro, PO1 a principios de diciembre, PO2 y cierre antes del 26 de febrero de 2027), la adecuación de los instrumentos y de la carga de trabajo autónomo, el uso de los laboratorios y de los créditos de AWS Academy, y la claridad de la calificación por RA. Después de cada tutoría se anotan en el diario de sesiones la fecha real, lo trabajado y las mejoras. Las propuestas para el curso siguiente se recogen en la memoria del departamento.

Los indicadores orientativos son el porcentaje de alumnado que supera cada RA, el porcentaje de prácticas entregadas en plazo, la cobertura de los 24 de 24 CE, una desviación temporal no mayor de un tramo y las incidencias de laboratorio que se registren, como recursos no eliminados o créditos agotados.

La plantilla del departamento cierra este contenido en el apartado 8.15. El apartado 13 solo remite aquí, para no repetirlo.

---

# 9. Desarrollo de las unidades de programación

Cada tema de los apuntes incluye los RA y CE que trabaja, el bloque de Cloud Foundations, la ampliación Practitioner, un videotutorial, la práctica, el Autocheck y el glosario. La tabla resume el reparto de las 72 h de centro, que son horas de trabajo del alumnado (tutoría y trabajo autónomo guiado); el detalle por tutoría está en el anexo B. Las siglas de la columna de instrumentos se explican en el apartado 8.3.1.

| Bloque | Horas | Resultados de aprendizaje | Periodo | Instrumentos |
| --- | ---: | --- | --- | --- |
| Tema 1 | 14 | RA1 y RA2 | 22 sep – 16 oct 2026 | PR101, PR102, PR103, PR104 |
| Tema 2 | 6 | RA2 | 19 oct – 30 oct 2026 | PR201 |
| Tema 3 | 7 | RA3 | 2 nov – 13 nov 2026 | PR301 |
| Tema 4 | 7 | RA3 | 16 nov – 27 nov 2026 | PR401 |
| Prueba de la 1.ª evaluación | 3 | RA1, RA2 y RA3 | 3 dic 2026, 10:00 (propuesta) | PO1 |
| Tema 5 | 6 | RA4 | 1 dic – 18 dic 2026 | PR501 |
| Tema 6 | 6 | RA4 | 11 ene – 22 ene 2027 | PR601 |
| Tema 7 | 6 | RA4 | 25 ene – 5 feb 2027 | PR701 |
| Tema 8 | 9 | RA3 y RA4 | 8 feb – 19 feb 2027 | PR801, AC802 |
| Prueba de la 2.ª evaluación | 4 | RA3 y RA4 | 22 feb – 26 feb 2027 | PO2 |
| Cierre | 4 | — | 22 feb – 26 feb 2027 | Repaso y cierre del módulo |
| **Total** | **72** | | | |

El Tema 1 recibe más horas porque concentra cuatro prácticas, y el Tema 8 porque reúne PR801 y AC802. Los Temas 3 y 4 sostienen la parte principal del RA3 y llevan una hora más que el Tema 2. El Tema 5 se reparte a ambos lados de las vacaciones de Navidad, y la segunda prueba y el cierre comparten la última semana de centro, antes del inicio de la FE.

### Criterios comunes de las fichas

Cada tema tiene a continuación su ficha, en una página. Los datos salen de los apartados 2, 3, 4, 5, 8, 10 y 12, del anexo B y de los apuntes (anexo C). La nota del boletín no se calcula por temas sino por RA, con los pesos del apartado 8.4; la nota de un tema, si se da, es informativa (apartado 8.7.5).

La fila «Criterios de evaluación y ponderación» indica, junto a cada CE, su ponderación en el módulo, calculada en el anexo A.3 a partir de las rúbricas. Es una ponderación única: si un CE se trabaja en dos temas, como CE3f, CE4c o CE4f, figura en las dos fichas con el mismo porcentaje. El cuestionario inicial y el autocheck de cada tema no se califican. Las pruebas PO1 y PO2 cubren varios temas y su peso dentro de cada RA se publica en Aules al cerrar su enunciado.

## 9.1. Tema 1. Fundamentos de la nube AWS

| Ficha del Tema 1 (1.ª ev.) | Fundamentos de la nube AWS |
| --- | --- |
| **Temporalización** | 14 h en el centro, 22 sep – 16 oct 2026. Tramo 1 (22-sep – 02-oct; tutoría colectiva 22-sep, individual 29-sep): PR101, PR102; 7 h. Tramo 2 (05-oct – 16-oct; tutoría colectiva 06-oct, individual 13-oct): PR103, PR104; Autocheck T1; 7 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M0–M3. RA foco: RA1 (+ arranque RA2). |
| **Resultados de aprendizaje** | RA1 (20 % de la nota): Comprende los fundamentos de la computación en la nube, sus ventajas frente a sistemas tradicionales, el marco de adopción, los principios de migración y los aspectos clave de facturación, como estimación y optimización de costos. RA2 (25 % de la nota): Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos. |
| **Criterios de evaluación y ponderación** | CE1a (2,65 %): Se ha comprendido los conceptos fundamentales de la computación en la nube. CE1b (2,65 %): Se ha demostrado la capacidad para explicar las ventajas de la nube frente a sistemas tradicionales. CE1c (5,87 %): Se ha participado en actividades relacionadas con el ecosistema de servicios en la nube. CE1d (2,35 %): Se han identificado los principios básicos de la facturación y costos en la nube. CE1e (3,24 %): Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos. CE1f (3,24 %): Se ha participado en actividades prácticas sobre gestión de costos. CE2a (5,18 %): Se ha adquirido conocimiento de los componentes de una infraestructura global en la nube. CE2b (4,88 %): Se ha demostrado la capacidad para explorar y describir las principales categorías de servicios disponibles. CE2c (5,80 %): Se ha realizado una evaluación del uso adecuado de servicios básicos en ejercicios prácticos. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | En este tema construimos el mapa que el resto del módulo da por sentado: qué es la nube pública, por qué una aplicación web deja el CPD propio, cómo se paga, y dónde viven realmente los recursos (región, zona de disponibilidad, consola). |
| **Contenidos** | Computación en la nube frente a on-premises; acceso por consola, CLI y API. · Modelos de servicio (IaaS, PaaS, SaaS) y de despliegue (pública, privada, híbrida, multicloud). · Ventajas, límites y trade-offs (agilidad, coste variable, dependencia del proveedor). · Adopción y migración: marco CAF y estrategias (7 R) a nivel de reconocimiento. · Economía: CAPEX / OPEX, TCO, dimensiones de precio, calculadora y presupuestos. · Infraestructura global: regiones, zonas de disponibilidad, edge; navegación por la consola. |
| **Metodología y tutorías** | Tutoría colectiva: Acceso, mapa del tema y cuestionario. Dudas del tramo anterior; facturación e infraestructura global. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR101 — Consola y ecosistema (RA1 c; RA2 b, c; PR 0–10). PR102 — Modelos (RA1 a, b, c; PR 0–10). PR103 — Estimación (RA1 d, e, f; PR 0–10). PR104 — Fábrica global (RA2 a, b, c; PR 0–10). Autocheck T1: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO1 (Temas 1 a 4, 0–100, propuesta para el jueves 3 de diciembre de 2026 a las 10:00). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 1 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | Los dominios Cloud Concepts y Billing, más región, AZ y edge, son el marco del examen en este bloque. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA1: PR102 (Modelos) y PR103 (Estimación). RA2: PR104 (Fábrica global) y PR201 (Usuarios y políticas). |

## 9.2. Tema 2. Seguridad, IAM y responsabilidad compartida

| Ficha del Tema 2 (1.ª ev.) | Seguridad, IAM y responsabilidad compartida |
| --- | --- |
| **Temporalización** | 6 h en el centro, 19 oct – 30 oct 2026. Tramo 3 (19-oct – 30-oct; tutoría colectiva 20-oct, individual 27-oct): PR201; Autocheck T2; 6 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M4. RA foco: RA2. |
| **Resultados de aprendizaje** | RA2 (25 % de la nota): Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos. |
| **Criterios de evaluación y ponderación** | CE2d (2,44 %): Se ha comprendido el modelo de responsabilidad compartida en la nube. CE2e (3,35 %): Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso. CE2f (3,35 %): Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Una API (interfaz de programación de aplicaciones) en la nube no «hereda» la seguridad del proveedor. |
| **Contenidos** | Seguridad de la nube frente a seguridad en la nube; el límite cambia con IaaS, PaaS y SaaS. · IAM: usuario raíz, usuarios, grupos, roles, políticas; mínimo privilegio; MFA. · Cifrado en tránsito y en reposo; AWS Artifact (portal de informes de cumplimiento de AWS) y conformidad (el RGPD —Reglamento General de Protección de Datos— no se cumple solo eligiendo región). · Servicios de detección y auditoría a nivel de reconocimiento (CloudTrail, GuardDuty, WAF…). |
| **Metodología y tutorías** | Tutoría colectiva: Responsabilidad compartida e IAM. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR201 — Usuarios y políticas (RA2 d, e, f; PR 0–10). Autocheck T2: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO1 (Temas 1 a 4, 0–100, propuesta para el jueves 3 de diciembre de 2026 a las 10:00). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 2 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | En Foundations practicas IAM en el lab; el examen te pide reconocer el modelo de responsabilidad compartida, el papel del usuario raíz y qué audita cada servicio. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA2: PR104 (Fábrica global) y PR201 (Usuarios y políticas). |

## 9.3. Tema 3. Redes, VPC y entrega de contenido

| Ficha del Tema 3 (1.ª ev.) | Redes, VPC y entrega de contenido |
| --- | --- |
| **Temporalización** | 7 h en el centro, 2 nov – 13 nov 2026. Tramo 4 (02-nov – 13-nov; tutoría colectiva 03-nov, individual 10-nov): PR301; Autocheck T3; 7 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M5. RA foco: RA3. El lab del Módulo 5: Creación de una VPC y lanzamiento de un servidor web. |
| **Resultados de aprendizaje** | RA3 (30 % de la nota): Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos. |
| **Criterios de evaluación y ponderación** | CE3a (3,86 %): Se ha realizado el diseño y configuración de redes virtuales privadas. CE3b (3,86 %): Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas. CE3c (2,81 %): Se ha participado activamente en la creación y configuración de una red funcional. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Tu front y tu API (interfaz de programación de aplicaciones) no «salen a internet» solos: viven en una VPC (Virtual Private Cloud, nube virtual privada), en subredes ligadas cada una a una zona de disponibilidad (AZ, Availability Zone), con tablas de rutas y cortafuegos. |
| **Contenidos** | VPC, CIDR, subredes (una AZ cada una), tablas de rutas, puerta de enlace a internet y NAT. · Security groups frente a NACL; subred pública frente a privada. · Route 53 y CloudFront: DNS y CDN. · VPN frente a Direct Connect (cuándo merece un enlace dedicado). |
| **Metodología y tutorías** | Tutoría colectiva: VPC pública y privada, y grupos de seguridad. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR301 — VPC y servidor web (RA3 a, b, c; PR 0–10). Autocheck T3: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO1 (Temas 1 a 4, 0–100, propuesta para el jueves 3 de diciembre de 2026 a las 10:00). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 3 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | El examen insiste en dónde publicas (ALB o CloudFront frente a base en privada), qué hace una CDN y la diferencia de estado entre security group y NACL. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA3: PR301 (VPC y servidor web) y PR401 (Lanzar y comparar cómputo). |

## 9.4. Tema 4. Cómputo: EC2, Lambda y contenedores

| Ficha del Tema 4 (1.ª ev.) | Cómputo: EC2, Lambda y contenedores |
| --- | --- |
| **Temporalización** | 7 h en el centro, 16 nov – 27 nov 2026. Tramo 5 (16-nov – 27-nov; tutoría colectiva 17-nov, individual 24-nov): PR401; Autocheck T4; 7 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M6. RA foco: RA3. Lab del Módulo 6. |
| **Resultados de aprendizaje** | RA3 (30 % de la nota): Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos. |
| **Criterios de evaluación y ponderación** | CE3d (4,74 %): Se ha realizado la selección de servicios de computación adecuados según casos de uso. CE3f (8,41 %): Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Tres maneras de «correr código» en AWS: máquina virtual (EC2 —Elastic Compute Cloud, nube elástica de cómputo—), contenedor (ECS / Fargate) y función (Lambda). |
| **Contenidos** | EC2: AMI, familia de instancia, red, compra (On-Demand, Spot, Savings Plans). · Lambda: evento, duración, coste por invocación. · ECS, EKS, Fargate: contenedores con o sin nodos cuyo SO tú parcheas. · Elastic Beanstalk, Lightsail: nombres; cuándo simplifican. |
| **Metodología y tutorías** | Tutoría colectiva: EC2, AMI y elección entre máquina virtual y Lambda. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR401 — Lanzar y comparar cómputo (RA3 d, f; PR 0–10). Autocheck T4: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO1 (Temas 1 a 4, 0–100, propuesta para el jueves 3 de diciembre de 2026 a las 10:00). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 4 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | En el CLF-C02 no basta con nombrar EC2 o Lambda: hay que separar tipo de instancia de modelo de precio y elegir servicio según estado, duración y quién mantiene el entorno (ECS/Fargate, EKS…). El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA3: PR301 (VPC y servidor web) y PR401 (Lanzar y comparar cómputo). |

## 9.5. Tema 5. Almacenamiento

| Ficha del Tema 5 (2.ª ev.) | Almacenamiento |
| --- | --- |
| **Temporalización** | 6 h en el centro, 1 dic – 18 dic 2026. Tramo 6 (30-nov – 11-dic; tutoría colectiva 01-dic, individual semana del 07-dic (el 08-dic es festivo)): inicio de PR501; las otras 3 h del tramo son la PO1; 3 h. Tramo 7 (14-dic – 18-dic; tutoría colectiva 15-dic, individual no hay: la semana del 21-dic solo tiene un día lectivo): PR501; Autocheck T5; 3 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M7. RA foco: RA4. El lab del Módulo 7: Ejercicio de laboratorio 4 — Trabajo con EBS. |
| **Resultados de aprendizaje** | RA4 (25 % de la nota): Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. |
| **Criterios de evaluación y ponderación** | CE4a (3,46 %): Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube. CE4c (7,30 %): Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | En una app web hay tres estilos de almacenamiento que conviene no mezclar: el disco de la máquina virtual, una carpeta de red compartida y un objeto al que se llega por HTTP (Hypertext Transfer Protocol, protocolo de transferencia de hipertexto). |
| **Contenidos** | Objeto (S3), bloque (EBS), fichero (EFS / FSx). · Clases S3, ciclo de vida, versionado, Block Public Access. · Instantáneas, instance store, copia de seguridad y movimiento de datos (Snow, Gateway, DataSync). |
| **Metodología y tutorías** | Tutoría colectiva: Arranque: objetos, bloques y ficheros. S3 frente a EBS y EFS, y ciclo de vida. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR501 — Objetos y bloques (RA4 a, c; PR 0–10). Autocheck T5: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO2 (Temas 5 a 8, 0–100, semana del 22 al 26 de febrero de 2027). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 5 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | El examen premia elegir el estilo de almacén (objeto, bloque o fichero) y no olvidar la salida de datos en la factura. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA4: PR501 (Objetos y bloques) y PR601 (RDS mínimo). |

## 9.6. Tema 6. Bases de datos

| Ficha del Tema 6 (2.ª ev.) | Bases de datos |
| --- | --- |
| **Temporalización** | 6 h en el centro, 11 ene – 22 ene 2027. Tramo 8 (11-ene – 22-ene; tutoría colectiva 12-ene, individual 19-ene): PR601; Autocheck T6; 6 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M8. RA foco: RA4. El lab del Módulo 8: Ejercicio de laboratorio 5 - Creación de un servidor de bases de datos. |
| **Resultados de aprendizaje** | RA4 (25 % de la nota): Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. |
| **Criterios de evaluación y ponderación** | CE4b (4,62 %): Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube. CE4c (7,30 %): Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Instalar MySQL en la misma EC2 (Elastic Compute Cloud, nube elástica de cómputo) que Express funciona en el aula y acopla fallo, actualizaciones y copia de seguridad: si cae la máquina, cae la API y la base de datos (BD). |
| **Contenidos** | BD en EC2 frente a RDS / Aurora (quién mantiene y actualiza el motor). · Relacional: Multi-AZ frente a réplica de lectura. · DynamoDB, ElastiCache, Redshift: cuándo no es RDS. · DMS / SCT: migración de datos (enlace con las 7 R del Tema 1). |
| **Metodología y tutorías** | Tutoría colectiva: RDS Multi-AZ frente a réplica de lectura, y DynamoDB. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR601 — RDS mínimo (RA4 b, c; PR 0–10). Autocheck T6: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO2 (Temas 5 a 8, 0–100, semana del 22 al 26 de febrero de 2027). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 6 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | Aquí el examen contrapone base gestionada frente a MySQL en la EC2, relacional frente a NoSQL, y Multi-AZ frente a réplica de lectura: no son sinónimos. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA4: PR501 (Objetos y bloques) y PR601 (RDS mínimo). |

## 9.7. Tema 7. Arquitectura Well-Architected

| Ficha del Tema 7 (2.ª ev.) | Arquitectura Well-Architected |
| --- | --- |
| **Temporalización** | 6 h en el centro, 25 ene – 5 feb 2027. Tramo 9 (25-ene – 05-feb; tutoría colectiva 26-ene, individual 02-feb): PR701; Autocheck T7; 6 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M9. RA foco: RA4. El Módulo 9 en Academy (sin laboratorio). |
| **Resultados de aprendizaje** | RA4 (25 % de la nota): Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. |
| **Criterios de evaluación y ponderación** | CE4d (4,23 %): Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas. CE4f (3,85 %): Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Una sola EC2 (Elastic Compute Cloud, nube elástica de cómputo) con MySQL local, una AMI (Amazon Machine Image, imagen de máquina de Amazon) hecha a mano y el puerto 3306 abierto al mundo funciona hasta el primer pico o el primer disco lleno. |
| **Contenidos** | Seis pilares y tensiones entre ellos. · Varias AZ, desacoplo (SNS/SQS), IaC como idea. · Well-Architected Tool y Trusted Advisor: existen; no son el entregable principal de PR701. |
| **Metodología y tutorías** | Tutoría colectiva: Pilares de Well-Architected y equilibrios de varias zonas de disponibilidad. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR701 — Mejorar un diagrama frágil (RA4 d, f; PR 0–10). Autocheck T7: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO2 (Temas 5 a 8, 0–100, semana del 22 al 26 de febrero de 2027). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 7 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | El Practitioner no pide un diagrama de cuarenta cajas: pide etiquetar el escenario con un pilar y no confundir una cola de trabajo (SQS) con una publicación/suscripción (SNS). El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA4: PR501 (Objetos y bloques) y PR601 (RDS mínimo). |

## 9.8. Tema 8. Escalado, monitorización y cierre CLF-C02

| Ficha del Tema 8 (2.ª ev.) | Escalado, monitorización y cierre CLF-C02 |
| --- | --- |
| **Temporalización** | 9 h en el centro, 8 feb – 19 feb 2027. Tramo 10 (08-feb – 19-feb; tutoría colectiva 09-feb, individual 16-feb): PR801, AC802; Autocheck T8; 9 h. |
| **Bloque de Cloud Foundations** | AWS Academy Cloud Foundations, M10. RA foco: RA3, RA4. El lab del Módulo 10: Ejercicio de laboratorio 6 - Escalado y balanceo de la carga de su arquitectura. |
| **Resultados de aprendizaje** | RA3 (30 % de la nota): Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos. RA4 (25 % de la nota): Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento. |
| **Criterios de evaluación y ponderación** | CE3e (6,32 %): Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático. CE3f (8,41 %): Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales. CE4e (1,54 %): Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización. CE4f (3,85 %): Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes. Ponderación única de cada CE en el módulo (anexo A.3). |
| **Objetivo del tema** | Si el Tema 7 dice por qué varias zonas de disponibilidad (AZ, Availability Zone), este dice cómo reparte el tráfico un ALB (Application Load Balancer, balanceador de carga de aplicaciones), cómo un ASG (Auto Scaling group, grupo de autoescalado) sigue la demanda y cómo te enteras (CloudWatch) antes que el usuario. |
| **Contenidos** | ELB (ALB / NLB), comprobaciones de estado (health checks). · Auto Scaling: mínimo, deseado y máximo; métricas; apagar entornos de desarrollo. · CloudWatch, CloudTrail, Config, Trusted Advisor, Health. · Repaso CLF-C02: IA/ML, analítica, integración (reconocer el servicio). |
| **Metodología y tutorías** | Tutoría colectiva: Balanceador, Auto Scaling y CloudWatch. Presenta el bloque y resuelve dudas, sin explicar el tema entero; la individual sigue prácticas y labs (apartado 5). |
| **Actividades e IE** | PR801 — Escalar y observar (RA3 e, f; RA4 e; PR 0–10). AC802 — Mapa de servicios CLF (RA3 f; RA4 f; AC 0–1). Autocheck T8: autoevaluación del tema, sin calificación (apartado 8.3.2). Prueba objetiva: PO2 (Temas 5 a 8, 0–100, semana del 22 al 26 de febrero de 2027). Entrega en Markdown por Aules; capturas sin Account ID ni claves (apartado 8.5). |
| **Recursos** | Apuntes del Tema 8 en el sitio MkDocs (anexo C): videotutorial, cuestionario inicial, Autocheck y glosario. AWS Academy, Learner Lab y consola; Aules. Guías de solución visibles como guía de estudio (apartado 8.5). |
| **Ampliación Practitioner** | Con ALB, Auto Scaling y CloudWatch cierras el núcleo Foundations de este tema. El +1 por la CLF-C02 suma según Aules (hasta 11) y no recupera un RA (apartado 8.7.3). |
| **Atención a la diversidad** | Medidas universales y DUA (apartado 10.2): vídeo, glosario, rúbrica visible y plazos en Aules. Si procede, apoyos de los apartados 10.3 y 10.4, sin rebajar el RA. |
| **Evaluación, calificación y recuperación** | Nota del RA = media ponderada de sus IE (anexo A.3 y apartado 8.7.2). Nota final = RA1 × 0,20 + RA2 × 0,25 + RA3 × 0,30 + RA4 × 0,25. Umbral del RA: 5, sin compensación. Recuperación en los apartados 8.9 y 8.10. |
| **Formación en empresa y empleabilidad** | Contexto de despliegue y operación en AWS (apartado 2). RA evaluados en el centro; la empresa emite informe APTO / NO APTO. Refuerzo sin las 28 h (apartado 12): RA3: PR301 (VPC y servidor web) y PR401 (Lanzar y comparar cómputo). RA4: PR501 (Objetos y bloques) y PR601 (RDS mínimo). |

---

# 10. Medidas de atención a la diversidad

## 10.1. Niveles de respuesta educativa

La atención a la diversidad sigue el marco de inclusión valenciano, establecido por el Decreto 104/2018 y la Orden 20/2019: medidas universales para todo el grupo, apoyos ordinarios adicionales y, si procede, apoyos especializados, en coordinación con el departamento de orientación. En régimen semipresencial, la mayor parte de estas medidas se aplica a través de los materiales y de la tutoría individual.

## 10.2. Medidas universales y Diseño Universal para el Aprendizaje (DUA)

El Diseño Universal para el Aprendizaje (DUA) se concreta en tres tipos de medidas. Hay varias formas de representación del contenido: apuntes, videotutorial, diagramas de arquitectura, glosario y laboratorio. Hay varias formas de acción y expresión: práctica en la consola, presupuesto en la calculadora, texto razonado en Markdown y prueba objetiva. Y hay varias formas de implicación: casos de aplicación web, autocheck para comprobar el propio progreso y preparación voluntaria de la certificación. Las prácticas tienen instrucciones en pasos cortos, rúbrica visible desde el principio y plantilla de entrega.

## 10.3. Tercer nivel de respuesta: apoyos ordinarios adicionales

Cuando hace falta, se amplía el plazo de una entrega, se ofrece refuerzo en la tutoría individual y se proporcionan materiales adicionales. Si una barrera de formato o de acceso impide una evidencia, se admite una evidencia equivalente que compruebe los mismos CE, sin rebajar el RA. Si el laboratorio de AWS Academy no está disponible, la práctica puede apoyarse en la parte de la rúbrica que no depende de él, como ya prevén algunos enunciados.

## 10.4. Cuarto nivel de respuesta: apoyos especializados adicionales

Se aplican según los dictámenes y los planes individualizados del equipo educativo y del departamento de orientación, manteniendo los RA como referentes.

## 10.5. Evaluación inclusiva y accesibilidad en el entorno digital

Los apuntes y Aules mantienen una estructura clara, con títulos, tablas y texto alternativo en las figuras. La plantilla de entrega y la guía de Visual Studio Code con Markdown evitan que el formato sea una barrera. En las pruebas objetivas se aplican las adaptaciones de tiempo y de formato que correspondan.

## 10.6. Coordinación, registro y revisión de las medidas

Las medidas se coordinan con la tutoría del grupo y con el departamento de orientación, se registran según los protocolos del centro y se revisan después de la evaluación inicial y en cada sesión de evaluación.

---

# 11. Actividades complementarias y extraescolares

## 11.1. Objetivos

Acercar al alumnado a la certificación profesional de base en la nube de AWS y al uso de los recursos oficiales de formación continua, en coherencia con la competencia p) del título.

## 11.2. Actividades previstas

| Actividad | Estado | Observación |
| --- | --- | --- |
| Preparación de la certificación CLF-C02: AWS Skill Builder, serie de vídeos de preparación, tests de práctica y autocheck de certificación | Prevista, voluntaria | Ampliación del itinerario Foundations. No sustituye ningún RA. |
| Visitas a empresas, charlas o jornadas técnicas | Sin concretar | Las fuentes del módulo no recogen ninguna. Si el departamento aprueba alguna, se añadirá a esta tabla. |

## 11.3. Integración curricular de las actividades

La preparación de la certificación se integra en cada tema a través del apartado de ampliación Practitioner y de la página de certificación de los apuntes. Refuerza los RA1 a RA4, porque el examen CLF-C02 cubre conceptos, seguridad, tecnología y facturación. No duplica la carga de las prácticas ordinarias.

## 11.4. Evaluación de las actividades

Una actividad complementaria solo entra en la calificación si se ha anunciado como IE de un RA. En ese caso se valora con la escala del instrumento que corresponda y dentro del RA declarado. La preparación de la certificación no es un IE: su único efecto en la nota es el punto adicional cuando se acredita la certificación (apartado 8.7.3).

## 11.5. Organización, responsables y seguimiento

El responsable es el profesorado del módulo. Los vales (vouchers) de examen y el acceso a Skill Builder se gestionan según la página de acceso de los apuntes. Si se organizara una salida, seguiría el protocolo del IES Macià Abela. El seguimiento se comunica al departamento de Informática.

---

# 12. Formación en la empresa

La formación en empresa (FE) se concibe como una extensión del proceso de enseñanza-aprendizaje del módulo. El centro garantiza el desarrollo y la evaluación de la totalidad de los resultados de aprendizaje y de los criterios de evaluación.

El porcentaje se fija en el **28 %** de las horas de cada módulo del ciclo, redondeado hacia abajo a horas enteras. El ciclo dura **2.000 h** también en semipresencial (Decreto 114/2025, art. 3.4 y anexo II; Orden 30/2022, art. 3). El Proyecto Intermodular (**133 h**) no se puede dualizar (Decreto 114/2025, art. 5.6; Resolución de 16 de julio de 2026, apartado 15.1.1.5), de modo que quedan **1.867 h** que pueden llevarse a la empresa. La FE debe ocupar entre el 25 % y el 35 % del ciclo, con un mínimo de **500 h** (Real Decreto 659/2023, art. 106.a; Decreto 114/2025, art. 7.6.a; pregunta frecuente 44 de la Dirección General de Formación Profesional), y ningún módulo puede superar el 65 % de sus horas en la empresa (Real Decreto 659/2023, art. 105.b).

Aplicado módulo a módulo, el 20 % suma 370 h, el 27 % llega a 500 h justas y el **28 % suma 520 h**, con margen sobre el mínimo y contando con la aportación de este módulo optativo. En semipresencial la FE se acumula en segundo y recoge también resultados de aprendizaje de primero (Resolución de 16 de julio de 2026, apartado 15.1.7; preguntas frecuentes 36 y 221), por lo que el cálculo se hace sobre todo el ciclo.

En este módulo, de **100 h** (Decreto 114/2025, anexo X-XVII, modificado por el Decreto 95/2026), el 28 % sale exacto: 100 × 0,28 = 28,00, que se redondean a **28 h**. El centro trabaja las **72 h** restantes. El porcentaje queda muy lejos del tope del 65 %.

| Concepto | Cálculo | Horas |
| --- | --- | ---: |
| Duración del ciclo | Decreto 114/2025, art. 3.4 y anexo II | 2.000 h |
| Proyecto Intermodular, no dualizable | 34 h en 1.º y 99 h en 2.º | 133 h |
| Horas que pueden ir a la empresa | 2.000 − 133 | 1.867 h |
| Mínimo de FE del ciclo | 25 % del ciclo, con suelo de 500 h | 500 h |
| Suma del ciclo al 28 %, redondeo hacia abajo | módulo a módulo | 520 h |
| Duración de este módulo | anexo X-XVII, modificado por el Decreto 95/2026 | 100 h |
| FE de este módulo | 100 × 0,28 = 28,00, redondeo hacia abajo | **28 h** |
| Centro | 100 − 28 | **72 h** |

Todos los resultados de aprendizaje se imparten y se evalúan en el centro, en esas 72 h, **sin asignar resultados de aprendizaje concretos a la empresa**. La calificación corresponde al profesorado y la empresa emite un informe **APTO / NO APTO**. Como la FE empieza el **1 de marzo de 2027**, los ocho temas, las dos pruebas y el cierre deben estar terminados antes de esa fecha.

Cuando la empresa no permite trabajar las 28 h previstas, la evidencia se completa con actividades de centro que ya existen. No se crean prácticas nuevas y estas actividades no cambian el peso del resultado de aprendizaje. El catálogo de refuerzo toma una o dos actividades por resultado de aprendizaje:

| Resultado de aprendizaje | Actividades de refuerzo en el centro |
| --- | --- |
| RA1 | PR102 (Modelos) y PR103 (Estimación) |
| RA2 | PR104 (Fábrica global) y PR201 (Usuarios y políticas) |
| RA3 | PR301 (VPC y servidor web) y PR401 (Lanzar y comparar cómputo) |
| RA4 | PR501 (Objetos y bloques) y PR601 (RDS mínimo) |

PR701, PR801 y AC802 siguen siendo instrumentos ordinarios de los Temas 7 y 8 y no se repiten en el catálogo. Los planes formativos de cada empresa se concretarán con la tutoría de FE y el departamento cuando se asignen las empresas.

---

# 13. Evaluación de la programación y de la práctica docente

La evaluación de la programación y de la práctica docente, con sus indicadores, está en el apartado 8.15. Este apartado solo remite allí, para no repetirlo.

---

# Referencias

**Normativa**

- Ley Orgánica 2/2006, de 3 de mayo, de Educación, en la redacción dada por la Ley Orgánica 3/2020, de 29 de diciembre.
- Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la Formación Profesional.
- Real Decreto 659/2023, de 18 de julio, por el que se desarrolla la ordenación del Sistema de Formación Profesional.
- Real Decreto 686/2010, de 20 de mayo, por el que se establece el título de Técnico Superior en Desarrollo de Aplicaciones Web y se fijan sus enseñanzas mínimas, actualizado por el Real Decreto 405/2023, de 29 de mayo.
- Real Decreto 500/2024, de 21 de mayo, por el que se modifican determinados reales decretos por los que se establecen títulos de Formación Profesional de grado superior y se fijan sus enseñanzas mínimas.
- Decreto 114/2025, de 29 de julio, del Consell, por el que se establecen los currículos de los ciclos formativos de grado medio y de grado superior de Formación Profesional (anexo X-XVII: Introducción a la Nube Pública), modificado por el Decreto 95/2026, de 19 de junio.
- Orden 30/2022, de 12 de mayo, de la Conselleria de Educación, Cultura y Deporte, que regula las enseñanzas de Formación Profesional en régimen semipresencial (artículos 3 y 28.2, este último modificado por la Orden 9/2025, de 5 de junio).
- Orden 8/2025, de evaluación en Formación Profesional.
- Decreto 104/2018 y Orden 20/2019, de inclusión educativa.
- Decreto 252/2019, de organización y funcionamiento de los centros.
- Resolución de 16 de julio de 2026, de la Secretaría Autonómica de Educación, de instrucciones para los centros que imparten los grados D y E de Formación Profesional en el curso 2026-2027.
- Resolución de 15 de junio de 2026, de la Dirección General de Centros Docentes, por la que se fija el calendario escolar del curso 2026-2027 en la Comunitat Valenciana.

**Evaluación en Formación Profesional**

- Solbes, R. [Los referentes para evaluar en FP](https://raulsolbes.com/2025/01/22/los-referentes-para-evaluar-en-fp/) (2025).
- Solbes, R. [Programaciones didácticas para FP: evaluación](https://raulsolbes.com/2025/04/04/programaciones-didacticas-para-fp-evaluacion/) (2025).
- Solbes, R. [Evaluación por competencias en FP](https://raulsolbes.com/2020/05/27/evaluacion-por-competencias-en-fp/) (2020).

**Recursos del módulo**

- Apuntes del módulo: <https://fjavier-hernandez.github.io/cloud/> (anexo C).
- AWS Academy Cloud Foundations y AWS Academy Learner Lab: <https://awsacademy.instructure.com>.
- Documentación oficial de AWS: <https://docs.aws.amazon.com/>.
- AWS Skill Builder: <https://skillbuilder.aws/>.
- Guía del examen AWS Certified Cloud Practitioner (CLF-C02): <https://aws.amazon.com/certification/certified-cloud-practitioner/>.
- AWS Pricing Calculator: <https://calculator.aws/>.
- Serrano, S. Apuntes de Cloud del IES Severo Ochoa: <https://salvasevero.github.io/cloud/>.
- Profe Santos Cloud, serie de preparación de Cloud Practitioner: <https://www.youtube.com/@ProfeSantosCloud>.

---

# Anexo A. Verificación de la cobertura y ponderación de los criterios de evaluación

Este anexo verifica que todos los CE del módulo se trabajan y se evalúan (A.1 y A.2) y expresa en porcentaje la ponderación de cada uno (A.3). La fuente es la matriz del módulo y las rúbricas publicadas en los apuntes.

## A.1. Resumen por resultado de aprendizaje

| RA | Nº CE del anexo | Cobertura | IE que puntúan |
| :---: | :---: | :---: | --- |
| RA1 | 6 | 6 de 6 | PR101, PR102, PR103, además de PO1 |
| RA2 | 6 | 6 de 6 | PR101, PR104, PR201, además de PO1 |
| RA3 | 6 | 6 de 6 | AC802, PR301, PR401, PR801, además de PO1 y PO2 |
| RA4 | 6 | 6 de 6 | AC802, PR501, PR601, PR701, PR801, además de PO2 |
| **Total** | **24** | **24 de 24** | |

## A.2. Matriz de criterios de evaluación

La columna de IE recoge los instrumentos con rúbrica que puntúan el CE. La prueba objetiva de la evaluación también evidencia los CE de sus temas y puntúa en el RA, pero no se asigna a un CE concreto (apartado 8.5). El autocheck y el cuestionario inicial de cada tema acompañan a todos sus CE como autoevaluación y diagnóstico, sin calificación.

| Código CE | Enunciado (anexo) | RA | Tema(s) | IE que puntúan |
| --- | --- | :---: | --- | --- |
| CE1a | Se ha comprendido los conceptos fundamentales de la computación en la nube. | RA1 | T1 | PR102; PO1 |
| CE1b | Se ha demostrado la capacidad para explicar las ventajas de la nube frente a sistemas tradicionales. | RA1 | T1 | PR102; PO1 |
| CE1c | Se ha participado en actividades relacionadas con el ecosistema de servicios en la nube. | RA1 | T1 | PR101, PR102; PO1 |
| CE1d | Se han identificado los principios básicos de la facturación y costos en la nube. | RA1 | T1 | PR103; PO1 |
| CE1e | Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos. | RA1 | T1 | PR103; PO1 |
| CE1f | Se ha participado en actividades prácticas sobre gestión de costos. | RA1 | T1 | PR103; PO1 |
| CE2a | Se ha adquirido conocimiento de los componentes de una infraestructura global en la nube. | RA2 | T1 | PR104; PO1 |
| CE2b | Se ha demostrado la capacidad para explorar y describir las principales categorías de servicios disponibles. | RA2 | T1 | PR101, PR104; PO1 |
| CE2c | Se ha realizado una evaluación del uso adecuado de servicios básicos en ejercicios prácticos. | RA2 | T1 | PR101, PR104; PO1 |
| CE2d | Se ha comprendido el modelo de responsabilidad compartida en la nube. | RA2 | T2 | PR201; PO1 |
| CE2e | Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso. | RA2 | T2 | PR201; PO1 |
| CE2f | Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad. | RA2 | T2 | PR201; PO1 |
| CE3a | Se ha realizado el diseño y configuración de redes virtuales privadas. | RA3 | T3 | PR301; PO1 |
| CE3b | Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas. | RA3 | T3 | PR301; PO1 |
| CE3c | Se ha participado activamente en la creación y configuración de una red funcional. | RA3 | T3 | PR301; PO1 |
| CE3d | Se ha realizado la selección de servicios de computación adecuados según casos de uso. | RA3 | T4 | PR401; PO1 |
| CE3e | Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático. | RA3 | T8 | PR801; PO2 |
| CE3f | Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales. | RA3 | T4, T8 | AC802, PR401, PR801; PO1 y PO2 |
| CE4a | Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube. | RA4 | T5 | PR501; PO2 |
| CE4b | Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube. | RA4 | T6 | PR601; PO2 |
| CE4c | Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos. | RA4 | T5, T6 | PR501, PR601; PO2 |
| CE4d | Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas. | RA4 | T7 | PR701; PO2 |
| CE4e | Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización. | RA4 | T8 | PR801; PO2 |
| CE4f | Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes. | RA4 | T7, T8 | AC802, PR701; PO2 |

## A.3. Ponderación de los criterios de evaluación

### Método de cálculo

Cada CE recibe una ponderación según su importancia, medida por los puntos que le dedican las rúbricas de los IE con los que se trabaja en el aula. El cálculo sigue cuatro pasos:

1. Cada criterio de una rúbrica se asigna al CE cuyo enunciado evidencia. Las prácticas valen 10 puntos y la actividad de clase AC802, 1 punto.
2. Los criterios genéricos de la rúbrica, como la claridad del Markdown, la limpieza o el knowledge check, se reparten a partes iguales entre los CE que declara el IE. La excepción es la limpieza de PR401 y de PR801, que se asigna al CE3f porque eliminar recursos al terminar es optimizar los recursos de cómputo.
3. Los puntos de cada CE se suman en todos los IE que lo evidencian. La ponderación del CE en el módulo es el peso de su RA multiplicado por los puntos del CE y dividido por los puntos de todo el RA.
4. Los porcentajes se redondean a dos decimales y el CE de mayor peso de cada RA absorbe el redondeo, para que la suma coincida con el peso del RA.

Las pruebas objetivas puntúan en el RA, pero no se asignan a un CE y no entran en este reparto. El cuestionario inicial y el autocheck no se califican. Si una rúbrica cambia, se recalcula este anexo con el mismo método y la ponderación de cada RA se mantiene.

### A.3.1. Asignación de los criterios de las rúbricas

| IE | Criterios de la rúbrica (puntos) y CE al que se asignan |
| --- | --- |
| PR101 | Acceso e introducción (2) → CE1c; consola sin coste (2) → CE2c; cinco servicios (4) → CE2b; claridad (2), repartida entre CE1c, CE2b y CE2c |
| PR102 | Cuatro situaciones (4) → CE1c; modelos coherentes (3) → CE1a; justificación (3) → CE1b |
| PR103 | Escenario 24/7 (3) → CE1e; escenario de 40 h (3) → CE1f; lectura de coste (2) → CE1d; laboratorio M2 o claridad (2), repartido entre CE1d, CE1e y CE1f |
| PR104 | Comparación de regiones (3) → CE2c; región y zonas de disponibilidad (3) → CE2a; conceptos (2) → CE2a; knowledge check o claridad (2), repartido entre CE2a, CE2b y CE2c |
| PR201 | Laboratorio y usuarios (3) → CE2f; mínimo privilegio (3) → CE2e; buenas prácticas (2) → CE2d; claridad (2), repartida entre CE2d, CE2e y CE2f |
| PR301 | VPC y subredes (3) → CE3a; rutas y puerta de enlace (2) → CE3c; grupo de seguridad (3) → CE3b; limpieza (2), repartida entre CE3a, CE3b y CE3c |
| PR401 | Laboratorio EC2 y AMI (3) → CE3f; comparación con Lambda (4) → CE3d; limpieza (2) → CE3f; claridad (1), repartida entre CE3d y CE3f |
| PR501 | Laboratorio de EBS (4) → CE4c; concepto de objeto y bloque (3) → CE4a; limpieza (2) y claridad (1), repartidas entre CE4a y CE4c |
| PR601 | Laboratorio de RDS (3) → CE4b; seguridad de red (3) → CE4c; secretos y claridad (2) → CE4b; limpieza (2), repartida entre CE4b y CE4c |
| PR701 | Cinco mejoras (4) → CE4f; pilares (3) → CE4d; equilibrio (2) → CE4d; claridad (1), repartida entre CE4d y CE4f |
| PR801 | Balanceador ALB (3) → CE3e; grupo de autoescalado (3) → CE3e; CloudWatch (2) → CE4e; limpieza (2) → CE3f |
| AC802 | Ocho tarjetas útiles (1), repartida entre CE3f y CE4f |

### A.3.2. Ponderación de cada criterio de evaluación

Los puntos son la suma de lo que aporta cada IE al CE, con dos decimales.

| Código CE | RA | IE y puntos | Puntos | Peso |
| --- | :---: | --- | ---: | ---: |
| CE1a | RA1 | PR102 3,00 | 3,00 | 2,65 % |
| CE1b | RA1 | PR102 3,00 | 3,00 | 2,65 % |
| CE1c | RA1 | PR101 2,67, PR102 4,00 | 6,67 | 5,87 % |
| CE1d | RA1 | PR103 2,67 | 2,67 | 2,35 % |
| CE1e | RA1 | PR103 3,67 | 3,67 | 3,24 % |
| CE1f | RA1 | PR103 3,67 | 3,67 | 3,24 % |
| **Suma RA1** | | | **22,67** | **20,00 %** |
| CE2a | RA2 | PR104 5,67 | 5,67 | 5,18 % |
| CE2b | RA2 | PR101 4,67, PR104 0,67 | 5,33 | 4,88 % |
| CE2c | RA2 | PR101 2,67, PR104 3,67 | 6,33 | 5,80 % |
| CE2d | RA2 | PR201 2,67 | 2,67 | 2,44 % |
| CE2e | RA2 | PR201 3,67 | 3,67 | 3,35 % |
| CE2f | RA2 | PR201 3,67 | 3,67 | 3,35 % |
| **Suma RA2** | | | **27,33** | **25,00 %** |
| CE3a | RA3 | PR301 3,67 | 3,67 | 3,86 % |
| CE3b | RA3 | PR301 3,67 | 3,67 | 3,86 % |
| CE3c | RA3 | PR301 2,67 | 2,67 | 2,81 % |
| CE3d | RA3 | PR401 4,50 | 4,50 | 4,74 % |
| CE3e | RA3 | PR801 6,00 | 6,00 | 6,32 % |
| CE3f | RA3 | AC802 0,50, PR401 5,50, PR801 2,00 | 8,00 | 8,41 % |
| **Suma RA3** | | | **28,50** | **30,00 %** |
| CE4a | RA4 | PR501 4,50 | 4,50 | 3,46 % |
| CE4b | RA4 | PR601 6,00 | 6,00 | 4,62 % |
| CE4c | RA4 | PR501 5,50, PR601 4,00 | 9,50 | 7,30 % |
| CE4d | RA4 | PR701 5,50 | 5,50 | 4,23 % |
| CE4e | RA4 | PR801 2,00 | 2,00 | 1,54 % |
| CE4f | RA4 | AC802 0,50, PR701 4,50 | 5,00 | 3,85 % |
| **Suma RA4** | | | **32,50** | **25,00 %** |
| **Total** | | | | **100,00 %** |

### A.3.3. Peso de cada instrumento dentro de su resultado de aprendizaje

El peso de un IE dentro de un RA es la parte de los puntos del RA que aporta su rúbrica. Cuando un IE evidencia CE de dos RA, figura en los dos con la parte que corresponde a cada uno. Estos pesos se refieren a la parte del RA calificada con prácticas y actividades de clase; el peso de las pruebas objetivas se publica en Aules al cerrar su enunciado. Los porcentajes se redondean a dos decimales y la diferencia de redondeo se aplica al IE cuya aportación no se repite, para que dos IE con los mismos puntos tengan el mismo peso.

| IE | RA | Puntos aportados al RA | Peso dentro del RA |
| --- | :---: | ---: | ---: |
| PR101 | RA1 | 2,67 | 11,76 % |
| PR102 | RA1 | 10,00 | 44,12 % |
| PR103 | RA1 | 10,00 | 44,12 % |
| **Suma RA1** | | **22,67** | **100,00 %** |
| PR101 | RA2 | 7,33 | 26,82 % |
| PR104 | RA2 | 10,00 | 36,59 % |
| PR201 | RA2 | 10,00 | 36,59 % |
| **Suma RA2** | | **27,33** | **100,00 %** |
| AC802 | RA3 | 0,50 | 1,75 % |
| PR301 | RA3 | 10,00 | 35,09 % |
| PR401 | RA3 | 10,00 | 35,09 % |
| PR801 | RA3 | 8,00 | 28,07 % |
| **Suma RA3** | | **28,50** | **100,00 %** |
| AC802 | RA4 | 0,50 | 1,54 % |
| PR501 | RA4 | 10,00 | 30,77 % |
| PR601 | RA4 | 10,00 | 30,77 % |
| PR701 | RA4 | 10,00 | 30,77 % |
| PR801 | RA4 | 2,00 | 6,15 % |
| **Suma RA4** | | **32,50** | **100,00 %** |

---

# Anexo B. Programación de aula

Este anexo recoge el detalle de los tramos y de las tutorías. El apartado 4.4 resume el calendario y el apartado 9 resume las horas por tema.

## B.1. Criterio de cómputo y ritmo

El módulo dura **100 h** (Decreto 114/2025, anexo X-XVII, modificado por el Decreto 95/2026). De ellas, **72 h (72 %)** se trabajan en el centro antes de la formación en empresa (FE) y **28 h (28 %)** quedan vinculadas a la FE. Las 72 h son horas de trabajo del alumnado en el periodo de centro: la tutoría más el trabajo autónomo guiado (apuntes, vídeos, laboratorios de Academy y entregas de Aules). No son horas de presencia en el aula y no equivalen a tres horas presenciales cada semana.

| Concepto | Valor |
| --- | --- |
| Duración del módulo | **100 h** |
| Trabajo en el centro, antes de la FE | **72 h** |
| Horas vinculadas a la FE | **28 h** |
| Ritmo de tutoría | Semanas alternas: una semana, tutoría colectiva; la siguiente, tutoría individual. Cada una tiene sesión de mañana y sesión de tarde, con el mismo contenido |
| Primera tutoría colectiva | **22-sep-2026** |
| Fin del periodo de centro | **26-feb-2027** |
| Inicio de la FE del ciclo | **1-mar-2027** |
| Evaluaciones | **1.ª** Temas 1 a 4 · **2.ª** Temas 5 a 8 (sin 3.ª) |

Los ocho temas, las dos pruebas objetivas y el cierre tienen que estar terminados en el centro antes del 1 de marzo de 2027. Que un tema esté publicado en la web no abre la entrega: los plazos los marcan Aules y el calendario de evaluaciones.

## B.2. Semanas lectivas

La Formación Profesional del curso 2026-2027 empieza el **9 de septiembre de 2026** y el periodo de centro de este módulo termina el **26 de febrero de 2027** (Resolución de 15 de junio de 2026, de la Dirección General de Centros Docentes, DOGV de 18 de junio de 2026). En ese intervalo hay **24 semanas** con algún día lectivo, contadas de lunes a viernes y descontando solo los festivos autonómicos que ya constan y las vacaciones de Navidad.

No se colocan tutorías del módulo antes del 22 de septiembre de 2026, porque esa es la primera tutoría colectiva. Las semanas del 9 al 11 de septiembre y del 14 al 18 de septiembre son lectivas y quedan fuera de las 72 h. Los festivos locales de Crevillent no están confirmados y no se han descontado.

| Periodo | Qué ocurre |
| --- | --- |
| 9-sep-2026 a 18-sep-2026 | Días lectivos de inicio de curso. Sin tutoría de este módulo y sin horas de las 72 h |
| 9-oct-2026 (viernes) y 12-oct-2026 (lunes) | Festivos. Las semanas siguen siendo lectivas y conservan su tutoría |
| 8-dic-2026 (martes) | Festivo. La tutoría individual de esa semana cae en otro día lectivo de la misma semana (7, 9, 10 u 11 de diciembre). El día concreto no se fija aquí |
| 22-dic-2026 a 6-ene-2027 | Vacaciones de Navidad, ambos inclusive |
| Semana del 21-dic-2026 | Solo es lectivo el lunes 21. No se programa tutoría |
| Semana del 4-ene-2027 | Solo son lectivos el jueves 7 y el viernes 8. No se programa tutoría |
| Festivos locales de Crevillent | Pendientes de confirmar. No se han inventado ni descontado |

La alternancia se ancla en la semana del 22 de septiembre (colectiva) y sigue semana a semana. Después de la colectiva del 15 de diciembre se saltan las dos semanas demasiado cortas y las vacaciones, y la siguiente colectiva es el **12 de enero de 2027**. Así se mantienen las fechas de tutoría colectiva que ya tenía el calendario. Desde el 22 de septiembre hasta el 26 de febrero quedan **11 tutorías colectivas** y **10 individuales**. La semana del 23 de febrero es colectiva y no tiene individual detrás, porque el 1 de marzo empieza la FE.

72 h repartidas en esas 21 tutorías salen a unas 3,4 h de trabajo del alumnado por semana de tutoría. El calendario permite el reparto sin comprimir un tema en un hueco que no da de sí.

La fecha que figura en cada tutoría es el martes de esa semana, el mismo día de la semana que la primera colectiva. No se indican horas del día. La excepción es la individual de primeros de diciembre: el martes 8 es festivo, así que la fecha queda como la semana y no como un día concreto.

## B.3. Reparto de las 72 h

| Bloque | Horas | Por qué esta carga |
| --- | ---: | --- |
| Tema 1 | 14 | Dos tramos y cuatro prácticas (PR101 a PR104) |
| Tema 2 | 6 | Un tramo y una práctica (PR201) |
| Tema 3 | 7 | Redes y VPC, dentro del RA3, que es el resultado de mayor peso |
| Tema 4 | 7 | Cómputo, también dentro del RA3 |
| Prueba objetiva de la 1.ª (PO1) | 3 | Prueba de los Temas 1 a 4, en el mismo tramo en el que arranca el Tema 5 |
| Tema 5 | 6 | Una práctica (PR501), partida por Navidad: 3 h antes y 3 h en la semana del 15 de diciembre |
| Tema 6 | 6 | Una práctica (PR601) |
| Tema 7 | 6 | Una práctica (PR701) |
| Tema 8 | 9 | PR801 y AC802 en un tramo completo |
| Prueba objetiva de la 2.ª (PO2) | 4 | Prueba de los Temas 5 a 8 |
| Cierre | 4 | Cierre del módulo en la misma semana que la PO2 |
| **Total** | **72** | |

## B.4. Tramos

| Tramo | Fechas | Colectiva | Individual | Contenido | Eval. | Instrumentos | Horas |
| ---: | --- | --- | --- | --- | --- | --- | ---: |
| 1 | 22-sep-2026 – 02-oct-2026 | 22-sep-2026 | 29-sep-2026 | Tema 1, parte 1: acceso, conceptos y modelos | 1.ª | PR101, PR102 | 7 |
| 2 | 05-oct-2026 – 16-oct-2026 | 06-oct-2026 | 13-oct-2026 | Tema 1, parte 2: facturación e infraestructura global | 1.ª | PR103, PR104; Autocheck T1 | 7 |
| 3 | 19-oct-2026 – 30-oct-2026 | 20-oct-2026 | 27-oct-2026 | Tema 2. Seguridad e identidad y acceso (IAM) | 1.ª | PR201; Autocheck T2 | 6 |
| 4 | 02-nov-2026 – 13-nov-2026 | 03-nov-2026 | 10-nov-2026 | Tema 3. Redes y nube privada virtual (VPC) | 1.ª | PR301; Autocheck T3 | 7 |
| 5 | 16-nov-2026 – 27-nov-2026 | 17-nov-2026 | 24-nov-2026 | Tema 4. Cómputo | 1.ª | PR401; Autocheck T4 | 7 |
| 6 | 30-nov-2026 – 11-dic-2026 | 01-dic-2026 | semana del 07-dic-2026 (el 08-dic es festivo) | PO1 y arranque del Tema 5 | 1.ª y 2.ª | PO1 (3 h; propuesta el jueves 3-dic-2026, 10:00); inicio de PR501 (3 h) | 6 |
| 7 | 14-dic-2026 – 18-dic-2026 | 15-dic-2026 | No hay: la semana del 21-dic solo tiene un día lectivo | Tema 5. Almacenamiento | 2.ª | PR501; Autocheck T5 | 3 |
| 8 | 11-ene-2027 – 22-ene-2027 | 12-ene-2027 | 19-ene-2027 | Tema 6. Bases de datos | 2.ª | PR601; Autocheck T6 | 6 |
| 9 | 25-ene-2027 – 05-feb-2027 | 26-ene-2027 | 02-feb-2027 | Tema 7. Well-Architected | 2.ª | PR701; Autocheck T7 | 6 |
| 10 | 08-feb-2027 – 19-feb-2027 | 09-feb-2027 | 16-feb-2027 | Tema 8. Escalado, monitorización y cierre | 2.ª | PR801, AC802; Autocheck T8 | 9 |
| 11 | 22-feb-2027 – 26-feb-2027 | 23-feb-2027 | No hay: la FE empieza el 01-mar-2027 | PO2 y cierre de la 2.ª evaluación | 2.ª | PO2 (4 h); cierre del módulo (4 h) | 8 |

La suma de la columna de horas es 7 + 7 + 6 + 7 + 7 + 6 + 3 + 6 + 6 + 9 + 8 = **72**. No se fusionan ni se eliminan prácticas: PR101 a PR104, PR201, PR301, PR401, PR501, PR601, PR701, PR801 y AC802 siguen en el tramo de su tema.

### Hitos

| Hito | Fecha |
| --- | --- |
| Primera tutoría colectiva (acceso y Tema 1) | 22-sep-2026 |
| PO1 (Temas 1 a 4) | Semana del 01-dic-2026. La fecha de examen la fija el centro y se publica en Aules |
| Colectiva del Tema 5, antes de Navidad | 15-dic-2026 |
| Reanudación (Tema 6) | 12-ene-2027 |
| PO2 (Temas 5 a 8) y cierre | Semana del 23-feb-2027, dentro del 22-feb-2027 al 26-feb-2027 |
| Inicio de la FE | 01-mar-2027 |

## B.5. Guion de la tutoría colectiva

La tutoría colectiva presenta el bloque, indica los recursos y resuelve las dudas del tramo anterior. No se explica el tema entero. El orden habitual es este:

1. Dudas del bloque anterior y estado de las entregas en Aules.
2. Mapa del tema nuevo y qué mirar en los apuntes o en Academy.
3. Demostración corta o captura de un laboratorio.
4. Encargo: vídeo, práctica y plazo de Aules.

La tutoría individual de la semana siguiente hace el seguimiento de esas prácticas y de los laboratorios. El contenido de la sesión de mañana y el de la sesión de tarde es el mismo.

## B.6. Encaje Foundations / Practitioner

| En la tutoría y en la evaluación del módulo | Ampliación (no sustituye el resultado de aprendizaje) |
| --- | --- |
| Bloque Foundations del tema y prácticas | Apartado Practitioner y página de Certificación |
| Laboratorios Academy de los módulos 0 a 10 | Skill Builder y tests del Cloud Practitioner |
| Autocheck del tema | Autocheck de certificación |

El **+1** por la certificación AWS Certified Cloud Practitioner (CLF-C02) se concede según las condiciones publicadas en Aules. Esta programación no incluye la rúbrica de ese punto.

## B.7. Instrumentos provisionales, a ampliar tras la verificación

- **PO1** y **PO2:** enunciado, peso dentro de cada resultado de aprendizaje y fecha exacta en Aules.
- Actividades de clase adicionales, por ejemplo los knowledge checks de Academy, si hiciera falta cubrir algún criterio de evaluación.
- Posible proyecto de arquitectura corta en los Temas 7 u 8, si el departamento lo exige.
- Importación del banco GIFT a Aules, en una fase posterior.

Los festivos locales de Crevillent siguen pendientes. Si el centro los sitúa en una semana de tutoría, la tutoría se mueve al día lectivo más cercano de esa misma semana y las horas del tramo no cambian.

---

# Anexo C. Sitio web de apuntes

Los apuntes del módulo se publican en <https://fjavier-hernandez.github.io/cloud/>. El sitio incluye la página de inicio con la evaluación y el mapa del curso, la página de acceso a AWS Academy, al laboratorio y a Skill Builder, el calendario que ve el alumnado, los Temas 1 a 8 y la página de preparación de la certificación CLF-C02. Cada tema contiene los RA y CE que trabaja, el bloque de Cloud Foundations, la ampliación Practitioner, un videotutorial, las prácticas con su rúbrica, el cuestionario inicial, el autocheck y el glosario. Las guías de solución de las prácticas y las soluciones del cuestionario inicial y del autocheck son visibles como guía de estudio; las soluciones de las pruebas objetivas no se publican.

# AndinaLog 03B · Proyecto Power BI

Proyecto académico del Grupo 06 del Diplomado en Gestión Industrial y Analítica de Datos, Módulo 4. Rol: Operaciones, Planificación y Datos de AndinaLog.

El proyecto apoyará decisiones sobre cadena de frío, vencimiento y merma de inventario y alertas de desviación térmica. Se desarrolla en Power BI como proyecto `.pbip`, utilizando una combinación de Spec First y Spec Anchored en OpenCode.

## Estado inicial

Se revisaron las guías S01–S11, las referencias y plantillas de entrega y cinco tablas Silver oficiales. Se realizaron controles independientes sobre los CSV y se consolidó el contexto del proyecto.

Todavía no se ha construido el proyecto Power BI, completado las plantillas del equipo ni ejecutado pruebas en Power BI Desktop. Las especificaciones se elaborarán progresivamente con el usuario en OpenCode.

La base documental y references/ están presentes y se revisaron. Las carpetas de implementación son previstas y se crearán cuando sean necesarias; MEMORY.md mantiene el estado operativo actualizado.

## Documentos de entrada

Antes de trabajar, leer:

1. `AGENTS.md`: instrucciones operativas del agente.
2. `MEMORY.md`: estado actual, avances y siguiente paso.
3. `docs/constitution.md`: principios del proyecto.
4. `docs/context.md`: mandato, requisitos, datos, hallazgos y pendientes.
5. `docs/decisions.md` y `docs/sources.md`: decisiones y procedencia documental.
6. La spec activa, su plan, tareas, auditoría y referencias del hito.

Si un documento necesario aún no existe o no puede leerse, indicarlo y resolver su disponibilidad antes de realizar trabajo dependiente. No asumir su contenido.

## Estructura

```text
Proyecto-Powerbi-Andinalog-rol03b/
├── README.md
├── AGENTS.md
├── MEMORY.md
├── .gitignore
├── docs/
│   ├── context.md
│   ├── constitution.md
│   ├── prompts.md
│   ├── decisions.md
│   └── sources.md
├── references/
│   ├── general/
│   ├── S01/ ... S11/
│   └── entrega/
├── specs/
│   └── NNN-hito-nombre/
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── AUDIT.md
├── powerbi/
├── validation/
│   ├── controles/
│   └── resultados/
├── evidence/
│   └── S01/ ... S11/
├── deliverables/
│   ├── tracking/
│   ├── pre-delivery/
│   └── final/
└── work/
```

- `references/`: guías y plantillas originales, sin completar.
- `specs/`: requisitos, planificación, tareas y auditorías por hito.
- `powerbi/`: un único proyecto de trabajo y sus carpetas nativas de modelo e informe.
- `validation/`: controles reproducibles y resultados de ejecución.
- `evidence/`: capturas, exportaciones y registros de pruebas por hito.
- `deliverables/`: documentos completados y paquetes de entrega.
- `work/`: temporales que deben excluirse de Git.

Las carpetas y archivos se incorporan cuando son necesarios. Los nombres definitivos del proyecto Power BI y los comandos de ejecución se documentarán al implementarlos.

## Datos oficiales

Ubicación de trabajo prescrita por S03:

```text
C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\
```

Las consultas deben utilizar el parámetro de texto `RutaSilver`, incluida la barra final. Los CSV originales permanecen fuera del repositorio y no se modifican.

| Archivo | Filas comprobadas | Grano |
| --- | ---: | --- |
| andinalog_iot_telemetry_silver.csv | 191.710 | Una lectura de un viaje, cada 30 minutos. |
| andinalog_productos_silver.csv | 120 | Un producto. |
| andinalog_flota_silver.csv | 100 | Un camión. |
| andinalog_inventory_tracking_silver.csv | 7.782 | Un lote con ingreso, salida y merma. |
| andinalog_warehouse_costs_silver.csv | 144 | Un centro en un mes. |

Los detalles, controles y limitaciones están en `docs/context.md`. `docs/sources.md` registrará ubicación, versión y controles de integridad. Los conteos anteriores proceden de lectura independiente de CSV; no acreditan carga correcta en Desktop.

## Flujo de desarrollo

```text
Spec aprobada → Plan → Build → Auditoría → Correcciones → Nueva auditoría → Cierre
```

1. **Spec:** requisitos numerados, alcance, criterios de aceptación y dudas.
2. **Plan:** implementación, dependencias y estrategia de comprobación.
3. **Tareas:** pasos pequeños, requisitos cubiertos y condición «Hecho cuando».
4. **Build:** implementar únicamente el alcance autorizado y ejecutar los controles pertinentes.
5. **Auditoría:** contrastar resultados contra la spec y las fuentes sin modificar los artefactos auditados.
6. **Correcciones:** resolver hallazgos identificados y comprobar efectos secundarios.
7. **Cierre:** acreditar todos los criterios y registrar el resultado antes de avanzar al siguiente hito con el usuario.

Cada spec tiene un solo `AUDIT.md`, con estado actual, hallazgos e historial de todas las rondas. `MEMORY.md` resume cada avance significativo y enlaza las evidencias de detalle.

Los cambios de alcance se acuerdan y reflejan en la spec antes de implementarse. Una propuesta no se considera aprobada por estar escrita.

## Recorrido por hitos

| Hito | Resultado principal |
| --- | --- |
| S01 | Decisión inicial, inventario, KPI candidatos y brecha DCAM. |
| S02 | Decisión concreta, arquitectura, mapa Silver y selección de 5–8 KPI. |
| S03 | Conexiones parametrizadas, privacidad, perfil completo y linaje. |
| S04 | Reglas de preparación contadas, justificadas y reversibles. |
| S05 | Pipeline consolidado, excepciones y controles de agregación. |
| S06 | Modelo, calendario, dimensiones, relaciones y pruebas de filtros. |
| S07 | Al menos tres KPI DAX validados y líneas base documentadas. |
| S08 | Storyboard, primera página, metas, semáforos y accesibilidad. |
| S09 | Interacción con propósito y mediciones de rendimiento. |
| S10 | What-if del umbral térmico, precisión, cobertura y recomendación condicionada. |
| S11 | RLS, comisionamiento, fichas completas y paquete de PreEntrega. |

Las plantillas finales también contemplan mejoras de S12 y defensa de S13. La rúbrica v4 y las guías específicas de esas sesiones siguen pendientes de revisión.

## Entorno y validación

- Power BI Desktop en Windows para apertura, actualización y pruebas del proyecto.
- OpenCode para el flujo SDD y trabajo sobre los archivos autorizados.
- Git para control de versiones.
- Python u otras herramientas justificadas para controles independientes y documentación, cuando se configuren.
- MCP local de Power BI y skills: incorporaciones previstas, todavía no configuradas ni necesarias para redactar las specs.

No hay comandos de construcción o pruebas acordados todavía. Se añadirán cuando existan y se hayan comprobado; no se copian comandos del ejemplo de software.

Distinguir siempre controles automáticos, pruebas ejecutadas en Desktop y procedimientos pendientes. Según la tarea se comprobarán datos, conciliación, relaciones, DAX, escenario, visuales, accesibilidad, rendimiento, RLS y portabilidad.

Una edición correcta de archivos no demuestra funcionamiento en Desktop. No declarar actualización, publicación, pruebas aprobadas ni entrenamiento de modelos sin ejecución y evidencia. La publicación en Service se documenta como arquitectura prevista conforme a las plantillas del curso.

## Entregables

- Proyecto `.pbip` y sus carpetas nativas, empaquetados según la convención de entrega.
- Libro de seguimiento con fichas KPI y evidencias por hito.
- Diccionario de datos.
- Informe de pruebas.
- Presentación y demostración.
- Evidencias de correcciones posteriores a PreEntrega y uso de IA.

Los entregables deben corresponder al mismo estado del proyecto. Los datos son sintéticos: una evaluación retrospectiva o una simulación no acredita impacto real en una operación empresarial.

## Siguiente paso

Comprobar que la base documental esté disponible y revisada. Después redactar y aclarar la spec de S01 con el usuario, aprovechando los análisis existentes sin dar por completadas las tareas que requieren Power BI.

No iniciar implementación de Power BI ni completar plantillas hasta que el usuario autorice el alcance correspondiente.

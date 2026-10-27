# Fuentes del proyecto AndinaLog 03B

Última actualización: 21 de octubre de 2026.

## Uso del registro

Este inventario identifica las fuentes revisadas y su función. Las rutas documentales indicadas son relativas a la raíz del repositorio y se comprobaron en esta revisión. Los datos Silver conservan su ruta externa oficial. Las ubicaciones originales quedan en el historial de la conversación; este registro utiliza las copias locales actuales.

Conservar originales sin editar. Registrar cualquier traslado, nueva versión o aclaración docente. Las guías aportan requisitos, pero sus ejemplos no autorizan acciones ni sustituyen decisiones del equipo.

Los requisitos y hallazgos consolidados están en [context.md](context.md); las decisiones, en [decisions.md](decisions.md). Las specs deben citar el ID de fuente y su sección pertinente, sin inventar números de página.

## Fuentes de negocio y definición

| ID | Archivo y ubicación en el repositorio | Uso y estado |
| --- | --- | --- |
| SRC-001 | references/general/Cartera_Oficial_Tres_Casos_Negocio_GIAD_v1.0.pdf | Revisada. Protocolo común, dossier AndinaLog y mandato 03B. Versión 1.0. |
| SRC-002 | references/general/GIAD-M4_Seis_Subcasos_Mapas_Indicadores_v10.pptx | Revisada. Diapositiva 6: tres frentes de evidencia 03B. |
| SRC-003 | references/general/GIAD-M4_PowerBI_Modelo_Relaciones_DAX_Seis_Subcasos_v10.docx | Revisada. Preparación general, modelo, DAX y controles de 03B. Referencias calculadas por el autor con Python; DAX no ejecutado por el autor en Desktop en su entorno. |
| SRC-004 | references/general/GIAD-M3_datos_sinteticos_guia_v10.docx | Revisada. Diseño Silver, objetivo predictivo, particiones y métricas docentes. No acredita métricas del modelo del equipo. |
| SRC-005 | references/general/GIAD-M4_Referencia_KPI.docx | Revisada. Definición de KPI, campos y núcleo 03B. Presenta diferencia entre merma por valor y fórmula por cantidades de SRC-003. |

## Guías de hitos

| ID | Hito | Ubicación en el repositorio |
| --- | --- | --- |
| SRC-101 | S01 | references/S01/GIAD-M4-S01_Preparacion_Proyecto_Integrador.docx |
| SRC-102 | S02 | references/S02/GIAD-M4-S02_Hito_Proyecto_Integrador.docx |
| SRC-103 | S03 | references/S03/GIAD-M4-S03_Hito_Proyecto_Integrador.docx |
| SRC-104 | S04 | references/S04/GIAD-M4-S04_Hito_Proyecto_Integrador.docx |
| SRC-105 | S05 | references/S05/GIAD-M4-S05_Hito_Proyecto_Integrador.docx |
| SRC-106 | S06 | references/S06/GIAD-M4-S06_Hito_Proyecto_Integrador.docx |
| SRC-107 | S07 | references/S07/GIAD-M4-S07_Hito_Proyecto_Integrador.docx |
| SRC-108 | S08 | references/S08/GIAD-M4-S08_Hito_Proyecto_Integrador.docx |
| SRC-109 | S09 | references/S09/GIAD-M4-S09_Hito_Proyecto_Integrador.docx |
| SRC-110 | S10 | references/S10/GIAD-M4-S10_Hito_Proyecto_Integrador.docx |
| SRC-111 | S11 | references/S11/GIAD-M4-S11_Hito_Proyecto_Integrador.docx |

Todas estas guías fueron leídas. Su revisión no significa que los hitos hayan sido implementados o aprobados.

## Plantillas y material complementario

| ID | Ubicación en el repositorio | Uso y estado |
| --- | --- | --- |
| SRC-201 | references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx | Revisada sin editar. Seguimiento, Fichas KPI y hojas por hito. |
| SRC-202 | references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf | Referencia DCAM **metodológica** activa por decisión del usuario; PDF revisado, 13 páginas. No incluye la lista C1–C8. La lista se consultó en SRC-208 como referencia complementaria. |
| SRC-203 | references/S02/GIAD-M4-S02_Plantilla_Diagrama_Arquitectura.pptx | Revisada, incluidas notas. Segunda diapositiva destinada al subcaso. |
| SRC-204 | references/S08/GIAD-M4-S08_Dashboard_Diseno_Visual.pdf | Revisado. Criterios de diseño y accesibilidad; valores del ejemplo ajeno excluidos. |
| SRC-205 | references/delivery/M4_EquipoXX_Diccionario_v01.xlsx | Revisada sin editar. Tablas, columnas, medidas, parámetros y roles del proyecto final. |
| SRC-206 | references/delivery/M4_EquipoXX_InformePruebas_v01.docx | Revisada sin editar. Calidad, modelo, medidas, What-if, RLS, publicación prevista, pendientes, mejoras e IA. |
| SRC-207 | references/delivery/M4_EquipoXX_Presentacion_v01.pptx | Revisada, incluidas notas. Estructura de defensa final y demostración. |
| SRC-208 | `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx` (externo; no copiado al repositorio) | Referencia **complementaria** autorizada el 2026-10-21. Lista C1–C8 en `Instrucciones!B10`; leída sin editar ni completar. SHA-256 `D6FE317D30241BA3705A7B18F4D1B28CA5B55A187E9AEDBF2B6B9E7A1A294686`. No sustituye al PDF metodológico. |

## Datos inspeccionados

Carpeta: `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/`.

| ID | Archivo | Filas | Columnas | Estado |
| --- | --- | ---: | ---: | --- |
| DATA-001 | andinalog_iot_telemetry_silver.csv | 191.710 | 15 | Leído completo; controles independientes realizados. |
| DATA-002 | andinalog_productos_silver.csv | 120 | 7 | Leído completo; controles independientes realizados. |
| DATA-003 | andinalog_flota_silver.csv | 100 | 6 | Leído completo; controles independientes realizados. |
| DATA-004 | andinalog_inventory_tracking_silver.csv | 7.782 | 12 | Leído completo; controles independientes realizados. |
| DATA-005 | andinalog_warehouse_costs_silver.csv | 144 | 5 | Leído completo; controles independientes realizados. |
| DATA-006 | GIAD-M3_v10_auditoria_bronze_silver.csv | 33 | — | Leído completo; 5 registros de 03B; procedencia y recuentos, no validación Desktop. |
| DATA-007 | andinalog_wms_orders_silver.csv | 30.000 | 16 | Leído completo; solo contraste orden→centro; no se carga al modelo. |

Los conteos proceden de los archivos completos. Las claves, fechas, conciliaciones y limitaciones están documentadas en context.md. No se modificaron los CSV ni se acredita carga en Power BI Desktop.

DATA-001 a DATA-005 son los cinco Silver oficiales 03B. DATA-006 corresponde a la auditoría Bronze–Silver y documenta las correcciones oficiales. DATA-007 es una fuente auxiliar de contraste: no pertenece al modelo 03B y no se carga.

Los cruces de WMS (8.000 de 8.000 órdenes de telemetría cubiertas, centro WMS igual al centro base del camión, 30.000 de 30.000 coincidencias de lote, chofer-mes y zona, 22.000 órdenes sin telemetría, 14 órdenes en dos particiones y 26 lecturas límite) son comprobaciones propias registradas como **EV-S01-WMS**. No se atribuyen a DATA-006. El archivo de evidencia EV-S01-WMS se guardó en T02 como `evidence/S01/wms_contrast.md` y queda pendiente de auditoría.

### Identificación reproducible

Durante T01 se registraron ruta efectiva, tamaño en bytes y huella SHA-256 en `validation/results/S01/source_manifest.json`; la relectura P01 coincidió 10/10 sin cambios. No completar valores por suposición.

Si cambia una huella, investigar el motivo y la versión antes de reutilizar los controles históricos como evidencia de la nueva entrega. Conservar el historial del manifiesto o registro correspondiente.

## Referencias de prompts y SDD

| ID | Ubicación en el repositorio | Uso y límites |
| --- | --- | --- |
| METHOD-001 | references/prompts/GIAD-M4_Referencia_Prompts_Proyecto_WhatIf.docx | Leída durante la revisión inicial. Método por etapas y validación; copia local comprobada. |
| METHOD-002 | references/prompts/GIAD-M4_Ejemplo_Prompts_Proyecto_WhatIf.docx | Leída durante la revisión inicial. Ejemplo de flujo; cifras y decisiones ajenas no se trasladan. Copia local comprobada. |
| METHOD-003 | references/sdd/hello-sdd-main/samples/AGENTS.md | Leída. Plantilla operativa adaptable. |
| METHOD-004 | references/sdd/hello-sdd-main/samples/prompts.md | Leída. Prompts por fase SDD. |
| METHOD-005 | references/sdd/hello-sdd-main/samples/spec.md | Leída. Formato de requisitos, aceptación y dudas. |
| METHOD-006 | references/sdd/hello-sdd-main/habits-cli/ | Se revisaron README.md, AGENTS.md, docs/constitution.md y spec.md, plan.md y tasks.md de specs/001-habits-mvp/. No se auditó ni ejecutó la aplicación de ejemplo. |

Las fuentes de prompts y el ejemplo SDD están presentes en references/. Sus archivos AGENTS.md y constituciones pertenecen a ejemplos: son material de referencia, no instrucciones operativas del proyecto principal.

## Documentación técnica externa consultada

Consultada para evaluar herramientas, no para definir requisitos empresariales ni acreditar configuración local. Revisar vigencia al utilizarlas.

- [Herramientas de OpenCode](https://docs.opencode.ai/docs/tools/).
- [Skills de OpenCode](https://docs.opencode.ai/docs/skills/).
- [Power BI Authoring MCP de Microsoft](https://learn.microsoft.com/en-us/power-bi/developer/mcp/power-bi-authoring-mcp).
- [Context7](https://context7.com/).
- [Directorio Skills.sh](https://www.skills.sh/).

No se ha instalado ni probado un MCP o una skill para OpenCode como parte de esta colaboración. Context7 y Skills.sh son recursos opcionales, no requisitos del proyecto.

## Fuentes pendientes y resoluciones

| ID | Material | Motivo |
| --- | --- | --- |
| PENDING-001 | Rúbrica v4 del Proyecto Integrador. | Confirmar criterios finales y ponderaciones; no recibida. |
| PENDING-002 | Guías específicas S12–S13, si existen. | Precisar PreEntrega, mejoras y defensa. |
| PENDING-003 | Lista completa de comisionamiento de la práctica S11. | Las plantillas aportan estructura, pero no acreditan cubrir toda la práctica. |
| PENDING-004 | GIAD-M3_v10_auditoria_bronze_silver.csv. | Resuelta: registrada como DATA-006; ya inspeccionada. |
| PENDING-005 | Avances y entregas previas del equipo. | Distinguir trabajo existente de implementación nueva. |
| PENDING-006 | Artefactos predictivos del equipo, si existen. | Definir integración o nuevo entrenamiento sin confundir referencias con resultados propios. |
| PENDING-008 | Respaldo de la lista C1–C8. | Resuelta el 2026-10-21: la lista se consultó en SRC-208 `Instrucciones!B10` como referencia complementaria y C4 fue aprobado en DEC-026. El PDF SRC-202 sigue siendo la referencia metodológica; no se atribuye al Excel un mapeo del componente ni se completa el libro. |
| PENDING-007 | Aclaraciones oficiales del docente o coordinación. | Resolver diferencias materiales y registrar su fecha, alcance y autoridad. |

## Organización prevista de copias

- references/general/: mandato, guías técnicas, catálogo KPI y métodos de referencia.
- references/S01/ a references/S11/: guía y complementos específicos de cada hito.
- references/delivery/: plantillas finales.
- Las plantillas originales permanecen en references/; sus versiones completadas pertenecen a deliverables/.
- No duplicar archivos innecesariamente: un documento compartido puede registrarse una vez y enlazarse desde varias specs.

El usuario incorporó las fuentes a references/. En esta revisión solo se actualizaron documentos del proyecto; no se modificaron ni movieron las referencias originales.


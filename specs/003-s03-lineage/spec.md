# Spec 003 — S03 · Conexión parametrizada, perfil y linaje Silver

**Versión:** 0.1  
**Estado de la spec:** Cerrada el 2026-10-28  
**Fase:** Close completada  
**Build:** Completado y auditado  
**Hito anterior:** S02 cerrado el 2026-10-27

## 1. Contexto y objetivo

El Grupo 06 trabaja el subcaso 03B de AndinaLog con cinco tablas Silver oficiales. El PBIP ya contiene el parámetro `RutaSilver`, cinco consultas en modo Import, tipado inicial, cero relaciones, cero medidas, cero roles y una página sin visuales.

S03 debe comprobar en Power BI Desktop que las fuentes puedan actualizarse mediante una ruta parametrizada, con región y privacidad documentadas, perfil calculado sobre todo el conjunto y excepciones trasladables a S04. También debe completar el linaje y las tablas fuente de los cinco KPI.

La pregunta de control es:

> ¿Las cinco fuentes oficiales pueden actualizarse mediante una ruta parametrizada, con tipos y calidad conocidos, de forma reproducible y sin ocultar excepciones que deban tratarse en S04?

La persona designada para compartir pantalla es **Rodrigo Tucuman, integrante del Grupo 06**.

## 2. Fuentes y dependencias

| ID | Fuente | Uso en S03 |
|---|---|---|
| SRC-103 | `GIAD-M4-S03_Hito_Proyecto_Integrador.docx` | Requisito principal |
| SRC-201 | `GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | `S03 Linaje` y `Fichas KPI` |
| SRC-003 | Modelo, relaciones y DAX de los seis subcasos | Referencia técnica |
| DATA-001 | Telemetría Silver | Fuente oficial 03B |
| DATA-002 | Productos Silver | Fuente oficial 03B |
| DATA-003 | Flota Silver | Fuente oficial 03B |
| DATA-004 | Inventario Silver | Fuente oficial 03B |
| DATA-005 | Costos de almacén Silver | Fuente oficial 03B |
| PBIP | `powerbi/AndinaLog_03B.pbip` | Proyecto que se continúa |

`andinalog_wms_orders_silver.csv` permanece fuera del modelo. Solo puede citarse como contraste heredado y no cuenta como sexta fuente.

## 3. Estado inicial verificable

| Tabla Power BI | Archivo | Filas de referencia | Columnas |
|---|---|---:|---:|
| Telemetria | `andinalog_iot_telemetry_silver.csv` | 191.710 | 15 |
| Productos | `andinalog_productos_silver.csv` | 120 | 7 |
| Flota | `andinalog_flota_silver.csv` | 100 | 6 |
| Inventario | `andinalog_inventory_tracking_silver.csv` | 7.782 | 12 |
| CostosAlmacen | `andinalog_warehouse_costs_silver.csv` | 144 | 5 |

Estos valores son referencias verificadas previamente. S03 debe contrastarlos mediante el perfil completo de Power Query; no se copiarán como si fueran una nueva ejecución.

## 4. Decisiones de S03

1. **Región:** Inglés (Estados Unidos), porque los Silver utilizan punto decimal. No se reemplazarán puntos por comas.
2. **Ruta:** `RutaSilver` conserva el valor `C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\` y todas las consultas usan `File.Contents(RutaSilver & "nombre_del_archivo.csv")`.
3. **Privacidad propuesta:** Organizacional para las cinco fuentes, por tratarse de archivos oficiales del proyecto en una carpeta común controlada. El nivel efectivo debe comprobarse en Desktop; si difiere, se registra antes de cambiarlo.
4. **Fechas:** `fecha_ingreso`, `fecha_salida` y `fecha_vencimiento` conservan fecha y hora. S03 no elimina la hora.
5. **Excepciones:** S03 las identifica y documenta, pero no las corrige. Su tratamiento corresponde a S04.

## 5. Requisitos funcionales

### RF-S03-01 — Región

Comprobar en Desktop que la región del archivo actual sea Inglés (Estados Unidos), o registrar la diferencia observada.

### RF-S03-02 — Parámetro único

Comprobar que `RutaSilver` sea un parámetro requerido de tipo Texto, con la ruta acordada y barra final.

### RF-S03-03 — Cinco conexiones oficiales

Las cinco consultas oficiales deben leer sus CSV mediante `RutaSilver`. WMS no se importa.

### RF-S03-04 — Privacidad

Registrar para cada fuente el nivel efectivo, su justificación y cualquier diferencia observada. Una declaración Markdown no sustituye la comprobación en Desktop.

### RF-S03-05 — Perfil completo

Activar **Generación de perfiles de columnas basada en todo el conjunto de datos** y documentar por fuente:

- total de filas;
- tipos;
- vacíos o errores relevantes;
- valores fuera de rango o excepciones;
- ausencia de anomalía confirmada cuando corresponda.

La vista de las primeras 1.000 filas no sustituye el perfil completo.

### RF-S03-06 — Linaje

Completar exactamente cinco filas en `S03 Linaje`, una por fuente oficial, con fuente, conector, parámetro, privacidad, filas, excepción y regla propuesta para S04.

### RF-S03-07 — Tablas fuente de los KPI

Completar `Fichas KPI`, columna `Tabla(s) fuente (S03)`:

| KPI | Tabla fuente principal |
|---|---|
| % de viajes con desviación | Telemetria |
| % de lecturas con desviación | Telemetria |
| Merma por cantidades | Inventario |
| % de lotes salidos vencidos | Inventario |
| Días promedio en almacén | Inventario |

`Productos` y `Flota` pueden documentarse como apoyo futuro de segmentación, pero no son necesarias para calcular esos cinco KPI en S03.

## 6. Excepciones iniciales por contrastar

| Fuente | Condición que se debe evaluar | Regla propuesta para S04 |
|---|---|---|
| Telemetría | 26 lecturas marcadas en el límite no se reproducen con la regla estricta `abs(temperatura − referencia) > tolerancia` | Conservar etiquetas; probar `>`/`>=` y redondeo; no relabelar por suposición |
| Productos | Solo 70 de 120 productos aparecen en la telemetría revisada | Tratar como cobertura referencial; no eliminar productos sin movimiento |
| Flota | `centro_distribucion_base` no tiene definición empresarial validada | No llamarlo origen o centro operativo; solicitar definición |
| Inventario | `fecha_salida` no está vacía y las fechas contienen hora; describe movimientos históricos, no stock vigente | Conservar fecha-hora; derivar fecha posteriormente |
| CostosAlmacen | La relación temporal de `periodo_mes` con movimientos está pendiente | Conservar el mes; validar después la clave centro-periodo |

El perfil completo puede confirmar, descartar o añadir observaciones, siempre con evidencia.

## 7. Requisitos no funcionales

### RNF-S03-01 — Reproducibilidad

Cambiar `RutaSilver` debe bastar para reubicar las cinco fuentes sin editar cada consulta.

### RNF-S03-02 — Integridad

No modificar los CSV Silver originales.

### RNF-S03-03 — Alcance mínimo

S03 no crea relaciones, medidas, roles, visuales, reglas correctivas, tablas calculadas ni una sexta fuente WMS.

### RNF-S03-04 — Evidencia auténtica

Región, privacidad y perfil completo deben acreditarse con Desktop. El MCP puede complementar conteos y estructura, pero no reemplazar evidencia visual exigida por la guía.

### RNF-S03-05 — Presupuesto documental

S03 conserva únicamente los documentos SDD, un `evidence.md`, un `validation.json`, el PBIP, el libro actualizado y las capturas indispensables. No se crean informes por microtarea, manifiestos redundantes ni renders permanentes sin función de entrega.

## 8. Evidencia mínima

1. Captura legible con panel Consultas, `RutaSilver`, paso `Origen` de una tabla y su fórmula `File.Contents(RutaSilver & ...)`.
2. Evidencia de región, privacidad de las cinco fuentes y perfil basado en todo el conjunto.
3. Conteos y excepciones de las cinco fuentes.
4. `S03 Linaje` con cinco filas.
5. `Fichas KPI` con las cinco tablas fuente.

No se exige una captura por microacción si una sola imagen demuestra varios requisitos.

## 9. Criterios de aceptación

| ID | Criterio |
|---|---|
| CA-S03-01 | `RutaSilver` existe, conserva la barra final y ninguna consulta tiene una ruta absoluta independiente |
| CA-S03-02 | Las cinco fuentes actualizan correctamente y WMS no está cargada |
| CA-S03-03 | La región compatible con punto decimal está documentada con evidencia Desktop |
| CA-S03-04 | La privacidad de las cinco fuentes está registrada y justificada |
| CA-S03-05 | El perfil completo acredita filas, tipos, vacíos/errores y excepciones por fuente |
| CA-S03-06 | `S03 Linaje` contiene exactamente cinco filas y una regla propuesta para S04 por fuente |
| CA-S03-07 | Los cinco KPI tienen su tabla fuente registrada |
| CA-S03-08 | No se modificaron Silver ni se añadieron relaciones, medidas, roles, visuales o WMS |
| CA-S03-09 | Las excepciones se documentaron sin aplicar correcciones de S04 |

## 10. Casos límite

- Si el perfil permanece en las primeras 1.000 filas, S03 no cumple.
- Si no hay anomalía confirmada, se registra «sin excepción confirmada» y las comprobaciones realizadas.
- Si la privacidad efectiva difiere de Organizacional, se registra antes de modificarla.
- Si Desktop muestra coma decimal, se documenta la anomalía regional y no se corrigen los datos.
- Si el perfil tarda en Telemetría, se espera; no se sustituye por la vista previa.
- Si una regla propuesta cambia datos, su ejecución se aplaza a S04.
- Si `fecha_salida` aparece vacía, se registra como hallazgo nuevo porque contradice la referencia docente para 03B.

## 11. Entregables

- PBIP con las cinco conexiones verificadas.
- Libro de seguimiento con `S03 Linaje` y la columna de tablas fuente en `Fichas KPI`.
- `evidence/S03/evidence.md`.
- `validation/results/S03/validation.json`.
- Capturas mínimas indispensables.

## 12. Fuera de alcance

- Limpieza o corrección de excepciones.
- Relaciones, calendario, medidas DAX, dashboard o RLS.
- Publicación en Power BI Service.
- Resolución empresarial del significado de centro.
- Uso de WMS como fuente del modelo.

## 13. Condiciones de cierre

S03 podrá cerrarse cuando:

1. CA-S03-01 a CA-S03-09 pasen.
2. La auditoría no tenga hallazgos bloqueantes.
3. Las limitaciones estén documentadas y no sustituyan requisitos.
4. El usuario apruebe explícitamente el cierre.
5. S04 no se haya iniciado antes del cierre de S03.

## 14. Dudas abiertas

- Confirmar en Desktop la privacidad efectiva de las cinco fuentes.
- Confirmar si el perfil completo reproduce los conteos de referencia.
- Determinar si aparecen excepciones adicionales.
- Mantener abiertos origen, propietarios y frecuencia de actualización no documentados.
- Mantener pendiente la validación empresarial de `centro_distribucion` y `centro_distribucion_base`.

## 15. Aprobación e historial

- 2026-10-27: el usuario aprobó la spec S03 v0.1 presentada en chat.
- La aprobación autoriza guardar la spec y actualizar el estado documental; no autoriza Plan ni Build.
- 2026-10-28: el usuario autorizó completar todas las tareas pendientes. La ronda 02 confirmó 21/21 requisitos y criterios; S03 quedó cerrado sin iniciar S04.

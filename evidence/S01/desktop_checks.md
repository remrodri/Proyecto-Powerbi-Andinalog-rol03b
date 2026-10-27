# S01 · Registro de entorno y verificación Desktop

## Estado de T01

- Fecha: 2026-10-20.
- Alcance ejecutado: verificación de fuentes y entorno; T01 únicamente.
- Resultado: fuentes y referencias localizadas; huellas SHA-256 registradas; entorno identificado.
- Límite: no se abrió Power BI, no se importaron tablas, no se completaron plantillas y no se ejecutó T02.

Manifiesto: [`validation/results/S01/source_manifest.json`](../../validation/results/S01/source_manifest.json).

## Fuentes verificadas

| ID | Rol | Estado | Bytes |
| --- | --- | --- | ---: |
| DATA-001 | Silver oficial | Presente | 19.440.087 |
| DATA-002 | Silver oficial | Presente | 6.272 |
| DATA-003 | Silver oficial | Presente | 4.528 |
| DATA-004 | Silver oficial | Presente | 961.833 |
| DATA-005 | Silver oficial | Presente | 6.407 |
| DATA-006 | Procedencia Bronze–Silver | Presente | 2.879 |
| DATA-007 | WMS de contraste | Presente | 3.545.848 |
| SRC-101 | Guía S01 | Presente | 39.313 |
| SRC-201 | Plantilla del Proyecto Integrador | Presente | 36.907 |
| SRC-202 | Referencia DCAM | Presente | 71.011 |

Las huellas, rutas efectivas y fechas de modificación están en el manifiesto. La comprobación fue de solo lectura; no se contaron filas ni columnas de los CSV en T01. P01: las 10 huellas se releyeron después de la verificación y coincidieron; no se modificaron las fuentes.

## Entorno

- Sistema: Windows NT 10.0.26200.0.
- PowerShell: 5.1.26100.9711.
- Cultura: `en-US`; configuración regional del sistema: `en-US`.
- Python: 3.14.6, `C:\Python314\python.exe`.
- Bibliotecas: `csv`, `json`, `hashlib`, `openpyxl` y `pandas` disponibles.
- Renderizador XLSX: `soffice` no encontrado; la revisión visual del libro se cubrió en T04 con PDF exportados desde Excel.
- Git: no se detectó repositorio `.git`; no se inicializó ni se hicieron commits.

## Power BI Desktop

- Paquete Microsoft Store detectado: `Microsoft.MicrosoftPowerBIDesktop`.
- Versión del paquete: 2.159.883.0.
- Instalación: `C:\Program Files\WindowsApps\Microsoft.MicrosoftPowerBIDesktop_2.159.883.0_x64__8wekyb3d8bbwe`.
- Proceso `PBIDesktop`: no estaba en ejecución.
- No se encontró ejecutable independiente en las rutas `Program Files` ni en `WindowsApps`; la instalación Store explica la ausencia.
- En T01 no se abrió la aplicación ni se validó su interfaz, región efectiva o actualización. La apertura y las comprobaciones de T05 se registran más abajo.
- Verificación T05 (2026-10-21): el proceso `PBIDesktop` PID 13056 ejecuta `2.159.883.0 (26.10)` desde la instalación Store; cultura del sistema `en-US` y cultura del modelo `en-US`. La ventana usada fue `AndinaLog_03B` (handle 2493880), no la ventana homónima de otro proyecto.

## Procedimiento T05

1. Abrir Power BI Desktop y confirmar versión, región efectiva y origen.
2. Importar solo DATA-001 a DATA-005; WMS no se importa.
3. Registrar archivo, filas y columnas/encabezados por tabla.
4. En tablas con campos decimales, registrar al menos un decimal leído o una anomalía regional documentada.
5. En Flota, comprobar enteros y fechas y documentar que no contiene campos decimales.
6. Guardar capturas o exportaciones auténticas; no declarar la prueba hasta ejecutarla.

Estado al 2026-10-21: pasos 1 y 2 ejecutados; el paso 3 está cubierto para las cinco tablas; el paso 4 para Productos, Inventario, CostosAlmacen y Telemetria; el paso 5 para Flota. La cobertura visual está completa y T05 fue confirmada como completada por el usuario el 2026-10-21. El 2026-10-20 T05 no se había ejecutado; al 2026-10-21 el modelo mínimo ya está importado y verificado.

Nota de cierre T05: las secciones de evidencia conservan las comprobaciones tal como se registraron. Las frases «T05 no se cierra» o «queda pendiente» dentro de esas secciones son históricas y quedan superadas por la confirmación del usuario y la conciliación T06 de la sección final.

## Evidencia MCP del modelo

La construcción y verificación por MCP del modelo mínimo consta en [mcp_model_checks.md](mcp_model_checks.md), con consultas DAX, resultados y comprobación en solo lectura del PBIP. Esa evidencia no sustituye las capturas de Desktop; la cobertura visual de las cinco tablas está completa y queda la evaluación final de T05.

## Evidencia visual T05 · Productos

- Fecha de captura: 2026-10-21, aproximadamente 00:51–00:54 (UTC−04:00).
- Ventana capturada: `AndinaLog_03B` (Power BI Desktop, PID 13056), Power Query Editor, handle 2493880, 1516×889.
- Método: captura de la ventana con `PrintWindow` y `PW_RENDERFULLCONTENT` sobre el handle identificado. No se usó como evidencia la ventana homónima de otro proyecto (`AndinaLog_03B_Modelo_KPI`) ni la evidencia MCP como sustituto.
- Consulta: `Productos`, con tres pasos: `Origen`, `Encabezados` y `Tipado`.
- Comprobaciones visuales:
  - [s01_t05_01_productos_powerquery.png](screenshots/s01_t05_01_productos_powerquery.png): 7 encabezados, `Columns: 7`, `Rows: 120`; `producto_id` muestra 120 distintos y 120 únicos.
  - [s01_t05_02_productos_origen.png](screenshots/s01_t05_02_productos_origen.png): paso `Origen` seleccionado y fórmula `Csv.Document(File.Contents(RutaSilver & "andinalog_productos_silver.csv"), [Delimiter=",", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; Applied Steps `Origen` → `Encabezados` → `Tipado`.
  - [s01_t05_03_productos_decimal.png](screenshots/s01_t05_03_productos_decimal.png): primera fila `PROD-0001`, `costo_unitario_bob = 23.73` y `precio_unitario_bob = 34.05`, con punto decimal; `Rows: 120`, `Columns: 7`.
- La vista del paso `Origen` muestra el preview inicial (`Rows: 99+`); el conteo completo de 120 filas se acredita en las capturas del paso `Tipado`.
- Los valores y encabezados coinciden con los controles de T02/T05. No se observó una anomalía regional en Productos.
- Huellas SHA-256:
  - `s01_t05_01_productos_powerquery.png`: `3C5CFA05F6F86456FE0A6C3BE7360F6FFB4914ECB0B2A5B509D4DCA2F16F5081`.
  - `s01_t05_02_productos_origen.png`: `DA32083A9BFFD0126C8D6B4580269981E8E44580A755DFA5631B7614761442D9`.
  - `s01_t05_03_productos_decimal.png`: `FF8B9BE6F3C1129809E1AFC0CA5231EA7BB6BAB0D14DA9FB73DDDE160B0CA307`.
- Límite histórico de esta captura: evidencia de Productos solamente. Flota, Inventario, CostosAlmacen y Telemetria se completaron después; ver la nota de cierre y la conciliación T06.

## Evidencia visual T05 · Flota

- Fecha de captura: 2026-10-21, aproximadamente 01:00–01:07 (UTC−04:00).
- Ventana capturada: `AndinaLog_03B` (Power BI Desktop, PID 13056), Power Query Editor, handle 2493880, 1516×889. No se actuó sobre `AndinaLog_03B_Modelo_KPI`.
- Consulta: `Flota`, con tres pasos: `Origen`, `Encabezados` y `Tipado`.
- [s01_t05_04_flota_powerquery.png](screenshots/s01_t05_04_flota_powerquery.png): 6 encabezados, `Columns: 6`, `Rows: 100`; `camion_id` muestra 100 distintos y 100 únicos. La primera fila `CAM-001` tiene `capacidad_kg = 8000` y `antiguedad_anios = 11`; `fecha_ultimo_mantenimiento` se muestra como `7/30/2024` por el formato regional de la interfaz.
- [s01_t05_05_flota_origen.png](screenshots/s01_t05_05_flota_origen.png): paso `Origen` seleccionado y fórmula `Csv.Document(File.Contents(RutaSilver & "andinalog_flota_silver.csv"), [Delimiter=",", Columns=6, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; Applied Steps `Origen` → `Encabezados` → `Tipado`. La vista del origen muestra `CAM-001` con `8000`, `11` y `2024-07-30`; el preview inicial indica `Rows: 99+` porque corresponde al paso de origen.
- La misma fecha aparece como `2024-07-30` en `Origen` y como `7/30/2024` en `Tipado`: es el mismo valor mostrado con distinto formato; no se modificó la consulta.
- Columnas decimales: 0. La barra de fórmulas de `Tipado` muestra `camion_id` y `centro_distribucion_base` como `text`, `capacidad_kg` y `antiguedad_anios` como `Int64.Type`, `tipo_camion` como `text` y `fecha_ultimo_mantenimiento` como `type date`; ninguna es `Decimal.Type`.
- Huellas SHA-256:
  - `s01_t05_04_flota_powerquery.png`: `1CEEFC3294F1A856949E8AEC150919079EA02EA76A1049B11A8EB1884369535C`.
  - `s01_t05_05_flota_origen.png`: `7C2D85AACCD52D8E2A9DEAA761806789B001D49B07DEF6AD7A173BAE7500785F`.
- Límite histórico de esta captura: evidencia de Flota solamente. Inventario, CostosAlmacen y Telemetria se completaron después; ver la nota de cierre y la conciliación T06.

## Evidencia visual T05 · Inventario

- Fecha de captura: 2026-10-21, aproximadamente 01:28–01:30 (UTC−04:00).
- Ventana capturada: `AndinaLog_03B` (Power BI Desktop, PID 13056), Power Query Editor, handle 2493880, 1888×1096 (maximizada). No se actuó sobre `AndinaLog_03B_Modelo_KPI`.
- Consulta: `Inventario`, con tres pasos: `Origen`, `Encabezados` y `Tipado`.
- [s01_t05_07_inventario_powerquery.png](screenshots/s01_t05_07_inventario_powerquery.png): paso `Tipado`, 12 encabezados, `Columns: 12` y `Rows: 99+` (vista parcial). La fila 1 muestra `MOV-0000001`, `LOT-0000001`, `PROD-0034`, `La Paz`; `cantidad_ingreso = 679`, `cantidad_salida = 657`, `cantidad_merma = 22`, `dias_en_almacen = 61` y `costo_unitario_bob = 47.11` con punto decimal.
- Las fechas de la fila 1 se ven como `1/10/2024 6:48:25 PM`, `3/11/2024 6:48:25 PM` y `11/5/2024 6:48:25 PM` en `Tipado`; el paso `Origen` las muestra como `2024-01-10 18:48:25`, `2024-03-11 18:48:25` y `2024-11-05 18:48:25`. Son los mismos valores con distinto formato de interfaz; no se modificó la consulta.
- [s01_t05_08_inventario_origen.png](screenshots/s01_t05_08_inventario_origen.png): paso `Origen` seleccionado y fórmula `Csv.Document(File.Contents(RutaSilver & "andinalog_inventory_tracking_silver.csv"), [Delimiter=",", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; Applied Steps `Origen` → `Encabezados` → `Tipado`.
- Tipos del paso `Tipado`: `movimiento_id`, `lote_id`, `producto_id` y `centro_distribucion` son `text`; `fecha_ingreso`, `fecha_salida` y `fecha_vencimiento` son `type datetime`; `cantidad_ingreso`, `cantidad_salida`, `cantidad_merma` y `dias_en_almacen` son `Int64.Type`; `costo_unitario_bob` es `type number`.
- Complemento MCP en solo lectura: `COUNTROWS(Inventario) = 7.782`; la primera fila devuelve los mismos valores y tipos (`costo_unitario_bob` como Double). El total no se deduce del preview `Rows: 99+`; se acredita con el conteo del modelo.
- No se observó una anomalía regional en el decimal `47.11`; se leyó con punto decimal.
- Huellas SHA-256:
  - `s01_t05_07_inventario_powerquery.png`: `6B894CFAB506F600612E512B7D468528B9444A91C6DFC2B4FFFBDF015F5D3090`.
  - `s01_t05_08_inventario_origen.png`: `CFD4F996FDE34F62F9C941B539F684B715509BAC39C7C0187A5DDE1EF54D062E`.
- Límite histórico de esta captura: evidencia de Inventario solamente. CostosAlmacen y Telemetria se completaron después; ver la nota de cierre y la conciliación T06.

## Evidencia visual T05 · CostosAlmacen

- Fecha de captura: 2026-10-21, aproximadamente 01:33–01:35 (UTC−04:00).
- Ventana capturada: `AndinaLog_03B` (Power BI Desktop, PID 13056), Power Query Editor, handle 2493880, 1888×1096 (maximizada). No se actuó sobre `AndinaLog_03B_Modelo_KPI`.
- Consulta: `CostosAlmacen`, con tres pasos: `Origen`, `Encabezados` y `Tipado`.
- [s01_t05_09_costos_powerquery.png](screenshots/s01_t05_09_costos_powerquery.png): paso `Tipado`, 5 encabezados, `Columns: 5` y `Rows: 99+` (vista parcial); 6 centros distintos y 24 periodos distintos. La fila 1 muestra `La Paz`, `rotacion_stock_dias = 32.9`, `perdida_mermas_bob = 37983.68`, `periodo_mes = 1/31/2024` y `costo_almacenamiento_mensual_bob = 155267.38`, con punto decimal.
- [s01_t05_10_costos_origen.png](screenshots/s01_t05_10_costos_origen.png): paso `Origen` seleccionado y fórmula `Csv.Document(File.Contents(RutaSilver & "andinalog_warehouse_costs_silver.csv"), [Delimiter=",", Columns=5, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; Applied Steps `Origen` → `Encabezados` → `Tipado`. El origen muestra `2024-01-31`, equivalente a `1/31/2024` en `Tipado`.
- Tipos del paso `Tipado`: `centro_distribucion` es `text`; `rotacion_stock_dias`, `perdida_mermas_bob` y `costo_almacenamiento_mensual_bob` son `type number`; `periodo_mes` es `type date`.
- Complemento MCP en solo lectura: `COUNTROWS(CostosAlmacen) = 144`; la fila `La Paz` de enero de 2024 devuelve los mismos valores y tipos (`Double` en las tres columnas numéricas). El total no se deduce del preview `Rows: 99+`.
- No se observó una anomalía regional en los decimales `32.9`, `37983.68` y `155267.38`; se leyeron con punto decimal.
- Huellas SHA-256:
  - `s01_t05_09_costos_powerquery.png`: `083B09FD90824E3DDFDB6D3283FE4CFA215C16D3DE0C85C7895C8CB7F448EC91`.
  - `s01_t05_10_costos_origen.png`: `FC1F748FE83BF46EEC98EF081754AE04840DA5673E9C39F037DFDB6818736815`.
- Límite histórico de esta captura: evidencia de CostosAlmacen solamente. Telemetria se completó después; ver la nota de cierre y la conciliación T06.

## Evidencia visual T05 · Telemetria

- Fecha de captura: 2026-10-21, aproximadamente 01:39–01:44 (UTC−04:00).
- Ventana capturada: `AndinaLog_03B` (Power BI Desktop, PID 13056), Power Query Editor, handle 2493880, 1888×1096 (maximizada). No se actuó sobre `AndinaLog_03B_Modelo_KPI`.
- Consulta: `Telemetria`, con tres pasos: `Origen`, `Encabezados` y `Tipado`.
- [s01_t05_11_telemetria_powerquery.png](screenshots/s01_t05_11_telemetria_powerquery.png): paso `Tipado`, 15 encabezados, `Columns: 15` y `Rows: 99+` (vista parcial). La fila 1 muestra `timestamp = 8/5/2025 1:47:11 AM`, `viaje_id = VIA-000001`, `order_id = ORD-0019394`, `camion_id = CAM-049`, `producto_id = PROD-0028`, `temperatura_cabina_c = 4.27`, `temp_unit = C`, `humedad_cabina_pct = 66.98`, `desviacion_termica_flag = 0` y `desviacion_proximos_60min_flag = 0`.
- [s01_t05_12_telemetria_columns.png](screenshots/s01_t05_12_telemetria_columns.png): continuación horizontal de la misma fila 1, con `temperatura_ambiente_c = 13.18`, `puerta_abierta_flag = 0`, `setpoint_c = 4`, `minutos_desde_despacho = 0` y `particion_modelo = TEST`. Entre ambas capturas se cubren los 15 encabezados.
- [s01_t05_13_telemetria_origen.png](screenshots/s01_t05_13_telemetria_origen.png): paso `Origen` seleccionado y fórmula `Csv.Document(File.Contents(RutaSilver & "andinalog_iot_telemetry_silver.csv"), [Delimiter=",", Columns=15, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; Applied Steps `Origen` → `Encabezados` → `Tipado`. El origen muestra `2025-08-05 01:47:11`, equivalente a `8/5/2025 1:47:11 AM` en `Tipado`.
- Tipos del paso `Tipado`: `timestamp` es `type datetime`; `viaje_id`, `order_id`, `camion_id`, `producto_id`, `temp_unit` y `particion_modelo` son `text`; `temperatura_cabina_c`, `humedad_cabina_pct`, `temperatura_ambiente_c` y `setpoint_c` son `type number`; `desviacion_termica_flag`, `desviacion_proximos_60min_flag`, `puerta_abierta_flag` y `minutos_desde_despacho` son `Int64.Type`.
- Complemento MCP en solo lectura: `COUNTROWS(Telemetria) = 191.710`; la primera lectura de `VIA-000001`, ordenada por `timestamp`, devuelve los mismos valores y tipos, con `minutos_desde_despacho = 0`. El total no se deduce del preview `Rows: 99+`.
- No se observó una anomalía regional en los decimales `4.27`, `66.98` y `13.18`; se leyeron con punto decimal.
- Huellas SHA-256:
  - `s01_t05_11_telemetria_powerquery.png`: `667B0EE22A3991CAAEAB859E6D374380E2C9C28559BEAFCB4DEE9E71642E4E05`.
  - `s01_t05_12_telemetria_columns.png`: `A0521239859941580E75C585A143D907BCA849FCDB4BC26EE6F7E1E2A811451C`.
  - `s01_t05_13_telemetria_origen.png`: `423667B5B4205152F8199789C5FDE31A5D90E1580C9C47B3EF11777CB89A312A`.
- Límite histórico: evidencia de Telemetria. Con las secciones anteriores quedan cubiertas las cinco tablas; T05 fue confirmada posteriormente y la conciliación se registra a continuación.

## Conciliación T06 — Desktop, controles e inventario

- Fecha: 2026-10-21. Alcance: T06 únicamente; sin modificar datos, modelo, PBIP, Excel ni requisitos.
- Las cinco tablas coinciden en archivo, filas y columnas entre Desktop, MCP, `csv_checks.json`, `preparation.md` y la hoja `S01 Inventario`.
- Productos y Flota muestran el total exacto en Desktop. Inventario, CostosAlmacen y Telemetria muestran `Rows: 99+`; el total exacto de 7.782, 144 y 191.710 se acredita por MCP y no se infiere del preview ni del CSV.
- Los decimales observados en Desktop (`23.73`, `34.05`, `47.11`, `32.9`, `37983.68`, `155267.38`, `4.27`, `66.98`, `13.18`) coinciden con los controles. Flota no contiene columnas decimales.
- Las fechas ISO del origen y las fechas con formato regional de la interfaz son el mismo valor. No se identificaron discrepancias materiales.
- El PBIP conservó `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE`; la copia Excel conservó `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`.
- Resultado: **P05 se mantiene conforme y T06 concilia 5/5 tablas con 0 discrepancias materiales**. No se inició T07 ni se declaró cerrado S01.

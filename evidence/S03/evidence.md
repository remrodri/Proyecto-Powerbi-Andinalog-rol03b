# Evidencia S03 · conexión, perfil y linaje Silver

Actualizado: 2026-10-28. Estado: **evidencia completa; S03 cerrado**.

## Alcance ejecutado

Se verificaron en modo de solo lectura el PBIP guardado y los cinco CSV completos. El perfil se calculó directamente sobre todos los registros con Python/pandas; es evidencia complementaria y **no sustituye** la comprobación exigida en Power BI Desktop de región, privacidad y selección de perfil completo.

El usuario indicó el 2026-10-28 que revisó la sesión Desktop y que el resultado estaba correcto. Esta confirmación humana se conserva, pero no aporta la captura exigida por SRC-103. Al intentar documentarla, Power BI Desktop ya no estaba abierto y los dos controladores visuales disponibles no pudieron inicializarse por un error local de ruta antes de interactuar con la aplicación. No se modificó el PBIP ni los CSV.

## PBIP guardado

- Cultura del modelo: `en-US`.
- Cultura de consultas: `en-US`.
- Parámetro requerido de texto: `RutaSilver = "C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\"`.
- Cinco tablas: `Productos`, `Flota`, `Inventario`, `CostosAlmacen`, `Telemetria`.
- Cada partición usa `File.Contents(RutaSilver & "archivo.csv")`.
- Relaciones: 0.
- Medidas: 0.
- Roles: 0.
- WMS: ausente.

Este estado en disco respalda estructura y parametrización, pero no acredita la configuración efectiva de privacidad ni la opción visual de perfil completo.

## Perfil completo de los CSV

| Fuente | Filas | Columnas | Vacíos | Filas duplicadas | Resultado relevante |
|---|---:|---:|---:|---:|---|
| Telemetria | 191.710 | 15 | 0 | 0 | 8.000 viajes, 100 camiones, 70 productos; 26 etiquetas no se reproducen con el límite estricto `>` |
| Productos | 120 | 7 | 0 | 0 | 120 productos; 70 están referenciados por Telemetria |
| Flota | 100 | 6 | 0 | 0 | 100 camiones; los 100 están referenciados por Telemetria; 6 centros base |
| Inventario | 7.782 | 12 | 0 | 0 | `fecha_salida` sin vacíos; las tres fechas contienen hora |
| CostosAlmacen | 144 | 5 | 0 | 0 | 6 centros × 24 meses; 0 duplicados de centro-periodo |

### Tipos y rangos observados

**Telemetria**

- Texto/fecha representada en CSV: `timestamp` (`2024-01-01 00:49:27` a `2025-12-31 13:31:20`).
- Texto: `viaje_id`, `order_id`, `camion_id`, `producto_id`, `temp_unit`, `particion_modelo`.
- Decimal: `temperatura_cabina_c` (-18,85 a 8,26), `humedad_cabina_pct` (44,45 a 95,66), `temperatura_ambiente_c` (1,42 a 35,26), `setpoint_c` (-18 a 4).
- Entero/indicador: `desviacion_termica_flag`, `desviacion_proximos_60min_flag`, `puerta_abierta_flag`, `minutos_desde_despacho` (0 a 870).
- `temp_unit` contiene únicamente `C`; las tres banderas contienen 0 y 1; `particion_modelo` contiene tres valores.

**Productos**

- Texto: `producto_id`, `nombre_producto`, `categoria_logistica`.
- Entero: `temperatura_conservacion_requerida_c` (-18 a 20), `tolerancia_temperatura_c` (2 a 6).
- Decimal: `costo_unitario_bob` (15,23 a 147,38), `precio_unitario_bob` (22,85 a 177,90).

**Flota**

- Texto: `camion_id`, `centro_distribucion_base`, `tipo_camion`.
- Entero: `capacidad_kg` (3.500 a 18.000), `antiguedad_anios` (1 a 15).
- Fecha representada en CSV: `fecha_ultimo_mantenimiento` (`2023-10-11` a `2025-11-27`).

**Inventario**

- Texto: `movimiento_id`, `lote_id`, `producto_id`, `centro_distribucion`.
- Fecha-hora representada en CSV: `fecha_ingreso`, `fecha_salida`, `fecha_vencimiento`.
- Entero: `cantidad_ingreso` (42 a 6.156), `cantidad_salida` (40 a 5.914), `cantidad_merma` (2 a 1.018), `dias_en_almacen` (3 a 74).
- Decimal: `costo_unitario_bob` (15,23 a 147,38).

**CostosAlmacen**

- Texto: `centro_distribucion`.
- Fecha/mes representado en CSV: `periodo_mes` (`2024-01-31` a `2025-12-31`).
- Decimal: `rotacion_stock_dias` (14,8 a 36,5), `perdida_mermas_bob` (29.673,27 a 532.674,16), `costo_almacenamiento_mensual_bob` (93.215,81 a 186.578,38).

Los rangos describen los datos observados; no constituyen por sí solos reglas empresariales de validez.

## Integridad de los Silver

| Archivo | SHA-256 vigente |
|---|---|
| `andinalog_iot_telemetry_silver.csv` | `A193F92A0C14EC95ED88DFC60125E530135F4E6E5C54A308AA53D5F076CF3BBE` |
| `andinalog_productos_silver.csv` | `E27824EB494ACE66AED9B9BBEDB82195B033A2FC6400EFF31FF1075E0DFEF28F` |
| `andinalog_flota_silver.csv` | `A30FF0BC0A0DED58B549AB03E8F196D187BCEE994C02FF749D1B492F13228307` |
| `andinalog_inventory_tracking_silver.csv` | `13EFBE4E2D7BB0EB60075E918600023FB1BAEAC9A930E5AF4D8CE2A2BF92A406` |
| `andinalog_warehouse_costs_silver.csv` | `D3D238E629D6C98E56D678AEF4B0D208A8E31C9CEFF1ECD91F5699AA5C192AC0` |

## Evidencia Desktop final

La sesión Desktop del 2026-10-28 demostró:

1. Región efectiva del archivo actual: **English (United States)**.
2. Power BI combina datos respetando el nivel configurado por fuente.
3. Las cinco fuentes fueron revisadas por el usuario con privacidad **Organizational**; `s03_privacy_level.png` conserva una fuente representativa y la lista de las cinco fuentes del archivo actual.
4. Power Query muestra seis consultas: cinco tablas y `RutaSilver`.
5. `Telemetria`, paso `Origen`, usa `File.Contents(RutaSilver & "andinalog_iot_telemetry_silver.csv")`.
6. El estado inferior muestra **Column profiling based on entire data set**, 15 columnas y perfil sin vacíos ni errores en las columnas visibles.

| Captura | SHA-256 | Acredita |
|---|---|---|
| `screenshots/s03_region_screen_1.png` | `D9FA343A71BDBF097D12E5EFDC904FD0BA8AE12FAF51B778244873DB02997A92` | Región del archivo |
| `screenshots/s03_privacy_level.png` | `9ED42934DA7FD14E5F042D6F9B4515746E3587A742665DE9F3E958A580C17064` | Cinco fuentes listadas y privacidad Organizational de la seleccionada; las restantes fueron revisadas por el usuario |
| `screenshots/s03_powerquery_profile.png` | `CF4D989262EB5496465351297C966974383612CE1ED2582480A0EA64ADB22223` | `RutaSilver`, `Origen`, fórmula y perfil sobre todo el conjunto |

## Libro de seguimiento

Se actualizó únicamente `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`:

- `S03 Linaje!B4,D4,F4`: Grupo 06, 03B y 2026-10-28.
- `S03 Linaje!A7:G11`: cinco fuentes oficiales; WMS ausente; conector, `RutaSilver`, privacidad Organizacional, filas, excepción y regla para S04.
- `Fichas KPI!F7:F11`: `Telemetria`, `Telemetria`, `Inventario`, `Inventario`, `Inventario`.
- Las cinco filas de linaje tienen ajuste de texto y altura local para evitar truncamiento.

Verificación del libro final:

- SHA-256: `B21D93E40DA8BC41AE6CE8511331E2E199953AA904F128C43E591A1EC91E7204`.
- 12 hojas en el mismo orden.
- 50 fórmulas, 11 validaciones de datos, 1 rango de formato condicional y 19 rangos combinados conservados.
- 0 diferencias de valor o estilo fuera de las celdas autorizadas.
- 0 errores de fórmula encontrados por el control disponible.
- Revisión visual: las cinco filas de linaje y las cinco tablas fuente de KPI se muestran legibles.

## Conciliación de alcance

- PBIP SHA-256: `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE`.
- El PBIP mantiene cinco tablas, `RutaSilver`, cultura `en-US`, 0 relaciones, 0 medidas, 0 roles y WMS ausente.
- Al abrir Desktop se generó `diagramLayout.json` con la posición visual de las cinco tablas. Es metadato de disposición, no añade relaciones, medidas, roles, consultas ni visuales de informe.
- Los cinco Silver conservan las huellas registradas en este documento.
- No se implementaron reglas de S04 ni se modificaron datos.
- `work/` está vacío.
- No se modificaron consultas ni datos durante la captura de evidencia.

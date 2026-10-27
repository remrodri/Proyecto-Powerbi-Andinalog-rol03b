# S01 · Evidencia MCP del modelo (T05)

- Fecha: 2026-10-21.
- Alcance: importación mínima de cinco fuentes, verificación de datos por MCP y comprobación en solo lectura del PBIP guardado.
- Límite: **esta evidencia no es por sí sola una captura de Power BI Desktop**. La cobertura visual de las cinco tablas consta en `desktop_checks.md`; T05 fue confirmada como completada por el usuario el 2026-10-21.
- Autorizaciones: el usuario autorizó crear `RutaSilver`, importar las cinco tablas, actualizarlas y verificar sus datos. Después guardó `powerbi/AndinaLog_03B.pbip`; esta ronda no reimportó datos.

## Herramientas y conexión

- Servidor: `powerbi-authoring-local` (`@microsoft/powerbi-modeling-mcp@1.0.0`).
- EULA aceptada por el usuario mediante `accept_eula` el 2026-10-21, URL `https://go.microsoft.com/fwlink/?LinkId=2381247`.
- Instancia: PID 33196, puerto 63146, `Untitled - Power BI Desktop`; conexión `PBIDesktop-Untitled - Power BI Desktop-63146`.
- Operaciones usadas: `CreateParameter`, `Get`, `table Create`, `RefreshWithXMLA`, `GetSchema`, `List`, `dax Execute`, `relationship List`, `measure List`.

## Parámetro

`RutaSilver` (M, tipo Texto, requerido):

```
"C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
```

## Tablas creadas

Todas en modo Import, una partición, con pasos M limitados a `Origen`, `Encabezados` y `Tipado`. Sin limpieza, relaciones, medidas, jerarquías ni visuales.

| Tabla | Archivo | Filas | Columnas CSV | Tipos |
| --- | --- | ---: | ---: | --- |
| Productos | andinalog_productos_silver.csv | 120 | 7 | 3 String, 2 Int64, 2 Double |
| Flota | andinalog_flota_silver.csv | 100 | 6 | 3 String, 2 Int64, 1 DateTime |
| Inventario | andinalog_inventory_tracking_silver.csv | 7.782 | 12 | 4 String, 3 DateTime, 4 Int64, 1 Double |
| CostosAlmacen | andinalog_warehouse_costs_silver.csv | 144 | 5 | 1 String, 1 DateTime, 3 Double |
| Telemetria | andinalog_iot_telemetry_silver.csv | 191.710 | 15 | 6 String, 1 DateTime, 3 Int64, 5 Double |

Cada tabla importada muestra además una columna interna oculta `RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61` (Int64, clave, no nula), generada por el motor. No pertenece al CSV y no se cuenta entre las columnas de origen.

## Consultas DAX y resultados

Ejecutadas con `dax_query_operations Execute` sobre el modelo abierto.

### Productos

```dax
EVALUATE ROW("Filas", COUNTROWS(Productos), "ColumnasConDatos", COUNTROWS(FILTER(Productos, NOT ISBLANK(Productos[producto_id]))), "Costo_PROD0001", CALCULATE(MIN(Productos[costo_unitario_bob]), Productos[producto_id] = "PROD-0001"), "Precio_PROD0001", CALCULATE(MIN(Productos[precio_unitario_bob]), Productos[producto_id] = "PROD-0001"), "CostoMin", MIN(Productos[costo_unitario_bob]), "CostoMax", MAX(Productos[costo_unitario_bob]))
```

Resultado: `120, 120, 23.73, 34.05, 15.23, 147.38`.

### Flota

```dax
EVALUATE ROW("Filas", COUNTROWS(Flota), "Centro", CALCULATE(MIN(Flota[centro_distribucion_base]), Flota[camion_id] = "CAM-001"), "Capacidad", CALCULATE(MIN(Flota[capacidad_kg]), Flota[camion_id] = "CAM-001"), "Tipo", CALCULATE(MIN(Flota[tipo_camion]), Flota[camion_id] = "CAM-001"), "Antiguedad", CALCULATE(MIN(Flota[antiguedad_anios]), Flota[camion_id] = "CAM-001"), "Fecha", CALCULATE(FORMAT(MIN(Flota[fecha_ultimo_mantenimiento]), "yyyy-MM-dd"), Flota[camion_id] = "CAM-001"))
```

Resultado: `100, Tarija, 8000, Refrigerado, 11, 2024-07-30`. Flota no contiene campos decimales.

### Inventario

```dax
EVALUATE ROW("Filas", COUNTROWS(Inventario), "Lote", CALCULATE(MIN(Inventario[lote_id]), Inventario[movimiento_id] = "MOV-0000001"), "Producto", CALCULATE(MIN(Inventario[producto_id]), Inventario[movimiento_id] = "MOV-0000001"), "Centro", CALCULATE(MIN(Inventario[centro_distribucion]), Inventario[movimiento_id] = "MOV-0000001"), "FechaIngreso", CALCULATE(FORMAT(MIN(Inventario[fecha_ingreso]), "yyyy-MM-dd HH:mm:ss"), Inventario[movimiento_id] = "MOV-0000001"), "FechaSalida", CALCULATE(FORMAT(MIN(Inventario[fecha_salida]), "yyyy-MM-dd HH:mm:ss"), Inventario[movimiento_id] = "MOV-0000001"), "FechaVencimiento", CALCULATE(FORMAT(MIN(Inventario[fecha_vencimiento]), "yyyy-MM-dd HH:mm:ss"), Inventario[movimiento_id] = "MOV-0000001"), "CantidadIngreso", CALCULATE(MIN(Inventario[cantidad_ingreso]), Inventario[movimiento_id] = "MOV-0000001"), "CantidadSalida", CALCULATE(MIN(Inventario[cantidad_salida]), Inventario[movimiento_id] = "MOV-0000001"), "CantidadMerma", CALCULATE(MIN(Inventario[cantidad_merma]), Inventario[movimiento_id] = "MOV-0000001"), "Dias", CALCULATE(MIN(Inventario[dias_en_almacen]), Inventario[movimiento_id] = "MOV-0000001"), "Costo", CALCULATE(MIN(Inventario[costo_unitario_bob]), Inventario[movimiento_id] = "MOV-0000001"))
```

Resultado: `7782, LOT-0000001, PROD-0034, La Paz, 2024-01-10 18:48:25, 2024-03-11 18:48:25, 2024-11-05 18:48:25, 679, 657, 22, 61, 47.11`.

### CostosAlmacen

```dax
EVALUATE ROW("Filas", COUNTROWS(CostosAlmacen), "Periodo", CALCULATE(FORMAT(MIN(CostosAlmacen[periodo_mes]), "yyyy-MM-dd"), CostosAlmacen[centro_distribucion] = "La Paz", CostosAlmacen[periodo_mes] = DATE(2024,1,31)), "Rotacion", CALCULATE(MIN(CostosAlmacen[rotacion_stock_dias]), CostosAlmacen[centro_distribucion] = "La Paz", CostosAlmacen[periodo_mes] = DATE(2024,1,31)), "Perdida", CALCULATE(MIN(CostosAlmacen[perdida_mermas_bob]), CostosAlmacen[centro_distribucion] = "La Paz", CostosAlmacen[periodo_mes] = DATE(2024,1,31)), "Costo", CALCULATE(MIN(CostosAlmacen[costo_almacenamiento_mensual_bob]), CostosAlmacen[centro_distribucion] = "La Paz", CostosAlmacen[periodo_mes] = DATE(2024,1,31)))
```

Resultado: `144, 2024-01-31, 32.9, 37983.68, 155267.38`.

### Telemetria

```dax
EVALUATE ROW("Filas", COUNTROWS(Telemetria), "FilasFiltro", CALCULATE(COUNTROWS(Telemetria), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Timestamp", CALCULATE(FORMAT(MIN(Telemetria[timestamp]), "yyyy-MM-dd HH:mm:ss"), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Order", CALCULATE(MIN(Telemetria[order_id]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Camion", CALCULATE(MIN(Telemetria[camion_id]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Producto", CALCULATE(MIN(Telemetria[producto_id]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "TempCabina", CALCULATE(MIN(Telemetria[temperatura_cabina_c]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Unidad", CALCULATE(MIN(Telemetria[temp_unit]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Humedad", CALCULATE(MIN(Telemetria[humedad_cabina_pct]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "FlagTermica", CALCULATE(MIN(Telemetria[desviacion_termica_flag]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Flag60", CALCULATE(MIN(Telemetria[desviacion_proximos_60min_flag]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "TempAmbiente", CALCULATE(MIN(Telemetria[temperatura_ambiente_c]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Puerta", CALCULATE(MIN(Telemetria[puerta_abierta_flag]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Setpoint", CALCULATE(MIN(Telemetria[setpoint_c]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Minutos", CALCULATE(MIN(Telemetria[minutos_desde_despacho]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)), "Particion", CALCULATE(MIN(Telemetria[particion_modelo]), Telemetria[viaje_id] = "VIA-000001", Telemetria[timestamp] = DATE(2025,8,5) + TIME(1,47,11)))
```

Resultado: `191710, 1, 2025-08-05 01:47:11, ORD-0019394, CAM-049, PROD-0028, 4.27, C, 66.98, 0, 0, 13.18, 0, 4, 0, TEST`.

## Verificación del PBIP (solo lectura)

Ruta: `powerbi/AndinaLog_03B.pbip`. Estructura: `.pbip`, `AndinaLog_03B.SemanticModel/definition/` y `AndinaLog_03B.Report/`. Formato de modelo TMDL.

- Tablas declaradas en `model.tmdl`: Productos, Flota, Inventario, CostosAlmacen, Telemetria (5).
- Columnas por TMDL: 7, 6, 12, 5 y 15, coincidentes con el CSV.
- Particiones: una por tabla, `mode: import`, con origen M que usa `RutaSilver`.
- `RutaSilver`: presente en `expressions.tmdl` con barra final y metadatos de parámetro.
- Rutas absolutas en las particiones: 0. Cada tabla referencia `RutaSilver` una vez.
- Relaciones: 0. No existe `relationships.tmdl` ni declaraciones `relationship` en el modelo.
- Medidas: 0. No hay declaraciones `measure` en ningún TMDL.
- Roles: 0. No hay declaraciones `role`.
- Informe: una página (`Page 1`) sin visuales; no hay contenedores de visual.
- No se reimportaron datos en esta verificación.

### Huellas SHA-256 del estado T05 (histórico)

Estas son las huellas registradas en T05. Las de `model.tmdl`, `expressions.tmdl` y `cache.abf` fueron superadas por un guardado posterior de Desktop; se conservan aquí como historial y se explican en la actualización T09 del final.

| Archivo | Bytes | SHA-256 |
| --- | ---: | --- |
| AndinaLog_03B.pbip | 292 | F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE |
| SemanticModel/definition.pbism | 170 | 73A1AE4C89D7488F553788ADC772A04C805D1C9E0D7333E2B2B5476AAD8E5A5F |
| Report/definition.pbir | 247 | CABED7524818F95B84DFE6D24D1BE773553D549CBAF074FA456629F54102015A |
| SemanticModel/.pbi/cache.abf | 3.707.867 | 2A1CD843E8766997DB4E85229FAC2E1315AB8A6D2568FA086948ED8BF2544AEE |
| definition/model.tmdl | 450 | 1CD2432BC56E40EC825F566D880BB77F0528206B2935A8673BEDABB979123E22 |
| definition/expressions.tmdl | 259 | 8C2EE5F7842E029A634A10D0AD007507C5F8E188A6034B8293C43B93E77096C5 |
| tables/Productos.tmdl | 1.726 | B3A144D0E1312F15F072018DD518A2BC2E855347CC68A92AE6C79BABA0F38071 |
| tables/Flota.tmdl | 1.461 | 5CA4DC18B079071D0277D8295A920B357B7C80580F3B768BCB18D647EDF7F3F5 |
| tables/Inventario.tmdl | 2.433 | 9893BCA1EA98DE5F8550543BC6E4F1F5E2B8AD754F21BD26EC8D033DE1985070 |
| tables/CostosAlmacen.tmdl | 1.377 | 8A9E75A85BF4F1F9806833C5137A9CFB9951A595762459044F629C58DDD728FE |
| tables/Telemetria.tmdl | 2.971 | C550CC0D87304654703296B9D7D32172B313047449E8C6FBCDC61F892A51D27E |

## Estado

- Modelo mínimo creado y guardado; cinco tablas verificadas por MCP.
- T05 **completada y confirmada**: la evidencia visual de las cinco tablas está en `desktop_checks.md`; esta fuente aporta los totales exactos de Inventario, CostosAlmacen y Telemetria, cuyos previews muestran `Rows: 99+`.
- T06 concilió Desktop, T02, T03 y T04 para las cinco fuentes con 0 discrepancias materiales.
- No se modificaron datos, modelo, PBIP, Excel ni la spec durante T06; T07 no se inició.


## Actualización T09 — 2026-10-22

Alcance: A-S01-001 únicamente. Se investigó la diferencia de huellas antes de actualizarlas. La comprobación fue de solo lectura; no se modificaron el modelo, los datos, el PBIP ni los TMDL. La tabla T05 se conserva como historial.

### Por qué cambiaron los archivos

- Todos los archivos del modelo semántico tienen la misma marca de tiempo, `2026-10-21 15:20:42`, posterior a la evidencia MCP de T05 (`03:08`) y a la conciliación T06 (`03:10`). El conjunto es consistente con un guardado posterior de Desktop, no con ediciones manuales aisladas.
- `model.tmdl`: la única diferencia es la anotación `PBI_QueryOrder = ["Productos","Flota","Inventario","CostosAlmacen","Telemetria","RutaSilver"]` y su línea en blanco. Al retirarla en memoria, el resultado mide 450 bytes y su SHA-256 es `1CD2432BC56E40EC825F566D880BB77F0528206B2935A8673BEDABB979123E22`, idéntico al registrado en T05. No hay otra diferencia.
- `expressions.tmdl`: la única diferencia es la anotación `PBI_ResultType = Text` y su línea en blanco. Al retirarla en memoria, el resultado mide 259 bytes y su SHA-256 es `8C2EE5F7842E029A634A10D0AD007507C5F8E188A6034B8293C43B93E77096C5`, idéntico al registrado en T05. El `lineageTag` ya estaba presente.
- `cache.abf`: es un respaldo local comprimido con XPress9 (cabecera `This backup was created using XPress9 compression.`), no un archivo de definición. No existe una copia anterior para comparar su contenido; el cambio de 3.707.867 a 3.708.561 bytes (+694) coincide con el guardado. No se usa como prueba de la semántica ni de los datos. Se registra como estado local volátil.
- `database.tmdl` (`compatibilityLevel: 1606`) y `cultures/en-US.tmdl` (`cultureInfo en-US`) no estaban en la tabla T05. Se incorporan al manifiesto actual; no contienen tablas, relaciones ni medidas.

### Comprobación del estado actual (solo lectura)

- `model.tmdl` declara exactamente cinco tablas: Productos, Flota, Inventario, CostosAlmacen y Telemetria.
- `expressions.tmdl` conserva `RutaSilver` con la ruta y la barra final.
- Relaciones: 0. No existe `relationships.tmdl` ni declaraciones `relationship`.
- Medidas: 0. No hay declaraciones `measure`.
- Roles: 0. No hay declaraciones `role`.
- Cinco TMDL de tabla, una partición `mode: import` por tabla y ninguna ruta absoluta en las particiones; columnas 7/6/12/5/15.
- No se reimportaron datos ni se modificó el modelo durante T09.

### Huellas actuales de los archivos persistidos

| Archivo | Bytes | SHA-256 | Categoría |
| --- | ---: | --- | --- |
| AndinaLog_03B.pbip | 292 | F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE | Contenedor |
| SemanticModel/definition.pbism | 170 | 73A1AE4C89D7488F553788ADC772A04C805D1C9E0D7333E2B2B5476AAD8E5A5F | Definición |
| Report/definition.pbir | 247 | CABED7524818F95B84DFE6D24D1BE773553D549CBAF074FA456629F54102015A | Definición del informe |
| definition/model.tmdl | 558 | C6EC473306801181A9C54187E8F9163A1EACE9E0F60AAF72F9D66739BCA8C6D1 | Definición |
| definition/expressions.tmdl | 296 | 9F3EFEC4AFA0ADB71B99FCF36DF540C7E2E6A0EE847A6A495C77FC112983228A | Definición |
| definition/database.tmdl | 39 | 822C914B643BCA32BB20ABD8A762DF8204A1B9EF02ACC2BC7348727F6699CB96 | Definición |
| definition/cultures/en-US.tmdl | 21 | 1109E38EBC2A662C6AC3926717B17F040C1EE6812D0A3DE88D781CDFAC626D19 | Cultura |
| definition/tables/Productos.tmdl | 1.726 | B3A144D0E1312F15F072018DD518A2BC2E855347CC68A92AE6C79BABA0F38071 | Definición |
| definition/tables/Flota.tmdl | 1.461 | 5CA4DC18B079071D0277D8295A920B357B7C80580F3B768BCB18D647EDF7F3F5 | Definición |
| definition/tables/Inventario.tmdl | 2.433 | 9893BCA1EA98DE5F8550543BC6E4F1F5E2B8AD754F21BD26EC8D033DE1985070 | Definición |
| definition/tables/CostosAlmacen.tmdl | 1.377 | 8A9E75A85BF4F1F9806833C5137A9CFB9951A595762459044F629C58DDD728FE | Definición |
| definition/tables/Telemetria.tmdl | 2.971 | C550CC0D87304654703296B9D7D32172B313047449E8C6FBCDC61F892A51D27E | Definición |
| SemanticModel/.pbi/cache.abf | 3.708.561 | 4EFBDF6D4829CCBD49807871AD8BE98F96727B56D2E9755E50A9E3E476038AE3 | Estado local volátil |

### Conclusión T09

- La diferencia de `model.tmdl` y `expressions.tmdl` queda explicada y reproducida: son anotaciones de herramienta, no cambios de tablas, consultas, relaciones ni medidas.
- El modelo conserva cinco tablas, `RutaSilver` y cero relaciones, medidas y roles. El caché local no se usa como definición ni como prueba de datos.
- A-S01-001 queda **corregido, pendiente de verificación**. No se ejecutó la ronda 02 ni se declaró cerrado S01.

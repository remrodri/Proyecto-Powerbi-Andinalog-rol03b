# AndinaLog 03B · Proyecto Power BI

Proyecto académico del Grupo 06 para apoyar a la Jefatura de Operaciones en la priorización semanal de controles de cadena de frío y revisión de lotes y centros.

## Estado

- S01: cerrado con sus limitaciones documentadas.
- S02: Build completado; auditoría requiere corregir la presentación de `S02 Mapa Silver!D10` y revalidar las huellas Silver. No está cerrado.
- S03–S11: no iniciados.
- Power BI: proyecto PBIP con `RutaSilver`, cinco tablas importadas, sin relaciones, medidas, roles ni visuales.

El estado operativo y el siguiente paso están en `MEMORY.md`.

## Estructura mínima

```text
docs/                 contexto, constitución, decisiones, fuentes y prompts
references/           guías y plantillas originales; no se modifican
specs/NNN-.../         spec.md, plan.md, tasks.md y un único AUDIT.md
powerbi/               único proyecto PBIP
deliverables/          archivos editables y entregables finales
evidence/SNN/          un evidence.md; capturas solo cuando son indispensables
validation/
  checks/              solo controles reutilizables
  results/SNN/         un validation.json consolidado
work/                  temporales ignorados y eliminados al terminar
```

No se guardan dependencias descargadas, copias de prueba, renders intermedios, informes por microtarea ni múltiples resultados que prueben lo mismo.

## Fuentes oficiales 03B

Los CSV permanecen fuera del repositorio en `C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\` y se consumen mediante `RutaSilver`.

| Archivo | Filas | Grano |
| --- | ---: | --- |
| `andinalog_iot_telemetry_silver.csv` | 191.710 | Lectura de viaje cada 30 minutos |
| `andinalog_productos_silver.csv` | 120 | Producto |
| `andinalog_flota_silver.csv` | 100 | Camión |
| `andinalog_inventory_tracking_silver.csv` | 7.782 | Lote con ingreso, salida y merma |
| `andinalog_warehouse_costs_silver.csv` | 144 | Centro y mes |

WMS es una fuente de contraste, no una sexta tabla del modelo 03B.

## Flujo

`Specify → Plan → Build → Audit → Fix → Audit → Close`

Cada fase necesita autorización independiente. El trabajo se agrupa por resultado, no por operación interna. Una tarea actualiza como máximo el entregable afectado, el registro único de evidencia y el resultado consolidado de validación.

Antes de trabajar, leer `AGENTS.md`, `MEMORY.md`, `docs/constitution.md`, la spec activa y únicamente las fuentes necesarias. Usar la skill local `andinalog-sdd-workflow`.

## Siguiente paso

Autorizar la fase Fix de S02 para resolver `A-S02-001`; después ejecutar una nueva ronda de auditoría. No iniciar S03 antes del cierre explícito de S02.

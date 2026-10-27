# Memoria del proyecto AndinaLog 03B

## Estado actual

- Última actualización: 22 de octubre de 2026.
- Fase: T01–T10 completadas. T08 ronda 01 **requiere correcciones**, T09 corrección y ronda 02 **conforme al alcance auditado**; A-S01-001 cerrado. El usuario aprobó el cierre de S01 el 2026-10-22 con limitaciones documentadas. S02 no iniciado.
- Hito/spec de referencia: [specs/001-s01-inventory/spec.md](specs/001-s01-inventory/spec.md), S01, versión 0.4, aprobada y cerrada con limitaciones; las dudas abiertas quedan trasladadas y no hay spec S02 aprobada.
- Alcance autorizado actual: T01–T10 completadas; S01 cerrado con las limitaciones documentadas el 2026-10-22; A-S01-001 cerrado. Los pendientes trasladados a S02, S08 y S11 no se declaran resueltos. S02 no iniciado.
- Implementación Power BI: PBIP `powerbi/AndinaLog_03B.pbip` con `RutaSilver`, cinco tablas, 0 relaciones, 0 medidas y sin visuales. Ronda 02 verificó 13/13 huellas, la reconstrucción exacta de los TMDL históricos y el estado semántico; `cache.abf` es estado local volátil, no definición. T09 no modificó modelo ni datos.
- Próximo paso: esperar autorización separada para S02; no iniciarlo automáticamente. La semántica de `centro_distribucion`, la selección final de KPI y los demás pendientes trasladados siguen abiertos.

## Cómo mantener esta memoria

Leer al iniciar una sesión. Actualizar después de cada avance significativo autorizado, conservando el historial y manteniendo este estado inicial al día.

Cada entrada debe resumir fecha, tarea/hito, trabajo realizado, verificaciones, decisiones y pendientes. Enlazar los documentos o evidencias de detalle; no duplicar informes ni registrar secretos. Distinguir propuestas de decisiones aprobadas y pruebas ejecutadas de resultados esperados.

## Ubicaciones y documentos

- Repositorio elegido: `C:/Users/remrodri/Github/Proyecto-Powerbi-Andinalog-rol03b/`.
- Se verificaron AGENTS.md, README.md, MEMORY.md, los cinco documentos de docs/ y las referencias locales. Se creó `specs/001-s01-inventory/spec.md`; no existe aún proyecto Power BI.
- Silver originales: `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/`.
- Contexto: [docs/context.md](docs/context.md).
- Principios: [docs/constitution.md](docs/constitution.md).
- Instrucciones operativas: [AGENTS.md](AGENTS.md).
- Entrada del proyecto: [README.md](README.md).
- Decisiones y fuentes: `docs/decisions.md` y `docs/sources.md`.

Los enlaces describen la estructura acordada. Si un archivo todavía no existe o no puede leerse, no asumir su contenido.

## Acuerdos de trabajo

- El usuario organiza las carpetas y solicita cada documento; no crear otros archivos ni avanzar de etapa por iniciativa propia.
- El contenido inicial se define con el usuario en esta conversación; las specs se desarrollarán progresivamente en OpenCode.
- Una carpeta por hito en specs/, con spec.md, plan.md, tasks.md y un único AUDIT.md.
- Ciclo: Spec aprobada → Plan → Build → Auditoría → Correcciones → Nueva auditoría → Cierre.
- AUDIT.md conserva todas las rondas y los hallazgos con identificadores estables. La auditoría no modifica los artefactos que revisa.
- MEMORY.md resume avances; tasks.md registra tareas; AUDIT.md conserva revisiones; decisions.md explica decisiones relevantes.
- Mantener Silver y referencias originales intactos y un único proyecto Power BI de trabajo.
- No declarar pruebas Desktop, publicación o resultados predictivos que no se hayan ejecutado.

## Base de conocimiento comprobada

Se revisaron el mandato 03B, mapa y guía técnica, referencia KPI, guías S01–S11, complemento visual S08 y plantillas de seguimiento, arquitectura, diccionario, informe y presentación. También se analizaron las plantillas y el ejemplo SDD proporcionados por el usuario.

Se leyeron completos los cinco Silver y se realizaron controles independientes:

| Tabla | Filas | Columnas |
| --- | ---: | ---: |
| Telemetría | 191.710 | 15 |
| Productos | 120 | 7 |
| Flota | 100 | 6 |
| Inventario | 7.782 | 12 |
| Costos de almacén | 144 | 5 |

No se encontraron nulos en la lectura realizada. La auditoría oficial sí documenta duplicados y valores centinela resueltos en Silver: flota 101→100, inventario 7.805→7.782, telemetría 192.285→191.710, productos 121→120 y costos 144→144. T02 reprodujo los conteos y las claves con 0 celdas vacías, 0 desbalances de inventario y cinco registros DATA-006 oficiales; WMS quedó en 30.000×16 y se contrastó sin importarlo. Esto no equivale a auditoría exhaustiva ni a validación en Desktop.

Controles globales reproducidos: 8.000 viajes; viajes con desviación 14,3625 %; lecturas con desviación 6,1395 %; 1.069 lotes salidos vencidos; merma por cantidades 7,3573 %. La merma valorizada concilia entre inventario y costos: Bs 35.574.924,68.

S10 prescribe umbral térmico 0,3–0,8 °C en pasos de 0,1, predeterminado 0,5. Se reprodujeron precisión y cobertura de las tres pruebas docentes. Los detalles y las fórmulas de referencia están en el contexto.

## Pendientes principales

1. S01 cerrado con limitaciones documentadas el 2026-10-22; T01–T10 completadas. La selección final de KPI, la semántica de `centro_distribucion` y los demás pendientes trasladados siguen abiertos en S02/S08/S11 y no se declaran resueltos. S02 no se inició.
2. .gitignore y los documentos iniciales están presentes. No se ha inicializado Git en esta colaboración. C4 quedó respaldado por DEC-026 mediante la lista complementaria de SRC-208 y la aprobación del usuario; la brecha A y el puntaje 1 siguen sujetos a auditoría y validación docente.
3. Obtener rúbrica v4, posibles guías S12–S13 y lista completa de comisionamiento. La auditoría Bronze–Silver ya está registrada como DATA-006.
4. Usuario, decisión, frecuencia y KPI candidatos definidos en DEC-016 y DEC-017; faltan selección final de KPI en S02, metas y umbrales en S08 y responsables empresariales en S11. El componente DCAM aplicable quedó resuelto como C4 en DEC-026.
5. Merma por cantidades acordada como candidata; falta decidir la medida económica por valor y su impacto.
6. T02 reprodujo 26 lecturas en límites térmicos (0,0136 %), 26 viajes y 0 viajes dependientes solo de ellas, además de 14 viajes/órdenes con 339 lecturas en dos particiones y 43 positivas. Falta definir su tratamiento e interpretación en S02 y el horizonte futuro incompleto al final del viaje.
7. Precisar relación temporal de costos y significado del centro base del camión en filtros y RLS.
8. Definir alcance predictivo y criterio operativo del What-if; no se ha entrenado ni integrado un modelo en esta colaboración.
9. T01 verificó Python 3.14.6, bibliotecas, PowerShell y Desktop Store 2.159.883.0. El MCP está instalado y conectado; el modelo mínimo y la evidencia visual por tabla fueron verificados. La revisión visual del Excel se cubrió con PDF exportados desde Excel; `soffice` continúa sin detectarse, pero no bloquea T06.
10. EV-S01-WMS quedó guardado como `evidence/S01/wms_contrast.md` en T02 y sus menciones se actualizaron en spec, `docs/sources.md` y DEC-019 sin cambiar requisitos. La copia de plantilla se completó en T04 (`deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`) y se verificó visualmente. T05 quedó confirmada con evidencia de archivo, filas, columnas, decimales y Flota sin campos decimales (DEC-023). T06 concilió 5/5 fuentes y 5/5 KPI con 0 discrepancias materiales; Inventario, CostosAlmacen y Telemetria usan `Rows: 99+` en el preview y totales exactos por MCP.
11. Rodrigo Tucuman, integrante del Grupo 06, quedó designado para compartir pantalla en S02 (DEC-027); su designación fue verificada en T08, pero la pantalla aún no se ha compartido.

## Historial resumido

### 2026-10-20 · Contexto y datos

- Se analizaron fuentes docentes de AndinaLog 03B y los cinco CSV completos.
- Se generó y actualizó el Markdown de contexto hasta versión 2, incorporando S01–S11 y paquete final.
- Se distinguieron referencias docentes, resultados calculados, propuestas y pendientes.
- No se modificaron Silver ni plantillas; no se ejecutaron pruebas en Power BI Desktop o Service.

### 2026-10-20 · Organización SDD

- Se acordó adaptar Spec First y Spec Anchored a los hitos Power BI.
- Se definieron estructura, ciclo iterativo de Build/auditoría y registro único de auditorías por spec.
- Se acordó avanzar paso a paso, con el usuario a cargo de crear carpetas y solicitar documentos.

### 2026-10-20 · Documentos iniciales

- AGENTS.md: contenido completo entregado en el chat; su ubicación en el repositorio no se verificó.
- constitution.md: archivo descargable entregado, destinado a docs/constitution.md; revisión y aprobación explícita pendientes de confirmar.
- README.md: archivo descargable entregado, destinado a la raíz.
- MEMORY.md: documento inicial preparado con acuerdos, controles realizados y pendientes.
- No se crearon specs, planes de implementación, tareas ni auditorías de hitos. No se construyó el .pbip ni se completaron entregables académicos.


### 2026-10-20 · Revisión del repositorio y referencias

- Se comprobó la base documental y la presencia de las guías S01–S11, referencias generales, prompts, ejemplo SDD y plantillas finales.
- Se actualizaron rutas documentales a references/, nombres ingleses y estado actual. Las rutas Silver externas se conservaron.
- El PDF DCAM de S01 sustituye al Excel del taller; el PDF de diseño S08 está presente. La plantilla general del Proyecto Integrador sigue activa.
- La lista C1–C8 queda identificada como información histórica pendiente de respaldo en una fuente activa.
- Se preservaron documentos docentes y datos; no se iniciaron specs, implementación ni pruebas Desktop. No se creó .gitignore.


### 2026-10-20 · Exclusiones de control de versiones

- Se creó .gitignore para work/, cachés locales de Power BI, entornos y cachés de herramientas, archivos de entorno y bloqueos de Office.
- No se excluyen definiciones PBIP/TMDL, referencias, evidencias ni entregables.
- No se inicializó Git, no se realizaron commits y no se iniciaron specs ni implementación.



### 2026-10-20 · Skill local del flujo SDD

- Se creó .opencode/skills/andinalog-sdd-workflow/SKILL.md y cuatro plantillas para spec, plan, tareas y auditoría.
- Se enlazó desde AGENTS.md y docs/prompts.md pasó a ser guía de invocación para evitar procedimientos duplicados.
- La skill distingue fases, autorizaciones y evidencia automática/Desktop; no inicia fases consecutivas por sí sola.
- La carga efectiva y el comportamiento con un modelo en OpenCode quedan pendientes de prueba. No se redactó S01 ni se construyó Power BI.

### 2026-10-20 · Spec S01 aprobada y guardada

- Se guardó `specs/001-s01-inventory/spec.md` versión 0.3 con decisión, fuentes, KPI candidatos, brecha DCAM tentativa y límites de S01.
- Se registraron DEC-016 a DEC-020 y se actualizaron los pendientes de decisión; se registraron DATA-006 y DATA-007 en fuentes, sin duplicar IDs.
- Se aclaró que WMS es solo contraste, que EV-S01-WMS no tenía archivo guardado en ese momento y que la evidencia Desktop sigue pendiente.
- No se creó plan ni tareas, no se completaron plantillas, no se abrió Power BI y no se ejecutó Build.

### 2026-10-20 · Rectificación de la spec S01

- Se restauró la numeración y el contenido de la v0.2: RF-S01-09 copia de plantilla, RF-S01-10 delimitación de implementación y RF-S01-11 procedencia Bronze–Silver.
- El inventario principal conserva exactamente las cinco fuentes oficiales; WMS quedó separado como contraste. Se corrigieron merma por cantidades, denominadores contextuales y días promedio en almacén.
- Se separó la aprobación de la spec del cumplimiento de S01 y se mantuvo la persona de pantalla como condición de cierre.
- Se corrigió DEC-017 y se añadió DEC-021. No se creó plan ni tareas, no se completaron plantillas y no se ejecutó Power BI.


### 2026-10-20 · Planificación de S01

- A petición del usuario se completaron plan.md y tasks.md en specs/001-s01-inventory/ con once RF, nueve RNF, seis CA y condiciones de cierre trazados.
- Ambos documentos quedan preparados para revisión, no marcados aprobados. Diez tareas sin ejecutar; no se inició Build ni auditoría.
- Se separaron controles CSV, copia Excel, inspección Desktop, dependencias humanas y cierre. El caso flota sin decimales se explicita para revisar el criterio antes de ejecutar.
- Spec preservada; sin cambios en datos, referencias, plantillas ni .pbip. El entorno de ejecución de OpenCode y Desktop debe verificarse en T01.

### 2026-10-20 · Ajuste aprobado de requisitos S01

- Se actualizó `specs/001-s01-inventory/spec.md` a v0.4: el cierre exige identificar y respaldar el componente DCAM aplicable, no evaluar C1–C8 ni reconstruir documentación reservada; en Desktop se verifican decimales solo en tablas con campos decimales y, en flota, enteros y fechas sin campos decimales, sin omitir archivo, filas y columnas.
- Se registraron DEC-022 y DEC-023; se alinearon `plan.md` a v0.2 y `tasks.md` a la spec v0.4, y se actualizaron los pendientes y el historial. Se conservaron las demás condiciones.
- No se ejecutaron tareas de Build, no se completaron plantillas, no se abrió Power BI y no se modificaron datos ni referencias.

### 2026-10-20 · Aprobación del plan y ejecución de T01

- Se corrigió solo la frase de autorización de la cabecera de la spec: la aprobación habilita la planificación, no el Build. Se aprobaron `plan.md` v0.2 y las tareas alineadas; se registró DEC-024.
- T01 verificó 10 fuentes/referencias, registró tamaños y SHA-256, y comprobó una relectura 10/10 sin cambios. Python 3.14.6, `csv`/`json`/`hashlib`, `openpyxl` y `pandas` están disponibles; Desktop Store 2.159.883.0 está instalado y no se abrió.
- Evidencia: `validation/results/S01/source_manifest.json` y `evidence/S01/desktop_checks.md`. No se importaron tablas, no se completaron plantillas y no se ejecutó T02.

### 2026-10-20 · Build T02: inventario, procedencia y contraste WMS

- Se creó y ejecutó `validation/checks/s01_inventory.py`; resultado en `validation/results/S01/csv_checks.json`, con detalle en `evidence/S01/provenance.md` y `evidence/S01/wms_contrast.md`.
- P01, P02 y P06 conformes; 0 discrepancias materiales. Las cinco fuentes oficiales conservaron 191.710×15, 120×7, 100×6, 7.782×12 y 144×5; claves únicas, 0 celdas vacías y 0 desbalances de inventario.
- DATA-006: 33 registros; cinco oficiales con `filas_silver` y `columnas_silver` coincidentes; el registro WMS se conserva aparte y no se cuenta entre los cinco.
- WMS: 30.000×16; cobertura 8.000 de 8.000 órdenes de telemetría; 22.000 WMS sin telemetría; 8.000/8.000 centros base, 30.000/30.000 lotes, 30.000/30.000 chofer-mes y 30.000/30.000 zona-cliente. No se importó WMS.
- Se documentaron 14 viajes/órdenes con dos particiones (339 lecturas y 43 positivas), 26 lecturas límite (0,0136 %, 26 viajes, 0 dependientes) y 70 productos refrigerados/congelados.
- No se abrió Power BI, no se importaron tablas, no se completó la plantilla y no se ejecutó T03.

### 2026-10-20 · Build T03: preparación S01

- Se creó `evidence/S01/preparation.md` con decisión, cinco fuentes oficiales, observaciones clasificadas, cinco KPI candidatos, medida de apoyo y brecha DCAM tentativa. P03 conforme con pendientes declarados.
- La DCAM conserva la brecha A (`centro_distribucion` sin definición explícita), dimensión Evidencia, puntaje 1 tentativo y confianza baja. T03 propuso inicialmente C4 — Conocimiento de los datos del negocio, sin respaldo.
- Se actualizaron las menciones de EV-S01-WMS en spec, `docs/sources.md` y DEC-019: el archivo existe como `evidence/S01/wms_contrast.md`; la auditoría sigue pendiente y no cambiaron requisitos.
- Siguen pendientes el respaldo del componente DCAM, la persona que compartirá pantalla y las pruebas Desktop. No se completó el Excel y no se ejecutó T04.

### 2026-10-20 · Revisión de la asignación DCAM

- Se revisó C4: provenía de la lista histórica C1–C8 referida por la guía S01 y `docs/context.md`; SRC-202 no enumera esa lista y ninguna decisión autorizó la asignación. DEC-018 fija la brecha A y DEC-022 exige respaldar el componente, pero no asigna C4.
- Se sustituyó por «componente pendiente de identificación y respaldo» en `evidence/S01/preparation.md`, conservando el historial. Se mantienen dimensión Evidencia, puntaje 1 tentativo y confianza baja.
- P03 no acredita cierre DCAM; RF-S01-07 y CA-S01-03 siguen pendientes. No se ejecutó T04.

### 2026-10-20 · Build T04: copia de la plantilla

- Se creó `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` desde la plantilla, sin modificar el original. SHA-256 original `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30`; copia `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`.
- S01 Inventario: identificación `Grupo 06` / `03B` / `2026-10-20` y cinco fuentes DATA-001–DATA-005 en A7:G11. Fichas KPI: identificación y cinco nombres/decisiones en A7:B11; campos de ejemplo limpiados; S02–S11 vacíos.
- Se conservaron 50 fórmulas, validaciones, formato condicional, celdas combinadas y las hojas futuras. P04 pasa con 0 diferencias fuera del rango autorizado; Excel 16.0 abrió, calculó y exportó sin reparación.
- Revisión visual mediante PDF: S01 muestra las cinco filas sin recorte y Fichas muestra los cinco KPI/decisiones. La plantilla conserva paginación de 2 páginas en S01 (segunda con filas vacías) y 8 en Fichas por su ancho; no se modificaron áreas de impresión. Evidencia en `evidence/S01/template_mapping.md`, `t04_s01_inventory.pdf` y `t04_fichas_kpi.pdf`.
- No se asignó componente DCAM, no se inventaron responsables, no se abrió Power BI y no se avanzó a T05.

### 2026-10-21 · T05 parcial: modelo mínimo y PBIP

- Con autorización del usuario se aceptó la EULA del MCP `powerbi-authoring-local` y se conectó a la instancia de Desktop PID 33196 (puerto 63146).
- Se creó `RutaSilver` con barra final y se importaron, con solo `Origen`/`Encabezados`/`Tipado`, las cinco fuentes: Productos 120×7, Flota 100×6, Inventario 7.782×12, CostosAlmacen 144×5 y Telemetria 191.710×15. Sin limpieza, relaciones, medidas ni visuales.
- La verificación por consultas DAX reprodujo filas, columnas y valores representativos, incluidos importes y fechas. Se confirmaron 0 relaciones y 0 medidas.
- El usuario guardó `powerbi/AndinaLog_03B.pbip`. La comprobación en solo lectura confirmó cinco tablas TMDL, `RutaSilver`, particiones Import, ausencia de relaciones/medidas/roles, una página sin visuales y 0 rutas absolutas en las particiones.
- Evidencia MCP y de estructura: `evidence/S01/mcp_model_checks.md`; referencia añadida en `desktop_checks.md`. No se reimportaron datos.
- T05 sigue en curso y no se marcó completa: falta la evidencia visual auténtica de Desktop por tabla.


### 2026-10-21 · MCP Power BI a nivel de proyecto

- Se añadió opencode.json en la raíz con powerbi-authoring-local, paquete oficial @microsoft/powerbi-modeling-mcp fijado a 1.0.0, transporte local stdio mediante npx.cmd y timeout 60 s.
- No se cambió configuración global ni se aceptó automáticamente la EULA. El arranque y la conexión al modelo son comprobaciones separadas; no equivalen a T05 completada.
- No se abrió ni modificó Power BI durante la creación de configuración. La prueba de conexión de solo lectura se realizará cuando haya una instancia/modelo disponible y la licencia haya sido revisada y aceptada por el usuario.

- Verificación de arranque: opencode mcp list informó powerbi-authoring-local connected (1 servidor). Esto demuestra conexión cliente-servidor MCP, no conexión a un modelo ni aceptación de EULA.

### 2026-10-21 · T05: evidencia visual de Productos

- Se identificó que la ventana `Power Query Editor` visible pertenecía a otro proyecto (`AndinaLog_03B_Modelo_KPI`, PID 17644), no al PBIP. Se abrió Power Query en la ventana correcta `AndinaLog_03B` (PID 13056, handle 2493880) mediante UI Automation.
- Se capturaron tres imágenes reales de la ventana con `PrintWindow`/`PW_RENDERFULLCONTENT`, sin modificar datos ni modelo y sin guardar el PBIP: el paso `Tipado` mostró 7 encabezados, `Columns: 7` y `Rows: 120`; el paso `Origen` mostró `RutaSilver & "andinalog_productos_silver.csv"`; la primera fila mostró `PROD-0001` con `costo_unitario_bob = 23.73` y `precio_unitario_bob = 34.05`.
- Evidencia en `evidence/S01/screenshots/` y detalle con hashes en `evidence/S01/desktop_checks.md`. T05 sigue en curso: faltan Flota, Inventario, CostosAlmacen y Telemetria. No se reimportaron datos.

### 2026-10-21 · T05: evidencia visual de Flota

- Autorizado únicamente Flota, se seleccionó la consulta en la ventana correcta `AndinaLog_03B` (PID 13056, handle 2493880), sin actuar sobre `AndinaLog_03B_Modelo_KPI` ni modificar datos o modelo.
- Capturas: 6 encabezados, `Columns: 6`, `Rows: 100`, `camion_id` con 100 distintos/únicos; `CAM-001` con `capacidad_kg = 8000`, `antiguedad_anios = 11` y `fecha_ultimo_mantenimiento = 7/30/2024` (formato regional de la interfaz). El paso `Origen` muestra `RutaSilver & "andinalog_flota_silver.csv"`, `Columns=6`, y la fecha `2024-07-30`.
- No hay columnas decimales: `camion_id`/`centro_distribucion_base`/`tipo_camion` son `text`; `capacidad_kg` y `antiguedad_anios` son `Int64.Type`; `fecha_ultimo_mantenimiento` es `type date`; 0 `Decimal.Type`.
- Evidencia en `evidence/S01/screenshots/s01_t05_04_flota_powerquery.png` (SHA-256 `1CEEFC3294F1A856949E8AEC150919079EA02EA76A1049B11A8EB1884369535C`) y `s01_t05_05_flota_origen.png` (`7C2D85AACCD52D8E2A9DEAA761806789B001D49B07DEF6AD7A173BAE7500785F`), documentada en `desktop_checks.md`. T05 sigue en curso: faltan Inventario, CostosAlmacen y Telemetria.

### 2026-10-21 · T05: evidencia visual de Inventario

- Autorizado únicamente Inventario, se trabajó en la ventana correcta `AndinaLog_03B` (PID 13056, handle 2493880), maximizada a 1888×1096, sin actuar sobre `AndinaLog_03B_Modelo_KPI` ni modificar datos o modelo.
- El paso `Tipado` mostró 12 encabezados, `Columns: 12` y `Rows: 99+` (vista parcial). La fila 1: `MOV-0000001`, `LOT-0000001`, `PROD-0034`, `La Paz`, `cantidad_ingreso = 679`, `cantidad_salida = 657`, `cantidad_merma = 22`, `dias_en_almacen = 61` y `costo_unitario_bob = 47.11` con punto decimal.
- El paso `Origen` mostró `Csv.Document(File.Contents(RutaSilver & "andinalog_inventory_tracking_silver.csv"), [Delimiter=",", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`. Las fechas `2024-01-10`, `2024-03-11` y `2024-11-05` coinciden con `1/10/2024`, `3/11/2024` y `11/5/2024` de `Tipado`; solo cambia el formato de la interfaz.
- El complemento MCP en solo lectura confirmó `COUNTROWS(Inventario) = 7.782` y los mismos valores/tipos de la primera fila; el total no se deduce del preview.
- Evidencia: `s01_t05_07_inventario_powerquery.png` (SHA-256 `6B894CFAB506F600612E512B7D468528B9444A91C6DFC2B4FFFBDF015F5D3090`) y `s01_t05_08_inventario_origen.png` (`CFD4F996FDE34F62F9C941B539F684B715509BAC39C7C0187A5DDE1EF54D062E`), documentada en `desktop_checks.md`. T05 sigue en curso: faltan CostosAlmacen y Telemetria.

### 2026-10-21 · T05: evidencia visual de CostosAlmacen

- Autorizado únicamente CostosAlmacen, se trabajó en la ventana correcta `AndinaLog_03B` (PID 13056, handle 2493880), maximizada a 1888×1096, sin actuar sobre `AndinaLog_03B_Modelo_KPI` ni modificar datos o modelo.
- El paso `Tipado` mostró 5 encabezados, `Columns: 5` y `Rows: 99+` (vista parcial); 6 centros y 24 periodos distintos. La fila 1: `La Paz`, `rotacion_stock_dias = 32.9`, `perdida_mermas_bob = 37983.68`, `periodo_mes = 1/31/2024` y `costo_almacenamiento_mensual_bob = 155267.38`.
- El paso `Origen` mostró `Csv.Document(File.Contents(RutaSilver & "andinalog_warehouse_costs_silver.csv"), [Delimiter=",", Columns=5, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; la fecha `2024-01-31` coincide con `1/31/2024` de `Tipado`.
- El complemento MCP en solo lectura confirmó `COUNTROWS(CostosAlmacen) = 144` y los mismos valores/tipos para La Paz de enero de 2024; el total no se deduce del preview.
- Evidencia: `s01_t05_09_costos_powerquery.png` (SHA-256 `083B09FD90824E3DDFDB6D3283FE4CFA215C16D3DE0C85C7895C8CB7F448EC91`) y `s01_t05_10_costos_origen.png` (`FC1F748FE83BF46EEC98EF081754AE04840DA5673E9C39F037DFDB6818736815`), documentada en `desktop_checks.md`. T05 sigue en curso: falta Telemetria.

### 2026-10-21 · T05: evidencia visual de Telemetria

- Autorizado únicamente Telemetria, se trabajó en la ventana correcta `AndinaLog_03B` (PID 13056, handle 2493880), maximizada a 1888×1096, sin actuar sobre `AndinaLog_03B_Modelo_KPI` ni modificar datos o modelo.
- El paso `Tipado` mostró 15 encabezados, `Columns: 15` y `Rows: 99+` (vista parcial). La fila 1: `timestamp = 8/5/2025 1:47:11 AM`, `VIA-000001`, `ORD-0019394`, `CAM-049`, `PROD-0028`, `temperatura_cabina_c = 4.27`, `humedad_cabina_pct = 66.98`, `temperatura_ambiente_c = 13.18`, `setpoint_c = 4`, `minutos_desde_despacho = 0` y `particion_modelo = TEST`.
- El paso `Origen` mostró `Csv.Document(File.Contents(RutaSilver & "andinalog_iot_telemetry_silver.csv"), [Delimiter=",", Columns=15, Encoding=65001, QuoteStyle=QuoteStyle.Csv])`; la fecha `2025-08-05 01:47:11` coincide con `8/5/2025 1:47:11 AM` de `Tipado`.
- El complemento MCP en solo lectura confirmó `COUNTROWS(Telemetria) = 191.710` y los mismos valores/tipos para la primera lectura de `VIA-000001`; el total no se deduce del preview.
- Evidencia: `s01_t05_11_telemetria_powerquery.png` (SHA-256 `667B0EE22A3991CAAEAB859E6D374380E2C9C28559BEAFCB4DEE9E71642E4E05`), `s01_t05_12_telemetria_columns.png` (`A0521239859941580E75C585A143D907BCA849FCDB4BC26EE6F7E1E2A811451C`) y `s01_t05_13_telemetria_origen.png` (`423667B5B4205152F8199789C5FDE31A5D90E1580C9C47B3EF11777CB89A312A`), documentadas en `desktop_checks.md`.
- Con esta captura quedaron cubiertas las cinco tablas; en ese momento T05 seguía pendiente de evaluación y T06 no se había iniciado. La confirmación se registra en la sección siguiente.

### 2026-10-21 · T05 completada y confirmada

- El usuario confirmó T05 con la evidencia de las cinco tablas; se marcó `[x]` en `tasks.md`.
- Cobertura: Productos 120×7, Flota 100×6, Inventario 7.782×12, CostosAlmacen 144×5 y Telemetria 191.710×15; archivo, columnas, decimales y Flota sin campos decimales documentados.
- En Inventario, CostosAlmacen y Telemetria el preview de Desktop muestra `Rows: 99+`; los totales exactos se acreditan por MCP y no se infieren del CSV. No se reimportaron datos ni se modificó el PBIP.
- Evidencia: `evidence/S01/desktop_checks.md`, `mcp_model_checks.md` y capturas `s01_t05_01`–`s01_t05_13`.

### 2026-10-21 · Build T06: conciliación después de Desktop

- Se ejecutó solo T06, con lectura de `desktop_checks.md`, `mcp_model_checks.md`, `csv_checks.json`, `preparation.md`, `template_mapping.md` y la copia Excel.
- Conciliación: 5/5 fuentes con archivo, filas, columnas, grano, clave, brecha y responsable coherentes; 5/5 nombres de KPI y decisiones coincidentes; 0 diferencias de contenido y 0 discrepancias materiales. Los valores de KPI no se recalcularon en T06.
- Diferencias de representación documentadas: `191.710` frente a `191710`, fechas ISO frente al formato regional de Desktop, `Rows: 99+` en tres tablas, columna interna `RowNumber` del motor y reserialización del Excel. Ninguna altera el dato.
- Huellas sin cambios: copia Excel `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`; plantilla `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30`; PBIP `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE`.
- Evidencia: `preparation.md` sección 9, `template_mapping.md` sección 7 y `desktop_checks.md` sección final. No se modificaron datos ni requisitos; T07 no se inició y S01 sigue abierto.

### 2026-10-21 · T07 parcial: traspaso documental a S02

- Se ejecutó únicamente la parte documental autorizada de T07 y se creó `evidence/S01/s02_handoff.md` con decisión, inventario, cinco KPI candidatos, evidencias T02–T06, límites y pendientes.
- Se revisaron las referencias locales: SRC-202 indica 8 componentes/34 capacidades/101 subcapacidades, pero no enumera C1–C8; SRC-101 remite a la plantilla del taller, ausente en `references/`, y solo da ejemplos C3/C5; la copia y la plantilla del proyecto no contienen la lista ni un mapeo de la brecha. No se localizó respaldo suficiente.
- El componente DCAM aplicable se mantiene como **pendiente de identificación y respaldo**; no se reintrodujo C4 por inferencia. El usuario indicó **Grupo 06** para compartir pantalla; el criterio de T07 exige persona concreta, por lo que la designación grupal queda registrada sin completar la tarea. No se modificaron datos, modelo, PBIP, Excel, spec ni requisitos.
- T07 permanece `[ ]`; solo se añadió su registro de ejecución parcial. No se inició auditoría ni se declaró cerrado S01.

### 2026-10-21 · T07 completada: C4 y designación de pantalla

- El usuario aprobó **C4 · Conocimiento de los datos del negocio** para la brecha A, dimensión Evidencia, puntaje 1 tentativo y confianza baja; y designó a **Rodrigo Tucuman, integrante del Grupo 06**, para compartir pantalla en S02.
- Se consultó `Instrucciones!B10` de SRC-208 como referencia complementaria (SHA-256 `D6FE317D30241BA3705A7B18F4D1B28CA5B55A187E9AEDBF2B6B9E7A1A294686`), sin editar ni completar el Excel. El PDF SRC-202 sigue siendo la referencia metodológica.
- Se registraron DEC-026/027 y se actualizaron `decisions.md`, `sources.md`, `context.md`, `spec.md`, `tasks.md`, `s02_handoff.md` y `preparation.md`. Tras verificar P07 (C4 respaldado y persona identificada), T07 queda `[x]`.
- El hecho se limita a las fuentes revisadas y no afirma ausencia empresarial. No se inició T08 ni se declaró cerrado S01.

### 2026-10-22 · Auditoría T08 ronda 01

- Se ejecutó la auditoría independiente de S01 y se creó [AUDIT.md](specs/001-s01-inventory/AUDIT.md) con alcance, matriz RF/RNF/CA, condiciones de cierre, hallazgo e historial.
- Resultado: 24 de 26 requisitos/criterios pasan; RNF-S01-01 y RNF-S01-07 quedan en falla parcial por el mismo hallazgo. La condición DCAM/pantalla pasa; el cierre sigue pendiente. No se abrió Desktop ni se modificó el modelo.
- Verificaciones: 10/10 huellas del manifiesto, 7/7 CSV, 12 capturas, original `0CCC4A53...D2DF30`, copia `E7F09B0A...DB74F1`, SRC-208 `D6FE317D...A294686` y `.pbip` `F8712089...8A1CCE`. Se reprodujeron conteos, claves, KPI, WMS y particiones; Excel con 74 cambios permitidos y 50 fórmulas conservadas.
- Hallazgo A-S01-001: `mcp_model_checks.md` registra 450/259/3.707.867 bytes para `model.tmdl`, `expressions.tmdl` y `cache.abf`; los actuales son 558/296/3.708.561. Los TMDL de tabla y el `.pbip` sí coinciden. El cambio observable es metadata-only y no añade tablas, relaciones, medidas, roles ni visuales, pero la evidencia no acredita de forma reproducible el estado actual. Queda abierto.
- Observaciones no bloqueantes: no existe `s01_t05_06` y `DUD-S01-07` sigue abierta pese a la verificación Desktop registrada; ninguna afecta los CA.
- T08 no se marcó en `tasks.md` porque el archivo es parte del alcance auditado y la instrucción fue no modificarlo. S01 no se declara cerrado y no se inició S02.


### 2026-10-22 · T09 corrección de A-S01-001

- Se ejecutó T09 únicamente para A-S01-001, en solo lectura sobre el modelo. No se modificaron modelo, datos, PBIP ni TMDL; no se ejecutó la ronda 02.
- Investigación: los archivos del modelo semántico comparten la marca `2026-10-21 15:20:42`, posterior a T05/T06. En `model.tmdl`, la única diferencia es la anotación `PBI_QueryOrder` y su línea en blanco; al retirarla en memoria se reproducen 450 bytes y el hash histórico `1CD2432B...123E22`. En `expressions.tmdl`, la única diferencia es `PBI_ResultType = Text` y su línea en blanco; al retirarla se reproducen 259 bytes y `8C2EE5F7...77096C5`.
- `cache.abf` es un respaldo local XPress9, no una definición. No hay copia anterior para comparar su contenido; el cambio de 3.707.867 a 3.708.561 bytes coincide con el guardado y se registra como estado local volátil, sin usarse como prueba de datos o semántica.
- Estado actual comprobado: cinco tablas, `RutaSilver` con barra final, 0 relaciones, 0 medidas, 0 roles, una partición Import por tabla y ninguna ruta absoluta en particiones.
- Evidencia actualizada en [mcp_model_checks.md](evidence/S01/mcp_model_checks.md): se conserva la tabla T05 como historial y se añade el manifiesto actual con `database.tmdl`, `cultures/en-US.tmdl` y el caché local. [AUDIT.md](specs/001-s01-inventory/AUDIT.md) registra A-S01-001 como **corregido, pendiente de verificación**.
- T09 no se marca en `tasks.md` porque su condición de cierre exige nueva evidencia de auditoría. S01 no se declara cerrado y no se inició S02.

### 2026-10-22 - Auditoría T08 ronda 02

- Se ejecutó la ronda 02 sobre A-S01-001 y la evidencia T09, en solo lectura. Se verificaron las 13 huellas del manifiesto actual; todas coinciden. Se reconstruyeron en memoria los TMDL históricos: retirar `PBI_QueryOrder` reproduce 450 bytes y `1CD2432B...123E22`; retirar `PBI_ResultType` reproduce 259 bytes y `8C2EE5F7...77096C5`. Los TMDL de tabla, `.pbip`, `definition.pbism` y `definition.pbir` conservan sus huellas.
- Estado verificado: cinco tablas, `RutaSilver` con barra final, 0 relaciones, 0 medidas, 0 roles y una partición Import por tabla. `cache.abf` se observa como estado local variable y no se usa como prueba semántica. La copia Excel conserva `E7F09B0A...DB74F1` y el original `0CCC4A53...D2DF30`.
- Resultado: A-S01-001 cerrado; 26/26 requisitos/criterios pasan. La condición de cierre sigue pendiente porque T10 y la aprobación no se ejecutaron; S01 no se declara cerrado. No hay hallazgos nuevos. Persisten las observaciones no bloqueantes sobre `s01_t05_06` y DUD-S01-07.
- No se modificaron modelo, datos, PBIP, TMDL, entregables, spec ni `tasks.md`. No se abrió Desktop ni se ejecutaron operaciones MCP. [AUDIT.md](specs/001-s01-inventory/AUDIT.md) conserva la ronda 01 y añade la ronda 02.

### 2026-10-22 - T10 propuesta de cierre de S01

- Se presentó en [AUDIT.md](specs/001-s01-inventory/AUDIT.md) la propuesta de cierre: entregable Excel de seguimiento, artefactos de evidencia y modelo mínimo; 26/26 requisitos/criterios pasan, con seis resultados `Pasa con limitación` documentados.
- Se resumieron las auditorías: ronda 01 (24/26, A-S01-001 abierto), corrección T09 y ronda 02 (26/26, A-S01-001 cerrado, sin hallazgos nuevos). Se conservó la limitación histórica `03:08` y la prueba por reconstrucción exacta de hashes.
- Pendientes trasladados, no incumplimientos S01: selección final de KPI y semántica/filtros/RLS de `centro_distribucion` en S02; tratamiento de límites térmicos, particiones, WMS y merma por valor; metas/umbrales en S08; responsables y RLS en S11; modelo relacional y visuales en hitos posteriores.
- No hay requisitos S01 incumplidos. La aprobación de cierre era una condición de gobernanza pendiente. No se marcó S01 cerrado, no se actualizó spec ni `tasks.md` y no se inició S02.

### 2026-10-22 - Cierre de S01 aprobado

- El usuario aprobó el cierre de S01 con las limitaciones documentadas y las precisiones de RF-S01-06, RF-S01-07, RF-S01-09, CA-S01-03, CA-S01-04 y CA-S01-06.
- Se completaron T08, T09 y T10; se actualizaron `spec.md`, `tasks.md`, `AUDIT.md`, `MEMORY.md` y las notas de estado de `plan.md` y `docs/context.md`. Se conservaron las rondas, el hallazgo cerrado, la limitación histórica `03:08` y las observaciones no bloqueantes.
- Los pendientes de S02, S08 y S11 siguen abiertos y no se declaran resueltos. No se modificaron modelo, datos, PBIP, TMDL ni entregables. S02 no se inició.

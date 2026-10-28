# Plan S03 · conexión, perfil y linaje Silver

**Spec aprobada:** `specs/003-s03-lineage/spec.md`, versión 0.1.  
**Estado del plan:** Aprobado por el usuario el 2026-10-27.  
**Build:** No iniciado.

## Resultado

El PBIP conservará las cinco fuentes oficiales conectadas mediante `RutaSilver`, con región y privacidad comprobadas en Desktop y perfil ejecutado sobre todo el conjunto. El libro de seguimiento contendrá cinco filas de linaje y las tablas fuente de los cinco KPI. Las excepciones se documentarán para S04 sin corregir datos en S03.

## Implementación mínima

1. Verificar en Power BI Desktop la configuración y el perfil completo de las cinco fuentes, conservando el modelo sin relaciones, medidas, roles, visuales ni WMS.
2. Completar en el libro de seguimiento `S03 Linaje` y la columna `Tabla(s) fuente (S03)` de los cinco KPI.
3. Consolidar la evidencia y validación de S03, conciliar PBIP, Excel, Silver y spec, y dejar el alcance listo para auditoría.

## Herramientas y responsabilidades

| Acción | Herramienta | Alcance |
|---|---|---|
| Región, privacidad y perfil completo | Power BI Desktop | Evidencia principal obligatoria |
| Parámetro, consultas, tablas, filas y ausencia de objetos fuera de alcance | Power BI Desktop y MCP local de Power BI | MCP complementa, pero no sustituye evidencia visual |
| Actualización del libro | Excel o edición controlada del XLSX | Solo `S03 Linaje`, `Fichas KPI!F7:F11` y encabezado necesario |
| Validación estructural del XLSX | `openpyxl` | Fórmulas, hojas y celdas fuera de alcance intactas |
| Integridad de Silver y entregables | SHA-256 y controles de solo lectura | Reutilizar referencias existentes; no crear otro manifiesto |
| Revisión visual del XLSX | Excel | Solo si el contenido modificado no puede validarse suficientemente desde el archivo |

## Correspondencia

| Resultado | Requisitos | Artefacto | Verificación |
|---|---|---|---|
| Región, `RutaSilver` y cinco conexiones verificadas | RF-S03-01 a RF-S03-03; RNF-S03-01 a RNF-S03-04; CA-S03-01 a CA-S03-03 y CA-S03-08 | `powerbi/AndinaLog_03B.pbip` | Evidencia Desktop; cinco consultas, rutas, actualización y ausencia de WMS |
| Privacidad y perfil completo | RF-S03-04 y RF-S03-05; CA-S03-04, CA-S03-05 y CA-S03-09 | PBIP y `evidence/S03/evidence.md` | Nivel efectivo por fuente; perfil completo; filas, tipos, vacíos, errores y excepciones |
| Linaje de cinco fuentes | RF-S03-06; CA-S03-06 | `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` | Cinco filas oficiales; WMS ausente; regla propuesta para S04 por fuente |
| Tablas fuente de cinco KPI | RF-S03-07; CA-S03-07 | Mismo XLSX | `Fichas KPI!F7:F11` completo y coherente con las fórmulas aprobadas |
| Integridad y alcance | RNF-S03-02, RNF-S03-03 y RNF-S03-05; CA-S03-08 y CA-S03-09 | `validation/results/S03/validation.json` | Silver intactos; cero relaciones, medidas, roles y visuales nuevos; sin correcciones de S04 |
| Trazabilidad final | Todos | `evidence/S03/evidence.md` y `validation/results/S03/validation.json` | Correspondencia completa entre spec, PBIP, Excel y evidencia |

## Secuencia de Build

### 1. Verificación y perfil en Desktop

- Confirmar que el PBIP correcto esté abierto.
- Comprobar región del archivo actual.
- Comprobar `RutaSilver`, incluida la barra final.
- Confirmar que las cinco consultas usan `File.Contents(RutaSilver & ...)`.
- Comprobar el nivel de privacidad efectivo de cada fuente.
- Si no existe una configuración previa respaldada, aplicar `Organizacional` y documentar la justificación.
- Activar el perfil basado en todo el conjunto.
- Actualizar las cinco fuentes.
- Documentar filas, tipos, vacíos, errores y excepciones.
- Confirmar que WMS no esté cargada.
- Conservar el PBIP sin relaciones, medidas, roles y visuales.

No se aplicarán reglas de limpieza ni se modificarán etiquetas, fechas o archivos Silver.

### 2. Actualización del libro

- Completar identificación de S03 si corresponde.
- Sustituir la fila gris de ejemplo de `S03 Linaje`.
- Escribir exactamente cinco filas, DATA-001 a DATA-005.
- Registrar conector `Texto/CSV`, `RutaSilver`, privacidad efectiva, filas, excepción y regla propuesta para S04.
- Completar `Fichas KPI!F7:F11` con `Telemetria`, `Telemetria`, `Inventario`, `Inventario`, `Inventario`.
- Preservar fórmulas, validaciones, formatos y hojas de otros hitos.

### 3. Conciliación

- Confirmar que los cinco Silver conservan sus huellas de referencia.
- Confirmar que el PBIP tiene cinco tablas oficiales y ningún objeto fuera de alcance.
- Confirmar que Excel contiene cinco fuentes y cinco KPI.
- Revisar visualmente solo las áreas modificadas del libro.
- Consolidar resultados en los dos registros únicos de S03.
- Vaciar `work/` al terminar.

## Evidencia mínima

Conservar únicamente capturas que acrediten información no reconstruible desde los entregables:

1. Región efectiva.
2. Parámetro `RutaSilver` y paso `Origen`.
3. Privacidad efectiva.
4. Perfil configurado sobre todo el conjunto y resultados relevantes.

Una captura puede cubrir varios requisitos. No se conservan capturas repetidas por tabla cuando los datos puedan acreditarse mediante PBIP, MCP o el libro.

## Archivos permitidos

- PBIP y sus carpetas de proyecto.
- Libro de seguimiento.
- `evidence/S03/evidence.md`.
- `validation/results/S03/validation.json`.
- Capturas indispensables bajo `evidence/S03/screenshots/`.
- Documentos SDD, `MEMORY.md` y `docs/decisions.md`.

No se crearán informes, manifiestos, resultados ni archivos de autorización por tarea.

## Límites

- WMS permanece fuera del modelo y del linaje oficial.
- No se corrigen excepciones.
- No se crean relaciones, calendario, medidas, roles ni visuales.
- No se inventan sistemas de origen, propietarios o frecuencias de actualización.
- El MCP no acredita por sí solo región, privacidad ni selección del perfil completo.
- La privacidad Organizacional es la propuesta aprobada; el nivel efectivo se registra antes de cualquier cambio.
- Las reglas de S04 se documentan, pero no se implementan.

## Gates

`Build → Audit → Fix → Audit → Close`

Cada fase requiere autorización independiente. Una autorización de Build no autoriza auditoría, correcciones o cierre.

## Aprobación

- 2026-10-27: el usuario aprobó este plan y sus seis tareas.
- La aprobación del plan no autoriza Build.

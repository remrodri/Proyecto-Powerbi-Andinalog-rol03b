# Auditoría S03 · conexión, perfil y linaje Silver

## Estado actual

Ronda: 02. Fecha: 2026-10-28. Versión auditada: spec v0.1, PBIP `F8712089…8A1CCE`, XLSX `B21D93E…1E7204`.

**Veredicto: conforme al alcance; S03 cerrado.**

Alcance: siete RF, cinco RNF y nueve CA. Se auditaron PBIP, cinco CSV completos, libro de seguimiento, evidencia y validación. No se modificaron los objetos auditados durante esta ronda.

Resultado vigente: **21 de 21 requisitos y criterios pasan**. `A-S03-001` está cerrado.

## Matriz vigente de aceptación

| Requisito/criterio | Prueba y contexto | Resultado | Evidencia | Hallazgo |
|---|---|---|---|---|
| RF-S03-01 | Región English (United States) visible en Desktop | Pasa | `s03_region_screen_1.png` | Ninguno |
| RF-S03-02 | Parámetro requerido, texto, ruta y barra final en TMDL | Pasa | PBIP y `validation.json` | Ninguno |
| RF-S03-03 | Cinco particiones usan `RutaSilver`; WMS ausente | Pasa | PBIP | Ninguno |
| RF-S03-04 | Cinco fuentes revisadas como Organizational; captura representativa y confirmación directa del usuario | Pasa | `s03_privacy_level.png` y `evidence.md` | Ninguno |
| RF-S03-05 | Perfil completo de CSV y Power Query basado en todo el conjunto | Pasa | `s03_powerquery_profile.png`, `evidence.md` y `validation.json` | Ninguno |
| RF-S03-06 | Cinco filas oficiales completas, WMS ausente | Pasa | `S03 Linaje!A7:G11` | Ninguno |
| RF-S03-07 | Cinco tablas fuente completas | Pasa | `Fichas KPI!F7:F11` | Ninguno |
| RNF-S03-01 | Un parámetro alimenta las cinco consultas | Pasa | PBIP | Ninguno |
| RNF-S03-02 | Cinco huellas Silver verificadas | Pasa | `evidence.md` | Ninguno |
| RNF-S03-03 | 0 relaciones, medidas y roles; sin WMS ni tratamiento S04 | Pasa | PBIP y libro | Ninguno |
| RNF-S03-04 | Tres capturas Desktop con huellas y perfil completo reproducible | Pasa | `evidence/S03/screenshots/` | Ninguno |
| RNF-S03-05 | Un `evidence.md`, un `validation.json`, un `AUDIT.md`; sin informes por tarea | Pasa | Estructura del repositorio | Ninguno |
| CA-S03-01 | Parámetro y cinco rutas correctos | Pasa | PBIP | Ninguno |
| CA-S03-02 | Cinco fuentes presentes; actualización confirmada por usuario; WMS ausente | Pasa con limitación | PBIP y confirmación registrada | Ninguno |
| CA-S03-03 | Región compatible documentada en Desktop | Pasa | `s03_region_screen_1.png` | Ninguno |
| CA-S03-04 | Privacidad Organizational registrada y comprobada | Pasa | `s03_privacy_level.png` y confirmación en `evidence.md` | Ninguno |
| CA-S03-05 | Conteos, tipos, vacíos, excepciones y perfil completo demostrados | Pasa | `s03_powerquery_profile.png`, perfil CSV y `validation.json` | Ninguno |
| CA-S03-06 | Cinco filas y cinco reglas S04 | Pasa | XLSX | Ninguno |
| CA-S03-07 | Cinco KPI con tabla fuente | Pasa | XLSX | Ninguno |
| CA-S03-08 | Silver intactos; sin objetos o WMS fuera de alcance; `diagramLayout.json` solo posiciona las cinco tablas | Pasa | Huellas y PBIP | Ninguno |
| CA-S03-09 | Excepciones documentadas, no corregidas | Pasa | XLSX y PBIP | Ninguno |

## Registro acumulado de hallazgos

| ID estable | Requisito | Evidencia e impacto | Corrección necesaria | Estado | Verificación de cierre |
|---|---|---|---|---|---|
| A-S03-001 | RF-S03-01, RF-S03-04, RF-S03-05, RNF-S03-04, CA-S03-03 a CA-S03-05 | Ronda 01 carecía de evidencia Desktop reproducible. | Conservar región, privacidad y Power Query con perfil completo. | Cerrado | Ronda 02: tres capturas con SHA-256; 21/21 pasan |

## Historial de rondas

### Ronda 01 — 2026-10-28

- Se verificaron PBIP, cinco Silver completos, libro, evidencia y validación.
- El libro pasa revisión estructural y visual; no presenta diferencias fuera del alcance autorizado.
- La falta de captura Desktop se distingue de una falla del modelo o de los datos.
- Hallazgo nuevo: `A-S03-001`.
- Veredicto: requiere corrección. T05 y T06 no pueden completarse sin la evidencia Desktop.

### Ronda 02 — 2026-10-28

- Se verificó región English (United States), privacidad Organizational y Power Query con `RutaSilver`, paso `Origen`, fórmula parametrizada y perfil basado en todo el conjunto.
- El usuario revisó las cinco fuentes y confirmó Organizational; la captura representativa muestra una fuente y la lista completa.
- Las tres capturas tienen huellas SHA-256 registradas en `evidence.md` y `validation.json`.
- `A-S03-001` queda cerrado; no se modificaron consultas, modelo ni datos durante la corrección.
- Resultado: 21/21 pasan, sin hallazgos abiertos. S03 se cierra por la autorización explícita previa del usuario para completar todas las tareas pendientes.

# Plan S02 · arquitectura y mapa Silver

Versión 0.2 · aprobado. Build ejecutado; auditoría requiere corrección.

## Resultado

Entregar un PPTX editable, su PDF y la actualización del libro de seguimiento con la decisión, arquitectura, mapa de cinco fuentes, cinco KPI tácticos y pendientes documentados, sin modificar el modelo Power BI.

## Implementación mínima

1. Preparar el contenido desde la spec y las fuentes docentes.
2. Completar el PPTX y exportar el PDF excluyendo la diapositiva de ejemplo.
3. Completar `S02 Mapa Silver` y `Fichas KPI` en la copia del libro.
4. Verificar contenido, integridad y legibilidad de los tres entregables.
5. Consolidar la evidencia y auditar contra los 30 requisitos/criterios.

## Correspondencia

| Resultado | Requisitos principales | Artefacto |
| --- | --- | --- |
| Decisión y arquitectura | RF-01/02/04/05; CA-01/02/04/05 | PPTX y PDF |
| Mapa Silver | RF-03; CA-03 | PPTX, PDF y hoja `S02 Mapa Silver` |
| KPI tácticos | RF-06/07; CA-06/07 | hoja `Fichas KPI` |
| Integridad de plantilla | RF-08; CA-08 | XLSX de seguimiento |
| Entrega editable/PDF | RF-09; CA-09 | PPTX y PDF |
| Ejecución y pendientes | RF-10/11; CA-10 | `evidence/S02/evidence.md` |
| No funcionales | RNF-01–09 | entregables, evidencia y auditoría |

## Verificación mínima

- Leer el contenido de XLSX, PPTX y PDF y contrastarlo con la spec.
- Comprobar visualmente únicamente las páginas/hojas finales afectadas.
- Confirmar que WMS no figura como sexta fuente, que existen cinco KPI tácticos y que no se inventaron origen o propietarios.
- Confirmar que la plantilla original, PBIP y fuentes no cambiaron.
- Registrar el resultado consolidado en `validation/results/S02/validation.json` y el detalle necesario en `evidence/S02/evidence.md`.

No se conservan copias temporales, renders repetidos, resultados por operación ni informes por tarea.

## Gates

- Build: entregables creados y verificados.
- Audit: un único `AUDIT.md`, sin modificar lo auditado.
- Fix: solo hallazgos autorizados.
- Close: 30/30 demostrados, sin hallazgos bloqueantes y con aprobación explícita.

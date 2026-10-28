# Tareas S02

## Build

- [x] T01 · Preparar el contenido aprobado de decisión, arquitectura, cinco fuentes, cinco KPI y pendientes.
  - Hecho cuando: coincide con la spec y no inventa origen, propietario ni validación empresarial.
- [x] T02 · Crear el PPTX editable y el PDF entregable.
  - Hecho cuando: el diagrama y mapa son legibles, el editable conserva la plantilla y el PDF excluye el ejemplo.
- [x] T03 · Actualizar el libro de seguimiento.
  - Hecho cuando: `S02 Mapa Silver` contiene cinco filas y `Fichas KPI` cinco KPI tácticos; fórmulas y hojas futuras se conservan.
- [x] T04 · Validar y conciliar entregables.
  - Hecho cuando: contenido e integridad pasan y la evidencia se consolida en `evidence/S02/evidence.md` y `validation/results/S02/validation.json`.

## Audit y cierre

- [x] T05 · Auditar S02 contra los 30 requisitos/criterios.
  - Resultado: ronda 01 ejecutada con veredicto `REQUIERE CORRECCIONES`; `A-S02-001` abierto y `RNF-S02-06` pendiente.
- [x] T06 · Corregir el hallazgo autorizado `A-S02-001`.
  - Resultado: fila 10 aumentada de 45 a 150 pt; D10 se lee completa sin cambiar su valor, ancho ni estilo. Corrección pendiente de verificación independiente. RNF-S02-06 queda fuera de este Fix.
- [ ] T07 · Ejecutar nueva auditoría y proponer cierre.
  - Hecho cuando: 30/30 pasan, no quedan hallazgos que impidan cierre y el usuario aprueba cerrar S02.

No crear tareas adicionales para pasos internos de una herramienta. Si aparece un requisito nuevo, actualizar primero la spec y este listado.

Nota de correspondencia: tras la simplificación documental, la antigua T11 equivale a T05 y la antigua T12 equivale a T06. La evidencia visual anterior de T09 fue refutada por la ronda 01 y corregida mediante A-S02-001; T09 no constituye una auditoría de cierre.

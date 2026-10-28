# Evidencia consolidada · S02

## Entregables

- `deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx`: editable con diagrama y mapa Silver.
- `deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf`: versión entregable sin la diapositiva de ejemplo.
- `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`: hojas `S02 Mapa Silver` y `Fichas KPI` completadas.

## Comprobaciones ejecutadas

- El mapa contiene exactamente DATA-001 a DATA-005; WMS queda solo como contraste y no se carga como sexta fuente.
- El PPTX conserva la plantilla, el PDF contiene tres páginas 16:9 y ambos incluyen el diagrama y el mapa.
- El libro conserva 12 hojas, 50 fórmulas, 11 validaciones, cuatro reglas de formato condicional y 19 rangos combinados.
- Las cinco fichas KPI tienen nivel táctico, fórmula en palabras y unidad.
- El PBIP conserva cinco tablas, `RutaSilver`, cero relaciones, cero medidas y cero roles; S02 no modifica el modelo.
- No se ejecutó una sesión de presentación, publicación, RLS ni actualización en Service.

El resultado consolidado de controles está en `validation/results/S02/validation.json`. Los temporales y resultados por microtarea se retiraron después de consolidar esta evidencia.

## Revisión visual y auditoría

PPTX y PDF pasan la revisión visual. El contenido completo de `S02 Mapa Silver!D10` está guardado en el libro, pero la última captura de Excel muestra el texto truncado. La captura retenida es `screenshots/s02_t09_xlsx_map_r2.png`.

La ronda 01 abrió `A-S02-001` por el truncamiento de D10. El Fix posterior está documentado abajo, pero el hallazgo no puede cerrarse hasta una nueva auditoría. También queda pendiente revalidar las huellas de los cinco Silver externos. Estas condiciones impiden cerrar S02, pero no invalidan los demás entregables.

## Pendientes trasladados

- Definir origen, propietario y frecuencia de actualización de las fuentes.
- Validar empresarialmente el significado de `centro_distribucion` y `centro_distribucion_base`.
- Definir filtros y RLS en S06/S11, metas y umbrales en S08 y responsables empresariales en S11.
- Tratar las 26 lecturas límite, las particiones/horizonte futuro y la medida económica de merma en sus hitos correspondientes.

## Corrección A-S02-001 · 2026-10-27

- Causa: la fila 10 tenía 45 pt y no mostraba completos los 107 caracteres de `S02 Mapa Silver!D10` con el ancho existente.
- Cambio autorizado: altura de la fila 10 de 45 a 150 pt. El valor, `WrapText`, ancho D, estilos, fórmulas, combinaciones y estructura no cambiaron.
- Herramienta: Excel COM. El libro se guardó, cerró y reabrió en modo de solo lectura sin solicitud de reparación.
- Hash anterior: `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D` (39.510 bytes).
- Hash posterior: `415A3C55F616E466E4072E3AE4E44E4E3C308FC62DDAB642B28740F367E9EF31` (39.518 bytes).
- Evidencia anterior: [`s02_t09_xlsx_map_r2.png`](screenshots/s02_t09_xlsx_map_r2.png).
- Evidencia nueva: [`s02_t12_xlsx_map_fixed.png`](screenshots/s02_t12_xlsx_map_fixed.png).
- Revisión visual: las siete columnas permanecen legibles y D10 muestra completa la frecuencia de inventario.
- Integridad: 0 diferencias de valores/fórmulas, 0 diferencias de estilos de celda y una sola diferencia de dimensión (fila 10); 12 hojas, 50 fórmulas, 11 validaciones, 1 rango condicional con 4 reglas y 19 combinaciones.
- PPTX, PDF, SRC-201, SRC-203 y PBIP conservaron sus hashes.
- Estado del hallazgo: **corregido, pendiente de verificación por nueva auditoría**.

## Estado

Build y Fix completados. A-S02-001 está corregido, pendiente de verificación independiente; RNF-S02-06 continúa pendiente. S02 no está cerrado y S03 no se inició.

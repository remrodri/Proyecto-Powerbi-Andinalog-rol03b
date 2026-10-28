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

La auditoría mantiene abierto `A-S02-001`: ajustar la presentación de D10, generar una nueva evidencia visual y volver a auditar. También queda pendiente revalidar las huellas de los cinco Silver externos cuando estén accesibles. Estas limitaciones impiden cerrar S02, pero no invalidan los demás entregables.

## Pendientes trasladados

- Definir origen, propietario y frecuencia de actualización de las fuentes.
- Validar empresarialmente el significado de `centro_distribucion` y `centro_distribucion_base`.
- Definir filtros y RLS en S06/S11, metas y umbrales en S08 y responsables empresariales en S11.
- Tratar las 26 lecturas límite, las particiones/horizonte futuro y la medida económica de merma en sus hitos correspondientes.

## Estado

Build completado. Auditoría: requiere corrección. S02 no está cerrado y S03 no se inició.

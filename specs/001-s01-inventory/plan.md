# Plan — S01 Preparación

Versión 0.2 · 20 de octubre de 2026.
Spec de entrada: [spec.md](spec.md), v0.4 corregida, aprobada con dudas abiertas.
Estado: aprobado por el usuario el 20 de octubre de 2026. Actualización de estado 2026-10-22: T01–T10 completadas; S01 cerrado con limitaciones documentadas. El plan aprobado no cambia y S02 no se inicia.

## 1. Objetivo y límite

Ejecutar posteriormente la preparación documental y la inspección de cinco fuentes de S01. WMS es contraste separado. No crear modelo analítico, limpieza, relaciones, DAX, visuales, RLS ni What-if. Las fuentes originales permanecen intactas.

Este plan no modifica la spec ni resuelve por suposición sus dudas. Su cabecera menciona que aprobación habilita Build: se interpreta junto a AGENTS.md y la skill, que exigen plan aprobado y alcance autorizado. No comenzar Build por la mera existencia de estos archivos.

## 2. Entradas y herramientas

- Documentos de raíz y docs/, spec activa y fuentes registradas en docs/sources.md.
- SRC-101: guía S01; SRC-201: plantilla original; SRC-202: PDF DCAM. Revisar fuentes originales pertinentes, no ejemplos ajenos como instrucciones.
- DATA-001–005: CSV oficiales externos; DATA-006: procedencia Bronze–Silver; DATA-007: WMS solo contraste.
- Las fuentes fueron inspeccionadas en sesiones previas; antes de ejecutar controles, comprobar su identidad actual y registrar SHA-256 y tamaño.
- Python y bibliotecas: verificar el intérprete disponible en la sesión OpenCode antes de fijar comandos; csv, json y hashlib bastan para inventario. Verificar biblioteca de lectura/edición de XLSX y renderizador antes de elegir herramienta. No asumir que el runtime usado en esta conversación estará disponible en OpenCode.
- Power BI Desktop: disponibilidad, versión, configuración regional y acceso de automatización pendientes. Verificar proceso/ruta de instalación o apertura por el usuario, incluida posible instalación Store. No concluir ausencia solo por no encontrar Program Files.
- Sin MCP configurado o probado. No es necesario para este inventario; si falta automatización, Grupo 06 ejecutará Desktop y aportará evidencia.
- Git: comprobar estado si existe repositorio; no inicializar ni hacer commits como efecto de estas tareas.

## 3. Artefactos previstos en Build

Rutas relativas a la raíz del proyecto; son propuestas del plan, no archivos ya existentes.

| Artefacto | Función |
| --- | --- |
| validation/checks/s01_inventory.py | Controles de lectura reproducibles, sin mutar fuentes. |
| validation/results/S01/source_manifest.json | Rutas efectivas, tamaños, hashes y metadatos de ejecución. |
| validation/results/S01/csv_checks.json | Conteos, claves, vacíos, duplicados y resultados verificables. |
| evidence/S01/preparation.md | Decisión, inventario, cinco candidatos, medida de apoyo, DCAM y límites. |
| evidence/S01/wms_contrast.md | EV-S01-WMS con método, cobertura, resultados y límites. |
| evidence/S01/provenance.md | Transcripción trazada de DATA-006, separada de controles propios. |
| evidence/S01/desktop_checks.md | Procedimiento y registro real de Desktop con enlaces a capturas/exportaciones. |
| evidence/S01/screenshots/ | Solo capturas auténticas, cuando se ejecuten pruebas. |
| evidence/S01/template_mapping.md | Correspondencia campo/celda entre Markdown y copia del libro. |
| evidence/S01/s02_handoff.md | Entregables, pendientes, responsable y persona de pantalla. |
| deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx | Una copia progresiva del libro, evitando un libro distinto por hito. |
| specs/001-s01-inventory/AUDIT.md | Historial único, creado al ejecutar la auditoría autorizada. |

Si una copia de seguimiento ya existe, inspeccionar y preservar su avance antes de editar. El nombre se fija como elección reversible de implementación, no como exigencia docente. Un .pbip de preparación es opcional: solo guardarlo si se decide que facilita continuidad en powerbi/, respetando el proyecto único y sin contenido analítico.

## 4. Diseño y decisiones

### Controles independientes

Leer completos los cinco CSV, contar filas/columnas, comprobar claves simples o compuestas y correspondencias pertinentes. No inferir calidad semántica de la ausencia de nulos. Verificar presencia de salidas, centros, cobertura de productos y anomalías conocidas si se usan para sustentar el inventario. No eliminar ni corregir filas.

WMS: comprobar orden única, cobertura de las 8.000 órdenes IoT, coincidencia de producto/camión y centro WMS frente a centro base. Para los cruces adicionales declarados con lote, chofer-mes y cliente, leer únicamente columnas necesarias de sus CSV, registrar sus identidades en la evidencia y no cargarlos a Power BI. No asumir que una coincidencia demuestra semántica operativa. Si no se reproduce un resultado histórico, documentar diferencia y solicitar resolverla, sin ajustar datos ni spec silenciosamente.

DATA-006: registrar sus nombres de columnas reales y los cinco registros correspondientes. Es evidencia del productor, no auditoría propia del Bronze. Conservar el dato de 6.709 conversiones F→C sin afirmar que se reejecutaron.

### Preparación documental

Usar la decisión y las cinco fórmulas ya acordadas. Incluir en los indicadores térmicos flota como dimensión de camión cuando se describa análisis por ese corte; no requiere cargarla ni crear relaciones en S01. No usar totales globales como denominadores fijos bajo filtros.

Clasificar por tabla: excepción demostrada, diferencia de cobertura, limitación de alcance o decisión de modelado. «Sin brecha observada» debe incluir comprobación y diferencia pendiente respecto de la guía; no se vuelve cumplimiento automático. No transformar datos sintéticos en un diagnóstico general de la empresa.

DCAM: conservar Evidencia, puntaje 1 tentativo y confianza baja con alcance documental; justificar por ausencia de definición en fuentes revisadas, sin afirmar ausencia empresarial. Identificar y respaldar el componente aplicable a la brecha priorizada. No se exige evaluar C1–C8 ni reconstruir documentación reservada; si falta respaldo del componente elegido, el criterio sigue pendiente. Criterio aprobado en DEC-022.

### Copia de la plantilla

Copiar SRC-201 sin editar original. En S01 Inventario completar identificación y cinco filas con las siete columnas de la plantilla. En Fichas KPI completar identificación, nombres y decisiones que apoyan de los cinco candidatos; no anticipar campos de S02–S11. Conservar fórmulas automáticas. Medida de apoyo, DCAM y contexto ampliado quedan en preparation.md, sin inventar celdas de plantilla que no existen.

Preservar hojas futuras y ejemplos no pertinentes, identificándolos como ejemplos y no avances del equipo. Verificar células/valores/fórmulas y que no haya modificaciones fuera del rango autorizado. Revisar visualmente las dos hojas editadas; si no es posible, registrar esa validación pendiente, no certificar formato.

### Inspección Desktop

Abrir exclusivamente cinco CSV; WMS no se importa. Registrar región real, origen, nombre de tabla, filas y cantidad de columnas/encabezados. En las tablas con campos decimales, registrar un valor decimal representativo; en flota, comprobar enteros y fechas y documentar que no contiene campos decimales. El número de columnas exige conteo o evidencia completa; una captura parcial de encabezados no basta.

Los campos numéricos decimales disponibles incluyen temperatura_cabina_c, costo_unitario_bob y costo_almacenamiento_mensual_bob. Flota no contiene campos decimales: no se inventa un ejemplo; se comprueban enteros y fechas y se documenta esa ausencia. Esto no exime de comprobar archivo, filas y columnas. Criterio aprobado en DEC-023.

Puede usarse una evidencia consolidada con cobertura individual. Evitar capturas limitadas a «999+ filas». Solo importación mínima y tipado inicial: si hay anomalía regional, conservar evidencia sin corregirla. La parametrización RutaSilver está permitida por la spec; no convertirla en limpieza de S03. Si no se guarda proyecto, capturar el origen/parametrización efectiva en el registro.

## 5. Matriz de trazabilidad

| Requisito | Tareas | Prueba y evidencia |
| --- | --- | --- |
| RF-S01-01 | T03 | P03: decisión acordada en preparation.md y copia consistente. |
| RF-S01-02 | T03 | P03: pregunta → KPI → fuente, sin promesas fuera de datos. |
| RF-S01-03 | T02, T03 | P01/P02: cinco fuentes, claves, conteos y responsable Grupo 06. |
| RF-S01-04 | T02, T03 | P02/P03: clasificación y evidencia de cada observación. |
| RF-S01-05 | T01, T05 | P05: importación/tipos/región y anomalías documentados. |
| RF-S01-06 | T05 | P05: evidencia Desktop por tabla; archivo, filas, columnas y criterio decimal/Flota. |
| RF-S01-07 | T03, T07 | P03/P07: DCAM y componente aplicable identificado y respaldado, o pendiente. |
| RF-S01-08 | T03, T04 | P03/P04: cinco candidatos, fórmulas y decisiones consistentes. |
| RF-S01-09 | T04 | P04: original intacto, copia y mapa de celdas consistentes. |
| RF-S01-10 | T01, T05, T08 | P05/P08: ausencia de limpieza y funcionalidad analítica. |
| RF-S01-11 | T02 | P02: cinco registros DATA-006 con procedencia explícita. |

RNF-S01-01/02: P02/P03, procedencia y estados; RNF-S01-03: P01/P02, ejecución reproducible; RNF-S01-04/05: P03/P04, idioma y correspondencia; RNF-S01-06: P01/P04, hashes y originales; RNF-S01-07/09: P05/P08, no inventar ejecución; RNF-S01-08: P01/P03/P05, mínimos campos y sin secretos.

## 6. Pruebas previstas

| ID | Tipo | Contexto y esperado | Evidencia |
| --- | --- | --- | --- |
| P01 | Automática/documental | Disponibilidad real y huellas antes/después de originales utilizados; no cambios. | source_manifest.json y registro de entorno. |
| P02 | Automática | CSV completos: 191.710×15, 120×7, 100×6, 7.782×12, 144×5; claves de spec únicas; WMS 30.000×16 y 8.000 órdenes cubiertas; DATA-006 33 registros/5 pertinentes. Comparación exacta de conteos. | csv_checks.json, wms_contrast.md, provenance.md. |
| P03 | Documental | Decisión, cinco filas, cinco candidatos, apoyo y DCAM con componente aplicable; estados y limitaciones explícitos. | preparation.md, matriz de requisitos. |
| P04 | Automática y visual | Misma información autorizada en Markdown/Excel; fórmulas conservadas; ningún cambio fuera de campos S01; hojas editadas legibles. | template_mapping.md y evidencia de revisión. |
| P05 | Desktop | Cinco tablas observadas con archivo, filas y columnas; en tablas con campos decimales, lectura decimal; en flota, enteros y fechas y ausencia de campos decimales; conteos coincidentes o diferencias explicadas; sin limpieza ni modelo analítico. | desktop_checks.md y archivos enlazados. |
| P06 | Documental | Contraste conserva método, archivos y resultados; no implica carga WMS ni semántica empresarial probada. | wms_contrast.md. |
| P07 | Documental/humana | Componente DCAM aplicable identificado y respaldado; si falta respaldo, el criterio sigue pendiente. Persona de pantalla identificada. | s02_handoff.md, fuente/acuerdo. |
| P08 | Auditoría | CA-S01-01–06 y todos RF/RNF evaluados; cinco fuentes/copia/Desktop y condiciones componente DCAM aplicable/pantalla demostradas antes del cierre. | AUDIT.md. |

No imponer nuevas tolerancias KPI ni calcular DAX en S01. Los valores del anexo B son referencias; si se recalculan como control auxiliar, distinguir su precisión de presentación del valor completo.

## 7. Dependencias y puertas

- Plan y tareas: aprobados por el usuario el 2026-10-20. Estado de ejecución 2026-10-22: T01–T10 completadas; S01 cerrado con limitaciones documentadas. S02 no se inició.
- T01–T04 pueden avanzar sin respaldo del componente DCAM ni persona de pantalla, conservando estados pendientes.
- Falta de Desktop bloquea T05, no el inventario automático ni documentos independientes.
- C4 y la persona de pantalla quedaron resueltos en DEC-026/027 y verificados en T08 antes del cierre. Propietarios empresariales y medida por valor quedan para etapas acordadas y no bloquean S01.
- Rúbrica, S12–S13 y comisionamiento pendientes no bloquean requisitos S01 ya definidos.
- Aceptación de «sin brecha observada»: documentar la diferencia docente y consultar si fuera necesaria aclaración; auditoría no la convierte por sí sola en conformidad.
- Desviación respecto de conteos u otros criterios: registrar antes de cambiar la spec.

## 8. Cierre y reversibilidad

Tras Build autorizado, ejecutar Audit, corregir hallazgos autorizados y repetir revisión pertinente. Un solo AUDIT.md conserva las rondas. No marcar cerrada la spec hasta evidencia completa y aprobación del usuario.

Todos los productos se crean en rutas propias; los originales se verifican por hash y permanecen intactos. Conservar evidencia fallida. Si existe un archivo de salida previo, comparar y preservar su contenido antes de actualizarlo, sin sobrescritura ciega.

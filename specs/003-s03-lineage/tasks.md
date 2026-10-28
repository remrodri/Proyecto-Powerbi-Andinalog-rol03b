# Tareas S03 · conexión, perfil y linaje Silver

**Spec aprobada:** `specs/003-s03-lineage/spec.md`, versión 0.1.  
**Plan aprobado:** `specs/003-s03-lineage/plan.md`, versión inicial del 2026-10-27.  
**Build/Audit/Fix/Close:** autorizados por el usuario el 2026-10-28; ejecución limitada por los criterios demostrables.

## Build

- [x] **T01 · Verificar y documentar las cinco conexiones en Power BI Desktop.**
  - Requisitos: RF-S03-01 a RF-S03-05; RNF-S03-01 a RNF-S03-04; CA-S03-01 a CA-S03-05, CA-S03-08 y CA-S03-09.
  - Hecho cuando: región, `RutaSilver`, cinco orígenes, privacidad efectiva y perfil completo están comprobados; las cinco fuentes actualizan; filas, tipos, vacíos, errores y excepciones están documentados; WMS está ausente; no hay objetos nuevos fuera de alcance; la evidencia está consolidada.

- [x] **T02 · Completar el linaje y las tablas fuente de los KPI en el libro de seguimiento.**
  - Requisitos: RF-S03-06, RF-S03-07; RNF-S03-02, RNF-S03-03 y RNF-S03-05; CA-S03-06 a CA-S03-09.
  - Hecho cuando: `S03 Linaje` contiene exactamente cinco fuentes oficiales con todos sus campos; WMS no aparece como fuente; `Fichas KPI!F7:F11` contiene las cinco tablas acordadas; fórmulas, validaciones, formatos y hojas fuera de alcance permanecen intactos; las áreas modificadas son legibles.

- [x] **T03 · Validar y conciliar los entregables de S03.**
  - Requisitos: todos los RF, RNF y CA de la spec.
  - Hecho cuando: PBIP, Excel, evidencia y spec son coherentes; las cinco huellas Silver coinciden; no existen objetos ni tratamientos fuera de alcance; `validation.json` y `evidence.md` están consolidados; `work/` queda vacío; Build queda listo para auditoría.

## Audit, Fix y Close

- [x] **T04 · Auditar S03 contra todos los requisitos y criterios.**
  - Hecho cuando `AUDIT.md` registra una ronda completa con evidencia independiente y un estado para cada requisito y criterio.
  - Requiere autorización de Audit independiente.

- [x] **T05 · Corregir únicamente los hallazgos autorizados.**
  - Hecho cuando cada corrección autorizada está vinculada a su ID, verificada y registrada como pendiente de nueva auditoría. Si no hay hallazgos, se registra como no necesaria.
  - Requiere autorización de Fix independiente.

- [x] **T06 · Ejecutar la auditoría final y cerrar S03.**
  - Hecho cuando la ronda vigente demuestra todos los criterios, no quedan hallazgos bloqueantes y el usuario aprueba explícitamente el cierre. S04 no se inicia dentro de esta tarea.
  - Requiere autorizaciones independientes de Audit y Close.

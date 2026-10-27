# Constitución del proyecto AndinaLog 03B

Versión 1.0 · 20 de octubre de 2026

Estos principios rigen las especificaciones, planes, implementación y auditorías del proyecto Power BI del Grupo 06. Los cambios a esta constitución requieren aprobación del usuario y registro en `docs/decisions.md`.

1. **Decisión y alcance trazables.** Cada requisito debe apoyar el mandato de AndinaLog 03B o una exigencia docente identificada. La spec activa define el objetivo y los criterios de aceptación; ningún cambio de alcance se implementa antes de acordarlo y actualizarla.

2. **Fuentes preservadas.** Los Silver oficiales y las referencias originales permanecen intactos. Toda transformación debe ser reproducible y documentar origen, regla, registros afectados y limitaciones; una excepción sin explicación se conserva o marca, no se corrige por suposición.

3. **Significado único de los indicadores.** Cada KPI documenta fórmula, unidad, grano, denominador, contexto y fuente. Las relaciones y agregaciones respetan esos granos y se comprueban mediante claves, conteos, filtros y conciliaciones.

4. **Evidencia y supuestos separados.** Se distinguen datos entregados, referencias docentes, resultados reproducidos, supuestos y recomendaciones. Observado, predicho y escenario se presentan por separado; no se atribuyen causalidad, ahorro ni capacidad predictiva sin evidencia o condiciones explícitas. Los predictores utilizan solo información disponible al momento de predecir.

5. **Construcción simple y reproducible.** Se mantiene un proyecto de trabajo `.pbip`, con rutas parametrizadas, convenciones coherentes y dependencias justificadas. Toda incorporación técnica debe responder a un requisito; las decisiones relevantes y sus motivos quedan registrados.

6. **Validación antes del cierre.** Cada requisito tiene una comprobación y un resultado esperado. Los controles automáticos no sustituyen pruebas de Desktop; únicamente se declaran acciones y resultados realmente ejecutados. Una validación pendiente impide cerrar el criterio que depende de ella.

7. **Auditoría con historial.** El ciclo es Spec → Plan → Build → Auditoría → Correcciones → Nueva auditoría. Cada spec conserva todas las rondas en un único `AUDIT.md`; la auditoría no modifica los artefactos auditados y solo cierra hallazgos con evidencia. Los criterios no se rebajan para obtener conformidad.

8. **Gobierno y continuidad.** Los accesos se justifican y la seguridad por filas se prueba, incluidos usuarios sin autorización. Proyecto, fichas KPI, diccionario y pruebas permanecen alineados; `MEMORY.md` registra cada avance significativo y sus pendientes. No se avanza fuera del alcance autorizado ni se registran secretos en el repositorio.

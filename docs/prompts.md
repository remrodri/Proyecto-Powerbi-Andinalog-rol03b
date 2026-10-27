# Invocaciones del flujo SDD · AndinaLog 03B

El procedimiento mantenido está en la skill local [andinalog-sdd-workflow](../.opencode/skills/andinalog-sdd-workflow/SKILL.md). Este documento contiene ejemplos de solicitud; no duplica sus instrucciones. AGENTS.md y la constitución siguen vigentes.

En OpenCode, pide cargar la skill por su nombre. Si no está disponible, indica el problema y lee su SKILL.md explícitamente; no afirmes haberla cargado. Una invocación autoriza solo el alcance que escribas.

## Inicio de S01

```text
Usa la skill andinalog-sdd-workflow en fase Specify para S01.
Carpeta propuesta: specs/001-s01-inventory/.
Lee las fuentes pertinentes y el contexto existente. Pregunta de una en una lo que falte y presenta un borrador. No guardes archivos ni implementes hasta mi aprobación.
```

## Otras fases

```text
Usa andinalog-sdd-workflow en fase Plan para <ruta de spec aprobada>. Presenta plan y tareas; no implementes ni guardes todavía.
```

```text
Usa andinalog-sdd-workflow en fase Build para implementar solo <tarea o alcance> de <ruta/tasks.md>, con spec y plan aprobados. Ejecuta sus controles y detente al terminar ese alcance.
```

```text
Usa andinalog-sdd-workflow en fase Audit para <ruta de spec>. Registra una nueva ronda en su único AUDIT.md, sin modificar lo auditado. Separa pruebas ejecutadas y pendientes.
```

```text
Usa andinalog-sdd-workflow en fase Fix para corregir solo <IDs> de <ruta/AUDIT.md>. Déjalos pendientes de nueva verificación; no realices la auditoría dentro de esta tarea.
```

```text
Usa andinalog-sdd-workflow en fase Close para <ruta de spec>. Comprueba los criterios y presenta la propuesta de cierre; espera mi aprobación para registrarlo.
```

## Reanudación o cambio

Para reanudar: lee AGENTS.md, MEMORY.md y la spec activa, resume estado y siguiente paso sin implementar.

Para un cambio: describe el requisito nuevo y pide analizar impacto y proponer la actualización de spec antes de tocar la implementación. Su aprobación no autoriza automáticamente otra fase.

Los prompts docentes permanecen como fuentes en references/prompts/; sus requisitos se adaptan a las guías de cada hito y a 03B, sin copiar datos de otros casos.

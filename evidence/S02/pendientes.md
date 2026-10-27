# Pendientes de S02 al cierre de T10

- Fecha: 2026-10-27.
- Fuente: `specs/002-s02-architecture/spec.md` §8.3, DEC-028 a DEC-033 y PEN-017 a PEN-019.
- Alcance: registrar lo que queda abierto; T10 no resuelve ninguno de estos pendientes.

## Tabla de pendientes

| Pendiente | Estado al cierre de S02 | Responsable | Hito de tratamiento |
| --- | --- | --- | --- |
| Definición y validación de `centro_distribucion` y `centro_distribucion_base` | Documentado como ausencia; no resuelto | Grupo 06; validador por acordar | S02 (documentación), S06 (filtros) y S11 (RLS) |
| Selección final de KPI | Resuelta en S02: cinco KPI tácticos | Grupo 06 | S02 |
| Metas y umbrales | Trasladado | Por acordar | S08 |
| Responsables empresariales de KPI | Trasladado | Por acordar | S11 |
| Roles y pruebas RLS | Trasladado | Por acordar | S11 |
| Merma por valor | Documentada como pendiente; no es KPI | Por acordar | Por acordar; impacto económico en S10 |
| 26 lecturas en límites térmicos | Trasladado | Grupo 06 | S04 |
| Particiones y horizonte futuro | Trasladado | Grupo 06 | S04 y S10 |
| Relación temporal de costos | Trasladado | Grupo 06 | S06 |
| Origen de los sistemas y propietarios de las fuentes | Documentado como no disponible; no resuelto | Grupo 06 documenta; propietario por acordar | Por acordar |
| Frecuencia de actualización | Documentada como «por acordar»; no resuelta | Por acordar | Por acordar |
| Sesión compartida de S02 (Rodrigo Tucuman) | No ejecutada ni declarada | Rodrigo Tucuman | S02 |
| Publicación en Service | Prevista, no ejecutada | Por acordar | S11 y entrega final |

## Lectura de control

- Registrar un pendiente no equivale a resolverlo. Centro, origen y frecuencia siguen abiertos.
- La brecha de `centro_distribucion` se mantiene como ausencia documentada; no se declara resuelta.
- Los pendientes sin respaldo conservan «Por acordar»; no se inventan propietarios, validadores ni frecuencias.
- La sesión compartida no se ejecutó ni se declaró ejecutada; Rodrigo Tucuman figura solo como designado.
- La publicación en Service no se ejecutó.
- Las metas, umbrales, DAX, responsables y RLS corresponden a hitos posteriores; no se completaron en S02.
- Merma por valor no se incorpora como KPI; queda pendiente su tratamiento económico.

## Referencias de decisiones

- **PEN-017**: origen y propietarios de las fuentes; documentar no resuelve.
- **PEN-018**: frecuencia de actualización; se distingue de la frecuencia de observación y queda «por acordar».
- **PEN-019**: validación empresarial del significado de centro; se registra como ausencia documentada y sigue pendiente.

## Traspaso

- S03 recibe mapa y frecuencias.
- S04 recibe límites térmicos y particiones.
- S06 recibe `dim_centro`, filtros y relación temporal de costos.
- S08 recibe metas y umbrales.
- S10 recibe impacto económico.
- S11 recibe responsables, RLS y publicación prevista.

# 3. Velocidad del Proyecto y Métricas (Tracker)

**Responsable:** I3 (Tracker) — Analy Yépez · **Revisores:** I2 (Coach) — Óscar Tamayo e I1 (Gestor) — Ronny Veloz.

## Cómo se calcula la velocidad
- Estimación en puntos Fibonacci (`1, 2, 3, 5, 8`); **1 punto ≈ 2–3 horas** de trabajo.
- **Fórmula:**
  $$\text{Velocidad} = \frac{\sum \text{puntos de historias aceptadas por el Cliente}}{\text{iteraciones completadas}}$$
- *Regla XP:* solo cuentan las historias **terminadas, con pruebas en verde y aceptadas por I1 (Cliente) e I4 (Tester)**. El trabajo a medias cuenta 0 puntos.

## Tablero de velocidad

| Iteración | Fecha | Puntos planificados | Puntos completados y aceptados | Velocidad acumulada | Observaciones |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Mar 17/11 | 8 | 8 *(aceptadas por I1 · Ronny Veloz)* | 8 | HU-01 y HU-02 terminadas y aceptadas; 13 pruebas en verde. |
| **2** | Mié 18/11 | 26 | 5 *(en curso: HU-03 lista; faltan HU-04..08)* | 13 *(parcial)* | HU-03 (`BombaAutomata` + `Bomba` + `mostrar_destruir`) terminada con pruebas en verde. |
| **3** | Jue 19/11 | 18 | `[Completar al cierre]` | `[ ]` | `[ ]` |

## Burndown (52 pts → 0)

| Hito | Restantes planificados | Restantes reales | Estado |
| :--- | :---: | :---: | :--- |
| Inicio del proyecto (17/11) | 52 | 52 | ✅ |
| Fin Iteración 1 (17/11) | 44 | 44 | ✅ En plan |
| Fin Iteración 2 (18/11, 20:00) | 18 | `[ ]` | En seguimiento |
| Fin Iteración 3 (19/11, entrega) | 0 | `[ ]` | Meta |

## Avance por historia

| HU | Título | Pts | Responsable | Estado | Pruebas |
| :--- | :--- | :---: | :--- | :--- | :--- |
| HU-01 | Inicio de sesión seguro | 3 | Analy | ✅ Terminada | `test_auth_service.py`, `test_sistema_ruso.py` |
| HU-02 | Datos del equipo y lectura de `Grupo06.csv` | 5 | Analy | ✅ Terminada | `test_sistema_ruso.py`, `test_utility.py`, `test_arsenal_catalogo.py` |
| HU-03 | Bomba con autómata (`IIA.buscar`) | 5 | Ronny | ✅ Terminada | `test_bomba_automata.py` (39 casos + oráculo `re` + CSV real) |
| HU-04 | Nacimiento como `HLarva` | 3 | Óscar | ⏳ Pendiente | `[ ]` |
| HU-05 | Metamorfosis por alimento | 5 | Óscar | ⏳ Pendiente | `[ ]` |
| HU-06 | Ensamblaje del `AntCiberDron` | 5 | Óscar | ⏳ Pendiente | `[ ]` |
| HU-07 | Fuente de poder con `IIA` | 3 | Óscar | ⏳ Pendiente | `[ ]` |
| HU-08 | Idiomas con expertos parlantes | 5 | Óscar | ⏳ Pendiente | `[ ]` |
| HU-09 | Hormiguero Virtual (consola) | 8 | Mateo | ⏳ Pendiente | `[ ]` |
| HU-10 | Docker sin incidentes | 5 | Mateo | ⏳ Pendiente | `[ ]` |
| HU-11 | 5 diagramas y bitácoras XP | 5 | Todos (cierra Ronny) | 🔄 En curso (casos de uso, autómata y plantilla final listos) | — |

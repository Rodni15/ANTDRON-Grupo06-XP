# 3. Velocidad del Proyecto y Métricas (Tracker)

**Responsable:** **I3 (Tracker)** · **Revisor:** I2 (Coach) e I1 (Gestor) · **Proyecto:** ANTDRON en **Python 3.12** (`pytest`, `sqlite3`, Docker).

## Cómo se calcula la Velocidad en nuestro equipo de 4
- Contamos con **1 pareja activa de programación (`I2 + I3`)**, apoyada por **I4 (Tester)** en automatización QA/CI e **I1 (Cliente/Gestor)** en definiciones y aceptación rápida.
- **Equivalencia inicial:** `1 punto XP ≈ 2.5 horas` de pareja productiva.
- **Fórmula oficial:**
  $$\text{Velocidad real} = \frac{\sum \text{Puntos de Historias Aceptadas por el Cliente}}{\text{Iteraciones completadas}}$$

> *Regla XP ("Yesterday's Weather"):* Solo cuentan los puntos de historias **100% terminadas, con tests en verde y aceptadas por I1 (Cliente)** al final de la iteración. El trabajo a medias cuenta **0 puntos** para la velocidad de esa iteración.

## Tablero de Velocidad (Plantilla de Seguimiento)

| Iteración | Puntos Planificados | Puntos Completados y Aceptados | Velocidad Acumulada | Variación / Ajuste |
| :---: | :---: | :---: | :---: | :--- |
| **Iteración 1** | 16 | `[Completar al cierre It.1]` | `[Pts It.1]` | `[Ej. Si se logran 14 pts, ajustar carga de It.2]` |
| **Iteración 2** | 18 | `[Completar al cierre It.2]` | `[Promedio It.1-2]` | `[Rebalancear alcance no crítico si baja velocidad]` |
| **Iteración 3** | 18 | `[Completar al cierre It.3]` | `[Promedio It.1-3]` | `[Cierre final: 52/52 pts]` |

## Burndown de Puntos Restantes (Meta: 52 pts $\rightarrow$ 0 pts)

| Hito | Puntos Restantes Planificados | Puntos Restantes Reales | Estado |
| :--- | :---: | :---: | :--- |
| Inicio del proyecto | `52` | `52` | Planificado |
| Fin Iteración 1 | `36` | `[ ]` | En seguimiento |
| Fin Iteración 2 | `18` | `[ ]` | En seguimiento |
| Fin Iteración 3 (Entrega) | `0` | `[ ]` | Meta de aceptación |

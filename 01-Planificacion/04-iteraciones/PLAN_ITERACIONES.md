# 4. Plan de Iteraciones

El proyecto se desarrolla en **Python 3.12** en **3 iteraciones cortas** (~1 semana por iteración). Al final de cada iteración existe código ejecutable en Python, probado con `pytest` y demostrable al Cliente (**I1**).

---

## Iteración 1 — Fundamentos, Consola, CSV y Metamorfosis (`16 pts`)
- **Historias:** `HU-01` (3), `HU-02` (5), `HU-04` (3), `HU-05` (5).
- **Meta de la iteración:** Contar con el contrato `pkAntCiberDronContract` en Python (`abc.ABC`), login con 3 intentos, lectura exacta de `Grupo06.csv` con animación `\ | / - |` y ciclo de vida `HLarva` $\rightarrow$ evolución/muerte.
- **Entregable ejecutable:** `Release 1 (MVP)` (`python main.py`).
- **Avance temprano de documentación:** Borrador de Diagrama de Clases y MER inicial en PlantUML.

## Iteración 2 — Autómata de la Bomba, `AntCiberDron` e Idiomas (`18 pts`)
- **Historias:** `HU-03` (5), `HU-06` (5), `HU-07` (3), `HU-08` (5).
- **Meta de la iteración:** Integrar `IIA` en `AntCiberDron`, implementar el AFD en Python generado con el último dígito de las 4 cédulas, modelar extremidades/láser/turbo/fuente y módulo de idiomas exclusivo de `ExpertoParlante`.
- **Entregable ejecutable:** `Release 2 (Núcleo Completo)`.
- **Avance de documentación:** Grafo PlantUML y Gramática formal del autómata + Casos de Uso en PlantUML.

## Iteración 3 — UI Hormiguero, SQLite, Docker y Cierre XP (`18 pts`)
- **Historias:** `HU-09` (8), `HU-10` (5), `HU-11` (5).
- **Meta de la iteración:** Conectar los menús de consola del Hormiguero Virtual con SQLite (`sqlite3`), empaquetar en Docker (`python:3.12-slim`), ejecutar CI verde sin incidentes y completar los 5 diagramas en PlantUML + checklist firmado.
- **Entregable ejecutable:** `Release 3 (Producto Final)`.

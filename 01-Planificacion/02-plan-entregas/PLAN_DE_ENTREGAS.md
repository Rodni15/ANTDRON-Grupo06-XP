# 2. Plan de Entregas (Release Plan)

**Responsables:** I1 (Cliente + Gestor) con estimaciones técnicas de I2 (Coach + Prog1) e I3 (Tracker + Prog2).  
**Stack de implementación:** **Python 3.12** (`abc.ABC`, consola, `sqlite3`, `pytest`, Docker) · **Diagramas:** **PlantUML**.

El proyecto se divide en **3 Releases incrementales** en Python 3.12, entregando software ejecutable desde la primera semana para reducir riesgos y evitar la penalización de `-0.5 puntos por incidente`.

| Release | Nombre del Hito | Historias Incluidas | Puntos | Valor Entregado al Cliente (I1) | Entregable Técnico |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Release 1 (R1)** | **MVP Consola, CSV y Ciclo de Larvas** | `HU-01`, `HU-02`, `HU-04`, `HU-05` | **16** | El sistema ya arranca en Python 3.12, autentica, muestra al equipo, lee `Grupo06.csv` con loading animado y simula nacimiento/evolución/muerte de hormigas. | `python main.py` ejecutable en consola + pruebas `pytest` de Login, CSV y Hormigas. |
| **Release 2 (R2)** | **Autómata, AntCiberDron e Idiomas** | `HU-03`, `HU-06`, `HU-07`, `HU-08` | **18** | La bomba evalúa el autómata real de las 4 cédulas y detona coordenadas; el dron arma sus extremidades, gestiona su fuente con `IIA` y aprende EN/ES de expertos. | Motor AFD verificado en Python + módulos `AntCiberDron` / `ModuloIdioma` + pruebas `pytest`. |
| **Release 3 (R3)** | **UI Hormiguero, SQLite, Docker y Diagramas** | `HU-09`, `HU-10`, `HU-11` | **18** | Sistema completo con menús de consola persistido en SQLite (`sqlite3`), dockerizado y acompañado de los 5 diagramas obligatorios en PlantUML y actas XP firmadas. | Imagen Docker `python:3.12-slim` lista + menús de consola + SQLite + 5 Diagramas PlantUML + Checklist firmado. |

## Criterio de Priorización del Cliente (I1)
1. **Primero riesgo estructural y entrada de datos** (`HU-01`, `HU-02`): sin login y sin lectura exacta de `Grupo06.csv` no hay flujo base.
2. **Luego núcleo de dominio** (`HU-04`, `HU-05`, `HU-03`): jerarquía de hormigas y autómata formal con TDD estricto.
3. **Finalmente capacidades extendidas, UI visual y empaquetado** (`HU-06`..`HU-11`), validando Docker desde R1 con imágenes base tempranas para que R3 no falle.

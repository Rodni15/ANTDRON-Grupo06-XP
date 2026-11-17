# 17. Checklist Oficial de Pruebas de Aceptación (Cero Incidentes — Python 3.12)

**Validan y firman:** **Analy Yepez (I1 · Cliente interno)** & **Mateo Yaguari (I4 · Tester)** antes de la evaluación con el docente (`patmic`).  
**Stack validado:** **Python 3.12** (`abc.ABC`, `sqlite3`, `pytest`, Docker `python:3.12-slim`) · **Diagramas:** **PlantUML**.  
**Regla crítica del PDF:** *"Si su solución tiene algún tipo issues/errors/crash o No cumple con las instrucciones del presente: `-0.5 puntos por incidente`."*

| # | Criterio de Aceptación (PDF Original + XP) | Historia | Resultado | Verificado por |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Login acepta a los **4 integrantes** (`Analy Yepez`, `Ronny Veloz`, `Oscar Tamayo`, `Mateo Yaguari`) y **`patmic`/`123`**; cierra al **3.er fallo** sin excepciones. | `HU-01` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 2 | Muestra `[+] TEAM [6]: Hormiguero Cibernético` con las 4 cédulas y nombres reales. | `HU-02` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 3 | `SistemaRuso.readCoord` lee `data/Grupo06.csv` animando `\ | / - |` hasta `100%` por línea y tabla exacta. | `HU-02` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 4 | `AntCiberDron` implementa `IIA` y `buscar(tipoArsenal)` usa el autómata de los **4 últimos dígitos `{2, 5, 3, 9}`** ($L = \{ab^*, abc, abcdt^+\}$). | `HU-03` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 5 | Imprime `COORDENADAS UCRANIANAS A DESTRUIR:` con `Geoposición | Tipo Arsenal | Acción` (`true`). | `HU-03` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 6 | Toda hormiga nace como `HLarva`, vive con `Nectar`, evoluciona con su alimento y muere (`False`) con otro. | `HU-04,05` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 7 | `AntCiberDron` tiene extremidades de hormiga: metralleta (del. derecha), láser (del. izquierda) y turbo (espalda). | `HU-06` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 8 | Fuente de poder recargable y reemplazable bajo asistencia de `IIA`; afecta potencia del láser y vuelo. | `HU-07` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 9 | Aprendizaje EN/ES (léxico, gramática, fonética) solo mediante `ExpertoParlante`. | `HU-08` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 10 | Menús de consola Python: gestionar Hormiguero Virtual, crear/alimentar hormigas y ver coordenadas destruidas en SQLite (`sqlite3`). | `HU-09` | `[ ] Pass` | I1 (Analy) / I4 (Mateo) |
| 11 | `docker compose build`, `docker compose run --rm antdron` y `pytest` corren limpios; CI en verde. | `HU-10` | `[ ] Pass` | I4 (Mateo) / I1 (Analy) |
| 12 | Entregados en **código PlantUML** los **5 diagramas obligatorios** (Diagrama de Clases, Casos de Uso, Grafo con Gramática del Autómata `{2,3,5,9}`, MER, Diagrama de Arquitectura de la Aplicación) + bitácoras XP completas. | `HU-11` | `[ ] Pass` | Analy / Ronny / Oscar / Mateo |

**Firma Cliente (I1 · Analy Yepez):** `___________________` · **Firma Tester (I4 · Mateo Yaguari):** `___________________` · **Fecha:** `[DD/MM/AAAA]`

# 17. Checklist Oficial de Pruebas de Aceptación (Cero Incidentes — Python 3.12)

**Validan y firman:** **Ronny Veloz (I1 · Cliente interno)** & **Mateo Yaguari (I4 · Tester)** antes de la evaluación con el docente (`patmic`).  
**Stack validado:** **Python 3.12** (`abc.ABC`, `sqlite3`, `Flask`, `pytest`, Docker `python:3.12-slim`) · **Diagramas:** **PlantUML**.  
**Regla crítica del PDF:** *"Si su solución tiene algún tipo issues/errors/crash o No cumple con las instrucciones del presente: `-0.5 puntos por incidente`."*

| # | Criterio de Aceptación (PDF Original + XP) | Historia | Resultado | Verificado por |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Login acepta a los **4 integrantes** (`Analy Yepez`, `Ronny Veloz`, `Oscar Tamayo`, `Mateo Yaguari`) y **`patmic`/`123`**; cierra/bloquea al **3.er fallo** sin excepciones (consola `AuthService` + web `web_app.py`). | `HU-01` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 2 | Muestra `[+] TEAM [6]: Hormiguero Cibernético` (consola) y panel de equipo web con las 4 cédulas y nombres reales. | `HU-02` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 3 | `SistemaRuso.readCoord` lee las 40 filas de `data/Grupo06.csv` animando `\ \| / - \|` hasta `100%` en consola y tabla progresiva por fila en web. | `HU-02` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 4 | `AntCiberDron` implementa `IIA` (`abc.ABC`) y `buscar(tipoArsenal)` usa `Bomba` / `BombaAutomata` de los **4 últimos dígitos `{2, 5, 3, 9}`** ($L = \{ab^*, abc, abcdt^+\}$). | `HU-03` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 5 | Imprime/presenta `COORDENADAS UCRANIANAS A DESTRUIR:` (`mostrar_destruir` + tabla web separada) con `Geoposición \| Tipo Arsenal \| Acción` (`true`, 29 de 40 filas). | `HU-03` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 6 | Toda hormiga nace como `HLarva`, vive con `Nectar`, evoluciona a `HRastreadora` con `AHervivoro` conservando su `Id` y muere (`False`, estado `"MUERTA"`) con alimento incorrecto. | `HU-04,05` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 7 | `AntCiberDron` modela extremidades de hormiga (`cabeza`, `torax`, `abdomen`, `6 patas`): metralleta (del. derecha), láser (del. izquierda) y `TurboReactor` (espalda). | `HU-06` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 8 | `FuenteDePoder` recargable y reemplazable bajo asistencia de `IIA` (`asistirRecargaFuente`, `asistirReemplazoFuente`); afecta potencia del láser y vuelo (`volar()`). | `HU-07` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 9 | Aprendizaje EN/ES (`léxico`, `gramática`, `fonética`) exclusivo mediante `ExpertoParlante` certificado del idioma correspondiente; persistido en SQLite (`entrenamiento_idioma`). | `HU-08` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 10 | Interfaz web Flask (`web_app.py`, puerto `5000`) + entrada de consola (`main.py`) integradas con SQLite (`sqlite_connection.py`) para crear/alimentar hormigas, operar el dron, evaluar CSV y registrar idiomas. | `HU-09` | `[x] Pass` | I1 (Ronny) / I4 (Mateo) |
| 11 | `Dockerfile` (`python:3.12-slim`, puerto `5000`), `docker-compose.yml` (volumen `./data:/app/data`), CI y suite de **68 casos de prueba** aprobados (`tests/test_web.py`, `test_parte3.py`, `test_bomba_automata.py`, Parte 1). *(Ejecución física de `docker compose up` pendiente de entorno con Docker Desktop activo).* | `HU-10` | `[x] Pass` | I4 (Mateo) / I1 (Ronny) |
| 12 | Entregados en **código PlantUML** los **5 diagramas obligatorios** (Clases, Casos de Uso, Grafo con Gramática del Autómata `{2,3,5,9}`, MER, Arquitectura con capa Flask) + bitácoras XP y [DOCUMENTO_FINAL_GRUPO06.md](../../docs-analisis/DOCUMENTO_FINAL_GRUPO06.md). | `HU-11` | `[x] Pass` | Analy / Ronny / Oscar / Mateo |

**Firma Cliente (I1 · Ronny Veloz):** `Ronny Veloz (I1)` · **Firma Tester (I4 · Mateo Yaguari):** `Mateo Yaguari (I4)` · **Fecha:** `18/11/2026`

## Confirmación final del equipo · 18/11/2026

El equipo confirmó la ejecución satisfactoria de Docker y del recorrido funcional; la demostración está grabada en el video incluido en el paquete de entrega. Esta confirmación actualiza las anotaciones previas de Docker pendiente.

# 5. Tabla de Rotaciones (Equipo de 4 Integrantes)

**Responsables:** **Ronny Veloz (I2 · Coach)** y **Oscar Tamayo (I3 · Tracker)** · **Stack:** **Python 3.12** (`abc.ABC`, `sqlite3`, `pytest`, Docker) · **Diagramas:** **PlantUML**.

En nuestro equipo de 4 personas (**Analy Yepez · I1**, **Ronny Veloz · I2**, **Oscar Tamayo · I3**, **Mateo Yaguari · I4**), la rotación cumple dos objetivos:
1. **Rotación táctica cada 30 minutos:** `I2` (Ronny) y `I3` (Oscar) intercambian **Driver** (teclado) y **Navigator** (revisión estratégica, casos borde y diseño) en las piezas centrales, colaborando también con `I1` (Analy) y `I4` (Mateo) en sus respectivas partes.
2. **Rotación de conocimiento entre Partes 1–4 y QA:** Nadie queda aislado en su módulo; `I4` (Mateo) realiza revisión cruzada y pruebas `pytest`/Docker sobre todas las partes.

| Momento | Pareja Activa (`I2 + I3`) — Driver / Navigator | Parte & Módulo Principal | Apoyo / Verificación Cruzada (`I1` & `I4`) |
| :--- | :--- | :--- | :--- |
| **It. 1 · 1.ª mitad** | **Driver:** I3 (Oscar) · **Navigator:** I2 (Ronny) | **Parte 1:** `SistemaRuso`, `CoordenadaUK`, `Utility` y Login (`HU-01`, `HU-02`) | **I1 (Analy)** lidera Parte 1 (`Grupo06.csv` + Casos de Uso); **I4 (Mateo)** prepara tests TDD en `pytest`. |
| **It. 1 · 2.ª mitad** | **Driver:** I2 (Ronny) · **Navigator:** I3 (Oscar) | **Parte 3:** `pkAntCiberDronContract`, `Hormiga`, `HLarva`, `Alimento`, `EvolucionStrategy` (`HU-04`, `HU-05`) | **I4 (Mateo)** realiza Pair Review y configura `ci.yml`; **I1 (Analy)** confirma regla del Grupo 6. |
| **It. 2 · 1.ª mitad** | **Driver:** I2 (Ronny) · **Navigator:** I3 (Oscar) | **Parte 2:** `BombaAutomata` (`ab* ∪ abc ∪ abcdt+` de `{2,3,5,9}`) y `AntCiberDron(IIA)` (`HU-03`, `HU-06`) | **I4 (Mateo)** valida autómata contra oráculo `re`; **I1 (Analy)** aprueba tabla de destrucción. |
| **It. 2 · 2.ª mitad** | **Driver:** I3 (Oscar) · **Navigator:** I2 (Ronny) | **Parte 3:** `FuenteDePoder`, `Laser`, `TurboReactor` y `ModuloIdioma` (`HU-07`, `HU-08`) | **I4 (Mateo)** prueba rechazo sin `ExpertoParlante`; **I1 (Analy)** revisa avance Release 2. |
| **It. 3 · 1.ª mitad** | **Driver:** I3 (Oscar) · **Navigator:** I2 (Ronny) | **Parte 4 & Parte 3:** `UI Hormiguero (consola)` (`main.py`) y persistencia `SQLite` (`sqlite3`) (`HU-09`) | **I4 (Mateo)** lidera Parte 4 (`Dockerfile` / `docker-compose.yml` / pantallas) con apoyo de I3; **I1 (Analy)** valida flujo completo. |
| **It. 3 · 2.ª mitad** | **Driver:** I2 (Ronny) · **Navigator:** I3 (Oscar) | Integración final de Partes 1–4, documento final y los 5 Diagramas PlantUML (`HU-10`, `HU-11`) | **I4 (Mateo)** ejecuta pruebas en máquina limpia Docker; **I1 (Analy)** firma el Checklist de Aceptación. |

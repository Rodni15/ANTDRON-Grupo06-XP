# 5. Tabla de Rotaciones (Equipo de 4 Integrantes)

**Responsables:** I2 (Coach) e I3 (Tracker) · **Stack:** **Python 3.12** (`abc.ABC`, `sqlite3`, `pytest`, Docker) · **Diagramas:** **PlantUML**.

En un equipo de 4 personas con **2 Programadores (`I2`, `I3`)**, **1 Cliente/Gestor (`I1`)** y **1 Tester (`I4`)**, la rotación cumple dos objetivos:
1. **Rotación táctica cada 30 minutos:** `I2` y `I3` intercambian **Driver** (teclado) y **Navigator** (revisión estratégica, casos borde y diseño).
2. **Rotación de conocimiento entre módulos y QA:** En cada mitad de iteración rotan el módulo liderado y realizan sesiones cruzadas con `I4 (Tester)` para que nadie sea el único dueño de un módulo.

| Momento | Pareja Activa (`I2 + I3`) — Driver / Navigator | Módulo Principal | Apoyo / Verificación Cruzada (`I4` & `I1`) |
| :--- | :--- | :--- | :--- |
| **It. 1 · 1.ª mitad** | **Driver:** I3 · **Navigator:** I2 | `SistemaRuso`, `CoordenadaUK`, `Utility` y Login (`HU-01`, `HU-02`) | **I4** prepara casos TDD en pytest; **I1** valida `Grupo06.csv` y formato consola. |
| **It. 1 · 2.ª mitad** | **Driver:** I2 · **Navigator:** I3 | `pkAntCiberDronContract`, `Hormiga`, `HLarva`, `Alimento`, `EvolucionStrategy` (`HU-04`, `HU-05`) | **I4** realiza Pair Review con I3 y configura `ci.yml`; **I1** confirma regla del Grupo 6. |
| **It. 2 · 1.ª mitad** | **Driver:** I2 · **Navigator:** I3 | `Autómata / AFD` y `AntCiberDron(IIA)` (`HU-03`, `HU-06`) | **I4** valida autómata contra oráculo `re`; **I1** aprueba salida de destrucción. |
| **It. 2 · 2.ª mitad** | **Driver:** I3 · **Navigator:** I2 | `FuenteDePoder`, `Laser`, `TurboReactor` y `ModuloIdioma` (`HU-07`, `HU-08`) | **I4** simula pruebas negativas sin `ExpertoParlante`; **I1** revisa avance Release 2. |
| **It. 3 · 1.ª mitad** | **Driver:** I3 · **Navigator:** I2 | `UI Hormiguero (consola)` y persistencia `SQLite` (`sqlite3`) (`HU-09`) | **I4** prueba flujo de menús + BD y arma `Dockerfile` / `docker-compose.yml` (`HU-10`). |
| **It. 3 · 2.ª mitad** | **Driver:** I2 · **Navigator:** I3 | Integración final, corrección de incidentes y Diagramas PlantUML (`HU-10`, `HU-11`) | **I4** ejecuta pruebas en máquina limpia; **I1** firma el Checklist de Aceptación. |

# 14. Bitácora de Programación por Parejas (Pair Programming — Python 3.12)

**Regla XP del Coach (I2):** Todo código de producción **Python 3.12** en `src/` se escribe en pareja (**I2 + I3**), rotando **Driver** (quien escribe) y **Navigator** (quien revisa diseño, casos borde y contrato `pkAntCiberDronContract`) cada **30 minutos**. Al finalizar cada historia, **I4 (Tester)** ejecuta una sesión de *Pair Review / Testing* con `pytest` antes de fusionar a `main`.

## Registro de Sesiones (Plantilla)

| Fecha | Iteración / HU | Driver (Teclado) | Navigator (Estrategia) | Revisor QA (I4) | Módulo Trabajado & Resultado |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[DD/MM]` | `It.1 / HU-01` | I3 | I2 | I4 | `AuthService` + `test_auth_service.py` (3 intentos). |
| `[DD/MM]` | `It.1 / HU-02` | I2 | I3 | I4 | `SistemaRuso.readCoord` + `CoordenadaUK` + `Utility`. |
| `[DD/MM]` | `It.1 / HU-04,05` | I2 / I3 | I3 / I2 | I4 | `IHormiga`, `Hormiga`, `HLarva`, `EvolucionStrategy`. |
| `[DD/MM]` | `It.2 / HU-03` | I2 | I3 | I4 | `BombaAutomata` + `AntCiberDron(IIA)` (implementa `IIA`). |
| `[DD/MM]` | `It.2 / HU-06,07,08` | I3 | I2 | I4 | Extremidades, `FuenteDePoder`, `Laser`, `ModuloIdioma`. |
| `[DD/MM]` | `It.3 / HU-09,10` | I3 / I2 | I2 / I3 | I4 | `UI consola` + `SQLite` (`sqlite3`) + verificación Docker (`python:3.12-slim`). |

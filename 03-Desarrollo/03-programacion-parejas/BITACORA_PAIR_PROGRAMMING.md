# 14. Bitácora de Programación por Parejas (Pair Programming — Python 3.12)

**Regla XP del Coach (I2 · Oscar Tamayo):** Todo código de producción **Python 3.12** en `src/` se escribe o revisa en pareja (**Ronny Veloz · I1** + **Oscar Tamayo · I2**, junto con **Analy Yepez · I3** en Parte 1 y **Mateo Yaguari · I4** en Parte 4), rotando **Driver** y **Navigator** cada **30 minutos**. Al finalizar cada historia, **Mateo Yaguari (I4 · Tester)** ejecuta una sesión de *Pair Review / Testing* con `pytest` antes de fusionar a `main`.

## Registro de Sesiones (Plantilla)

| Fecha | Iteración / HU | Parte | Driver (Teclado) | Navigator (Estrategia) | Revisor QA (I4) | Módulo Trabajado & Resultado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `[DD/MM]` | `It.1 / HU-01` | **Parte 1** | I3 (Analy) | I1 (Ronny) | I4 (Mateo) | `AuthService` + `test_auth_service.py` (3 intentos). |
| `[DD/MM]` | `It.1 / HU-02` | **Parte 1** | I3 (Analy) | I2 (Oscar) | I4 (Mateo) | `SistemaRuso.readCoord` + `CoordenadaUK` + `Utility` + `Grupo06.csv`. |
| `[DD/MM]` | `It.1 / HU-04,05` | **Parte 3** | I2 (Oscar) | I1 (Ronny) | I4 (Mateo) | `IHormiga`, `Hormiga`, `HLarva`, `EvolucionStrategy`. |
| `[DD/MM]` | `It.2 / HU-03` | **Parte 2** | I1 (Ronny) | I2 (Oscar) | I4 (Mateo) | `BombaAutomata` (`{2,3,5,9}`) + tabla de destrucción + `AntCiberDron(IIA)`. |
| `[DD/MM]` | `It.2 / HU-06,07,08` | **Parte 3** | I2 (Oscar) | I1 (Ronny) | I4 (Mateo) | Extremidades, `FuenteDePoder`, `Laser`, `ModuloIdioma`. |
| `[DD/MM]` | `It.3 / HU-09,10` | **Parte 4** | I4 (Mateo) | I2 (Oscar) | I3 (Analy) | `UI consola` (`main.py`) + `SQLite` (`sqlite3`) + verificación Docker (`python:3.12-slim`). |

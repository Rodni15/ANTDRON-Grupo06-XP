# 14. Bitácora de Programación por Parejas (Pair Programming — Python 3.12)

**Regla XP del Coach (I2 · Óscar Tamayo):** Todo código de producción **Python 3.12** en `src/` y `web_app.py` se revisa en pareja (**Ronny Veloz · I1**, **Óscar Tamayo · I2**, **Analy Yépez · I3** y **Mateo Yaguari · I4**), rotando **Driver** y **Navigator** cada **30 minutos** en los puntos de integración y realizando revisión cruzada con pruebas antes de fusionar a `main`.

## Registro de Sesiones Realizadas

| Fecha | Iteración / HU | Parte | Driver (Teclado) | Navigator (Estrategia) | Revisor QA (I4) | Módulo Trabajado & Resultado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `17/11` | `It.1 / HU-01` | **Parte 1** | I3 (Analy) | I1 (Ronny) | I4 (Mateo) | `AuthService` + `test_auth_service.py` (3 intentos) — **Mergeado PR #1**. |
| `17/11` | `It.1 / HU-02` | **Parte 1** | I3 (Analy) | I2 (Óscar) | I4 (Mateo) | `SistemaRuso.readCoord` + `CoordenadaUK` + `Utility` + `Grupo06.csv` (40 filas) — **Mergeado PR #1**. |
| `17/11` | `It.2 / HU-03` | **Parte 2** | I1 (Ronny) | I3 (Analy) / I2 (Óscar) | I4 (Mateo) | `BombaAutomata` (`{2,3,5,9}`) + `Bomba.explotar` + `mostrar_destruir` + `test_bomba_automata.py` — **Mergeado PR #2**. |
| `17/11` | `It.2 / HU-04..08` | **Parte 3** | I2 (Óscar) | I1 (Ronny) | I4 (Mateo) | `Alimento`, `Hormiga`/`HLarva`/`HRastreadora`, `AntCiberDron(IIA)`, `ModuloIdioma`, `SqliteConnection` + `test_parte3.py` — **Mergeado PR #3**. |
| `18/11` | `It.3 / HU-09,10` | **Parte 4** | I4 (Mateo) | I2 (Óscar) | I1 (Ronny) | Interfaz web Flask (`web_app.py`, `templates/`, `static/`) + `Dockerfile`/`docker-compose.yml` + `test_web.py` — **Mergeado PR #4**. |
| `18/11` | `It.3 / Regresión` | **Revisión** | I2 (Óscar) | I4 (Mateo) | I1 (Ronny) / I3 (Analy) | Corrección de evaluación individual por fila en `web_app.py`, formulario de idiomas, spinner progresivo y prueba de regresión (`test_resultado_es_individual_por_fila`) — **68 casos en verde (PR #5)**. |

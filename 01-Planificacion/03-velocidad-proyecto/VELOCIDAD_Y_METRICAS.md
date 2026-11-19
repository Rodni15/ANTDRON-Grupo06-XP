# 3. Velocidad del Proyecto y Métricas (Tracker)

**Responsable:** I3 (Tracker) — Analy Yépez · **Revisores:** I2 (Coach) — Óscar Tamayo e I1 (Cliente + Gestor) — Ronny Veloz.

## Cómo se calcula la velocidad
- Estimación en puntos Fibonacci (`1, 2, 3, 5, 8`); **1 punto ≈ 2–3 horas** de trabajo.
- **Fórmula:**
  $$\text{Velocidad} = \frac{\sum \text{puntos de historias aceptadas por el Cliente}}{\text{iteraciones completadas}}$$
- *Regla XP:* solo cuentan las historias **terminadas, con pruebas en verde y aceptadas por I1 (Cliente) e I4 (Tester)**. El trabajo a medias cuenta 0 puntos.

## Tablero de velocidad

| Iteración | Fecha | Puntos planificados | Puntos completados y aceptados | Velocidad acumulada | Observaciones |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Mar 17/11 | 8 | 8 *(aceptadas por I1 · Ronny Veloz y I4 · Mateo Yaguari)* | 8.0 | HU-01 y HU-02 terminadas y aceptadas; 13 pruebas en verde. |
| **2** | Mié 18/11 | 26 | 26 *(aceptadas por I1 · Ronny Veloz y I4 · Mateo Yaguari)* | 17.0 | HU-03 (Parte 2) y HU-04..HU-08 (Parte 3) terminadas y verificadas en pruebas de dominio y web. |
| **3** | Mié 18/11 – Jue 19/11 | 18 | 18 *(HU-09, HU-10, HU-11 aceptadas)* | 17.3 | Interfaz web Flask + 68 casos de prueba en verde + 5 diagramas + documento final. *(Pendiente solo ejecución física de `docker compose up` en entorno con Docker Desktop activo).* |

## Burndown (52 pts → 0)

| Hito | Restantes planificados | Restantes reales | Estado |
| :--- | :---: | :---: | :--- |
| Inicio del proyecto (17/11) | 52 | 52 | ✅ |
| Fin Iteración 1 (17/11) | 44 | 44 | ✅ En plan |
| Fin Iteración 2 (18/11, 20:00) | 18 | 18 | ✅ En plan |
| Fin Iteración 3 (18/11 cierre / 19/11 entrega) | 0 | 0 | ✅ Aceptado por Cliente (I1) y Tester (I4) |

## Avance por historia

| HU | Título | Pts | Responsable | Estado | Pruebas |
| :--- | :--- | :---: | :--- | :--- | :--- |
| HU-01 | Inicio de sesión seguro | 3 | Analy | ✅ Aceptada (I1 / I4) | `test_auth_service.py`, `test_sistema_ruso.py`, `test_web.py` |
| HU-02 | Datos del equipo y lectura de `Grupo06.csv` | 5 | Analy | ✅ Aceptada (I1 / I4) | `test_sistema_ruso.py`, `test_utility.py`, `test_arsenal_catalogo.py`, `test_web.py` |
| HU-03 | Bomba con autómata (`IIA.buscar`) | 5 | Ronny | ✅ Aceptada (I3 / I4) | `test_bomba_automata.py`, `test_parte3.py`, `test_web.py` |
| HU-04 | Nacimiento como `HLarva` | 3 | Óscar | ✅ Aceptada (I1 / I4) | `test_parte3.py`, `test_web.py` |
| HU-05 | Metamorfosis por alimento | 5 | Óscar | ✅ Aceptada (I1 / I4) | `test_parte3.py`, `test_web.py` |
| HU-06 | Ensamblaje del `AntCiberDron` | 5 | Óscar | ✅ Aceptada (I1 / I4) | `test_parte3.py`, `test_web.py` |
| HU-07 | Fuente de poder con `IIA` | 3 | Óscar | ✅ Aceptada (I1 / I4) | `test_parte3.py`, `test_web.py` |
| HU-08 | Idiomas con expertos parlantes | 5 | Óscar | ✅ Aceptada (I1 / I4) | `test_parte3.py`, `test_web.py` |
| HU-09 | Hormiguero Virtual (Web Flask + SQLite) | 8 | Mateo | ✅ Aceptada (I1 / I4) | `test_web.py` (8 pruebas HTTP completas) |
| HU-10 | Docker sin incidentes | 5 | Mateo | ✅ Aceptada (config + tests; falta `up` físico) | `Dockerfile`, `docker-compose.yml`, 68 casos en verde |
| HU-11 | 5 diagramas, bitácoras XP y doc. final | 5 | Todos (cierra Ronny) | ✅ Aceptada (I1 / I4) | 5 diagramas PlantUML + `DOCUMENTO_FINAL_GRUPO06.md` |

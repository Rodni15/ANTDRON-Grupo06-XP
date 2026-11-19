# 6. Actas y Protocolo de Reuniones XP

> Aquí se registran las reuniones del equipo de 4 integrantes (**I1 · Ronny Veloz** [Parte 2 · Cliente/Gestor], **I2 · Oscar Tamayo** [Parte 3 · Coach/Prog1], **I3 · Analy Yepez** [Parte 1 · Tracker/Prog2], **I4 · Mateo Yaguari** [Parte 4 · Tester]) para el proyecto ANTDRON en **Python 3.12** (`pytest`, `sqlite3` y Docker).

---

## Registro 1: Planning Game — Iteración 1
- **Fecha:** 17/11/2026 · **Modalidad:** grupo de mensajería (encuesta de partes)
- **Participantes:** Ronny Veloz (I1), Oscar Tamayo (I2), Analy Yepez (I3), Mateo Yaguari (I4).
- **Acuerdos:**
  - Lenguaje Python 3.12 y diagramas en PlantUML; repositorio `Rodni15/ANTDRON-Grupo06-XP` con ramas `feature/parteN-...` y Pull Request revisado por Mateo (I4).
  - División por partes: Analy (1 · login, equipo y CSV), Ronny (2 · autómata y documento), Oscar (3 · hormigas y AntCiberDron), Mateo (4 · pantallas y Docker).
  - Roles XP según la parte de cada uno: Ronny Cliente + Gestor, Oscar Coach + Programador 1, Analy Tracker + Programador 2, Mateo Tester.
  - Lenguaje de la bomba con los últimos dígitos {2, 3, 5, 9}: $L = \{ab^*,\ abc,\ abcdt^+\}$.
- **Historias de la Iteración 1:** HU-01, HU-02.
- **Riesgos:** tipo de hormiga del Grupo 6 (no aparece en la tabla del PDF); carga alta de la Parte 3.
- **Plazo:** cada parte se sube al repositorio hasta el miércoles 18/11 a las 20:00; presentación el jueves 19/11.

---

## Registro 2: Validación de Iteración 1 e Inicio / Avance de Iteración 2 (Parte 2)
- **Fecha:** 17/11/2026 – 18/11/2026 · **Participantes:** Ronny Veloz (I1 · Cliente/Gestor), Óscar Tamayo (I2 · Coach/Prog1), Analy Yépez (I3 · Tracker/Prog2), Mateo Yaguari (I4 · Tester).
- **Validación del Cliente (I1 · Ronny Veloz) de la Iteración 1:**
  - `HU-01` (Login 3 intentos + `patmic`/`123`): **ACEPTADA** (3 pts).
  - `HU-02` (Presentación `[+] TEAM [6]` + lectura animada de `data/Grupo06.csv` con 40 filas): **ACEPTADA** (5 pts).
- **Avance de Iteración 2 — Parte 2 (`HU-03`, `HU-11`):**
  - Se implementó `BombaAutomata` (`Automata`), `Bomba` y `mostrar_destruir` en `src/ant/iia/` siguiendo la tabla de transición $\delta$ de $\{2, 3, 5, 9\}$ ($L = \{ab^*, abc, abcdt^+\}$).
  - Suite `tests/ant/iia/test_bomba_automata.py` en verde (incluye validación exhaustiva contra oráculo `re.fullmatch` y prueba real con las 40 filas de `data/Grupo06.csv`, detonando 29 objetivos).
  - Se dejó listo el documento consolidado base en `docs-analisis/DOCUMENTO_FINAL_GRUPO06.md` con portada, metáfora y roles para integrar las Partes 3 y 4.

---

## Registro 3: Integración Partes 3 y 4, Revisión de Cumplimiento y Aceptación Final
- **Fecha:** 18/11/2026 · **Participantes:** Ronny Veloz (I1 · Cliente/Gestor), Óscar Tamayo (I2 · Coach/Prog1), Analy Yépez (I3 · Tracker/Prog2), Mateo Yaguari (I4 · Tester).
- **Resultados verificados en `main` (`PR #3`, `PR #4`, `PR #5`):**
  - **Parte 3 (`HU-04`..`HU-08` — Óscar):** Implementada jerarquía `Hormiga`/`Alimento`, metamorfosis `HLarva` + `AHervivoro` $\rightarrow$ `HRastreadora`, `AntCiberDron(IIA)` conectado a `Bomba`, `ModuloIdioma` con `ExpertoParlante` y `SqliteConnection` (`data/antdron.db`), más diagramas PNG de Clases y MER. **ACEPTADA** por I1 e I4.
  - **Parte 4 (`HU-09`, `HU-10` — Mateo + revisión PR #5):** Implementada aplicación web Flask (`web_app.py`), corregida evaluación individual por fila (`29` autorizadas de `40`), tabla separada de destrucción, animación progresiva, formulario EN/ES y pruebas web (`tests/test_web.py`). **68 casos de prueba en verde**. **ACEPTADA** por I1 e I4 (con nota de ejecutar `docker compose up` en máquina con Docker Desktop activo).
  - **Cierre (`HU-11` — Ronny + equipo):** Completado [DOCUMENTO_FINAL_GRUPO06.md](../../docs-analisis/DOCUMENTO_FINAL_GRUPO06.md), actualizadas las tarjetas HU, matriz TDD, tablero de velocidad y firmada [CHECKLIST_ACEPTACION_CLIENTE.md](../../04-Pruebas/02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md).
- **Acuerdo de mejora (Retrospectiva):** Validar resultados individuales por fila y pruebas de regresión HTTP antes de hacer merge a `main`.

---

## Plantilla 1: Planning Game (Inicio de Iteración)
- **Iteración:** `[1 / 2 / 3]` · **Fecha:** `[DD/MM/AAAA]` · **Duración:** `45 min`
- **Participantes:** Analy Yepez (I3), Ronny Veloz (I1), Oscar Tamayo (I2), Mateo Yaguari (I4).
- **Velocidad de referencia:** `[16 / promedio real]` pts.
- **Historias seleccionadas por I1 (Ronny Veloz · Cliente):** `[Ej. HU-01, HU-02, HU-04, HU-05]`.
- **Riesgos identificados:** `[Ej. Confirmar grupo 6 con el docente; formato exacto del loading en Docker]`.
- **Compromiso del equipo:** Ninguna historia pasa a terminada sin pruebas TDD en verde y aceptación de Ronny (I1) + Mateo (I4).

---

## Plantilla 2: Daily Stand-up (Diario — 10 minutos)

| Fecha | Integrante | ¿Qué hice ayer? | ¿Qué haré hoy? | Bloqueos detectados |
| :--- | :--- | :--- | :--- | :--- |
| `[DD/MM]` | **I3 · Analy Yepez** *(Parte 1 · Tracker/Prog2)* | `[Ej. Redacté criterios de HU-02]` | `[Ej. Generar Grupo06.csv y Casos de Uso]` | `[Ninguno]` |
| `[DD/MM]` | **I1 · Ronny Veloz** *(Parte 2 · Cliente/Gestor)* | `[Ej. Grafo y Gramática {2,3,5,9}]` | `[Ej. Implementar BombaAutomata]` | `[Confirmar estrategia Grupo 6]` |
| `[DD/MM]` | **I2 · Oscar Tamayo** *(Parte 3 · Coach/Prog1)* | `[Ej. Diagrama de Clases y MER]` | `[Ej. Implementar Hormiga/HLarva/Dron]` | `[Ninguno]` |
| `[DD/MM]` | **I4 · Mateo Yaguari** *(Parte 4 · Tester)* | `[Ej. Tests pytest + Arquitectura]` | `[Ej. Pantallas Hormiguero y Docker]` | `[Probar TTY en Docker]` |

---

## Plantilla 3: Validación con el Cliente y Retrospectiva (Fin de Iteración)
- **Iteración:** `[1 / 2 / 3]` · **Fecha:** `[DD/MM/AAAA]`
- **Resultados presentados por I3 (Tracker):**
  - Puntos comprometidos: `[X]` · Puntos aceptados por I1: `[Y]` · Velocidad resultante: `[Y]`
- **Decisiones de aceptación (I1 + I4):**
  - `[HU-XX]`: **ACEPTADA / RECHAZADA** — Observaciones: `[...]`
- **Retrospectiva (2 cosas bien hechas / 2 mejoras para la próxima iteración):**
  1. **Mantener:** `[Ej. Rotar Driver/Navigator cada 30 min redujo errores en el autómata]`
  2. **Mejorar:** `[Ej. Escribir primero el test antes de tocar los menús o SQLite]`

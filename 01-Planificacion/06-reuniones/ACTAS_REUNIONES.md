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

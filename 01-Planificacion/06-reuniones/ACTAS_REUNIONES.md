# 6. Actas y Protocolo de Reuniones XP

> Aquí se registran las reuniones del equipo de 4 integrantes (**I1 · Analy Yepez** [Parte 1 · Cliente/Gestor], **I2 · Ronny Veloz** [Parte 2 · Coach/Prog1], **I3 · Oscar Tamayo** [Parte 3 · Tracker/Prog2], **I4 · Mateo Yaguari** [Parte 4 · Tester]) para el proyecto ANTDRON en **Python 3.12** (`pytest`, `sqlite3` y Docker).

---

## Plantilla 1: Planning Game (Inicio de Iteración)
- **Iteración:** `[1 / 2 / 3]` · **Fecha:** `[DD/MM/AAAA]` · **Duración:** `45 min`
- **Participantes:** Analy Yepez (I1), Ronny Veloz (I2), Oscar Tamayo (I3), Mateo Yaguari (I4).
- **Velocidad de referencia:** `[16 / promedio real]` pts.
- **Historias seleccionadas por I1 (Analy Yepez · Cliente):** `[Ej. HU-01, HU-02, HU-04, HU-05]`.
- **Riesgos identificados:** `[Ej. Confirmar grupo 6 con el docente; formato exacto del loading en Docker]`.
- **Compromiso del equipo:** Ninguna historia pasa a terminada sin pruebas TDD en verde y aceptación de Analy (I1) + Mateo (I4).

---

## Plantilla 2: Daily Stand-up (Diario — 10 minutos)

| Fecha | Integrante | ¿Qué hice ayer? | ¿Qué haré hoy? | Bloqueos detectados |
| :--- | :--- | :--- | :--- | :--- |
| `[DD/MM]` | **I1 · Analy Yepez** *(Parte 1 · Cliente/Gestor)* | `[Ej. Redacté criterios de HU-02]` | `[Ej. Generar Grupo06.csv y Casos de Uso]` | `[Ninguno]` |
| `[DD/MM]` | **I2 · Ronny Veloz** *(Parte 2 · Coach/Prog1)* | `[Ej. Grafo y Gramática {2,3,5,9}]` | `[Ej. Implementar BombaAutomata]` | `[Confirmar estrategia Grupo 6]` |
| `[DD/MM]` | **I3 · Oscar Tamayo** *(Parte 3 · Tracker/Prog2)* | `[Ej. Diagrama de Clases y MER]` | `[Ej. Implementar Hormiga/HLarva/Dron]` | `[Ninguno]` |
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

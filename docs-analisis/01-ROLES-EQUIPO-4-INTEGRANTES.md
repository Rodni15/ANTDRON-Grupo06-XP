# Roles XP del Equipo (4 Integrantes) y Protocolo de Colaboración

**Fecha:** `[PENDIENTE: DD/MM/AAAA]` | **#Grupo:** `06` | **Lenguaje:** `Python 3.12` | **Diagramas:** `PlantUML` | **Metáfora:** `[PENDIENTE: Nombre del Equipo]`

> A diferencia de `WORKSHOP-XP.md` (planteado para 6 personas y con el profesor como único Cliente), este proyecto en **Python 3.12** se adapta a **4 integrantes reales** cubriendo exactamente los **7 roles XP solicitados**: **Cliente (uno de nosotros)**, **Gestor**, **Coach**, **Tracker**, **2 Programadores** y **Tester**.

---

## 1. Registro Oficial del Equipo (Formato Portada PDF)

| # | Cédula | Apellido y Nombre | Roles XP Asignados | Último Dígito (Autómata) |
| :---: | :--- | :--- | :--- | :---: |
| **I1** | `[Cédula 1]` | `[Apellido y Nombre 1]` | **Cliente (KGD)** + **Gestor (Big Boss)** | `[D1]` |
| **I2** | `[Cédula 2]` | `[Apellido y Nombre 2]` | **Coach XP** + **Programador 1** | `[D2]` |
| **I3** | `[Cédula 3]` | `[Apellido y Nombre 3]` | **Tracker (Rastreador)** + **Programador 2** | `[D3]` |
| **I4** | `[Cédula 4]` | `[Apellido y Nombre 4]` | **Tester** *(+ Apoyo en Pair Review & QA/Docker)* | `[D4]` |

> **Nota sobre el Docente (`patmic`) y Expertos Parlantes:**
> - **El Cliente XP operativo es I1** (miembro activo del equipo disponible en todo momento para priorizar historias, resolver dudas de reglas y firmar aceptación). El docente `patmic` funge como *Sponsor / Evaluador final* y usuario con credenciales `patmic` / `123`.
> - **Expertos Parlantes (EN/ES):** En el dominio del software (`ExpertoParlante`), el entrenamiento de léxico, gramática y fonética solo acepta entradas provenientes de objetos/actores `ExpertoParlante` certificados en inglés o español (durante las pruebas de aceptación, I1/I4 simulan o invitan a los expertos para validar el flujo).

---

## 2. Matriz Detallada de Responsabilidades (7 Roles en 4 Personas)

| Rol XP | Titular | ¿Qué hace dentro de la metodología XP? | Artefactos / Carpetas bajo su custodia |
| :--- | :---: | :--- | :--- |
| **Cliente (KGD)** | **I1** | Escribe las tarjetas de Historias de Usuario simples, prioriza qué entra en cada release/iteración, responde dudas de negocio al instante (*Disponibilidad del cliente*) y valida/firma las Pruebas de Aceptación. | `01-Planificacion/01-historias-usuario/`, `03-Desarrollo/01-disponibilidad-cliente/`, `04-Pruebas/02-pruebas-aceptacion/` |
| **Gestor (Big Boss)** | **I1** | Coordina tiempos de iteración, resuelve bloqueos logísticos, custodia el repositorio Git, organiza las reuniones y asegura el cumplimiento de los 5 diagramas en PlantUML y la entrega sin penalizaciones (`-0.5`). | `01-Planificacion/02-plan-entregas/`, `01-Planificacion/06-reuniones/`, `04-Pruebas/01-implantacion/` |
| **Coach XP** | **I2** | Garantiza que el equipo aplique disciplina XP en Python 3.12: ciclo TDD (`pytest`), cambios de Driver/Navigator cada 30 min, tarjetas CRC antes de codificar, Metáfora consistente y Reciclaje continuo. | `02-Diseno/` (Metáfora, CRC, Spikes, Reciclaje), `03-Desarrollo/03-programacion-parejas/` |
| **Tracker** | **I3** | Mide la velocidad real del equipo (`puntos aceptados / iteración`), registra el avance diario en el tablero, actualiza el burndown y controla las rotaciones de roles y módulos. | `01-Planificacion/03-velocidad-proyecto/`, `01-Planificacion/04-iteraciones/`, `01-Planificacion/05-rotaciones/` |
| **Programador 1** | **I2** | Programa en pareja con I3 en Python 3.12 (`abc.ABC`). Lidera arquitectura del contrato `pkAntCiberDronContract`, `Autómata/IIA` y `AntCiberDron`. | `src/pkAntCiberDronContract/`, `src/ant/iia/`, `src/ant/dron/` |
| **Programador 2** | **I3** | Programa en pareja con I2 en Python 3.12. Lidera `SistemaRuso`, `Jerarquía Hormiga/Alimento`, persistencia SQLite (`sqlite3`) y `UI consola` del Hormiguero. | `src/ant/ruso/`, `src/ant/hormiguero/`, `src/ant/ui/`, `src/ant/db/` |
| **Tester** | **I4** | Redacta las pruebas de aceptación con I1 (Cliente), mantiene la suite unitaria `pytest` junto a I2+I3, valida la cobertura TDD, administra GitHub Actions (`CI`) y certifica Docker `python:3.12-slim` (`-0.5` cero fallos). | `03-Desarrollo/02-unidad-pruebas-tdd/`, `03-Desarrollo/04-integracion-continua/`, `04-Pruebas/`, `tests/` |

---

## 3. Reglas Anti-Sesgo y Prevención de Islas de Conocimiento

Al combinar roles en 4 personas, aplicamos 3 reglas XP estrictas:
1. **Separación Cliente/Tester vs Programadores:** Quien codifica (`I2 + I3`) **no aprueba solo** su propia historia; **I4 (Tester)** ejecuta la verificación técnica/CI y **I1 (Cliente)** valida el criterio de negocio antes del merge.
2. **Pareja activa única + Rotación de revisión:** `I2` y `I3` rotan Driver/Navigator cada **30 minutos**. Al finalizar cada historia, **I4** realiza una sesión de *Pair Testing / Code Review* con uno de los programadores para dominar también los módulos.
3. **Propiedad colectiva del código:** Cualquier miembro puede corregir o refactorizar cualquier clase siempre que pasen todas las pruebas pytest y se documente en `02-Diseno/05-reciclaje/`.

---

## 4. Protocolo de Reuniones entre los 4 Integrantes

| Reunión | Participantes | Frecuencia | Objetivo concreto en AntCiberDron |
| :--- | :--- | :--- | :--- |
| **Planning Game** | I1 (Cliente+Gestor) + I2 (Coach+Prog1) + I3 (Tracker+Prog2) + I4 (Tester) | Inicio de cada iteración (45 min) | I1 prioriza HU; I2+I3 estiman puntos; I3 calcula capacidad según velocidad; I4 define criterios medibles. |
| **Daily Stand-up** | Todos (I1, I2, I3, I4) | Diario (10 min de pie/llamada) | ¿Qué hice ayer? ¿Qué haré hoy? ¿Qué bloqueo hay (autómata, CSV, menús, Docker)? I3 actualiza el tablero. |
| **Sesión CRC & Diseño Simple** | I2 (Coach+Prog1) + I3 (Prog2) + I4 (Tester) | Antes de cada módulo nuevo | Definir responsabilidades/colaboradores en tarjetas CRC y validar el contrato `pkAntCiberDronContract`. |
| **Revisión / Aceptación** | I1 (Cliente) + I4 (Tester) + I2/I3 (demo) | Fin de iteración (30 min) | Demostración funcional en consola y Docker; I1 marca *Aceptada* o *Rechazada*. |
| **Retrospectiva** | Todos (I1, I2, I3, I4), modera I2 (Coach) | Fin de iteración (20 min) | I3 presenta métricas de velocidad; el equipo acuerda 2 mejoras concretas para la siguiente iteración. |

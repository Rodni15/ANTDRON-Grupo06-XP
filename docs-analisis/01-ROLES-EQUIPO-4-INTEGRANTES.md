# Roles XP del Equipo (4 Integrantes) y Repartición por Partes

**Fecha:** `[DD/MM/AAAA]` | **#Grupo:** `06` | **Lenguaje:** `Python 3.12` | **Diagramas:** `PlantUML` | **Metáfora:** `Hormiguero Cibernético`

> Este proyecto se organiza con **4 integrantes reales** cubriendo los **7 roles XP** (**Cliente**, **Gestor**, **Coach**, **Tracker**, **2 Programadores** y **Tester**) y repartiendo el desarrollo y entregables en **4 Partes coordinadas**.

---

## 1. Registro Oficial del Equipo (Formato Portada PDF)

| # | Cédula | Apellido y Nombre | Roles XP Asignados | Parte Asignada | Último Dígito (Autómata) |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **I1** | `1721396412` | **Yepez Analy** | **Cliente (KGD)** + **Gestor (Big Boss)** | **Parte 1:** Login, equipo y CSV | `2` (`Coord-02` · `ab*`) |
| **I2** | `1724490055` | **Veloz Ronny** | **Coach XP** + **Programador 1** | **Parte 2:** Autómata y documento | `5` (`Coord-05` · `abcdt+`) |
| **I3** | `1722578703` | **Tamayo Oscar** | **Tracker (Rastreador)** + **Programador 2** | **Parte 3:** Hormigas y `AntCiberDron` | `3` (`Coord-03` · `abc`) |
| **I4** | `1726389099` | **Yaguari Mateo** | **Tester** *(QA / CI / Docker)* | **Parte 4:** Pantallas (`main.py`) y Docker | `9` (`Coord-09` · `ab*`) |

> **Nota sobre el Docente (`patmic`) y Expertos Parlantes:**
> - **El Cliente XP operativo es Analy Yepez (I1)** (miembro activo del equipo disponible para priorizar historias, resolver dudas de reglas y firmar aceptación). El docente `patmic` funge como *Sponsor / Evaluador final* y usuario con credenciales `patmic` / `123`.
> - **Expertos Parlantes (EN/ES):** En el dominio del software (`ExpertoParlante`), el entrenamiento de léxico, gramática y fonética solo acepta entradas provenientes de objetos/actores `ExpertoParlante` certificados en inglés o español.

---

## 2. Matriz Detallada de Responsabilidades (7 Roles y 4 Partes)

| Rol XP | Titular | Parte | ¿Qué hace dentro de la metodología XP y del código? | Artefactos / Carpetas bajo su custodia |
| :--- | :--- | :---: | :--- | :--- |
| **Cliente (KGD) + Gestor (Big Boss)** | **I1 · Analy Yepez** | **Parte 1** | Implementa Login (máx. 3 intentos: grupo + `patmic`/`123`), presentación del equipo y lectura de `Grupo06.csv` con animación de carga; coordina entregas de coordenadas hacia Parte 3, prioriza HU y firma aceptación. | `src/ant/ruso/`, `src/pkAntCiberDronContract/` (`SistemaRuso`, `CoordenadaUK`, `Utility`), `data/Grupo06.csv`, `02-Diseno/diagramas/02-diagrama-casos-de-uso.md`, `01-Planificacion/01-historias-usuario/`, `03-Desarrollo/01-disponibilidad-cliente/` |
| **Coach XP + Programador 1** | **I2 · Ronny Veloz** | **Parte 2** | Implementa `BombaAutomata` (`ab* ∪ abc ∪ abcdt+` de las 4 cédulas), lógica de detonación e impresión de tabla de coordenadas a destruir; vela por las prácticas XP, elabora portada/roles, Grafo + Gramática del Autómata y consolida el documento final. | `src/ant/iia/` (`BombaAutomata`), `02-Diseno/diagramas/03-automata-grafo-gramatica.md`, `02-Diseno/` (Metáfora, CRC, Spikes, Reciclaje), `03-Desarrollo/03-programacion-parejas/`, documento final |
| **Tracker + Programador 2** | **I3 · Oscar Tamayo** | **Parte 3** | Implementa jerarquía `Hormiga` (`HLarva`, `HRastreadora`, etc.), `Alimento`, `IIA`, `AntCiberDron` (extremidades, metralleta, láser, turbo reactor, fuente con `IIA`, idiomas con expertos) y DAOs SQLite (`sqlite3`); elabora Diagrama de Clases y MER; mide velocidad y burndown. | `src/ant/hormiguero/`, `src/ant/alimento/`, `src/ant/dron/`, `src/ant/db/`, `src/resources/`, `02-Diseno/diagramas/01-diagrama-clases.md`, `02-Diseno/diagramas/04-modelo-entidad-relacion.md`, `01-Planificacion/03-velocidad-proyecto/`, `01-Planificacion/05-rotaciones/` |
| **Tester (QA / CI / Docker)** | **I4 · Mateo Yaguari** | **Parte 4** | Implementa pantallas de consola del Hormiguero Virtual (`Hormiguero.crear_hormiga()`, `listar()`) y flujo completo en `main.py`; dockeriza (`Dockerfile`, `docker-compose.yml`), mantiene suite `pytest` y GitHub Actions (`CI`), elabora Diagrama de Arquitectura y certifica 0 incidentes (`-0.5`). | `src/ant/ui/`, `main.py`, `tests/`, `Dockerfile`, `docker-compose.yml`, `.github/workflows/ci.yml`, `02-Diseno/diagramas/05-arquitectura-aplicacion.md`, `03-Desarrollo/02-unidad-pruebas-tdd/`, `03-Desarrollo/04-integracion-continua/`, `04-Pruebas/` |

---

## 3. Reglas Anti-Sesgo y Prevención de Islas de Conocimiento

Al combinar roles en 4 personas, aplicamos 3 reglas XP estrictas:
1. **Separación Cliente/Tester vs Programadores:** Quien codifica **no aprueba solo** su propia historia; **Mateo Yaguari (I4 · Tester)** ejecuta la verificación técnica/CI y **Analy Yepez (I1 · Cliente)** valida el criterio de negocio antes del merge.
2. **Pareja activa + Rotación de revisión:** **Ronny Veloz (I2)** y **Oscar Tamayo (I3)** rotan Driver/Navigator cada **30 minutos** en las partes críticas de dominio/autómata; **Analy (I1)** y **Mateo (I4)** coordinan entradas/salidas en consola y pruebas cruzadas.
3. **Propiedad colectiva del código:** Cualquier miembro puede corregir o refactorizar cualquier clase siempre que pasen todas las pruebas `pytest` y se documente en `02-Diseno/05-reciclaje/`.

---

## 4. Protocolo de Reuniones entre los 4 Integrantes

| Reunión | Participantes | Frecuencia | Objetivo concreto en AntCiberDron |
| :--- | :--- | :--- | :--- |
| **Planning Game** | Analy (I1) + Ronny (I2) + Oscar (I3) + Mateo (I4) | Inicio de cada iteración (45 min) | I1 prioriza HU; I2+I3 estiman puntos; I3 calcula capacidad según velocidad; I4 define criterios medibles. |
| **Daily Stand-up** | Todos (Analy, Ronny, Oscar, Mateo) | Diario (10 min de pie/llamada) | ¿Qué hice ayer? ¿Qué haré hoy? ¿Qué bloqueo hay (CSV, autómata, dron, Docker)? I3 actualiza el tablero. |
| **Sesión CRC & Diseño Simple** | Ronny (I2) + Oscar (I3) + Mateo (I4) | Antes de cada módulo nuevo | Definir responsabilidades/colaboradores en tarjetas CRC y validar el contrato `pkAntCiberDronContract`. |
| **Revisión / Aceptación** | Analy (I1) + Mateo (I4) + Ronny/Oscar (demo) | Fin de iteración (30 min) | Demostración funcional en consola y Docker; I1 marca *Aceptada* o *Rechazada*. |
| **Retrospectiva** | Todos, modera Ronny (I2 · Coach) | Fin de iteración (20 min) | I3 presenta métricas de velocidad; el equipo acuerda 2 mejoras concretas para la siguiente iteración. |

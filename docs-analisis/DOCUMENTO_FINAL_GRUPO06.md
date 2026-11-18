# Documento Final Consolidado — Proyecto ANTDRON / AntCiberDron (Grupo 06)

> **Escuela Politécnica Nacional (EPN) · Facultad de Ingeniería en Informática · Metodologías Ágiles**  
> **Documento consolidado por:** **Ronny Veloz (`I1` · Cliente + Gestor · Parte 2)**

---

## 1. Portada Oficial (Formato Enunciado PDF)

- **Fecha de Entrega:** `19/11/2026`
- **Número de Grupo:** `06`
- **Nombre del Equipo / Metáfora del Sistema:** `Hormiguero Cibernético`
- **Lenguaje y Stack Tecnológico:** `Python 3.12` · `SQLite (sqlite3)` · `pytest` · `Docker (python:3.12-slim)` · `PlantUML`

### Registro Oficial de Integrantes, Roles XP y Partes

| # | Cédula | Apellido y Nombre | Usuario | Roles XP Asignados | Parte Desarrollada | Último Dígito (Autómata) |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: |
| **I1** | `1724490055` | **Veloz Ronny** | `rveloz` | **Cliente (KGD)** + **Gestor** | **Parte 2:** Autómata, Bomba y documento final | `5` (`Coord-05` · `abcdt+`) |
| **I2** | `1722578703` | **Tamayo Óscar** | `otamayo` | **Coach XP** + **Programador 1** | **Parte 3:** Hormigas, `AntCiberDron` y SQLite | `3` (`Coord-03` · `abc`) |
| **I3** | `1721396412` | **Yépez Analy** | `ayepez` | **Tracker** + **Programadora 2** | **Parte 1:** Login, equipo y `Grupo06.csv` | `2` (`Coord-02` · `ab*`) |
| **I4** | `1726389099` | **Yaguari Mateo** | `myaguari` | **Tester** *(QA / CI / Docker)* | **Parte 4:** Pantallas (`main.py`) y Docker | `9` (`Coord-09` · `ab*`) |

- **Usuario administrativo evaluador:** `patmic` / `123`.

---

## 2. Parte 1 — Login, Equipo, `Grupo06.csv` y Casos de Uso *(Analy Yépez · I3)*

### 2.1. Resumen de Implementación (`HU-01`, `HU-02`)
- **Autenticación (`src/ant/ruso/auth_service.py` y `SistemaRuso.login`):** Permite hasta 3 intentos para cualquiera de los 4 integrantes (`ayepez`, `rveloz`, `otamayo`, `myaguari` con clave `123`) o el docente (`patmic` / `123`). Al tercer intento fallido bloquea el acceso y cierra limpiamente sin excepciones.
- **Presentación del equipo (`SistemaRuso.mostrarEquipo`):** Imprime `[+] TEAM [6]: Hormiguero Cibernético` junto con la cédula y nombre de los 4 alumnos desde `data/integrantes.json`.
- **Lectura de `data/Grupo06.csv` (`SistemaRuso.readCoord` + `Utility`):** Lee las **40 filas** generadas a partir de los 40 dígitos de las 4 cédulas del grupo, animando el spinner `\ | / -` de `0%` a `100%` antes de imprimir cada coordenada.

### 2.2. Diagrama Obligatorio 2: Diagrama de Casos de Uso
- Ver archivo completo y gráfico en [`02-Diseno/diagramas/02-diagrama-casos-de-uso.md`](../02-Diseno/diagramas/02-diagrama-casos-de-uso.md) y [`02-Diseno/diagramas/img/02-casos-de-uso.png`](../02-Diseno/diagramas/img/02-casos-de-uso.png).

---

## 3. Parte 2 — Autómata de la Bomba, Gramática y Tabla de Destrucción *(Ronny Veloz · I1)*

### 3.1. Definición Formal del Autómata $A = (Q, \Sigma, \delta, q_0, F)$ (`HU-03`)
A partir de los últimos dígitos de las 4 cédulas (`{2, 3, 5, 9}`), el lenguaje unido que hace explotar la bomba es:
$$L = \{ \text{ab}^*, \; \text{abc}, \; \text{abcdt}^+ \}$$
sobre el alfabeto de arsenal bélico $\Sigma = \{ a \text{ (Avión)}, b \text{ (Barco)}, c \text{ (Convoy)}, d \text{ (Dron)}, t \text{ (Tanque)} \}$.

- **Conjunto de estados:** $Q = \{ q_0, q_1, q_2, q_{2b}, q_3, q_4, q_5, q_{\text{err}} \}$
- **Estado inicial:** $q_0$
- **Estados de aceptación:** $F = \{ q_1, q_2, q_{2b}, q_3, q_5 \}$

| Estado | `a` | `b` | `c` | `d` | `t` | ¿Acepta? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`q0` *(inicial)*** | `q1` | `q_err` | `q_err` | `q_err` | `q_err` | No |
| **`q1`** | `q_err` | `q2` | `q_err` | `q_err` | `q_err` | **Sí** (`a`) |
| **`q2`** | `q_err` | `q2b` | `q3` | `q_err` | `q_err` | **Sí** (`ab`) |
| **`q2b`** | `q_err` | `q2b` | `q_err` | `q_err` | `q_err` | **Sí** (`abb+`) |
| **`q3`** | `q_err` | `q_err` | `q_err` | `q4` | `q_err` | **Sí** (`abc`) |
| **`q4`** | `q_err` | `q_err` | `q_err` | `q_err` | `q5` | No |
| **`q5`** | `q_err` | `q_err` | `q_err` | `q_err` | `q5` | **Sí** (`abcdt+`) |
| **`q_err` *(pozo)*** | `q_err` | `q_err` | `q_err` | `q_err` | `q_err` | No |

### 3.2. Diagrama Obligatorio 3: Grafo y Gramática Regular del Autómata
- Ver archivo completo en [`02-Diseno/diagramas/03-automata-grafo-gramatica.md`](../02-Diseno/diagramas/03-automata-grafo-gramatica.md) y fuente PlantUML en [`02-Diseno/diagramas/img/03-automata.puml`](../02-Diseno/diagramas/img/03-automata.puml).
- **Gramática Regular $G = (V_N, V_T, P, S)$:**
  - $S \rightarrow aA \mid a$
  - $A \rightarrow bB \mid b$
  - $B \rightarrow bB_2 \mid b \mid cC \mid c$
  - $B_2 \rightarrow bB_2 \mid b$
  - $C \rightarrow dD$
  - $D \rightarrow tE \mid t$
  - $E \rightarrow tE \mid t$

### 3.3. Clases y Métodos Implementados (`src/ant/iia/`)
- **`BombaAutomata` / `Automata`** (`src/ant/iia/bomba_automata.py`):
  - `aceptar(cadena: str) -> bool` y `evaluar(palabra: str) -> bool`: evalúan la cadena sobre la tabla $\delta$ sin expresiones regulares.
- **`Bomba` y `mostrar_destruir`** (`src/ant/iia/bomba.py`):
  - `Bomba(automata).explotar(palabra: str) -> bool` (y alias `buscar(tipoArsenal: str) -> bool`).
  - `mostrar_destruir(coordenadas, evaluador=None) -> list[CoordenadaUK]`: evalúa las 40 coordenadas de `data/Grupo06.csv`, imprime la tabla `COORDENADAS UCRANIANAS A DESTRUIR` y retorna las **29 coordenadas detonadas (`true`)** (rechazando las 11 filas cuyos arsenales son `aa`, `aaa`, `aaaa`, `abcd`, `abcdd`, `abcddd`).

---

## 4. Parte 3 — Hormigas, `AntCiberDron`, SQLite, Clases y MER *(Óscar Tamayo · I2)*

> *[Sección reservada para integrar el entregable de Óscar Tamayo (Parte 3)]*

- **Código (`HU-04` a `HU-08`):**
  - Jerarquía `Hormiga` (`IHormiga.comer`), `HLarva` y evolución del grupo con `Alimento` (`Nectar`, `ACarnivoro`, `AOmnivoro`, `AHervivoro`).
  - `AntCiberDron(IIA)` con extremidades de hormiga (metralleta derecha, láser izquierdo dependiente de la energía, turbo reactor en espalda, `FuenteDePoder` recargable/reemplazable con asistencia de `IIA` y entrenamiento de idiomas exclusivo con `ExpertoParlante`).
  - Persistencia en SQLite (`src/ant/db/`).
- **Diagrama Obligatorio 1 — Diagrama de Clases:** [`02-Diseno/diagramas/01-diagrama-clases.md`](../02-Diseno/diagramas/01-diagrama-clases.md).
- **Diagrama Obligatorio 4 — Modelo Entidad-Relación (MER):** [`02-Diseno/diagramas/04-modelo-entidad-relacion.md`](../02-Diseno/diagramas/04-modelo-entidad-relacion.md).

---

## 5. Parte 4 — Pantallas del Hormiguero Virtual, `main.py`, Docker y Arquitectura *(Mateo Yaguari · I4)*

> *[Sección reservada para integrar el entregable de Mateo Yaguari (Parte 4)]*

- **Código (`HU-09`, `HU-10`):**
  - Pantallas de consola del Hormiguero Virtual (`src/ant/ui/`, `Hormiguero.crear_hormiga()`, `Hormiguero.listar()`).
  - Flujo completo integrado en `main.py` (`login -> equipo -> CSV -> búsqueda AntCiberDron -> tabla a destruir -> hormiguero`).
  - Empaquetado y prueba final dentro de Docker (`Dockerfile`, `docker-compose.yml`) con 0 incidentes (`-0.5`).
- **Diagrama Obligatorio 5 — Diagrama de Arquitectura de la Aplicación:** [`02-Diseno/diagramas/05-arquitectura-aplicacion.md`](../02-Diseno/diagramas/05-arquitectura-aplicacion.md).

---

## 6. Evidencia de las 4 Fases y 17 Pasos de XP

| Fase XP | Pasos Documentados en el Repositorio | Carpeta |
| :--- | :--- | :--- |
| **I. Planificación** | 1. Historias de Usuario · 2. Plan de Entregas · 3. Velocidad · 4. Iteraciones · 5. Rotaciones · 6. Reuniones | [`01-Planificacion/`](../01-Planificacion/README.md) |
| **II. Diseño** | 7. Metáfora del Sistema · 8. Tarjetas CRC · 9. Soluciones Puntuales · 10. Funcionalidad Mínima · 11. Reciclaje + **5 Diagramas Obligatorios** | [`02-Diseno/`](../02-Diseno/README.md) |
| **III. Desarrollo** | 12. Disponibilidad del Cliente · 13. Unidad de Pruebas (TDD) · 14. Programación por Parejas · 15. Integración Continua | [`03-Desarrollo/`](../03-Desarrollo/README.md) |
| **IV. Pruebas** | 16. Implantación (Docker) · 17. Pruebas de Aceptación (Checklist firmada por Cliente e I4) | [`04-Pruebas/`](../04-Pruebas/README.md) |

# Documento Final Consolidado — Proyecto ANTDRON / AntCiberDron (Grupo 06)

> **Escuela Politécnica Nacional (EPN) · Facultad de Ingeniería en Informática · Metodologías Ágiles**  
> **Documento consolidado por:** **Ronny Veloz (`I1` · Cliente + Gestor · Parte 2)**

---

## 1. Portada Oficial (Formato Enunciado PDF)

- **Fecha de Entrega:** `19/11/2026`
- **Número de Grupo:** `06`
- **Nombre del Equipo / Metáfora del Sistema:** `Hormiguero Cibernético`
- **Lenguaje y Stack Tecnológico:** `Python 3.12` · `Flask >=3.0,<4.0` · `SQLite (sqlite3)` · `pytest` · `Docker (python:3.12-slim)` · `PlantUML`

### Registro Oficial de Integrantes, Roles XP y Partes

| # | Cédula | Apellido y Nombre | Usuario | Roles XP Asignados | Parte Desarrollada | Último Dígito (Autómata) |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: |
| **I1** | `1724490055` | **Veloz Ronny** | `rveloz` | **Cliente (KGD)** + **Gestor** | **Parte 2:** Autómata, Bomba y documento final | `5` (`Coord-05` · `abcdt+`) |
| **I2** | `1722578703` | **Tamayo Óscar** | `otamayo` | **Coach XP** + **Programador 1** | **Parte 3:** Hormigas, `AntCiberDron` y SQLite | `3` (`Coord-03` · `abc`) |
| **I3** | `1721396412` | **Yépez Analy** | `ayepez` | **Tracker** + **Programadora 2** | **Parte 1:** Login, equipo y `Grupo06.csv` | `2` (`Coord-02` · `ab*`) |
| **I4** | `1726389099` | **Yaguari Mateo** | `myaguari` | **Tester** *(QA / CI / Docker)* | **Parte 4:** Interfaz web Flask y Docker | `9` (`Coord-09` · `ab*`) |

- **Usuario administrativo evaluador:** `patmic` / `123`.

---

## 2. Parte 1 — Login, Equipo, `Grupo06.csv` y Casos de Uso *(Analy Yépez · I3)*

### 2.1. Resumen de Implementación (`HU-01`, `HU-02`)
- **Autenticación (`src/ant/ruso/auth_service.py` y `SistemaRuso.login`):** Permite hasta 3 intentos para cualquiera de los 4 integrantes (`ayepez`, `rveloz`, `otamayo`, `myaguari` con clave `123`) o el docente (`patmic` / `123`). Al tercer intento fallido bloquea el acceso y cierra limpiamente sin excepciones.
- **Presentación del equipo (`SistemaRuso.mostrarEquipo`):** Imprime `[+] TEAM [6]: Hormiguero Cibernético` junto con la cédula y nombre de los 4 alumnos desde `data/integrantes.json`.
- **Lectura de `data/Grupo06.csv` (`SistemaRuso.readCoord` + `Utility` y `tools/generar_csv.py`):** Lee las **40 filas** generadas a partir de los 40 dígitos de las 4 cédulas del grupo, animando el spinner `\ | / -` de `0%` a `100%` antes de imprimir cada coordenada.

### 2.2. Diagrama Obligatorio 2: Diagrama de Casos de Uso
- Archivo completo y gráfico: [`02-Diseno/diagramas/02-diagrama-casos-de-uso.md`](../02-Diseno/diagramas/02-diagrama-casos-de-uso.md) · [`02-Diseno/diagramas/img/02-casos-de-uso.png`](../02-Diseno/diagramas/img/02-casos-de-uso.png) · [`02-Diseno/diagramas/img/02-casos-de-uso.puml`](../02-Diseno/diagramas/img/02-casos-de-uso.puml).

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
- Archivo completo: [`02-Diseno/diagramas/03-automata-grafo-gramatica.md`](../02-Diseno/diagramas/03-automata-grafo-gramatica.md) · fuente PlantUML: [`02-Diseno/diagramas/img/03-automata.puml`](../02-Diseno/diagramas/img/03-automata.puml).
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
  - `aceptar(cadena: str) -> bool`, `evaluar(palabra: str) -> bool` y `recorrido(cadena: str) -> list[str]`: evalúan la cadena sobre `TRANSICIONES` carácter por carácter sin expresiones regulares.
- **`Bomba` y `mostrar_destruir`** (`src/ant/iia/bomba.py`):
  - `Bomba(automata).explotar(palabra: str) -> bool` (y alias `buscar(tipoArsenal: str) -> bool`).
  - `mostrar_destruir(coordenadas, evaluador=None) -> list[CoordenadaUK]`: evalúa las 40 coordenadas de `data/Grupo06.csv`, imprime la tabla `COORDENADAS UCRANIANAS A DESTRUIR` y retorna las **29 coordenadas detonadas (`true`)** (rechazando las 11 filas cuyos arsenales son `aa`, `aaa`, `aaaa`, `abcd`, `abcdd`, `abcddd`).

---

## 4. Parte 3 — Hormigas, `AntCiberDron`, SQLite, Clases y MER *(Óscar Tamayo · I2)*

### 4.1. Jerarquía de Alimentos y Ciclo Biológico (`HU-04`, `HU-05`)
- **Alimentos (`src/ant/alimento/alimento.py`):** Clase abstracta `Alimento(ABC)` con `__str__()` y subclases concretas `Nectar` (`"néctar"`), `ACarnivoro` (`"carnívoro"`), `AOmnivoro` (`"omnívoro"`) y `AHervivoro` (`"herbívoro"`).
- **Hormigas (`src/ant/hormiguero/hormiga.py`):**
  - Interfaz `IHormiga(ABC)` con `@abstractmethod comer(alimento: Alimento) -> bool`.
  - Clase base `Hormiga(IHormiga)` (`@dataclass` con `Id: int`, `sexo: str`, `estado: str = "VIVA"`, método `morir()` y `__str__()`).
  - Subclases `HLarva` (sobrevive con `Nectar` y `AHervivoro`), `HRastreadora` (decisión oficial del Grupo 6: sobrevive únicamente con `AHervivoro`), `HSoldado` (`ACarnivoro`) y `HZangano` (`AOmnivoro`). Ante alimento incorrecto pasan a `"MUERTA"` y devuelven `False`.
- **Gestión del Hormiguero (`src/ant/hormiguero/hormiguero.py`):**
  - `Hormiguero(almacenamiento)`: `crearLarva(sexo)` instancia siempre una `HLarva` viva; `alimentar(id_hormiga, alimento)` transforma a `HLarva` en `HRastreadora` al comer `AHervivoro` **conservando su `Id`**, guarda tipo, estado e historial en SQLite dentro de una transacción (`BEGIN IMMEDIATE`) y `listarHormigas()` reconstruye las instancias según su tipo actual.

### 4.2. Exoesqueleto `AntCiberDron`, Contrato `IIA` e Idiomas (`HU-06`, `HU-07`, `HU-08`)
- **Contrato (`src/ant/iia/iia.py`):** Define el protocolo `Evaluador` (`explotar(palabra) -> bool`) y la interfaz `IIA(ABC)` (`@abstractmethod buscar(tipoArsenal: str) -> bool`).
- **Dron (`src/ant/dron/ant_ciber_dron.py`):**
  - `AntCiberDron(IIA)` recibe una instancia `bomba: Evaluador`, `FuenteDePoder(capacidad=100)` y `ModuloIdioma`.
  - Modela anatomía de hormiga: `cabeza` (`"cabeza con antenas"`), `torax` (`"tórax"`), `abdomen` y 6 `Pata`s: `delantera izquierda` con `Laser`, `delantera derecha` con `Metralleta`, más `media` y `trasera` izquierda/derecha.
  - `buscar(tipoArsenal)` delega en `self.bomba` (`explotar`/`evaluar`/`aceptar`); `volar()` activa `TurboReactor` consumiendo `1` unidad de energía; `dispararLaser()` retorna la potencia igual a `fuente.getEnergia()`; `asistirRecargaFuente()` y `asistirReemplazoFuente(nueva)` operan bajo asistencia de `IIA`.
- **Módulo de Idiomas (`src/ant/dron/modulo_idioma.py`):**
  - Define `Idioma` (`EN`, `ES`), `Area` (`léxico`, `gramática`, `fonética`), `ExpertoParlante(nombre, idioma, certificado)` y `Entrenamiento`.
  - `ModuloIdioma.entrenar(idioma, area, dato, experto)` valida que el experto esté certificado y coincida con el idioma solicitado antes de registrar en memoria o SQLite (`entrenamiento_idioma`); `consultar(idioma)` devuelve la tupla de enseñanzas guardadas.

### 4.3. Persistencia SQLite y Pruebas de Parte 3 (`src/ant/db/sqlite_connection.py`)
- `SqliteConnection("data/antdron.db")` activa `PRAGMA foreign_keys = ON` y crea las tablas `hormiga`, `alimentacion` (FK a `hormiga(id)`) y `entrenamiento_idioma`.
- **Pruebas verificadas (`tests/ant/hormiguero/test_parte3.py`):** 4 pruebas de integración que cubren persistencia de evolución/muerte, anatomía/energía/vuelo del `AntCiberDron`, entrenamiento certificado EN/ES e integración `Grupo06.csv` + `Bomba` + `AntCiberDron` + `mostrar_destruir`.
- **Guía de integración:** [`03-Desarrollo/04-integracion-continua/PARTE_3_GRUPO_06.md`](../03-Desarrollo/04-integracion-continua/PARTE_3_GRUPO_06.md).

### 4.4. Diagramas Obligatorios 1 y 4
- **Diagrama 1 — Diagrama de Clases:** [`02-Diseno/diagramas/01-diagrama-clases.md`](../02-Diseno/diagramas/01-diagrama-clases.md) · [`02-Diseno/diagramas/img/01-diagrama-clases.png`](../02-Diseno/diagramas/img/01-diagrama-clases.png).
- **Diagrama 4 — Modelo Entidad-Relación (MER):** [`02-Diseno/diagramas/04-modelo-entidad-relacion.md`](../02-Diseno/diagramas/04-modelo-entidad-relacion.md) · [`02-Diseno/diagramas/img/04-modelo-entidad-relacion.png`](../02-Diseno/diagramas/img/04-modelo-entidad-relacion.png).

---

## 5. Parte 4 — Interfaz Web Flask, Docker y Arquitectura *(Mateo Yaguari · I4)*

### 5.1. Aplicación Web Flask e Integración del Sistema (`HU-09`)
- **Servidor (`web_app.py`) y vistas (`web/templates/`, `web/static/`):** Reutiliza directamente `SistemaRuso`, `Hormiguero`, `AntCiberDron(Bomba())`, `ModuloIdioma` y `SqliteConnection("data/antdron.db")`, manteniendo `main.py` como alternativa en consola.
- **Rutas y funcionalidades implementadas:**
  - `GET /`, `POST /login`, `POST /logout`: login conectado a `SistemaRuso.login(...)` con límite de 3 intentos por sesión (`MAX_INTENTOS = 3`, bloqueo de sesión al 3.er fallo) y decorador `@protegido` en `/panel`.
  - `GET /panel`: muestra el equipo del Grupo 06 (nombres, roles y cédulas completas), estado del hormiguero en SQLite, controles del `AntCiberDron`, tabla de coordenadas y módulo de idiomas.
  - `POST /hormiguero/crear` y `POST /hormiguero/alimentar`: creación de `HLarva` (`hembra`/`macho`) y aplicación de alimentos (`nectar`, `herbivoro`, `carnivoro`, `omnivoro`) con actualización en tiempo real en SQLite.
  - `POST /dron/operacion`: acciones `recargar`, `volar` y `reemplazar` fuente con capacidad personalizada.
  - `POST /coordenadas`: lee `data/Grupo06.csv` (40 filas), evalúa cada fila individualmente con `dron.buscar(...)` (`29` autorizadas, `11` no autorizadas), anima la carga progresiva en `web/static/app.js` y presenta una tabla separada con las coordenadas destruidas (`Geoposición | Tipo Arsenal | Acción = true`).
  - `POST /idiomas/entrenar`: registra enseñanzas de `EN` y `ES` validando la correspondencia entre idioma y `ExpertoParlante` certificado.

### 5.2. Pruebas Web, Dockerización y Despliegue (`HU-10`)
- **Pruebas HTTP (`tests/test_web.py`):** 8 pruebas funcionales y de regresión con `app.test_client()` que validan protección de rutas, bloqueo tras 3 fallos, logout, ciclo de hormiga, operaciones del dron, rechazo de expertos incorrectos y evaluación individual por fila (`test_resultado_es_individual_por_fila`: 40 filas / 29 autorizadas).
- **Empaquetado Docker (`Dockerfile`, `docker-compose.yml`, `requirements.txt`):** Imagen base `python:3.12-slim` con `pytest>=8.0` y `Flask>=3.0,<4.0`, exposición del puerto `5000` (`CMD ["python", "web_app.py"]`) y volumen `./data:/app/data` para persistir `antdron.db` y leer `Grupo06.csv`.
  - *Nota de verificación:* Se comprobó que no existen rutas absolutas locales en el código Python; la ejecución física de `docker compose up` queda pendiente de correr en un equipo con el daemon de Docker Desktop activo.

### 5.3. Diagrama Obligatorio 5: Diagrama de Arquitectura de la Aplicación
- Archivo completo (actualizado con la capa de presentación web Flask `web_app.py` + `web/templates/` y consola alternativa `main.py`): [`02-Diseno/diagramas/05-arquitectura-aplicacion.md`](../02-Diseno/diagramas/05-arquitectura-aplicacion.md).

---

## 6. Evidencia XP, Pruebas Totales y Cierre

| Evidencia / Artefacto | Detalle Verificado | Archivo |
| :--- | :--- | :--- |
| **Fase I — Planificación** | 11 tarjetas HU (`52 pts`), 3 releases, velocidad/burndown cerrados, 3 iteraciones, rotaciones y actas | [`01-Planificacion/`](../01-Planificacion/README.md) |
| **Fase II — Diseño** | Metáfora, tarjetas CRC, 3 spikes, MVP, reciclaje + **5 Diagramas Obligatorios en PlantUML** | [`02-Diseno/`](../02-Diseno/README.md) |
| **Fase III — Desarrollo** | Disponibilidad del cliente, matriz TDD en verde, bitácora de parejas y estrategia CI/ramas | [`03-Desarrollo/`](../03-Desarrollo/README.md) |
| **Fase IV — Pruebas** | Guía de implantación Docker y **Checklist de Aceptación** firmada por Cliente (`I1`) y Tester (`I4`) | [`04-Pruebas/`](../04-Pruebas/README.md) |
| **Revisión de Cumplimiento** | Auditoría punto por punto contra el PDF y **68 casos de prueba** aprobados (`tests/`) | [`REVISION_CUMPLIMIENTO_2026-11-18.md`](REVISION_CUMPLIMIENTO_2026-11-18.md) |
| **Trazabilidad Git / PRs** | Registro de commits, enlaces a PRs `#1`–`#4` y dashboard de actividades | [`evidencias/DASHBOARD_ACTIVIDADES.md`](../evidencias/DASHBOARD_ACTIVIDADES.md) |

## Confirmación final del equipo · 18/11/2026

El equipo confirmó la ejecución satisfactoria de Docker y del recorrido funcional; la demostración está grabada en el video incluido en el paquete de entrega. Esta confirmación actualiza las anotaciones previas de Docker pendiente.

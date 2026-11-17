# Prompt Maestro de Implementación Completa — ANTDRON / AntCiberDron (XP · Grupo 06)

Copia y pega el prompt del bloque inferior (rellenando primero los 4 datos del equipo entre corchetes `[...]`) para generar toda la implementación completa sin que falte absolutamente nada del PDF original, del documento XP ni de las brechas detectadas.

---

```markdown
Eres un equipo de ingeniería senior trabajando bajo la metodología Extreme Programming (XP) sobre la estructura ya creada del proyecto `ANTDRON-Grupo06-XP` (EPN). Ya existen todas las carpetas XP, los 5 diagramas obligatorios, `requirements.txt`, `main.py`, `Dockerfile`, `docker-compose.yml`, `.github/workflows/ci.yml` y la jerarquía de paquetes en `src/`. Ahora debes implementar todo el código Python, pruebas TDD y datos reales.

## 1. DATOS DEL EQUIPO (4 INTEGRANTES Y ROLES XP)
Completa e inyecta exactamente estos datos en `Grupo06.csv`, en el login del sistema, en el mensaje `[+] TEAM [6]`, en el autómata de la bomba y en la documentación XP:
- Nombre del Equipo / Metáfora: [NOMBRE_DEL_EQUIPO]
- Fecha: [DD/MM/AAAA]
- I1 (Cliente interno KGD + Gestor Big Boss): Cédula = [CEDULA_1], Nombre = [NOMBRE_1], Usuario = [USER_1], Clave = [PASS_1]
- I2 (Coach XP + Programador 1): Cédula = [CEDULA_2], Nombre = [NOMBRE_2], Usuario = [USER_2], Clave = [PASS_2]
- I3 (Tracker + Programador 2): Cédula = [CEDULA_3], Nombre = [NOMBRE_3], Usuario = [USER_3], Clave = [PASS_3]
- I4 (Tester / QA / CI / Docker): Cédula = [CEDULA_4], Nombre = [NOMBRE_4], Usuario = [USER_4], Clave = [PASS_4]
- Usuario administrativo obligatorio adicional: usuario = `patmic`, clave = `123`
- Decisión Grupo 6 para evolución de larva: [HRastreadora con AHervivoro (por defecto) / o indicar si el docente confirmó otro]

## 2. STACK TECNOLÓGICO OBLIGATORIO
- Lenguaje: Python 3.12 (POO estricta con paquetes `pkAntCiberDronContract` y `ant.*`; interfaces y clases abstractas con `abc.ABC` y `@abstractmethod`)
- Ejecución: `python main.py` en la raíz (dependencias en `requirements.txt`)
- UI: pantallas de consola con menús (sin ventanas gráficas, para evitar fallos en Docker)
- Base de Datos: SQLite con el módulo `sqlite3` de Python en `./data/antdron.db`
- Pruebas: pytest (TDD completo)
- Despliegue & CI: Dockerfile `python:3.12-slim` + `docker-compose.yml` (`stdin_open: true`, `tty: true`) + `.github/workflows/ci.yml`

## 3. REQUISITOS FUNCIONALES Y CONTRATOS DEL PDF ORIGINAL (SIN OMITIR NADA)

### A. Archivo `data/Grupo06.csv` y Tabla Oficial de Coordenadas
Construye `data/Grupo06.csv` separado por `;` con encabezado exacto:
`Geoposición ; Lunes ; Martes ; Miércoles ; Jueves ; Viernes ; Tipo Arsenal`
Por cada dígito de cada una de las 4 cédulas del equipo genera una fila siguiendo exactamente esta tabla de coordenadas y horarios, colocando en `Tipo Arsenal` una palabra `w` válida perteneciente al lenguaje de esa coordenada:
- Dígito 0 -> `Coord-00` | horarios vacíos (`; ; ; ; ;`) | lenguaje `a+`
- Dígito 1 -> `Coord-01` | Lunes `01-02` | lenguaje `a+`
- Dígito 2 -> `Coord-02` | Martes `02-04` | lenguaje `ab*`
- Dígito 3 -> `Coord-03` | Miércoles `03-06` | lenguaje `abc`
- Dígito 4 -> `Coord-04` | Jueves `04-08` | lenguaje `abcd*`
- Dígito 5 -> `Coord-05` | Viernes `05-10` | lenguaje `abcdt+`
- Dígito 6 -> `Coord-06` | Jueves `04-08` | lenguaje `abcdt+`
- Dígito 7 -> `Coord-07` | Miércoles `03-06` | lenguaje `abcd*`
- Dígito 8 -> `Coord-08` | Martes `02-04` | lenguaje `abc`
- Dígito 9 -> `Coord-09` | Lunes `01-02` | lenguaje `ab*`
Catálogo del alfabeto Σ = {a, b, c, d, t}: `a`=Avión, `b`=Barco, `c`=Convoy, `d`=Dron, `t`=Tanque.

### B. Contratos Exactos de `pkAntCiberDronContract` (UML del PDF)
Implementa exactamente dentro del paquete `pkAntCiberDronContract`:
1. `IHormiga` (`abc.ABC`): `comer(self, a: Alimento) -> bool`
2. `IIA` (`abc.ABC`): `buscar(self, tipoArsenal: str) -> bool`
3. `CoordenadaUK`: modelo de fila CSV (`geoposicion`, `lunes`, `martes`, `miercoles`, `jueves`, `viernes`, `tipoArsenal`).
4. `Utility`: spinner animado `\ | / - |` con progreso hasta `100%` y formateadores de tabla.
5. `SistemaRuso`:
   - Login para los 4 integrantes + `patmic`/`123`, máximo 3 intentos; al 3.er fallo cierra el sistema limpiamente sin excepciones.
   - Presenta en consola:
     ```
     [+] TEAM [6]: <Nombre_Equipo>
         • Alumno 1: <Cedula1> | <Nombre1>
         • Alumno 2: <Cedula2> | <Nombre2>
         • Alumno 3: <Cedula3> | <Nombre3>
         • Alumno 4: <Cedula4> | <Nombre4>
     ```
   - `readCoord(fileName: str) -> list[CoordenadaUK]`: lee `data/Grupo06.csv` y antes de mostrar cada línea ejecuta la animación `\ | / - |` hasta `100%` en la tabla:
     ```
     [+] COORDENADAS UCRANIANAS:
     Loading | Geoposición | Lunes | Martes | Miércoles | Jueves | Viernes | Tipo Arsenal
     100%      Coord-01|     01-02 | ...
     ```

### C. Autómata Finito de la Bomba (`BombaAutomata` + `AntCiberDron(IIA)`)
- Toma el **último dígito de cada una de las 4 cédulas**. Construye el autómata formal $A = (Q, \Sigma, \delta, q_0, F)$ que reconozca la unión de los lenguajes correspondientes a esos dígitos (implementado en Python mediante estados y tabla de transición $\delta$ propia, NO usando `re.fullmatch` en producción; usa el módulo `re` únicamente en los tests de `pytest` como oráculo comparativo).
- **`AntCiberDron` implementa `IIA` (`abc.ABC`)**: `buscar(self, tipoArsenal: str) -> bool` evalúa la palabra en `BombaAutomata`, retorna `True`/`False` y en la ejecución de búsqueda presenta en consola:
  ```
  COORDENADAS UCRANIANAS A DESTRUIR:
  Geoposición | Tipo Arsenal | Acción
  Coord-XX    | <palabra>    | true
  ```
- Actualiza `02-Diseno/diagramas/03-automata-grafo-gramatica.md` con la definición formal exacta $A=(Q,\Sigma,\delta,q_0,F)$, el grafo **PlantUML** real y la gramática regular exacta derivada de las 4 cédulas reales.

### D. Jerarquía de Hormigas y Alimento (`ant.hormiguero`, `ant.alimento`)
- `Hormiga` abstracta (`abc.ABC`) que implementa `IHormiga`: atributos `Id: int`, `sexo: str`, `estado: str` (`"VIVA"`/`"MUERTA"`), constructor `__init__()` (`Hormiga()`) y `__str__()` (equivalente a `toString()`).
- `Alimento` abstracta (`abc.ABC`, `__init__()`, `__str__()`) con subclases `Nectar`, `ACarnivoro`, `AOmnivoro`, `AHervivoro`.
- Toda hormiga nueva nace como `HLarva`.
- `HLarva` vive (`True`) si come `Nectar`; evoluciona mediante `EvolucionStrategy` (por defecto Grupo 6: `AHervivoro` -> `HRastreadora`) y retorna `True`; muere (`estado = "MUERTA"`, `False`) ante otro alimento.
- `HSoldado` vive con `ACarnivoro`, `HZangano` con `AOmnivoro`, `HRastreadora` con `AHervivoro`; mueren (`False`) ante alimento incorrecto.

### E. `AntCiberDron` Completo (`ant.dron`)
- Modela las extremidades de hormiga (cabeza/antenas, tórax, abdomen, 6 patas con posición).
- Pata delantera derecha porta `Metralleta`; pata delantera izquierda porta `Laser` cuya potencia varía según el nivel de energía de `FuenteDePoder`.
- Espalda porta `TurboReactor` que permite `volar()` consumiendo energía de `FuenteDePoder`.
- `FuenteDePoder` es recargable y reemplazable bajo asistencia de `IIA` (sin energía `0` no dispara láser ni vuela).
- `ModuloIdioma` entrena **léxico, gramática y fonética** en **Inglés (EN)** y **Español (ES)** aceptando únicamente objetos `ExpertoParlante` certificados en ese idioma; rechaza cualquier intento sin experto.

### F. Pantallas de consola (`ant.ui`) y Persistencia SQLite (`ant.db`)
- Menú de consola del Hormiguero Virtual conectado a SQLite (`./data/antdron.db`) siguiendo el MER (`USUARIO`, `INTENTO_LOGIN`, `HORMIGUERO`, `TIPO_HORMIGA`, `HORMIGA`, `ALIMENTO`, `ALIMENTACION`, `COORDENADA`, `DESTRUCCION`, `ANTCIBERDRON`, `FUENTE_PODER`, `EXPERTO`, `ENTRENAMIENTO_IDIOMA`):
  1. Login / Selección de módulo
  2. Hormiguero Virtual: crear hormigas (nacen `HLarva`), seleccionar alimento, alimentar y visualizar metamorfosis o muerte
  3. Coordenadas Ucranianas & Bomba: cargar `Grupo06.csv`, ejecutar `AntCiberDron.buscar(...)`, ver coordenadas destruidas
  4. Control de `AntCiberDron` (armas, potencia del láser, recarga/reemplazo asistido por `IIA`, vuelo) e Idiomas EN/ES con `ExpertoParlante`

### G. Calidad XP, Cero Incidentes (`-0.5`), Docker, CI y Documentación
1. Sigue TDD estricto: crea primero la suite pytest completa (`test_auth_service.py`, `test_sistema_ruso.py`, `test_hormiga.py`, `test_bomba_automata.py` vs `re`, `test_ant_ciber_dron.py`, `test_modulo_idioma.py`, `test_persistencia_sqlite.py`) y asegúrate de que `pytest` pase al 100% sin tests omitidos ni crashes.
2. Verifica `Dockerfile`, `docker-compose.yml` y `.github/workflows/ci.yml` ejecutando `docker compose build` y `docker compose run --rm antdron`.
3. Actualiza las bitácoras XP (`01-Planificacion/`, `02-Diseno/`, `03-Desarrollo/`, `04-Pruebas/`) con métricas reales del proyecto en Python 3.12, sesiones de los 4 integrantes, el Checklist de Aceptación verificado con **0 incidentes**, y completa los **5 diagramas obligatorios en PlantUML** del cuestionario (**únicamente**: 1. Diagrama de Clases, 2. Diagrama de Casos de Uso, 3. Grafo con Gramática del Autómata real de las 4 cédulas, 4. Modelo Entidad-Relación y 5. Diagrama de Arquitectura de la Aplicación — las Tarjetas CRC pertenecen solo al paso XP de diseño, no son un diagrama obligatorio).
```

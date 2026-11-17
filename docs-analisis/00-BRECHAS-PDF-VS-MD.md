# Análisis de Brechas: PDF Original vs `WORKSHOP-XP.md` (Adaptación a Python 3.12 y PlantUML)

Este documento extrae **todo lo que aparece en el enunciado original del PDF (`METODOLOGÍAS ÁGILES - WORKSHOP XP`)** y que **no estaba incluido, estaba incompleto o presentaba inconsistencias en el archivo `WORKSHOP-XP.md`**, detallando cómo se implementa en **Python 3.12** (`abc.ABC`, `sqlite3`, `pytest`) y se documenta en **PlantUML**.

---

## 1. Contrato UML `pkAntCiberDronContract` y Correcciones de Diseño

En la página 2 del PDF aparece un diagrama UML oficial con diferencias críticas respecto al diagrama inicial de `WORKSHOP-XP.md` (y cuya representación definitiva en este proyecto se entrega en **PlantUML** con tipos de **Python 3.12**):

| Elemento | En el PDF Original (UML) | En `WORKSHOP-XP.md` (Brecha / Error) | Acción en el Proyecto (**Python 3.12**) |
| :--- | :--- | :--- | :--- |
| **Paquete de contrato** | Existe el paquete explícito **`pkAntCiberDronContract`**. | Se inventaron paquetes (`ant.hormiguero`, `ant.iia`, etc.) omitiendo `pkAntCiberDronContract`. | Incluir `pkAntCiberDronContract` en Python (`abc.ABC`) para interfaces y contratos base, y paquetes `ant.*` para implementaciones. |
| **Retorno de `IHormiga.comer`** | `+ comer(Alimento): boolean` | Se puso sin tipo de retorno (`void`). | Respetar **`comer(self, a: Alimento) -> bool`** (`True` si vive/evoluciona, `False` si muere). |
| **Atributos de `Hormiga`** | `- Id: Integer`, `- sexo: String`, `- estado: String`, `+ Hormiga()`, `+ toString(): String`. | Tenía `#nombre: String` y `#viva: boolean`. | Usar **`Id: int`, `sexo: str` y `estado: str`** (`"VIVA"`/`"MUERTA"`), con `__init__()` y `__str__()` (equivalente a `toString()`). |
| **¿Quién implementa `IIA`?** | **`AntCiberDron` implementa `IIA`** (`IIA <|.. AntCiberDron`). El texto dice: *"AntCiberDron debe implementar inteligencia artificial que tiene una interfaz para buscar el Tipo de arsenal..."*. | Se colocó `Hormiga <|-- IIA` (haciendo a `IIA` hija de `Hormiga` y desvinculando la realización directa). | **`AntCiberDron(IIA)`** implementa directamente la interfaz **`IIA`** (`abc.ABC`). |
| **Clase `SistemaRuso` y `CoordenadaUK`** | Método explícito **`+ readCoord(filename: String): List<CoordenadaUK>`**. | No existía la clase modelo `CoordenadaUK` ni la firma exacta `readCoord(...)`. | Crear el modelo **`CoordenadaUK`** y la firma exacta **`readCoord(self, filename: str) -> list[CoordenadaUK]`**. |
| **Clase `Utility`** | Aparece **`Utility`** dentro de `pkAntCiberDronContract` (para utilidades como el spinner/loading de consola). | Completamente omitida. | Crear **`Utility`** dentro de `pkAntCiberDronContract` en Python (incluye animación de loading `\ | / - |`). |
| **Grupo 9 (`IIA`) en tabla de evolución** | La tabla del PDF solo lista: `HLarva (todos)`, `HSoldado (1, 2)`, `HZángano (3, 4)`, `HRastreadora (5)`. **No existe el grupo 9**. | `WORKSHOP-XP.md` decía *"y 9 (`IIA`)"* en la sección 0. | Eliminar la referencia errónea al grupo 9; documentar que el Grupo 6 no figura en tabla y se parametriza con `EvolucionStrategy` consultando al Cliente (I1 + docente). |

---

## 2. Tabla Completa de Coordenadas, Horarios y Lenguajes (Página 1 del PDF)

En `WORKSHOP-XP.md` no figuraba la tabla completa de 10 coordenadas ni sus horarios por día. Del PDF original se extrae la matriz exacta:

| Geoposición | Lunes | Martes | Miércoles | Jueves | Viernes | Tipo Arsenal (Lenguaje) |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `Coord-01` | `01-02` | | | | | `a+` |
| `Coord-02` | | `02-04` | | | | `ab*` |
| `Coord-03` | | | `03-06` | | | `abc` |
| `Coord-04` | | | | `04-08` | | `abcd*` |
| `Coord-05` | | | | | `05-10` | `abcdt+` |
| `Coord-06` | | | | `04-08` | | `abcdt+` |
| `Coord-07` | | | `03-06` | | | `abcd*` |
| `Coord-08` | | `02-04` | | | | `abc` |
| `Coord-09` | `01-02` | | | | | `ab*` |
| `Coord-00` | *(vacío)* | *(vacío)* | *(vacío)* | *(vacío)* | *(vacío)* | `a+` |

---

## 3. Diccionario / Códigos de Arsenal Bélico (Alfabeto $\Sigma$)

Completamente ausente en `WORKSHOP-XP.md`:

| Código ($\Sigma$) | Arsenal Bélico (Significado de Dominio) |
| :---: | :--- |
| `a` | Avión |
| `b` | Barco |
| `c` | Convoy |
| `d` | Dron |
| `t` | Tanque *(en el PDF aparece con errata tipográfica `"Taque"`)* |

---

## 4. Formato Exacto del Archivo `Grupo06.csv` y Salidas de Consola

Tampoco estaban especificados en `WORKSHOP-XP.md` los formatos literales mostrados en las capturas del PDF:

1. **Estructura de `Grupo06.csv`** (delimitado por `;`):
   - Encabezado: `Geoposición ; Lunes ; Martes ; Miércoles ; Jueves ; Viernes ; Tipo Arsenal`
   - Filas: una fila por **cada dígito** de cada cédula de los integrantes del equipo, copiando los horarios exactos de esa coordenada y poniendo en `Tipo Arsenal` una palabra válida `w` perteneciente al lenguaje de la coordenada (ej. para dígito `5`: `Coord-05; ; ; ; ; 05-10 ; abcdttt`).
2. **Salida de equipo en consola:**
   ```text
   [+] TEAM [6]: <Nombre_Metafora>
       • Alumno 1: <Cedula_1> | <Nombre_1>
       • Alumno 2: <Cedula_2> | <Nombre_2>
       • Alumno 3: <Cedula_3> | <Nombre_3>
       • Alumno 4: <Cedula_4> | <Nombre_4>
   ```
3. **Salida de lectura del CSV con animación previa por línea:**
   ```text
   [+] COORDENADAS UCRANIANAS:
   Loading | Geoposición | Lunes | Martes | Miércoles | Jueves | Viernes | Tipo Arsenal
   100%      Coord-01|     01-02 |        |           |        |         | aaaa
   ...
   / 10%
   ```
   *(Mientras carga cada fila, el spinner gira `\ | / - |` subiendo el porcentaje hasta `100%` antes de imprimir la línea de la coordenada).*
4. **Salida de coordenadas destruidas por la bomba (`IIA.buscar`):**
   ```text
   COORDENADAS UCRANIANAS A DESTRUIR:
   Geoposición | Tipo Arsenal | Acción
   Coord-05    | abcdttt      | true
   Coord-09    | ab           | true
   ```
   El PDF exige explícitamente: *"La acción de buscar debe presentar la coordenada donde la bomba explota"*.

---

## 5. Regla Exacta del Autómata de la Bomba

En `WORKSHOP-XP.md` se mencionaba en la sección 5 sin dar la regla operativa del PDF:
- Se toma **únicamente el último dígito de la cédula de cada integrante** del grupo (en nuestro caso, los **4 últimos dígitos**, uno por cada miembro del equipo).
- El lenguaje reconocido por la bomba $L$ es la **unión de los lenguajes** de las coordenadas correspondientes a esos últimos dígitos (ej. dígitos `5` y `9` $\rightarrow$ $L = \{ \text{abcdt}^+, \text{ab}^* \}$).
- Se exige entrega formal completa: $A = (Q, \Sigma, \delta, q_0, F)$, **Grafo** y **Gramática**.

---

## 6. Anatomía Completa de `AntCiberDron`

El PDF especifica:
- *"AntCiberDron se compone de las **mismas extremidades de la hormiga**, la **pata delantera derecha** puede cargar una metralleta y el **izquierdo** un láser cuya potencia varía según la energía de la fuente de poder."*
- *"AntCiberDron tiene un **turbo reactor en la parte de la espalda** que le permiten volar usando energía de la fuente de poder. La fuente de poder es **recargable y reemplazable bajo la asistencia del IIA**."*
- No basta con `Pata[6]`; conviene modelar las extremidades de la hormiga (cabeza/antenas, tórax, abdomen, 6 patas con posiciones anatómicas claras: delantera derecha $\rightarrow$ metralleta, delantera izquierda $\rightarrow$ láser, espalda $\rightarrow$ turbo reactor).

---

## 7. Cuestionario Obligatorio: Diagramas Faltantes (en PlantUML) y Regla de Penalización

| Ítem del PDF | Estado en `WORKSHOP-XP.md` | Incluido en este Proyecto (**Código PlantUML**) |
| :--- | :--- | :--- |
| **Diagrama de Clases** | Incompleto / desalineado del UML oficial. | [`02-Diseno/diagramas/01-diagrama-clases.md`](../02-Diseno/diagramas/01-diagrama-clases.md) |
| **Diagrama de Casos de Uso** | **Omitido** (solo citado en HU-11). | [`02-Diseno/diagramas/02-diagrama-casos-de-uso.md`](../02-Diseno/diagramas/02-diagrama-casos-de-uso.md) |
| **Grafo y Gramática del Autómata** | **Omitido** (dejado como pendiente). | [`02-Diseno/diagramas/03-automata-grafo-gramatica.md`](../02-Diseno/diagramas/03-automata-grafo-gramatica.md) |
| **Modelo Entidad-Relación (MER)** | Incluido en Mermaid; convertido a PlantUML/SQLite. | [`02-Diseno/diagramas/04-modelo-entidad-relacion.md`](../02-Diseno/diagramas/04-modelo-entidad-relacion.md) |
| **Diagrama de Arquitectura de la Aplicación** | **Omitido** (solo citado en HU-11). | [`02-Diseno/diagramas/05-arquitectura-aplicacion.md`](../02-Diseno/diagramas/05-arquitectura-aplicacion.md) |
| **Penalización `-0.5 puntos por incidente`** | Mencionado de paso solo en CI. | Documentado en [`04-Pruebas/02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md`](../04-Pruebas/02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md) |
| **Nombres exactos del árbol XP del PDF** | Cambió *"Soluciones Puntuales"* por *"Spikes"* y *"Reciclaje"* por *"Refactorización"*. | Se usan los nombres oficiales del diagrama del PDF con su equivalente técnico entre paréntesis. |
| **Portada oficial (Fecha, #Grupo, Metáfora, Cédulas)** | Sin campo `FECHA`. | Incluida en [`01-ROLES-EQUIPO-4-INTEGRANTES.md`](01-ROLES-EQUIPO-4-INTEGRANTES.md). |

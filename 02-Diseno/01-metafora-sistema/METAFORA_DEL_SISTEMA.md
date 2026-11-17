# 7. Metáfora del Sistema: "Hormiguero Cibernético"

**Guía:** I2 (Coach XP) · **Aprobado por:** I1 (Cliente) · **Lenguaje:** **Python 3.12** (`abc.ABC`, `sqlite3`, consola interactiva)

## Narrativa Común del Dominio
Todo el equipo habla el mismo lenguaje ubícuo para que la KGD (Cliente) y los programadores (`I2`, `I3`) se entiendan sin jerga técnica innecesaria:

- **El Hormiguero (`Hormiguero`)** es el centro de mando ruso donde nacen, se alimentan y evolucionan las hormigas guerreras.
- **Cada hormiga nace como `HLarva`**, vulnerable y alimentada con `Néctar`, hasta recibir el `Alimento` específico que dispara su metamorfosis (o su muerte si ingiere el incorrecto).
- **El `AntCiberDron`** es el exoesqueleto biomecánico con las mismas extremidades de una hormiga (6 patas, metralleta en pata delantera derecha, láser en pata delantera izquierda, turbo reactor en la espalda), que **implementa la interfaz de Inteligencia Artificial (`IIA` con `abc.ABC`)** para operar la bomba inteligente.
- **El `SistemaRuso`** intercepta y descifra el archivo ucraniano `Grupo06.csv` (`readCoord`), convierte cada fila en una `CoordenadaUK` y ordena al `AntCiberDron` buscar qué objetivos detonan según el autómata.
- **Los `ExpertoParlante`** (Inglés y Español) son los únicos instructores autorizados para entrenar léxico, gramática y fonética al módulo de idiomas del dron.

## Mapa de Paquetes del Código Fuente (Python 3.12)

| Paquete | Rol dentro de la Metáfora | Origen (PDF vs MD) |
| :--- | :--- | :--- |
| `pkAntCiberDronContract` | Contratos oficiales del sistema (`IHormiga`, `IIA`, `SistemaRuso`, `CoordenadaUK`, `Utility`) en `abc.ABC`. | **PDF Original (UML pág. 2)** |
| `ant.hormiguero` | `Hormiga` (abstracta `abc.ABC`), `HLarva`, `HSoldado`, `HZangano`, `HRastreadora`, `EvolucionStrategy`, `Hormiguero`. | PDF + MD |
| `ant.alimento` | `Alimento` (abstracta `abc.ABC`), `Nectar`, `ACarnivoro`, `AOmnivoro`, `AHervivoro`. | PDF + MD |
| `ant.dron` | `AntCiberDron(IIA)` (implementa `IIA`), `Pata`, `Metralleta`, `Laser`, `TurboReactor`, `FuenteDePoder`, `ModuloIdioma`, `ExpertoParlante`. | PDF + MD |
| `ant.iia` | `BombaAutomata` (AFD $A=(Q,\Sigma,\delta,q_0,F)$) que asiste a `AntCiberDron` en `buscar(...)` y recarga de fuente. | PDF + MD |
| `ant.ruso` | `AuthService` (login 3 intentos + `patmic`/`123`), `Integrante`, `ArsenalCatalogo`. | PDF + MD |
| `ant.db` | Persistencia `SQLite` mediante el módulo estándar `sqlite3` de Python (DAOs alineados al MER). | MD + PDF |
| `ant.ui` | Pantallas de consola con menús en Python (Hormiguero Virtual, creación/alimentación, coordenadas destruidas). | PDF + MD |

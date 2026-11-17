# 8. Tarjetas CRC (Clase · Responsabilidades · Colaboradores — Python 3.12)

**Participantes:** I2 (Coach+Prog1), I3 (Prog2), I4 (Tester) · **Lenguaje:** **Python 3.12** (`abc.ABC`, `@abstractmethod`).  
Todas las tarjetas respetan estrictamente los contratos del diagrama UML del PDF (`pkAntCiberDronContract`) adaptados a la sintaxis y tipado de **Python 3.12**.

| Clase | Responsabilidades | Colaboradores |
| :--- | :--- | :--- |
| **`IHormiga`** *(interfaz `abc.ABC`)* | Definir el contrato de alimentación `+ comer(self, a: Alimento) -> bool`. | `Alimento`, `Hormiga` |
| **`IIA`** *(interfaz `abc.ABC`)* | Definir el contrato de inteligencia artificial `+ buscar(self, tipoArsenal: str) -> bool`. | `AntCiberDron`, `CoordenadaUK` |
| **`Hormiga`** *(abstracta `abc.ABC`)* | Almacenar `Id: int`, `sexo: str`, `estado: str` (`"VIVA"`/`"MUERTA"`); implementar base de `IHormiga` y `__str__()` (equivalente a `toString()`). | `IHormiga`, `Alimento` |
| **`HLarva`** | Vivir comiendo `Nectar`; evolucionar mediante `EvolucionStrategy` si recibe el alimento objetivo del grupo; morir (`estado = "MUERTA"`, retorna `False`) ante otro alimento. | `Alimento`, `EvolucionStrategy`, `HRastreadora` *(u otro tipo)* |
| **`HSoldado` / `HZangano` / `HRastreadora`** | Vivir comiendo su alimento asignado (`ACarnivoro`, `AOmnivoro`, `AHervivoro`); morir (`False`) si comen otro. | `Alimento`, `Hormiguero` |
| **`Alimento`** *(abstracta `abc.ABC`)* | Representar el nutriente con `__init__()` y `__str__()` (equivalente a `toString()`); ser especializado por `Nectar`, `ACarnivoro`, `AOmnivoro`, `AHervivoro`. | `Hormiga`, `HLarva` |
| **`AntCiberDron`** | **Implementar `IIA`** (`buscar(self, tipoArsenal: str) -> bool`); ensamblar extremidades de hormiga (6 patas, metralleta derecha, láser izquierdo con potencia ligada a fuente, turbo reactor en espalda); volar, disparar, recargar/reemplazar fuente asistida por `IIA`, y entrenar EN/ES. | `IIA`, `BombaAutomata`, `FuenteDePoder`, `Laser`, `Metralleta`, `TurboReactor`, `ModuloIdioma` |
| **`BombaAutomata`** | Modelar $A = (Q, \Sigma, \delta, q_0, F)$ con los últimos dígitos de las 4 cédulas; evaluar cadenas carácter a carácter con tabla $\delta$ en Python y devolver `True`/`False`. | `AntCiberDron` |
| **`FuenteDePoder`** | Mantener nivel de energía (`int`); permitir recarga y reemplazo bajo asistencia de `IIA`; alimentar potencia de `Laser` y vuelo de `TurboReactor`. | `AntCiberDron`, `Laser`, `TurboReactor` |
| **`ModuloIdioma` & `ExpertoParlante`** | Entrenar léxico (`dict`), gramática (`list`) y fonética (`list`) en inglés o español **solo** si el origen es una instancia válida de `ExpertoParlante` certificada. | `AntCiberDron` |
| **`SistemaRuso`** | Autenticar usuarios (4 integrantes + `patmic`/`123`, máx. 3 intentos); imprimir `[+] TEAM [6]`; ejecutar `+ readCoord(self, filename: str) -> list[CoordenadaUK]` con animación de `Utility`; presentar coordenadas destruidas. | `CoordenadaUK`, `Utility`, `AntCiberDron`, `Hormiguero` |
| **`CoordenadaUK`** | Representar una fila del CSV (`geoposicion`, `lunes`, `martes`, `miercoles`, `jueves`, `viernes`, `tipoArsenal` de tipo `str`). | `SistemaRuso`, `AntCiberDron` |
| **`Utility`** | Proveer animación de carga `\ \| / - \|` hasta `100%` por línea y utilidades de consola/formato en Python. | `SistemaRuso` |
| **`Hormiguero`** | Gestionar colección `list[Hormiga]`, crear nuevas larvas, registrar alimentaciones y conservar historial de coordenadas destruidas (conectado a SQLite vía `ant.db` con `sqlite3`). | `Hormiga`, `HLarva`, `Alimento`, `ant.db` *(DAOs `sqlite3`)* |

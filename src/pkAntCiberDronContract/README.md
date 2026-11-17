# `src/pkAntCiberDronContract/`

Contratos e interfaces oficiales extraídos del diagrama UML de la página 2 del PDF original *(código Python pendiente hasta contar con las 4 cédulas)*. Las interfaces se implementan como clases abstractas con `abc.ABC` y `@abstractmethod`:

- `i_hormiga.py` → `IHormiga` — `comer(self, a: Alimento) -> bool`
- `iia.py` → `IIA` — `buscar(self, tipoArsenal: str) -> bool`
- `coordenada_uk.py` → `CoordenadaUK` — Modelo de coordenada leída desde `Grupo06.csv` (`geoposicion`, `lunes`..`viernes`, `tipoArsenal`).
- `utility.py` → `Utility` — Animación de carga `\ | / - |` hasta `100%` por línea y utilidades de formato de consola.
- `sistema_ruso.py` → `SistemaRuso` — Autenticación (máx. 3 intentos, 4 integrantes + `patmic`/`123`), presentación `[+] TEAM [6]` y `readCoord(self, fileName: str) -> list[CoordenadaUK]`.

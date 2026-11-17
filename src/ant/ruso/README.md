# `src/ant/ruso/`

Seguridad, datos de integrantes y catálogo de arsenal *(código Python pendiente hasta tener las 4 cédulas)*:

- `auth_service.py` → clase `AuthService` — Validación de credenciales de los **4 integrantes** y **`patmic`/`123`** con bloqueo al 3.er intento fallido.
- `integrante.py` → clase `Integrante` — Datos de cada miembro del Grupo 06 (`cedula`, `nombre`, `usuario`, `rol`).
- `arsenal_catalogo.py` → clase `ArsenalCatalogo` — Mapeo oficial del PDF ($\Sigma = \{a,b,c,d,t\}$: Avión, Barco, Convoy, Dron, Tanque) y tabla de horarios `Coord-00`..`Coord-09`.

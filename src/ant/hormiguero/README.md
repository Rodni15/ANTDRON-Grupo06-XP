# `src/ant/hormiguero/`

Clases del ciclo biológico del hormiguero *(código Python pendiente)*:

- `hormiga.py` → `Hormiga` *(abstracta, implementa `IHormiga`)* — `Id: int`, `sexo: str`, `estado: str` (`"VIVA"` / `"MUERTA"`), `__init__()`, `__str__()` (equivalente a `toString()`).
- `h_larva.py` → `HLarva` — Vive con `Nectar`; evoluciona vía `EvolucionStrategy` o muere (`False`) con otro alimento.
- `h_soldado.py` → `HSoldado` — Vive con `ACarnivoro` (Grupos 1, 2).
- `h_zangano.py` → `HZangano` — Vive con `AOmnivoro` (Grupos 3, 4).
- `h_rastreadora.py` → `HRastreadora` — Vive con `AHervivoro` (Grupo 5 / por defecto Grupo 6).
- `evolucion_strategy.py` → `EvolucionStrategy` — Patrón Strategy parametrizable para el Grupo 6.
- `hormiguero.py` → `Hormiguero` — Creación, alimentación y listado de hormigas.

# `src/ant/dron/`

Exoesqueleto cibernético y capacidades del dron en **Python 3.12** *(código Python pendiente)*:

- `ant_ciber_dron.py` → `AntCiberDron(IIA)` — Implementa la interfaz `IIA` (`abc.ABC`), coordina extremidades, `buscar(tipoArsenal: str) -> bool`, `volar() -> bool`, armas, fuente de poder y aprendizaje de idiomas.
- `pata.py` → `Pata` — Extremidades de la hormiga (6 patas + cabeza/antenas, tórax, abdomen).
- `metralleta.py` → `Metralleta` — Equipada en la pata delantera derecha.
- `laser.py` → `Laser` — Equipado en la pata delantera izquierda; potencia dependiente de `FuenteDePoder`.
- `turbo_reactor.py` → `TurboReactor` — Equipado en la espalda para volar con energía de la fuente.
- `fuente_de_poder.py` → `FuenteDePoder` — Energía recargable y reemplazable bajo asistencia de `IIA`.
- `modulo_idioma.py` → `ModuloIdioma` — Entrenamiento de léxico, gramática y fonética (Inglés / Español).
- `experto_parlante.py` → `ExpertoParlante` — Único actor autorizado para entrenar `ModuloIdioma`.

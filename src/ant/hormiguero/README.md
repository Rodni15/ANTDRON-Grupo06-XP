# `src/ant/hormiguero/`

- `hormiga.py` define `IHormiga`, `Hormiga`, `HLarva` y `HRastreadora`.
- `hormiguero.py` crea larvas, registra su alimentación y cambia una larva viva por una rastreadora al darle `AHervivoro()`. El identificador se conserva.
- `Hormiguero()` funciona en memoria. `Hormiguero(SqliteConnection(...))` conserva las hormigas y el historial de alimentación en SQLite.

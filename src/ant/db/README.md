# `src/ant/db/`

Capa de persistencia SQLite con el módulo `sqlite3` de Python *(código pendiente)*:

- `sqlite_connection.py` → `SqliteConnection` — Conexión e inicialización automática de `./data/antdron.db`.
- DAOs alineados al MER (`02-Diseno/diagramas/04-modelo-entidad-relacion.md`):
  - `usuario_dao.py` (`USUARIO`, `INTENTO_LOGIN`)
  - `hormiguero_dao.py` (`HORMIGUERO`, `TIPO_HORMIGA`, `HORMIGA`, `ALIMENTO`, `ALIMENTACION`)
  - `destruccion_dao.py` (`COORDENADA`, `DESTRUCCION`)
  - `dron_dao.py` (`ANTCIBERDRON`, `FUENTE_PODER`, `EXPERTO`, `ENTRENAMIENTO_IDIOMA`)

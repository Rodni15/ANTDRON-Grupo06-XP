# Carpeta `data/` (Datos de Entrada y Base de Datos — Python 3.12)

Aquí se almacenan los archivos leídos y generados por la aplicación en **Python 3.12** (`csv` y `sqlite3`):
1. **`Grupo06.csv`** *(a generar a partir de [`Grupo06.csv.template`](Grupo06.csv.template) cuando se tengan las 4 cédulas del equipo)*.
   - Delimitado por `;` con encabezado: `Geoposición ; Lunes ; Martes ; Miércoles ; Jueves ; Viernes ; Tipo Arsenal`.
   - Una fila por cada dígito de las 4 cédulas según la tabla oficial del PDF.
2. **`antdron.db`** *(base de datos embebida SQLite gestionada desde Python con `sqlite3` y generada automáticamente en tiempo de ejecución según `02-Diseno/diagramas/04-modelo-entidad-relacion.md`)*.

> Esta carpeta también se monta como volumen en `docker-compose.yml` (`./data:/app/data`).

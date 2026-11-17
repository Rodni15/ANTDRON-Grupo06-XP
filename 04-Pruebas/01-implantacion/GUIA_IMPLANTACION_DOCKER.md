# 16. Guía de Implantación (Python 3.12 y Docker)

**Responsables:** **I4 (Tester)** & **I1 (Gestor)** · **Entorno:** **Python 3.12** (`python:3.12-slim`, `pytest`, `sqlite3`).

## Requisitos de Despliegue
- Archivo real `data/Grupo06.csv` generado con las 4 cédulas del equipo.
- `Dockerfile` con imagen `python:3.12-slim` y `docker-compose.yml` con `stdin_open: true` y `tty: true` para que la animación `\ | / - | 100%` funcione correctamente dentro del contenedor.

## Comandos de Verificación en Equipo Limpio
```bash
# 1. Construir imagen desde cero
docker compose build

# 2. Ejecutar modo consola (Login 3 intentos, Team, CSV + Loading, Bomba Autómata)
docker compose run --rm antdron

# 3. Alternativa sin Docker (Windows/macOS/Linux con Python 3.12)
pip install -r requirements.txt
pytest
python main.py
```

## Validaciones de No-Crash (`-0.5` cero incidentes)
- [ ] La carpeta `./data` persiste `antdron.db` (SQLite) entre reinicios del contenedor.
- [ ] No existen rutas absolutas locales (`C:\...`) en el código Python.
- [ ] El archivo `Grupo06.csv` se encuentra correctamente tanto en local como dentro de `/app/data/`.

# 16. Guía de Implantación (Python 3.12 y Docker)

**Responsables:** **I4 (Tester)** & **I1 (Gestor)** · **Entorno:** **Python 3.12** (`python:3.12-slim`, `pytest`, `sqlite3`).

## Requisitos de Despliegue
- Archivo real `data/Grupo06.csv` generado con las 4 cédulas del equipo (40 filas).
- `Dockerfile` con imagen `python:3.12-slim`, exposición del puerto `5000` (`CMD ["python", "web_app.py"]`) y `docker-compose.yml` con mapeo `"5000:5000"` y volumen `./data:/app/data` para persistir SQLite (`antdron.db`).

## Comandos de Verificación en Equipo Limpio
```bash
# 1. Construir imagen desde cero
docker compose build

# 2. Levantar aplicación web Flask (puerto 5000)
docker compose up -d
# Abrir http://localhost:5000

# 3. Alternativa sin Docker (Windows/macOS/Linux con Python 3.12+)
pip install -r requirements.txt
pytest -q
python web_app.py
# Consola alternativa (flujo inicial): python main.py
```

## Validaciones de No-Crash (`-0.5` cero incidentes)
- [x] La carpeta `./data` se monta como volumen `./data:/app/data` y `web_app.py` apunta a `RAIZ / "data" / "antdron.db"` para persistir SQLite. *(Prueba física del contenedor pendiente de ejecutar en máquina con Docker Desktop activo).*
- [x] No existen rutas absolutas locales (`C:\...`) en el código Python (`src/`, `main.py`, `web_app.py`).
- [x] El archivo `data/Grupo06.csv` (40 filas) existe localmente y se incluye en `/app/data/` mediante `COPY . .`.

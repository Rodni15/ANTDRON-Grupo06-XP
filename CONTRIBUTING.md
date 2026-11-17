# Guía de Colaboración en el Repositorio — ANTDRON Grupo 06 (Python 3.12 · XP)

Guía rápida para que los **4 integrantes (`I1`, `I2`, `I3`, `I4`)** clonen el repositorio, trabajen en ramas XP y mantengan `main` siempre en verde.

## 1. Clonar y preparar entorno local (Python 3.12)
```bash
git clone <URL_DEL_REPOSITORIO>
cd ANTDRON-Grupo06-XP

python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
python main.py
```

## 2. Flujo de ramas y Pull Requests (XP)
1. **Nunca hacer `push` directo a `main`.**
2. Crea una rama corta por historia desde `main` actualizado:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/HU-01-login
   ```
3. Trabaja en pareja (**I2 + I3**, rotando Driver/Navigator cada 30 min) siguiendo TDD (`pytest` primero).
4. Sube tu rama y abre un **Pull Request** hacia `main`:
   ```bash
   git push -u origin feature/HU-01-login
   ```
5. **I4 (Tester)** revisa el PR y verifica que GitHub Actions (`.github/workflows/ci.yml`: `pytest -q` + `docker build`) esté en verde antes de hacer merge.

## 3. Verificación con Docker
```bash
docker compose build
docker compose run --rm antdron
```

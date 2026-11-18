# Guía de Colaboración en el Repositorio — ANTDRON Grupo 06 (Python 3.12 · XP)

Guía rápida para que los **4 integrantes (`I1 · Ronny Veloz`, `I2 · Oscar Tamayo`, `I3 · Analy Yepez`, `I4 · Mateo Yaguari`)** clonen el repositorio, trabajen en ramas XP y mantengan `main` siempre en verde.

## Repartición por Partes
- **Parte 1 (`Analy Yepez` — I3):** Login, equipo, `Grupo06.csv` y Diagrama de Casos de Uso (`feature/parte1-login-csv`).
- **Parte 2 (`Ronny Veloz` — I1):** Autómata (`{2, 3, 5, 9}`), Bomba, tabla de destrucción, Grafo+Gramática y documento final (`feature/parte2-automata`).
- **Parte 3 (`Oscar Tamayo` — I2):** Hormigas, `Alimento`, `IIA`, `AntCiberDron`, SQLite, Diagrama de Clases y MER (`feature/parte3-hormigas-dron`).
- **Parte 4 (`Mateo Yaguari` — I4):** Pantallas del Hormiguero Virtual, `main.py`, Docker, pruebas `pytest` y Diagrama de Arquitectura (`feature/parte4-ui-docker`).

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

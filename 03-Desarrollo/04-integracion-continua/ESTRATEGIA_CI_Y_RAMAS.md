# 15. Estrategia de Integración Continua (CI) y Control de Versiones (Python 3.12)

**Responsables:** **I4 (Tester)** mantiene el pipeline Python/Docker; **I1 (Gestor)** custodia la rama `main`.

## Flujo de Trabajo Git
1. **Rama `main` siempre estable y desplegable:** Prohibido hacer `push` directo sin pasar pruebas.
2. **Ramas cortas por historia:** `feature/HU-01-login`, `feature/HU-03-automata`, etc.
3. **Pull Request + Checklist de calidad:**
   - Todo test TDD con `pytest` (Python 3.12) escrito y en verde (`pytest`).
   - Revisión cruzada por **I4 (Tester)** verificando cumplimiento exacto del PDF (evitando `-0.5` por incidentes).
   - El workflow de GitHub Actions (`.github/workflows/ci.yml`) configura Python 3.12, ejecuta `pytest` y valida `docker build -t antdron:ci .`.
4. **Integración frecuente:** Mínimo una integración a `main` por historia terminada (varias veces por iteración).

> **Prevención de la penalización `-0.5` del PDF:** Si algún test de `pytest` o el `docker build` se rompe en `main`, la prioridad #1 del equipo entero es repararlo antes de iniciar otra historia.

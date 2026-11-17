# 10. Funcionalidad Mínima (MVP — Release 1 · Python 3.12)

**Definido por:** I1 (Cliente+Gestor) & I2 (Coach) · **Lenguaje:** **Python 3.12**.

En XP se construye primero el **sistema mínimo útil de extremo a extremo** antes de añadir adornos o módulos secundarios.

## Alcance Exacto del MVP (Final de Iteración 1)
1. **Autenticación (`HU-01`):** Login en consola Python para los **4 integrantes** y **`patmic`/`123`** con bloqueo al 3.er fallo.
2. **Presentación + Lectura CSV (`HU-02`):** Impresión de `[+] TEAM [6]` y lectura mediante `SistemaRuso.readCoord("data/Grupo06.csv")` con loading animado `\ | / - | 100%` por línea.
3. **Núcleo Biológico (`HU-04`, `HU-05`):** Contrato `pkAntCiberDronContract.IHormiga` (`comer(self, a: Alimento) -> bool`), clase abstracta `Hormiga` (`Id: int`, `sexo: str`, `estado: str`), `HLarva` que vive con `Nectar` y evoluciona (o muere) mediante `EvolucionStrategy`.
4. **Entregable Ejecutable:** `python main.py` ejecutable, suite `pytest` verde en GitHub Actions y primer `Dockerfile` (`python:3.12-slim`) capaz de ejecutar la consola interactiva.

**Lo que queda explícitamente fuera del MVP (entra en R2/R3):** menús de consola completos del Hormiguero, persistencia SQLite, extremidades/láser/turbo del `AntCiberDron` y entrenamiento de idiomas EN/ES.

# `src/ant/ui/`

Pantallas del Hormiguero Virtual en **consola con menús** *(código Python pendiente)*. Se usa consola en lugar de ventanas gráficas para que funcione sin fallos dentro de Docker:

- `login_view.py` — Pantalla de autenticación (3 intentos).
- `hormiguero_menu.py` — Menú principal con opciones:
  - Gestión del Hormiguero Virtual (crear `HLarva`, seleccionar `Alimento`, visualizar evolución/muerte).
  - Carga de `Grupo06.csv` y tabla de Coordenadas Destruidas (`IIA.buscar`).
  - Panel de `AntCiberDron` (extremidades, potencia de láser, recarga/reemplazo de fuente asistida por `IIA`, vuelo y entrenamiento EN/ES exclusivo con `ExpertoParlante`).

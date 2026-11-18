# `tests/ant/iia/`

Pruebas unitarias TDD en **Python 3.12** (`pytest`) del autómata y la bomba (**Parte 2 — Ronny Veloz**):

- `test_bomba_automata.py` — Verifica rechazo de cadena vacía y símbolos fuera de $\Sigma = \{a,b,c,d,t\}$, aceptación de palabras de $L = \{ab^*, abc, abcdt^+\}$, rechazo de casos trampa (`abbc`, `abcd`, `abcdd`), comparación masiva contra el oráculo `re.fullmatch()`, `Bomba.explotar(...)`, `mostrar_destruir(...)` e integración con `data/Grupo06.csv`.

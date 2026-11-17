# `tests/ant/iia/`

Pruebas unitarias TDD en **Python 3.12** (`pytest`) del autómata *(pendientes hasta tener las 4 cédulas)*:

- `test_bomba_automata.py` — Rechaza cadena vacía y símbolos fuera de $\Sigma = \{a,b,c,d,t\}$; acepta palabras del lenguaje unido de los 4 últimos dígitos; comparación masiva contra el oráculo `re.fullmatch()` del módulo `re`.

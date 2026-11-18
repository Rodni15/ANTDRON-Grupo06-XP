# `src/ant/iia/`

Motor formal del autómata de la bomba e impresión de coordenadas a destruir (**Parte 2 — Ronny Veloz (`I1`) · Historia de Usuario `HU-03`**):

- `bomba_automata.py` → `BombaAutomata` (y alias `Automata`): implementación propia del AFD $A = (Q, \Sigma, \delta, q_0, F)$ para los últimos dígitos `{2, 3, 5, 9}` ($L = \{ab^*, abc, abcdt^+\}$), con métodos `aceptar(cadena: str) -> bool`, `evaluar(palabra: str) -> bool` y `recorrido(cadena: str) -> list[str]`.
- `bomba.py` → `Bomba(automata)` con `explotar(palabra: str) -> bool` (y alias `buscar(tipoArsenal: str) -> bool`), más `mostrar_destruir(coordenadas, evaluador=None) -> list[CoordenadaUK]`.

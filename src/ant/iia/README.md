# `src/ant/iia/`

Motor formal del autómata de la bomba *(código Python pendiente hasta tener las 4 cédulas)*:

- `bomba_automata.py` → clase `BombaAutomata` — Implementación propia del AFD $A = (Q, \Sigma, \delta, q_0, F)$ construido con el **último dígito de cada una de las 4 cédulas** (diccionario de transición $\delta$ y estado pozo, sin usar `re.fullmatch()` en producción).

"""Motor formal del Autómata Finito Determinista (AFD) de la bomba (Grupo 06).

Últimos dígitos de las 4 cédulas del equipo:
  - Analy Yépez   (1721396412) -> 2 -> Coord-02 -> ab*
  - Óscar Tamayo  (1722578703) -> 3 -> Coord-03 -> abc
  - Ronny Veloz   (1724490055) -> 5 -> Coord-05 -> abcdt+
  - Mateo Yaguari (1726389099) -> 9 -> Coord-09 -> ab*

Lenguaje unido reconocido por la bomba:
  L = { ab*, abc, abcdt+ } sobre Σ = { a, b, c, d, t }
"""

ALFABETO: frozenset[str] = frozenset({"a", "b", "c", "d", "t"})
ESTADO_INICIAL: str = "q0"
ESTADO_ERROR: str = "q_err"
ESTADOS_ACEPTACION: frozenset[str] = frozenset({"q1", "q2", "q2b", "q3", "q5"})

# Tabla de transición δ: Q × Σ -> Q (toda transición no listada cae en q_err)
TRANSICIONES: dict[str, dict[str, str]] = {
    "q0": {"a": "q1"},
    "q1": {"b": "q2"},
    "q2": {"b": "q2b", "c": "q3"},
    "q2b": {"b": "q2b"},
    "q3": {"d": "q4"},
    "q4": {"t": "q5"},
    "q5": {"t": "q5"},
    "q_err": {},
}


class BombaAutomata:
    """AFD A = (Q, Σ, δ, q0, F) evaluado carácter por carácter sin usar regex."""

    def __init__(self) -> None:
        self.alfabeto: frozenset[str] = ALFABETO
        self.estadoInicial: str = ESTADO_INICIAL
        self.estadoError: str = ESTADO_ERROR
        self.estadosAceptacion: frozenset[str] = ESTADOS_ACEPTACION
        self.transiciones: dict[str, dict[str, str]] = TRANSICIONES

    def recorrido(self, cadena: str) -> list[str]:
        """Devuelve la secuencia de estados visitados al evaluar la cadena."""
        if not isinstance(cadena, str):
            return [self.estadoError]
        palabra = cadena.strip()
        if not palabra:
            return [self.estadoInicial]

        estado = self.estadoInicial
        visitados = [estado]
        for simbolo in palabra:
            if simbolo not in self.alfabeto:
                estado = self.estadoError
            else:
                estado = self.transiciones.get(estado, {}).get(simbolo, self.estadoError)
            visitados.append(estado)
        return visitados

    def aceptar(self, cadena: str) -> bool:
        """Retorna True si la palabra pertenece a L = {ab*, abc, abcdt+}."""
        if not isinstance(cadena, str):
            return False
        palabra = cadena.strip()
        if not palabra:
            return False

        estado = self.estadoInicial
        for simbolo in palabra:
            if simbolo not in self.alfabeto:
                return False
            estado = self.transiciones.get(estado, {}).get(simbolo, self.estadoError)
            if estado == self.estadoError:
                return False
        return estado in self.estadosAceptacion

    def evaluar(self, palabra: str) -> bool:
        """Alias compatible con la firma Automata.evaluar(palabra) -> True/False."""
        return self.aceptar(palabra)


# Alias para compatibilidad directa con la especificación de Parte 2 (Automata.evaluar)
Automata = BombaAutomata

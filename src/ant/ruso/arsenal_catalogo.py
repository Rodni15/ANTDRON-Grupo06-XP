"""Catálogo oficial del PDF: alfabeto, horarios y lenguaje de cada coordenada."""

ALFABETO = {"a": "Avión", "b": "Barco", "c": "Convoy", "d": "Dron", "t": "Tanque"}
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# dígito -> (día, horario, lenguaje, palabras de ejemplo del lenguaje)
COORDENADAS = {
    0: (None, "", "a+", ["a", "aa", "aaa"]),
    1: ("Lunes", "01-02", "a+", ["aaaa", "a", "aa"]),
    2: ("Martes", "02-04", "ab*", ["ab", "abbb", "a"]),
    3: ("Miércoles", "03-06", "abc", ["abc"]),
    4: ("Jueves", "04-08", "abcd*", ["abcd", "abc", "abcddd"]),
    5: ("Viernes", "05-10", "abcdt+", ["abcdt", "abcdttt", "abcdtt"]),
    6: ("Jueves", "04-08", "abcdt+", ["abcdttttt", "abcdt"]),
    7: ("Miércoles", "03-06", "abcd*", ["abcdd", "abc"]),
    8: ("Martes", "02-04", "abc", ["abc"]),
    9: ("Lunes", "01-02", "ab*", ["ab", "a", "abbbb"]),
}


class ArsenalCatalogo:
    @staticmethod
    def lenguaje(digito: int) -> str:
        return COORDENADAS[digito][2]

    @staticmethod
    def filaCSV(digito: int, uso: int = 0) -> str:
        """Fila de Grupo06.csv para un dígito; 'uso' rota la palabra de ejemplo."""
        dia, hora, _, palabras = COORDENADAS[digito]
        celdas = [hora if d == dia else "" for d in DIAS]
        return f"Coord-0{digito};" + ";".join(celdas) + f";{palabras[uso % len(palabras)]}"

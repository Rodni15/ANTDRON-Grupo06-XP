from pkAntCiberDronContract.coordenada_uk import CoordenadaUK
from pkAntCiberDronContract.utility import Utility


def test_mostrarLoading_llega_a_100_con_spinner(capsys):
    Utility.mostrarLoading(0)
    salida = capsys.readouterr().out
    assert "100%" in salida
    for simbolo in "\\|/-":
        assert simbolo in salida


def test_formatearFila():
    fila = Utility.formatearFila(CoordenadaUK("Coord-05", "", "", "", "", "05-10", "abcdttt"))
    assert "Coord-05" in fila and "05-10" in fila and fila.endswith("abcdttt")

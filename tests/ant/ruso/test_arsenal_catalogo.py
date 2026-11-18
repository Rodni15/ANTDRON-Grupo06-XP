import re

from ant.ruso.arsenal_catalogo import COORDENADAS, ArsenalCatalogo


def test_fila_respeta_horario_del_pdf():
    assert ArsenalCatalogo.filaCSV(5) == "Coord-05;;;;;05-10;abcdt"
    assert ArsenalCatalogo.filaCSV(1) == "Coord-01;01-02;;;;;aaaa"
    assert ArsenalCatalogo.filaCSV(0) == "Coord-00;;;;;;a"


def test_palabras_de_ejemplo_pertenecen_a_su_lenguaje():
    for d, (_, _, lenguaje, palabras) in COORDENADAS.items():
        for p in palabras:
            assert re.fullmatch(lenguaje, p), (d, p)

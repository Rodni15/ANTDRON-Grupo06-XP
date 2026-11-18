"""Pruebas TDD (pytest) para Parte 2: BombaAutomata, Bomba y mostrar_destruir."""
import itertools
from pathlib import Path
import re

import pytest

from ant.iia.bomba import Bomba, mostrar_destruir
from ant.iia.bomba_automata import Automata, BombaAutomata
from pkAntCiberDronContract.coordenada_uk import CoordenadaUK
from pkAntCiberDronContract.sistema_ruso import SistemaRuso

PATRON_ORACULO = re.compile(r"(?:ab*|abc|abcdt+)")


@pytest.fixture
def automata() -> BombaAutomata:
    return BombaAutomata()


@pytest.mark.parametrize(
    "palabra",
    [
        "a",
        "ab",
        "abb",
        "abbb",
        "abbbb",
        "abc",
        "abcdt",
        "abcdtt",
        "abcdttt",
        "abcdttttt",
    ],
)
def test_automata_acepta_palabras_validas_grupo06(automata: BombaAutomata, palabra: str):
    assert automata.aceptar(palabra) is True
    assert automata.evaluar(palabra) is True


@pytest.mark.parametrize(
    "palabra",
    [
        "",
        "   ",
        "aa",
        "aaa",
        "aaaa",
        "b",
        "ba",
        "abbc",
        "abbbc",
        "abbcdt",
        "ac",
        "ad",
        "at",
        "abcd",
        "abcdd",
        "abcddd",
        "abcdta",
        "abcdtd",
        "abcde",
        "xyz",
        "123",
        "A",
    ],
)
def test_automata_rechaza_palabras_invalidas_y_trampa(automata: BombaAutomata, palabra: str):
    assert automata.aceptar(palabra) is False
    assert automata.evaluar(palabra) is False


def test_automata_rechaza_entradas_no_str(automata: BombaAutomata):
    assert automata.aceptar(None) is False  # type: ignore[arg-type]
    assert automata.evaluar(123) is False  # type: ignore[arg-type]


def test_alias_automata_y_recorrido():
    afd = Automata()
    assert afd.evaluar("abcdt") is True
    assert afd.recorrido("abcdt") == ["q0", "q1", "q2", "q3", "q4", "q5"]
    assert afd.recorrido("abbc")[-1] == "q_err"


def test_comparacion_masiva_contra_oraculo_re(automata: BombaAutomata):
    alfabeto_prueba = ("a", "b", "c", "d", "t", "x")
    for longitud in range(0, 7):
        for tupla in itertools.product(alfabeto_prueba, repeat=longitud):
            palabra = "".join(tupla)
            esperado = bool(PATRON_ORACULO.fullmatch(palabra))
            obtenido = automata.aceptar(palabra)
            assert obtenido is esperado, f"Discrepancia en '{palabra}': AFD={obtenido} vs re={esperado}"


def test_bomba_explotar():
    afd = Automata()
    bomba = Bomba(afd)
    assert bomba.explotar("ab") is True
    assert bomba.explotar("abc") is True
    assert bomba.explotar("abcdttt") is True
    assert bomba.explotar("abcd") is False
    assert bomba.explotar("aaaa") is False
    assert bomba.buscar("abcdt") is True


def test_mostrar_destruir_imprime_tabla_solo_detonadas(capsys):
    coords = [
        CoordenadaUK("Coord-01", lunes="01-02", tipoArsenal="aaaa"),
        CoordenadaUK("Coord-02", martes="02-04", tipoArsenal="ab"),
        CoordenadaUK("Coord-03", miercoles="03-06", tipoArsenal="abc"),
        CoordenadaUK("Coord-04", jueves="04-08", tipoArsenal="abcd"),
        CoordenadaUK("Coord-05", viernes="05-10", tipoArsenal="abcdttt"),
    ]
    destruidas = mostrar_destruir(coords)
    salida = capsys.readouterr().out

    assert [c.getGeoposicion() for c in destruidas] == ["Coord-02", "Coord-03", "Coord-05"]
    assert "COORDENADAS UCRANIANAS A DESTRUIR:" in salida
    assert "Geoposición | Tipo Arsenal | Acción" in salida
    assert "Coord-02" in salida and "ab" in salida and "true" in salida
    assert "Coord-03" in salida and "abc" in salida
    assert "Coord-05" in salida and "abcdttt" in salida
    assert "Coord-01" not in salida
    assert "Coord-04" not in salida


def test_integracion_con_grupo06_csv_real(capsys):
    raiz = Path(__file__).resolve().parents[3]
    csv_path = raiz / "data" / "Grupo06.csv"
    coords = SistemaRuso(delayMs=0).readCoord(str(csv_path), mostrar=False)
    assert len(coords) == 40

    destruidas = mostrar_destruir(coords)
    salida = capsys.readouterr().out

    esperadas = [c for c in coords if PATRON_ORACULO.fullmatch(c.getTipoArsenal())]
    assert len(destruidas) == len(esperadas) == 29
    assert "COORDENADAS UCRANIANAS A DESTRUIR:" in salida

from ant.ruso.integrante import Integrante
from pkAntCiberDronContract.coordenada_uk import CoordenadaUK
from pkAntCiberDronContract.sistema_ruso import SistemaRuso

CSV = (
    "Geoposición;Lunes;Martes;Miércoles;Jueves;Viernes;Tipo Arsenal\n"
    "Coord-01;01-02;;;;;aaaa\n"
    "Coord-05;;;;;05-10;abcdttt\n"
    "\n"
    "Coord-09;01-02;;;;;ab\n"
)


def sistema():
    return SistemaRuso([Integrante("1700000001", "Ana", "ana", "clave")], delayMs=0)


def test_login_profesor_e_integrante():
    s = sistema()
    assert s.login("patmic", "123")
    assert s.login("ana", "clave")


def test_login_rechaza_credenciales_incorrectas():
    s = sistema()
    assert not s.login("patmic", "999")
    assert not s.login("intruso", "123")
    assert not s.login("", "")


def test_readCoord_devuelve_coordenadas(tmp_path):
    archivo = tmp_path / "Grupo06.csv"
    archivo.write_text(CSV, encoding="utf-8")
    coords = sistema().readCoord(str(archivo), mostrar=False)
    assert len(coords) == 3
    assert all(isinstance(c, CoordenadaUK) for c in coords)
    assert coords[1].getGeoposicion() == "Coord-05"
    assert coords[1].getTipoArsenal() == "abcdttt"


def test_readCoord_muestra_tabla(tmp_path, capsys):
    archivo = tmp_path / "Grupo06.csv"
    archivo.write_text(CSV, encoding="utf-8")
    sistema().readCoord(str(archivo))
    salida = capsys.readouterr().out
    assert "[+] COORDENADAS UCRANIANAS:" in salida
    assert "100%" in salida and "Coord-09" in salida


def test_readCoord_archivo_inexistente_no_falla(tmp_path):
    assert sistema().readCoord(str(tmp_path / "no_existe.csv")) == []


def test_mostrarEquipo(capsys):
    s = sistema()
    s.mostrarEquipo("Hormiguero Cibernético", s.integrantes, 6)
    salida = capsys.readouterr().out
    assert "[+] TEAM [6]: Hormiguero Cibernético" in salida
    assert "Alumno 1: 1700000001 | Ana" in salida

from ant.ruso.auth_service import AuthService
from ant.ruso.integrante import Integrante
from pkAntCiberDronContract.sistema_ruso import SistemaRuso


def servicio(respuestas):
    datos = iter(respuestas)
    s = SistemaRuso([Integrante("1700000001", "Ana", "ana", "clave")])
    return AuthService(s, entrada=lambda _: next(datos), entradaClave=lambda _: next(datos))


def test_acceso_al_primer_intento():
    assert servicio(["patmic", "123"]).autenticar()


def test_acceso_en_el_tercer_intento():
    assert servicio(["x", "1", "y", "2", "ana", "clave"]).autenticar()


def test_bloqueo_tras_tres_fallos(capsys):
    assert not servicio(["x", "1", "y", "2", "z", "3"]).autenticar()
    assert "Acceso bloqueado" in capsys.readouterr().out

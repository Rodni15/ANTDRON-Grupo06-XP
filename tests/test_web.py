"""Pruebas de aceptación de la interfaz web de la Parte 4."""
import pytest

from web_app import create_app


@pytest.fixture
def cliente(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "antdron.db"), "SECRET_KEY": "prueba"})
    return app.test_client()


def iniciar(cliente):
    return cliente.post("/login", data={"usuario": "myaguari", "clave": "123"}, follow_redirects=True)


def test_rutas_protegidas_y_login(cliente):
    assert cliente.get("/panel").status_code == 302
    respuesta = iniciar(cliente)
    assert respuesta.status_code == 200
    assert b"Centro de coordinaci" in respuesta.data


def test_limite_de_tres_intentos(cliente):
    for _ in range(3):
        respuesta = cliente.post("/login", data={"usuario": "incorrecto", "clave": "incorrecta"}, follow_redirects=True)
    assert b"Acceso bloqueado" in respuesta.data
    assert b"Iniciar sesi" in respuesta.data


def test_integracion_csv_y_hormiguero(cliente):
    iniciar(cliente)
    coordenadas = cliente.post("/coordenadas", follow_redirects=True)
    assert b"coordenadas ucranianas" in coordenadas.data.lower()
    creada = cliente.post("/hormiguero/crear", data={"sexo": "hembra"}, follow_redirects=True)
    assert b"Larva #1 creada" in creada.data
    alimentada = cliente.post(
        "/hormiguero/alimentar",
        data={"id_hormiga": "1", "alimento": "herbivoro"},
        follow_redirects=True,
    )
    assert b"HRastreadora" in alimentada.data


def test_validaciones_hormiguero(cliente):
    iniciar(cliente)
    creada = cliente.post("/hormiguero/crear", data={"sexo": "otro"}, follow_redirects=True)
    assert b"Selecciona un sexo v" in creada.data

    alimentada = cliente.post(
        "/hormiguero/alimentar",
        data={"id_hormiga": "999", "alimento": "nectar"},
        follow_redirects=True,
    )
    assert b"Identificador o alimento inv" in alimentada.data


def test_bloqueo_persistente_y_logout(cliente):
    for _ in range(3):
        cliente.post("/login", data={"usuario": "no", "clave": "no"}, follow_redirects=True)

    bloqueado = cliente.post("/login", data={"usuario": "myaguari", "clave": "123"}, follow_redirects=True)
    assert b"Acceso bloqueado" in bloqueado.data

    cliente.post("/logout", follow_redirects=True)
    assert cliente.get("/panel").status_code == 302


def test_operaciones_reales_dron(cliente):
    iniciar(cliente)
    vuelo = cliente.post("/dron/operacion", data={"accion": "volar"}, follow_redirects=True)
    assert b"turbo reactor" in vuelo.data.lower()

    recarga = cliente.post("/dron/operacion", data={"accion": "recargar"}, follow_redirects=True)
    assert b"recargada" in recarga.data.lower()

    reemplazo = cliente.post(
        "/dron/operacion",
        data={"accion": "reemplazar", "capacidad": "250"},
        follow_redirects=True,
    )
    assert b"reemplazada" in reemplazo.data.lower()

from pathlib import Path

from ant.alimento.alimento import AHervivoro, Nectar
from ant.db.sqlite_connection import SqliteConnection
from ant.dron.ant_ciber_dron import AntCiberDron, FuenteDePoder, Laser, Metralleta
from ant.dron.modulo_idioma import Area, ExpertoParlante, Idioma, ModuloIdioma
from ant.hormiguero.hormiga import HLarva, HRastreadora
from ant.hormiguero.hormiguero import Hormiguero
from ant.iia import Bomba, mostrar_destruir
from ant.iia.iia import IIA
from pkAntCiberDronContract.sistema_ruso import SistemaRuso


class EvaluadorPrueba:
    def explotar(self, palabra: str) -> bool:
        return palabra == "abc"


def test_evolucion_y_muerte_persisten(tmp_path):
    db = SqliteConnection(tmp_path / "antdron.db")
    hormiguero = Hormiguero(db)
    larva = hormiguero.crearLarva("hembra")
    assert isinstance(larva, HLarva)
    assert hormiguero.alimentar(larva.Id, Nectar())
    assert isinstance(hormiguero.listarHormigas()[0], HLarva)
    assert hormiguero.alimentar(larva.Id, AHervivoro())

    hormiguero = Hormiguero(db)
    adulta, = hormiguero.listarHormigas()
    assert isinstance(adulta, HRastreadora)
    assert (adulta.Id, adulta.sexo) == (larva.Id, larva.sexo)
    assert not hormiguero.alimentar(adulta.Id, Nectar())
    assert not hormiguero.alimentar(adulta.Id, AHervivoro())
    assert Hormiguero(db).listarHormigas()[0].estado == "MUERTA"


def test_dron_acepta_palabras_del_lector_y_modela_la_energia():
    dron = AntCiberDron(EvaluadorPrueba(), FuenteDePoder(1))
    csv = Path(__file__).resolve().parents[3] / "data" / "Grupo06.csv"
    palabras = [fila.getTipoArsenal() for fila in SistemaRuso().readCoord(csv, mostrar=False)]
    assert "abc" in palabras
    assert [dron.buscar(palabra) for palabra in palabras] == [p == "abc" for p in palabras]
    assert isinstance(dron, IIA)
    assert len(dron.patas) == 6
    assert isinstance(dron.patas[0].equipo, Laser)
    assert isinstance(dron.patas[1].equipo, Metralleta)
    assert dron.dispararLaser() == 1
    assert dron.volar()
    assert not dron.volar()
    assert dron.dispararLaser() == 0
    dron.asistirRecargaFuente()
    assert dron.dispararLaser() == 1
    dron.asistirReemplazoFuente(FuenteDePoder(3))
    assert dron.dispararLaser() == 3


def test_entrenamiento_certificado_persiste_por_idioma(tmp_path):
    db = SqliteConnection(tmp_path / "antdron.db")
    modulo = ModuloIdioma(db)
    certificado = ExpertoParlante("Experta", Idioma.ES, True)
    aprendiz = ExpertoParlante("Aprendiz", Idioma.ES)
    assert not modulo.entrenar(Idioma.EN, Area.LEXICO, "dato", certificado)
    assert not modulo.entrenar(Idioma.ES, Area.LEXICO, "dato", aprendiz)
    for area in Area:
        assert modulo.entrenar(Idioma.ES, area, "dato", certificado)
    en = ExpertoParlante("English tutor", Idioma.EN, True)
    assert modulo.entrenar(Idioma.EN, Area.FONETICA, "th", en)
    modulo = ModuloIdioma(db)
    assert [registro.contenido for registro in modulo.consultar(Idioma.EN)] == ["th"]
    assert {registro.area for registro in modulo.consultar(Idioma.ES)} == set(Area)


def test_csv_bomba_y_dron_comparten_el_contrato():
    csv = Path(__file__).resolve().parents[3] / "data" / "Grupo06.csv"
    filas = SistemaRuso().readCoord(csv, mostrar=False)
    bomba = Bomba()
    esperadas = [fila for fila in filas if bomba.explotar(fila.getTipoArsenal())]
    assert len(filas) == 40
    assert len(esperadas) == 29
    assert mostrar_destruir(filas, AntCiberDron(bomba)) == esperadas

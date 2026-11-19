"""Aplicación web de ANTDRON basada en los servicios del dominio."""
from functools import wraps
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from flask import Flask, flash, redirect, render_template, request, session, url_for

from ant.alimento.alimento import ACarnivoro, AHervivoro, AOmnivoro, Nectar
from ant.db.sqlite_connection import SqliteConnection
from ant.dron.ant_ciber_dron import AntCiberDron, FuenteDePoder
from ant.dron.modulo_idioma import Area, ExpertoParlante, Idioma, ModuloIdioma
from ant.hormiguero.hormiguero import Hormiguero
from ant.iia.bomba import Bomba
from ant.ruso.auth_service import MAX_INTENTOS
from ant.ruso.integrante import Integrante
from pkAntCiberDronContract.sistema_ruso import SistemaRuso


RAIZ = Path(__file__).resolve().parent


def create_app(test_config=None):
    app = Flask(__name__, template_folder="web/templates", static_folder="web/static")
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("ANTDRON_SECRET_KEY", "antdron-desarrollo"),
        DATABASE=str(RAIZ / "data" / "antdron.db"),
    )
    if test_config:
        app.config.update(test_config)

    equipo, grupo, integrantes = Integrante.cargarEquipo(RAIZ / "data" / "integrantes.json")
    sistema = SistemaRuso(integrantes, delayMs=0)
    almacenamiento = SqliteConnection(app.config["DATABASE"])
    expertos = {
        "experto-en": ExpertoParlante("Experto de inglés (simulación)", Idioma.EN, True),
        "experto-es": ExpertoParlante("Experto de español (simulación)", Idioma.ES, True),
    }
    hormiguero = Hormiguero(almacenamiento)
    dron = AntCiberDron(Bomba(), modulo_idioma=ModuloIdioma(almacenamiento))
    app.extensions["antdron"] = {
        "equipo": equipo,
        "grupo": grupo,
        "integrantes": integrantes,
        "sistema": sistema,
        "hormiguero": hormiguero,
        "dron": dron,
    }

    def protegido(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            if not session.get("autenticado"):
                flash("Inicia sesión para continuar.", "error")
                return redirect(url_for("login"))
            return view(*args, **kwargs)
        return wrapper

    @app.get("/")
    def login():
        if session.get("autenticado"):
            return redirect(url_for("panel"))
        return render_template("login.html", intentos=session.get("intentos", 0))

    @app.post("/login")
    def autenticar():
        if session.get("bloqueado"):
            flash("Acceso bloqueado tras tres intentos fallidos.", "error")
            return redirect(url_for("login"))
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "")
        intentos = session.get("intentos", 0) + 1
        if sistema.login(usuario, clave):
            session.clear()
            session["autenticado"] = True
            session["usuario"] = usuario
            return redirect(url_for("panel"))
        session["intentos"] = intentos
        if intentos >= MAX_INTENTOS:
            session.clear()
            session["bloqueado"] = True
            flash("Acceso bloqueado tras tres intentos fallidos.", "error")
        else:
            flash(f"Credenciales incorrectas. Intentos restantes: {MAX_INTENTOS - intentos}.", "error")
        return redirect(url_for("login"))

    @app.post("/logout")
    def cerrar_sesion():
        session.clear()
        return redirect(url_for("login"))

    @app.get("/panel")
    @protegido
    def panel():
        coordenadas = []
        if session.get("csv_cargado"):
            filas = sistema.readCoord(RAIZ / "data" / f"Grupo{grupo:02d}.csv", mostrar=False)
            coordenadas = [
                {"geoposicion": c.getGeoposicion(), "tipo": c.getTipoArsenal(),
                 "horarios": c.getHorarios(), "aceptada": dron.buscar(c.getTipoArsenal())}
                for c in filas
            ]
        destruidas = [c for c in coordenadas if c["aceptada"]]
        hormigas = hormiguero.listarHormigas()
        return render_template(
            "dashboard.html",
            equipo=equipo,
            grupo=grupo,
            integrantes=integrantes,
            hormigas=hormigas,
            coordenadas=coordenadas,
            destruidas=destruidas,
            energia=dron.fuente.getEnergia(),
            cantidad_coordenadas=len(coordenadas),
            cantidad_destruidas=len(destruidas),
            cantidad_hormigas=len(hormigas),
            modulo_idioma=dron.moduloIdioma,
            potencia_laser=dron.dispararLaser(),
            expertos=expertos,
            idiomas=list(Idioma),
            areas=list(Area),
        )

    @app.post("/coordenadas")
    @protegido
    def cargar_coordenadas():
        ruta = RAIZ / "data" / f"Grupo{grupo:02d}.csv"
        coordenadas = sistema.readCoord(ruta, mostrar=False)
        if not coordenadas:
            session["coordenadas"] = []
            session["destruidas"] = []
            flash("No se encontraron coordenadas válidas en el CSV.", "error")
            return redirect(url_for("panel", _anchor="coordenadas"))
        session.pop("coordenadas", None)
        session.pop("destruidas", None)
        session["csv_cargado"] = True
        session["animar_csv"] = True
        flash(f"Se cargaron {len(coordenadas)} coordenadas.", "success")
        return redirect(url_for("panel", _anchor="coordenadas"))

    @app.post("/idiomas/entrenar")
    @protegido
    def entrenar_idioma():
        try:
            experto = expertos[request.form.get("experto", "")]
            aceptado = dron.moduloIdioma.entrenar(
                Idioma(request.form.get("idioma")),
                Area(request.form.get("area")),
                request.form.get("contenido", ""), experto,
            )
            flash("Entrenamiento guardado." if aceptado else "Selecciona un experto del idioma y contenido válido.",
                  "success" if aceptado else "error")
        except (KeyError, ValueError):
            flash("Idioma, área o experto inválido.", "error")
        return redirect(url_for("panel", _anchor="idiomas"))

    @app.post("/hormiguero/crear")
    @protegido
    def crear_larva():
        sexo = request.form.get("sexo", "").strip()
        if sexo not in {"hembra", "macho"}:
            flash("Selecciona un sexo válido.", "error")
        else:
            larva = hormiguero.crearLarva(sexo)
            flash(f"Larva #{larva.Id} creada correctamente.", "success")
        return redirect(url_for("panel", _anchor="hormiguero"))

    @app.post("/dron/operacion")
    @protegido
    def operar_dron():
        accion = request.form.get("accion", "")
        if accion == "recargar":
            dron.asistirRecargaFuente()
            flash("Fuente de poder recargada.", "success")
        elif accion == "volar":
            if dron.volar():
                flash("El turbo reactor inició el vuelo.", "success")
            else:
                flash("El vuelo no fue posible: la fuente no tiene energía.", "error")
        elif accion == "reemplazar":
            capacidad = request.form.get("capacidad", "").strip()
            try:
                dron.asistirReemplazoFuente(FuenteDePoder(int(capacidad)))
                flash("Fuente de poder reemplazada.", "success")
            except (TypeError, ValueError):
                flash("Indica una capacidad de energía válida.", "error")
        else:
            flash("Operación del dron no reconocida.", "error")
        return redirect(url_for("panel", _anchor="dron"))

    @app.post("/hormiguero/alimentar")
    @protegido
    def alimentar():
        try:
            identificador = int(request.form.get("id_hormiga", ""))
            alimentos = {
                "nectar": Nectar,
                "herbivoro": AHervivoro,
                "carnivoro": ACarnivoro,
                "omnivoro": AOmnivoro,
            }
            alimento = alimentos[request.form.get("alimento", "")]
            vive = hormiguero.alimentar(identificador, alimento())
            flash("La hormiga sobrevivió la alimentación." if vive else "La hormiga murió.", "success" if vive else "error")
        except (ValueError, KeyError):
            flash("Identificador o alimento inválido.", "error")
        return redirect(url_for("panel", _anchor="hormiguero"))

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=False)

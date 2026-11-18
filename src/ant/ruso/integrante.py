"""Datos de cada miembro del Grupo 06."""
import json


class Integrante:
    def __init__(self, cedula: str, nombre: str, usuario: str = "", clave: str = "", rol: str = ""):
        self.cedula = cedula
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.rol = rol

    @staticmethod
    def cargarEquipo(ruta: str) -> tuple[str, int, list["Integrante"]]:
        """Lee data/integrantes.json -> (nombre del equipo, número de grupo, integrantes)."""
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
        integrantes = [Integrante(**i) for i in datos["integrantes"]]
        return datos["equipo"], int(datos["grupo"]), integrantes

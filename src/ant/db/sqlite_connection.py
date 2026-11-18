"""Persistencia del hormiguero y del entrenamiento del grupo 06."""

from contextlib import contextmanager
from pathlib import Path
import sqlite3


class SqliteConnection:
    def __init__(self, ruta: str | Path = Path("data/antdron.db")) -> None:
        self.ruta = ruta
        with self.abrir() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS hormiga (
                    id INTEGER PRIMARY KEY,
                    tipo TEXT NOT NULL CHECK (tipo IN ('HLarva', 'HRastreadora')),
                    sexo TEXT NOT NULL,
                    estado TEXT NOT NULL CHECK (estado IN ('VIVA', 'MUERTA'))
                );
                CREATE TABLE IF NOT EXISTS alimentacion (
                    id INTEGER PRIMARY KEY,
                    hormiga_id INTEGER NOT NULL REFERENCES hormiga(id),
                    alimento TEXT NOT NULL,
                    resultado TEXT NOT NULL,
                    fecha TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS entrenamiento_idioma (
                    id INTEGER PRIMARY KEY,
                    experto TEXT NOT NULL,
                    idioma TEXT NOT NULL CHECK (idioma IN ('EN', 'ES')),
                    area TEXT NOT NULL,
                    contenido TEXT NOT NULL,
                    fecha TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """)

    @contextmanager
    def abrir(self):
        db = sqlite3.connect(self.ruta)
        try:
            db.execute("PRAGMA foreign_keys = ON")
            with db:
                yield db
        finally:
            db.close()

"""Genera data/Grupo06.csv a partir de las cédulas de data/integrantes.json.
Una fila por cada dígito de cada cédula, según la tabla oficial del PDF.
Uso (desde la raíz del proyecto): python tools/generar_csv.py
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "src"))

from ant.ruso.arsenal_catalogo import ArsenalCatalogo  # noqa: E402
from ant.ruso.integrante import Integrante  # noqa: E402


def main():
    _, grupo, integrantes = Integrante.cargarEquipo(RAIZ / "data" / "integrantes.json")
    usos = {d: 0 for d in range(10)}
    filas = ["Geoposición;Lunes;Martes;Miércoles;Jueves;Viernes;Tipo Arsenal"]
    for i in integrantes:
        for ch in i.cedula:
            d = int(ch)
            filas.append(ArsenalCatalogo.filaCSV(d, usos[d]))
            usos[d] += 1
    salida = RAIZ / "data" / f"Grupo{grupo:02d}.csv"
    salida.write_text("\n".join(filas) + "\n", encoding="utf-8")
    print(f"Generado {salida.name} con {len(filas) - 1} coordenadas")


if __name__ == "__main__":
    main()

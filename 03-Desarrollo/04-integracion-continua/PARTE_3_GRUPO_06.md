# Grupo 06 · Integración de la Parte 3

## Para las pantallas

```python
from ant.alimento.alimento import AHervivoro, Nectar
from ant.db.sqlite_connection import SqliteConnection
from ant.hormiguero.hormiguero import Hormiguero
from ant.dron.modulo_idioma import ModuloIdioma

db = SqliteConnection("data/antdron.db")
hormiguero = Hormiguero(db)
larva = hormiguero.crearLarva("hembra")
hormiguero.alimentar(larva.Id, Nectar())
hormiguero.alimentar(larva.Id, AHervivoro())
rastreadora = hormiguero.listarHormigas()[0]
idiomas = ModuloIdioma(db)
```

El menú consulta `listarHormigas()` después de alimentar para mostrar el tipo y estado actuales. `alimentar()` devuelve si la hormiga está viva. Cada alimentación guarda el tipo y estado resultantes junto con el historial en una transacción.

## Para el autómata

```python
from ant.dron.ant_ciber_dron import AntCiberDron

# bomba es la instancia de la Parte 2 con explotar(palabra) -> bool.
dron = AntCiberDron(bomba, modulo_idioma=idiomas)
aceptadas = [fila for fila in coordenadas if dron.buscar(fila.getTipoArsenal())]
```

La Parte 2 construye la tabla final a partir de las filas aceptadas. La Parte 4 puede usar `dron.asistirRecargaFuente()`, `dron.asistirReemplazoFuente(nueva)` y `dron.moduloIdioma.consultar(idioma)`. La simulación usa 100 unidades iniciales por defecto y consume una unidad por vuelo.

## Entregables XP

- [Historias HU-04 a HU-08](../../01-Planificacion/01-historias-usuario/TARJETAS_HISTORIAS_USUARIO.md)
- [Diagrama de clases](../../02-Diseno/diagramas/01-diagrama-clases.md)
- [Modelo entidad-relación](../../02-Diseno/diagramas/04-modelo-entidad-relacion.md)
- [Pruebas de la Parte 3](../../tests/ant/hormiguero/test_parte3.py)

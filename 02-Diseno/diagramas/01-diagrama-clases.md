# Grupo 06 · Diagrama de clases

El diagrama cubre la Parte 3 y los contratos que usa durante la integración. Ronny proporciona la implementación de `Evaluador`; Mateo conecta el menú con `Hormiguero` y `ModuloIdioma`.

![Diagrama de clases del grupo 06](img/01-diagrama-clases.png)

```plantuml
@startuml
title ANTDRON · Grupo 06 · Diagrama de clases
skinparam classAttributeIconSize 0
skinparam packageStyle rectangle
hide empty members

package pkAntCiberDronContract {
  class SistemaRuso {
    +login(usuario, clave): bool
    +readCoord(filename, mostrar): list
    +mostrarEquipo(equipo, integrantes, numero)
  }
  class CoordenadaUK {
    +getGeoposicion(): str
    +getTipoArsenal(): str
    +getHorarios(): list
  }
  class Utility
}

package ant.ruso {
  class AuthService
  class Integrante
}

package ant.alimento {
  abstract class Alimento
  class Nectar
  class AHervivoro
}

package ant.hormiguero {
  interface IHormiga {
    +comer(alimento): bool
  }
  abstract class Hormiga {
    +Id: int
    +sexo: str
    +estado: str
    +morir()
  }
  class HLarva
  class HRastreadora
  class Hormiguero {
    +crearLarva(sexo): HLarva
    +alimentar(id_hormiga, alimento): bool
    +listarHormigas(): list
  }
}

package ant.iia {
  interface Evaluador {
    +explotar(palabra): bool
  }
  interface IIA {
    +buscar(tipoArsenal): bool
  }
}

package ant.dron {
  class AntCiberDron {
    +buscar(tipoArsenal): bool
    +volar(): bool
    +dispararLaser(): int
    +asistirRecargaFuente()
    +asistirReemplazoFuente(nueva)
  }
  class FuenteDePoder {
    +getEnergia(): int
    +consumir(cantidad): bool
    +recargar()
  }
  class Pata {
    +posicion: str
    +equipo
  }
  class Metralleta
  class Laser
  class TurboReactor
  class ModuloIdioma {
    +entrenar(idioma, area, dato, experto): bool
    +consultar(idioma): tuple
  }
  class ExpertoParlante {
    +nombre: str
    +idioma: Idioma
    +certificado: bool
  }
  class Entrenamiento
  enum Idioma {
    EN
    ES
  }
  enum Area {
    LEXICO
    GRAMATICA
    FONETICA
  }
}

package ant.db {
  class SqliteConnection {
    +abrir()
  }
}

AuthService --> SistemaRuso
SistemaRuso ..> Integrante
SistemaRuso ..> CoordenadaUK
SistemaRuso ..> Utility
IHormiga <|.. Hormiga
Hormiga <|-- HLarva
Hormiga <|-- HRastreadora
Alimento <|-- Nectar
Alimento <|-- AHervivoro
Hormiga ..> Alimento
Hormiguero "1" o-- "0..*" Hormiga
Hormiguero ..> HLarva : crea
Hormiguero ..> HRastreadora : transforma
Hormiguero --> "0..1" SqliteConnection
IIA <|.. AntCiberDron
AntCiberDron --> Evaluador
AntCiberDron o-- FuenteDePoder
AntCiberDron *-- "6" Pata
AntCiberDron *-- TurboReactor
AntCiberDron o-- ModuloIdioma
Pata --> "0..1" Laser
Pata --> "0..1" Metralleta
Laser ..> FuenteDePoder
Metralleta ..> FuenteDePoder
TurboReactor ..> FuenteDePoder
ModuloIdioma ..> Entrenamiento
ModuloIdioma --> "0..1" SqliteConnection
Entrenamiento --> ExpertoParlante
Entrenamiento --> Area
ExpertoParlante --> Idioma
@enduml
```

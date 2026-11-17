# Diagrama Obligatorio 4: Modelo Entidad-Relación (MER — SQLite en Python 3.12 · PlantUML)

> **Responsable (Parte 3):** **Oscar Tamayo (`I3`)**  
> Base de datos embebida **SQLite** ubicada en `./data/antdron.db`, gestionada desde **Python 3.12** mediante el módulo estándar `sqlite3` (`src/ant/db/`), alineada con el dominio del PDF y `WORKSHOP-XP.md`.

```plantuml
@startuml
title Modelo Entidad-Relación (MER — SQLite ./data/antdron.db · Python 3.12)
hide circle
skinparam linetype ortho

entity USUARIO {
  * id : INTEGER <<PK>>
  --
  usuario : TEXT
  clave : TEXT
  cedula : TEXT
  rol : TEXT
}

entity INTENTO_LOGIN {
  * id : INTEGER <<PK>>
  --
  * usuario_id : INTEGER <<FK>>
  fecha : TEXT
  exito : INTEGER
}

entity HORMIGUERO {
  * id : INTEGER <<PK>>
  --
  nombre : TEXT
}

entity TIPO_HORMIGA {
  * id : INTEGER <<PK>>
  --
  nombre : TEXT
  alimento_requerido : TEXT
}

entity HORMIGA {
  * id : INTEGER <<PK>>
  --
  * hormiguero_id : INTEGER <<FK>>
  * tipo_id : INTEGER <<FK>>
  sexo : TEXT
  estado : TEXT
}

entity ALIMENTO {
  * id : INTEGER <<PK>>
  --
  nombre : TEXT
  tipo : TEXT
}

entity ALIMENTACION {
  * id : INTEGER <<PK>>
  --
  * hormiga_id : INTEGER <<FK>>
  * alimento_id : INTEGER <<FK>>
  fecha : TEXT
  resultado : TEXT
}

entity COORDENADA {
  * codigo : TEXT <<PK>>
  --
  lunes : TEXT
  martes : TEXT
  miercoles : TEXT
  jueves : TEXT
  viernes : TEXT
  arsenal : TEXT
}

entity DESTRUCCION {
  * id : INTEGER <<PK>>
  --
  * hormiguero_id : INTEGER <<FK>>
  * coordenada_codigo : TEXT <<FK>>
  palabra_arsenal : TEXT
  detono : INTEGER
  fecha : TEXT
}

entity ANTCIBERDRON {
  * id : INTEGER <<PK>>
  --
  * fuente_id : INTEGER <<FK>>
  nombre : TEXT
}

entity FUENTE_PODER {
  * id : INTEGER <<PK>>
  --
  nivel : INTEGER
  estado : TEXT
}

entity EXPERTO {
  * id : INTEGER <<PK>>
  --
  nombre : TEXT
  idioma : TEXT
  certificado : INTEGER
}

entity ENTRENAMIENTO_IDIOMA {
  * id : INTEGER <<PK>>
  --
  * dron_id : INTEGER <<FK>>
  * experto_id : INTEGER <<FK>>
  area : TEXT
  contenido : TEXT
  fecha : TEXT
}

USUARIO ||--o{ INTENTO_LOGIN : registra
HORMIGUERO ||--o{ HORMIGA : contiene
HORMIGA }o--|| TIPO_HORMIGA : es
HORMIGA ||--o{ ALIMENTACION : recibe
ALIMENTO ||--o{ ALIMENTACION : usado_en
HORMIGUERO ||--o{ DESTRUCCION : registra
COORDENADA ||--o{ DESTRUCCION : objetivo
ANTCIBERDRON ||--|| FUENTE_PODER : usa
ANTCIBERDRON ||--o{ ENTRENAMIENTO_IDIOMA : aprende
EXPERTO ||--o{ ENTRENAMIENTO_IDIOMA : imparte
@enduml
```

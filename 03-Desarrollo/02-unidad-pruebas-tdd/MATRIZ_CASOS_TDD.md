# 13. Unidad de Pruebas (TDD: Rojo $\rightarrow$ Verde $\rightarrow$ Reciclaje — Python 3.12)

**Responsables:** **I4 (Tester)** diseña casos base; **I2 + I3 (Programadores)** escriben cada test en **`pytest` (Python 3.12)** **antes** de la clase de producción.

| Módulo / Historia | Archivo de Test (`pytest`) | Casos de Prueba (Escritos antes del código Python) | Estado Objetivo |
| :--- | :--- | :--- | :--- |
| **Login (`HU-01`)** | `test_auth_service.py` | 1) Acceso válido para cada uno de los 4 integrantes.<br>2) Acceso válido para `patmic` / `123`.<br>3) Rechazo en intentos 1 y 2; bloqueo/cierre definitivo al 3.er fallo. | `[ ] Verde` |
| **CSV y Loading (`HU-02`)** | `test_sistema_ruso.py` | 1) `readCoord("data/Grupo06.csv")` retorna todas las filas mapeadas a `CoordenadaUK`.<br>2) Columnas de horario y `tipoArsenal` respetan `;`.<br>3) Error controlado si no existe archivo.<br>4) `Utility` genera progreso hasta `100%`. | `[ ] Verde` |
| **Hormigas y Metamorfosis (`HU-04`, `HU-05`)** | `test_hormiga.py` | 1) Toda nueva instancia nace como `HLarva` con estado `"VIVA"`.<br>2) `HLarva.comer(Nectar())` $\rightarrow$ `True` (sigue viva).<br>3) `HLarva.comer(alimento_grupo_6)` $\rightarrow$ `True` y evoluciona al tipo configurado.<br>4) `HLarva.comer(alimento_incorrecto)` $\rightarrow$ `False` y estado `"MUERTA"`. | `[ ] Verde` |
| **Autómata / IIA (`HU-03`)** | `test_bomba_automata.py` | 1) Cadena vacía `""` rechazada.<br>2) Cadenas válidas de los lenguajes de los 4 últimos dígitos retornan `True` en `dron.buscar(...)`.<br>3) Símbolos fuera de $\Sigma = \{a,b,c,d,t\}$ rechazados.<br>4) Comparación masiva contra oráculo `re.fullmatch()` con 100% coincidencia. | `[ ] Verde` |
| **Dron y Fuente (`HU-06`, `HU-07`)** | `test_ant_ciber_dron.py` | 1) `isinstance(dron, IIA)` es `True`.<br>2) Pata delantera derecha tiene `Metralleta`, izquierda tiene `Laser`, espalda tiene `TurboReactor`.<br>3) Potencia del láser aumenta al recargar o reemplazar la fuente con `IIA`.<br>4) Con energía `0`, `volar()` retorna `False` y el láser no dispara. | `[ ] Verde` |
| **Idiomas (`HU-08`)** | `test_modulo_idioma.py` | 1) Entrenar léxico, gramática y fonética con `ExpertoParlante("EN")` y `ExpertoParlante("ES")` exitoso.<br>2) Intentar entrenar sin experto (`None`) o con experto no certificado es rechazado. | `[ ] Verde` |
| **SQLite (`HU-09`)** | `test_persistencia_sqlite.py` | Guardar y consultar hormigas, historial de alimentación, coordenadas destruidas y entrenamientos en BD temporal (`sqlite3`). | `[ ] Verde` |

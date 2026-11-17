# 9. Soluciones Puntuales (Spikes Técnicos — Python 3.12)

En el diagrama XP del PDF este paso se denomina **Soluciones Puntuales** *(Spikes)*: prototipos breves en **Python 3.12**, aislados y desechables (máx. 1 día) para eliminar incertidumbre técnica antes de escribir código de producción.

---

## Spike 1: Motor del Autómata Finito $A=(Q,\Sigma,\delta,q_0,F)$ vs módulo `re`
- **Responsables:** I2 (Coach+Prog1) & I4 (Tester)
- **Pregunta técnica:** ¿Cómo garantizar que el autómata propio construido con el último dígito de las 4 cédulas evalúe cadenas de forma determinista (AFD) sin hacer trampa usando solo `re.fullmatch()`, y cómo verificarlo automáticamente?
- **Experimento:** Prototipo de tabla de transición $\delta: Q \times \Sigma \rightarrow Q$ con estado pozo (`q_error`) para símbolos fuera de $\Sigma = \{a,b,c,d,t\}$ y generador de casos positivos/negativos comparado contra un oráculo `re.fullmatch()` en pytest.
- **Conclusión:** Producción usa exclusivamente `BombaAutomata` (transiciones $\delta$ formales); el módulo `re` se usa **únicamente dentro de los tests pytest** de I4 como oráculo de validación cruzada.

---

## Spike 2: Animación de Loading `\ | / - | 100%` en Consola y Docker TTY
- **Responsables:** I3 (Prog2) & I4 (Tester)
- **Pregunta técnica:** ¿Cómo lograr que el spinner `\ | / - |` anime porcentajes hasta `100%` sobrescribiendo la misma línea antes de mostrar cada coordenada, tanto en Windows/Linux como dentro de `docker compose run`?
- **Experimento:** Prueba con retorno de carro `\r` (`sys.stdout.write(f"\r{spinner} {pct}% ")` + `sys.stdout.flush()`, o `print(..., end="", flush=True)`) dentro de `Utility` y prueba con `docker compose run --rm antdron`.
- **Conclusión:** Sin terminal interactiva el contenedor no renderiza `\r` correctamente; por ello `docker-compose.yml` obliga `stdin_open: true` y `tty: true`, y los tests automatizados permiten configurar retardo `0 ms` para no ralentizar `pytest`.

---

## Spike 3: Consola + SQLite en Entorno Local y Docker
- **Responsables:** I3 (Prog2) & I4 (Tester)
- **Pregunta técnica:** ¿Cómo correr los menús de consola y SQLite con cero errores (`-0.5` incidentes) tanto en Windows/Mac como en Linux/Docker?
- **Experimento:** Prueba del módulo `sqlite3` creando el archivo local `./data/antdron.db` montado como volumen Docker, y ejecución con `python main.py` en la imagen `python:3.12-slim`.
- **Conclusión:** Se descartan las ventanas gráficas: toda la interfaz es de consola con menús, por lo que funciona igual en Windows, Mac, Linux y Docker sin servidor gráfico.

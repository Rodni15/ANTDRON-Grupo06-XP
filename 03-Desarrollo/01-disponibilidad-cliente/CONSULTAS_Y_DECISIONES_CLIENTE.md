# 12. Disponibilidad del Cliente (Bitácora de Consultas y Decisiones)

**Cliente operativo del equipo:** **I1** · **Sponsor/Evaluador externo:** Docente (`patmic`) · **Lenguaje:** **Python 3.12**

En XP el Cliente forma parte del equipo para resolver dudas en minutos sin frenar el desarrollo en Python 3.12. Aquí quedan registradas las definiciones clave del dominio:

| # | Duda técnica / de negocio surgida | Respuesta del Cliente (I1 / `patmic`) | Impacto en Código / Criterios de Aceptación |
| :---: | :--- | :--- | :--- |
| **C-01** | La tabla del PDF define evolución solo para grupos `1-2`, `3-4` y `5`. ¿Qué hormiga evoluciona para nuestro **Grupo 6**? | Se parametriza con `EvolucionStrategy` usando **`HRastreadora` (`AHervivoro`)** por defecto; **confirmar con el docente `patmic`** antes de la entrega final y ajustar 1 línea de configuración en Python si indica otro tipo. | `EvolucionStrategy` (`abc.ABC`) desacoplada de `HLarva`; test parametrizable en `pytest`. |
| **C-02** | ¿Qué ocurre exactamente cuando una `HLarva` o una hormiga adulta ingiere un alimento distinto al suyo? | La hormiga **muere** inmediatamente (`estado = "MUERTA"`) y `comer(a)` retorna **`False`**. | Contrato `IHormiga.comer(self, a: Alimento) -> bool` validado en `pytest`. |
| **C-03** | ¿Cómo debe actuar `patmic`/`123` respecto a las credenciales de los 4 integrantes? | Tanto las **4 cédulas/usuarios del grupo** como **`patmic`/`123`** son válidos; cualquier combinación errónea cuenta hacia el máximo de **3 intentos** y al 3.er fallo cierra el sistema. | `AuthService` con contador exacto de 3 intentos y salida controlada en Python. |
| **C-04** | En el PDF, `AntCiberDron` lleva metralleta derecha, láser izquierdo y fuente de poder. ¿Cómo varía la potencia del láser? | La potencia del láser es directamente proporcional al porcentaje/nivel de la `FuenteDePoder`; con energía `0` no dispara ni vuela. | `Laser.calcularPotencia(FuenteDePoder)` + pruebas de borde en `0%` y `100%`. |
| **C-05** | ¿Quién puede entrenar inglés y español al dron? | **Exclusivamente** objetos/actores `ExpertoParlante` certificados en `EN` o `ES` para léxico, gramática y fonética. Cualquier otra entrada se rechaza. | `ModuloIdioma.entrenar(...)` lanza excepción/retorna `False` si `experto is None` o no certificado. |

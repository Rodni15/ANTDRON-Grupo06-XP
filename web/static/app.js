document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[data-carga]").forEach((formulario) => {
    formulario.addEventListener("submit", () => {
      const boton = formulario.querySelector("button[type='submit']");
      if (boton) {
        boton.disabled = true;
        boton.dataset.texto = boton.textContent;
        boton.textContent = "Procesando...";
      }
    });
  });

  document.querySelectorAll("nav a").forEach((enlace) => {
    enlace.addEventListener("click", () => {
      document.querySelectorAll("nav a").forEach((item) => item.classList.remove("activo"));
      enlace.classList.add("activo");
    });
  });

  document.querySelectorAll("[data-validacion]").forEach((formulario) => {
    formulario.addEventListener("submit", (evento) => {
      if (!formulario.checkValidity()) {
        evento.preventDefault();
        formulario.reportValidity();
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", async () => {
  const cuerpo = document.querySelector('tbody[data-animar="si"]');
  if (!cuerpo) return;
  const filas = [...cuerpo.querySelectorAll("[data-coordenada]")];
  filas.forEach(fila => { fila.hidden = true; });
  for (const fila of filas) {
    fila.hidden = false;
    const celda = fila.querySelector("[data-loading]");
    for (const [simbolo, porcentaje] of [["|", 25], ["/", 50], ["-", 75], ["|", 100]]) {
      celda.textContent = simbolo + " " + porcentaje + "%";
      await new Promise(resolve => setTimeout(resolve, 35));
    }
    celda.textContent = "100%";
  }
});

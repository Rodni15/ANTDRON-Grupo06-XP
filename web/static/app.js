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

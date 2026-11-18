"""Login interactivo con máximo 3 intentos."""
from getpass import getpass
import sys

MAX_INTENTOS = 3


class AuthService:
    def __init__(self, sistema, entrada=input, entradaClave=None):
        self.sistema = sistema
        self.entrada = entrada
        self.entradaClave = entradaClave or (getpass if sys.stdin.isatty() else input)

    def autenticar(self) -> bool:
        print("=== AUTENTICACIÓN KGD ===")
        for intento in range(1, MAX_INTENTOS + 1):
            try:
                usuario = self.entrada("Usuario: ")
                clave = self.entradaClave("Contraseña: ")
            except (EOFError, KeyboardInterrupt):
                print("\nAutenticación cancelada.")
                return False
            if self.sistema.login(usuario, clave):
                print(f"Bienvenido, {usuario.strip()}.")
                return True
            restantes = MAX_INTENTOS - intento
            if restantes:
                print(f"Credenciales incorrectas. Intentos restantes: {restantes}")
        print("Acceso bloqueado: se superó el máximo de 3 intentos.")
        return False

from datetime import datetime

class Usuario:
    def __init__(self, id_usuario, nombre, email, contrasena):
        # Atributos
        self.id_usuario = id_usuario  # int (PK)
        self.nombre = nombre          # string
        self.email = email            # string
        self.contrasena = contrasena  # string
        
    # Métodos del Diagrama UML
    def login(self, contrasena_ingresada):
        """Simula el inicio de sesión."""
        if contrasena_ingresada == self.contrasena:
            return f"Usuario {self.nombre} ha iniciado sesión con éxito."
        else:
            return "Contraseña incorrecta."

    def actualizarPerfil(self, nuevo_nombre=None, nuevo_email=None):
        """Actualiza el nombre y/o email del usuario."""
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_email:
            self.email = nuevo_email
        return f"Perfil de {self.nombre} actualizado."
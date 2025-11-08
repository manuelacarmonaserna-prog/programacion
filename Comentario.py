from datetime import datetime 

class Comentario:
    def __init__(self, id_comentario, texto, usuario_id, tarea_id):
        # Atributos (Según tu Diagrama UML)
        self.id_comentario = id_comentario  # int (PK)
        self.texto = texto                # string
        self.usuario_id = usuario_id        # int (FK a Usuario)
        self.tarea_id = tarea_id            # int (FK a Tarea)
        self.fecha_creacion = datetime.now() # datetime (Ahora sí puede usar datetime)

    # Métodos del Diagrama UML
    def crearComentario(self):
        """Simula la acción de guardar el comentario."""
        return f"Comentario ID {self.id_comentario} creado por Usuario {self.usuario_id} en Tarea {self.tarea_id}."
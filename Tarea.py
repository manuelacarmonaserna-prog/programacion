from datetime import datetime

class Tarea:
    ESTADOS_VALIDOS = ["Pendiente", "En Progreso", "Revisión", "Terminado"]

    def __init__(self, id_tarea, titulo, descripcion, fecha_limite, proyecto_id, asignado_a_id):
        # Atributos
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = self.ESTADOS_VALIDOS[0]  # Estado inicial
        self.fecha_limite = fecha_limite
        self.proyecto_id = proyecto_id          # FK a Proyecto
        self.asignado_a_id = asignado_a_id      # FK a Usuario
        self.fecha_creacion = datetime.now() 

    # Métodos del Diagrama UML
    def cambiarEstado(self, nuevo_estado):
        """Implementa la acción de mover la tarjeta en el Kanban."""
        if nuevo_estado in self.ESTADOS_VALIDOS:
            self.estado = nuevo_estado
            return f"Estado de la tarea '{self.titulo}' actualizado a: {self.estado}"
        else:
            return f"Error: El estado '{nuevo_estado}' no es válido."
            
    def asignarMiembro(self, nuevo_miembro_id):
        """Cambia el ID del usuario responsable de la tarea."""
        self.asignado_a_id = nuevo_miembro_id
        return f"Tarea '{self.titulo}' reasignada al miembro ID: {nuevo_miembro_id}"
        
    def editarTarea(self, nuevo_titulo=None, nueva_descripcion=None):
        """Permite modificar el contenido de la tarea."""
        if nuevo_titulo:
            self.titulo = nuevo_titulo
        if nueva_descripcion:
            self.descripcion = nueva_descripcion
        return f"Tarea '{self.titulo}' modificada con éxito."
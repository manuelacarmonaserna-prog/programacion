from datetime import datetime
from Tarea import Tarea # Importación crucial

class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, creador_id, fecha_limite):
        # Atributos
        self.id_proyecto = id_proyecto      # int (PK)
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now() 
        self.fecha_limite = fecha_limite
        self.creador_id = creador_id        # int (FK a Usuario)
        self.tareas = []                    # Lista para almacenar objetos Tarea

    # Métodos del Diagrama UML
    def crearTarea(self, id_tarea, titulo, descripcion, fecha_limite, asignado_a_id):
        """Crea un objeto Tarea y lo añade a la lista del proyecto."""
        
        nueva_tarea = Tarea(
            id_tarea, 
            titulo, 
            descripcion, 
            fecha_limite, 
            self.id_proyecto, # Se pasa el ID de este proyecto
            asignado_a_id
        )
        self.tareas.append(nueva_tarea)
        return f"Tarea '{titulo}' creada y añadida al proyecto '{self.nombre}'."

    def obtenerTareas(self):
        """Devuelve una lista con los títulos de todas las tareas del proyecto."""
        if not self.tareas:
            return []
        
        return [tarea.titulo for tarea in self.tareas]

    def cerrarProyecto(self):
        """Simula el cierre del proyecto."""
        return f"El proyecto '{self.nombre}' ha sido marcado como CERRADO."
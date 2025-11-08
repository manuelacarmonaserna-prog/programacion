from datetime import datetime
from Usuario import Usuario     
from Proyecto import Proyecto   
from Tarea import Tarea         
from Comentario import Comentario # Importación final

# --- DATOS DE PRUEBA ---
fecha_limite_proyecto = datetime(2025, 12, 31) 
fecha_limite_tarea = datetime(2025, 11, 20) 

# 1. CREACIÓN DE INSTANCIAS CLAVE
print("\n--- 1. CREACIÓN DE INSTANCIAS ---")

# Crear Usuario
usuario1 = Usuario(1, "Manuela Garcia", "manuela@app.com", "clave123")
print(f"Usuario Creado: ID {usuario1.id_usuario} ({usuario1.nombre})")

# Crear Proyecto (Creador_id = 1, el ID de Manuela)
proyecto_web = Proyecto(
    id_proyecto=101,
    nombre="Diseño Web Landing Page",
    descripcion="Página principal de marketing.",
    creador_id=usuario1.id_usuario, # Atributo, NO lleva paréntesis
    fecha_limite=fecha_limite_proyecto
)
print(f"Proyecto Creado: ID {proyecto_web.id_proyecto} ({proyecto_web.nombre})")


# 2. PROBAR RELACIÓN Y MÉTODOS
print("\n--- 2. PRUEBA DE RELACIONES Y MÉTODOS ---")

# Usar el método crearTarea() del Proyecto
resultado_creacion_tarea = proyecto_web.crearTarea(
    id_tarea=501,
    titulo="Wireframes de la Home",
    descripcion="Definir estructura y secciones.",
    fecha_limite=fecha_limite_tarea,
    asignado_a_id=usuario1.id_usuario
)
print(resultado_creacion_tarea)

# Crear Comentario
comentario1 = Comentario(
    id_comentario=1,
    texto="Revisar tipografía.",
    usuario_id=usuario1.id_usuario,
    tarea_id=501
)
print(comentario1.crearComentario())


# 3. PROBAR MÉTODOS DE LA TAREA Y KANBAN
print("\n--- 3. PRUEBA DE KANBAN ---")

# Acceder a la tarea creada 
tarea_actual = proyecto_web.tareas[0] 

print(f"Estado Inicial: {tarea_actual.estado}")

# Cambiar estado (Método del Diagrama)
resultado_cambio = tarea_actual.cambiarEstado("En Progreso")
print(resultado_cambio)

# Otro cambio de estado
resultado_final = tarea_actual.cambiarEstado("Revisión")
print(resultado_final)


# 4. PRUEBA FINAL
print("\n--- 4. ESTADO FINAL ---")
print(f"Tareas del Proyecto: {proyecto_web.obtenerTareas()}")
print(f"Estado Final de la Tarea: {tarea_actual.estado}")
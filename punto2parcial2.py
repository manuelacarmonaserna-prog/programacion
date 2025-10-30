# ------------------------------------------------
# Definición de la Clase base (Superclase)
# ------------------------------------------------
class Persona:
    """
    Representa una persona con información básica.
    """
    # Atributos definidos en el diagrama:
    # + nombre: Nombre (representado como str)
    # + nif: Nif (representado como str)
    # + fechaNac: Fecha (representado como str o date)
    
    def __init__(self, nombre: str, nif: str, fechaNac: str):
        self.nombre = nombre
        self.nif = nif
        self.fechaNac = fechaNac

    def __str__(self):
        return f"Persona(Nombre: {self.nombre}, NIF: {self.nif}, Fecha Nac.: {self.fechaNac})"

# ------------------------------------------------
# Definición de la Clase Hija (Subclase)
# ------------------------------------------------
# Jugador hereda de Persona, por eso se pasa 'Persona' entre paréntesis
class Jugador(Persona):
    """
    Representa un jugador. Hereda todos los atributos de Persona.
    """
    # Atributo específico de Jugador:
    # + numFed: integer (representado como int)

    def __init__(self, nombre: str, nif: str, fechaNac: str, numFed: int):
        # 1. Llamar al constructor de la clase padre (Persona)
        # para inicializar los atributos heredados.
        super().__init__(nombre, nif, fechaNac)
        
        # 2. Inicializar el atributo propio de Jugador
        self.numFed = numFed

    def __str__(self):
        # Combina la representación de la clase padre con su propio atributo
        return f"Jugador(Nombre: {self.nombre}, NIF: {self.nif}, Num Fed.: {self.numFed})"

# ------------------------------------------------
# Ejemplo de Uso y Verificación
# ------------------------------------------------
print("--- Creando instancias ---")

# Crear un objeto Persona
p1 = Persona("Ana López", "12345678A", "01/01/1980")
print(p1)

# Crear un objeto Jugador. Notar que necesita los 4 parámetros:
# nombre, nif, fechaNac (de Persona) y numFed (propio)
j1 = Jugador("Carlos Pérez", "98765432B", "15/05/2000", 45678)
print(j1)

print("\n--- Verificación de Herencia ---")
# El objeto Jugador tiene los atributos del padre
print(f"Nombre del jugador: {j1.nombre}")
# El objeto Jugador tiene sus propios atributos
print(f"Número de federado: {j1.numFed}")

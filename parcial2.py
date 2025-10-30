def invertir_array(arr):
    """
    Función que recibe un array y retorna una nueva lista con los elementos invertidos.
    """
   
    return arr[::-1] # Retorna una copia invertida

def main():
    # 1. Solicitar la cantidad de elementos del array
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de elementos del array: "))
            if cantidad >= 0:
                break
            else:
                print("La cantidad debe ser un número positivo o cero.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")

    # 2. Solicitar por pantalla el valor de cada uno de los elementos
    array_original = []
    print(f"\n--- Ingrese los {cantidad} elementos ---")
    for i in range(cantidad):
        # Solicitamos el valor como string, como lo pide el ejercicio
        elemento = input(f"Elemento {i + 1}: ")
        array_original.append(elemento)

    # 3. Crear una función que reciba el array y retorne el array invertido (Llamada a la función)
    array_invertido = invertir_array(array_original)

    # 4. Mostrar en pantalla el array original y el invertido
    print("\n--- Resultados ---")
    print(f"Array Original: {array_original}")
    print(f"Array Invertido: {array_invertido}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
# Implementación del algoritmo Mergesort
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    
    # Combinar y ordenar las mitades
    return merge(izquierda, derecha)

# Función para combinar y ordenar dos listas
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    # Comparar elementos y agregar el menor a la lista resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar elementos restantes (si los hay)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# Programa principal
def main():
    # Solicitar la lista al usuario
    try:
        entrada = input("Ingrese los números separados por espacios: ")
        lista = [int(x) for x in entrada.split()]
        
        print("\nLista original:")
        print(lista)

        # Ordenar la lista con Mergesort
        lista_ordenada = mergesort(lista)
        print("\nLista ordenada:")
        print(lista_ordenada)
    
    except ValueError:
        print("Por favor, ingrese solo números enteros separados por espacios.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

# Método de ordenamiento por Burbuja (Bubble Sort)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Método de ordenamiento por Selección (Selection Sort)
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Método de ordenamiento por Inserción (Insertion Sort)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Método de ordenamiento rápido (Quick Sort)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivot]
    iguales = [x for x in lista if x == pivot]
    mayores = [x for x in lista if x > pivot]
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Método de ordenamiento por mezcla (Merge Sort)
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = merge_sort(lista[:mid])
    derecha = merge_sort(lista[mid:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Función principal para elegir el método de ordenamiento
def ordenar_lista():
    lista = list(map(int, input("Ingresa los números separados por espacios: ").split()))
    print("\nMétodos de ordenamiento:")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Quick Sort")
    print("5. Merge Sort")
    opcion = int(input("Elige un método (1-5): "))

    if opcion == 1:
        print("Lista ordenada con Burbuja:", bubble_sort(lista))
    elif opcion == 2:
        print("Lista ordenada con Selección:", selection_sort(lista))
    elif opcion == 3:
        print("Lista ordenada con Inserción:", insertion_sort(lista))
    elif opcion == 4:
        print("Lista ordenada con Quick Sort:", quick_sort(lista))
    elif opcion == 5:
        print("Lista ordenada con Merge Sort:", merge_sort(lista))
    else:
        print("Opción no válida.")

# Ejecutar el programa
ordenar_lista()

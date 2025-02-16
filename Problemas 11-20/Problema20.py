def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna la posición donde encontró el elemento
    return -1  # Retorna -1 si el elemento no está en la lista

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el punto medio

        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
objetivo = int(input("Ingrese el número a buscar: "))

# Prueba de Búsqueda Lineal
indice_lineal = busqueda_lineal(lista, objetivo)
print(f"Búsqueda Lineal: {'Encontrado en posición ' + str(indice_lineal) if indice_lineal != -1 else 'No encontrado'}")

# Ordenamos la lista para la Búsqueda Binaria
lista.sort()
indice_binaria = busqueda_binaria(lista, objetivo)
print(f"Búsqueda Binaria: {'Encontrado en posición ' + str(indice_binaria) if indice_binaria != -1 else 'No encontrado'}")

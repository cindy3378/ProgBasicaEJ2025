import random

def generar_lista(cantidad, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def main():
    cantidad = int(input("Ingrese la cantidad de números a generar: "))
    minimo = int(input("Ingrese el valor mínimo: "))
    maximo = int(input("Ingrese el valor máximo: "))
    
    lista = generar_lista(cantidad, minimo, maximo)
    print("\nLista generada:", lista)

    lista_ordenada = quicksort(lista)
    print("\nLista ordenada con Quicksort:", lista_ordenada)

    objetivo = int(input("\nIngrese un número para buscar en la lista: "))
    resultado = busqueda_binaria(lista_ordenada, objetivo)

    if resultado != -1:
        print(f"El número {objetivo} fue encontrado en la posición {resultado}.")
    else:
        print(f"El número {objetivo} no se encuentra en la lista.")

if __name__ == "__main__":
    main()

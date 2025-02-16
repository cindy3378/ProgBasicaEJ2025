pila = list()

def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila

def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila

if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila,1)
    print(estupila)
    insertarPila(estupila,"mi pelo")
    print(estupila)
    insertarPila(estupila,"ideota")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)

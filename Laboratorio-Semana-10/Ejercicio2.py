productos = []

def agregar_producto(nombre, categoria, precio, cantidad):
    producto = {
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

def eliminar_producto(nombre):
    global productos
    productos = [producto for producto in productos if producto['nombre'].lower() != nombre.lower()]
    print(f"Producto '{nombre}' eliminado exitosamente." if any(producto['nombre'].lower() == nombre.lower() for producto in productos) else f"Producto '{nombre}' no encontrado.")

def buscar_producto(nombre):
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print("Producto encontrado:")
            print(producto)
            return
    print(f"Producto '{nombre}' no encontrado.")

def mostrar_productos_ordenados():
    if productos:
        productos_ordenados = sorted(productos, key=lambda x: x['precio'])
        print("Productos ordenados por precio (de menor a mayor):")
        for producto in productos_ordenados:
            print(producto)
    else:
        print("No hay productos en el inventario.")

def menu():
    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Buscar Producto")
        print("4. Mostrar Productos Ordenados por Precio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(nombre, categoria, precio, cantidad)
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(nombre)
        elif opcion == '4':
            mostrar_productos_ordenados()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

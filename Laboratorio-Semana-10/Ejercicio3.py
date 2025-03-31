contactos = []

def agregar_contacto(nombre, numero, correo):
    contacto = (nombre, numero, correo)
    contactos.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")

def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto[0].lower() == nombre.lower():
            print("Contacto encontrado:")
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            return
    print(f"Contacto '{nombre}' no encontrado.")

def listar_contactos_ordenados():
    if contactos:
        contactos_ordenados = sorted(contactos, key=lambda x: x[0].lower())
        print("Contactos en orden alfabético:")
        for contacto in contactos_ordenados:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
    else:
        print("No hay contactos en la agenda.")

def menu():
    while True:
        print("\n1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Listar Contactos en Orden Alfabético")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            numero = input("Número: ")
            correo = input("Correo: ")
            agregar_contacto(nombre, numero, correo)
        elif opcion == '2':
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '3':
            listar_contactos_ordenados()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

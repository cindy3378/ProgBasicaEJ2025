# vehiculo.py
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, num_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.num_puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")


# programa_principal.py
from vehiculo import Automovil, Motocicleta

def menu():
    vehiculos = []
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar Automóvil")
        print("2. Agregar Motocicleta")
        print("3. Mostrar Información de Vehículos")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            precio = float(input("Precio: "))
            num_puertas = int(input("Número de puertas: "))
            vehiculo = Automovil(marca, modelo, anio, precio, num_puertas)
            vehiculos.append(vehiculo)
        elif opcion == '2':
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            precio = float(input("Precio: "))
            cilindrada = int(input("Cilindrada (cc): "))
            vehiculo = Motocicleta(marca, modelo, anio, precio, cilindrada)
            vehiculos.append(vehiculo)
        elif opcion == '3':
            if vehiculos:
                print("\nInformación de Vehículos:")
                for v in vehiculos:
                    v.mostrar_informacion()
                    print("-")
            else:
                print("No hay vehículos registrados.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

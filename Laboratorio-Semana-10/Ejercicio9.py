# Implementación del programa utilizando múltiples paradigmas
import random

# 1. Paradigma Estructurado y Modular: Funciones para operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b


# 2. Paradigma Orientado a Objetos: Clases para Vehículos
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        # Muestra la información básica del vehículo
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def mostrar_info(self):
        # Muestra la información extendida del automóvil
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")


# 3. Paradigma Imperativo: Funciones para la interfaz de usuario y control del flujo
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Operaciones Matemáticas")
    print("2. Información de Vehículos")
    print("3. Salir")

def obtener_numero(mensaje):
    # Solicita un número al usuario
    return float(input(mensaje))

def realizar_operacion(opcion):
    if opcion in ['1', '2', '3', '4']:
        a = obtener_numero("Ingrese el primer número: ")
        b = obtener_numero("Ingrese el segundo número: ")
        
        if opcion == '1':
            print("Resultado:", suma(a, b))
        elif opcion == '2':
            print("Resultado:", resta(a, b))
        elif opcion == '3':
            print("Resultado:", multiplicacion(a, b))
        elif opcion == '4':
            print("Resultado:", division(a, b))
    else:
        print("Opción no válida.")


# 4. Programación Principal: Control de flujo y ejecución del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su elección: ")

        if opcion == '1':
            # Operaciones matemáticas
            print("\nMenú de Operaciones Matemáticas:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            op = input("Seleccione una operación: ")
            realizar_operacion(op)

        elif opcion == '2':
            # Crear y mostrar información de un automóvil
            print("\nCreando un automóvil...")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            anio = int(input("Ingrese el año del vehículo: "))
            puertas = int(input("Ingrese el número de puertas: "))

            auto = Automovil(marca, modelo, anio, puertas)
            print("\nInformación del automóvil:")
            auto.mostrar_info()

        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

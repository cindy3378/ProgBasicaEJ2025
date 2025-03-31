# conversor.py
def kilometros_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172


# programa_principal.py
import conversor

def menu():
    while True:
        print("\nSeleccione una conversión:")
        print("1. Kilómetros a Millas")
        print("2. Celsius a Fahrenheit")
        print("3. Litros a Galones")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            km = float(input("Ingrese la distancia en kilómetros: "))
            print(f"{km} kilómetros son {conversor.kilometros_a_millas(km)} millas.")
        elif opcion == '2':
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{celsius}°C son {conversor.celsius_a_fahrenheit(celsius)}°F.")
        elif opcion == '3':
            litros = float(input("Ingrese el volumen en litros: "))
            print(f"{litros} litros son {conversor.litros_a_galones(litros)} galones.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

import math

def calcular_estadisticas(*args):
    if not args:
        return "No se proporcionaron números."

    numeros = sorted(args)
    n = len(numeros)

    # Calcular el promedio usando lambda
    promedio = (lambda nums: sum(nums) / len(nums))(numeros)

    # Calcular la mediana
    if n % 2 == 0:
        mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
    else:
        mediana = numeros[n//2]

    # Calcular la desviación estándar
    varianza = sum((x - promedio) ** 2 for x in numeros) / n
    desviacion_estandar = math.sqrt(varianza)

    return promedio, mediana, desviacion_estandar

def menu():
    while True:
        print("\n1. Calcular Estadísticas")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
                promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)
                print(f"Promedio: {promedio}")
                print(f"Mediana: {mediana}")
                print(f"Desviación Estándar: {desviacion_estandar}")
            except ValueError:
                print("Por favor, ingrese solo números válidos.")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

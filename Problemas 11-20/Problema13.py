# Pedir datos al usuario
valor = float(input("Ingresa la temperatura: "))
origen = input("Ingresa la escala de origen (C, F, K): ").upper()
destino = input("Ingresa la escala de destino (C, F, K): ").upper()

# Convertir temperaturas
def convertir_temperatura(valor, origen, destino):
    if origen == "C":  # Celsius a otras escalas
        if destino == "F":
            return (valor * 9/5) + 32  # Celsius a Fahrenheit
        elif destino == "K":
            return valor + 273.15  # Celsius a Kelvin

    elif origen == "F":  # Fahrenheit a otras escalas
        if destino == "C":
            return (valor - 32) * 5/9  # Fahrenheit a Celsius
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15  # Fahrenheit a Kelvin

    elif origen == "K":  # Kelvin a otras escalas
        if destino == "C":
            return valor - 273.15  # Kelvin a Celsius
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32  # Kelvin a Fahrenheit

    return None  # Si no se reconoce la conversión

# Realizar conversión
resultado = convertir_temperatura(valor, origen, destino)

# Mostrar resultado
if resultado is not None:
    print(f"La temperatura convertida es: {resultado:.2f}°{destino}")
else:
    print("Conversión no válida")

# 8. Calcular el área y la circunferencia de un círculo.

radio = float(input("Ingresa el radio del círculo: "))
pi = 3.141592653589793
area = pi * radio ** 2
circunferencia = 2 * pi * radio

print(f"Área del círculo: {area}")
print(f"Circunferencia del círculo: {circunferencia}")
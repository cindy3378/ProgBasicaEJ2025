# 7. Determinar si un número es par, impar o múltiplo de otro.

numero = int(input("Ingresa un número: "))
otro = int(input("Ingresa otro número para verificar si es múltiplo: "))
par = numero % 2 == 0
impar = not par
multiplo = numero % otro == 0

print(f"El número {numero} es par: {par}")
print(f"El número {numero} es impar: {impar}")
print(f"El número {numero} es múltiplo de {otro}: {multiplo}")
# 2. Crear una calculadora simple que realice operaciones básicas.

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "Error"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
# 3. Calcular el factorial de un número dado.

n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)
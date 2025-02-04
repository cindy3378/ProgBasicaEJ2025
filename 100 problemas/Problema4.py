# 4. Generar la secuencia de Fibonacci hasta un número dado de términos.

limite = int(input("Ingresa el número de términos de Fibonacci: "))
fibonacci = [0, 1]  #La serie de Fibonacci comienza siempre con 0 y 1.
for _ in range(limite - 2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"Secuencia de Fibonacci ({limite} términos): {fibonacci}")
# 5. Verificar si un número es primo.

num = int(input("Ingresa un número para verificar si es primo: "))
es_primo = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

print(f"¿El número {num} es primo?: {es_primo}")
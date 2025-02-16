import random

def generar_numeros_aleatorios(n):
    print(f"\nGenerando {n} números aleatorios con diferentes distribuciones:\n")

    print("Distribución Uniforme [0,1]:", [random.random() for _ in range(n)])
    print("Distribución Uniforme [10, 50]:", [random.uniform(10, 50) for _ in range(n)])
    print("Distribución Triangular [10, 50, 30]:", [random.triangular(10, 50, 30) for _ in range(n)])
    print("Distribución Beta (2, 5):", [random.betavariate(2, 5) for _ in range(n)])
    print("Distribución Exponencial (λ=1):", [random.expovariate(1) for _ in range(n)])
    print("Distribución Gamma (α=2, β=2):", [random.gammavariate(2, 2) for _ in range(n)])
    print("Distribución Gaussiana (μ=0, σ=1):", [random.gauss(0, 1) for _ in range(n)])
    print("Distribución Log-normal (μ=0, σ=1):", [random.lognormvariate(0, 1) for _ in range(n)])
    print("Distribución Normal (μ=0, σ=1):", [random.normalvariate(0, 1) for _ in range(n)])
    print("Distribución Pareto (α=2):", [random.paretovariate(2) for _ in range(n)])
    print("Distribución Weibull (α=1, β=1.5):", [random.weibullvariate(1, 1.5) for _ in range(n)])

# Pedir al usuario la cantidad de números a generar
n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
generar_numeros_aleatorios(n)

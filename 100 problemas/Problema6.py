# 6. Calcular el interés compuesto dado un capital, tasa y tiempo.

capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés: "))
tiempo = int(input("Ingresa el tiempo en años: "))
interes_compuesto = capital * (1 + tasa / 100) ** tiempo   #Aplicar la fórmula del interés compuesto.

print(f"El interés compuesto después de {tiempo} años es: {interes_compuesto}")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

def ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        # Dos soluciones reales
        x1 = (-b + (discriminante ** 0.5)) / (2 * a)
        x2 = (-b - (discriminante ** 0.5)) / (2 * a)
        return f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
    
    elif discriminante == 0:
        # Una única solución real
        x = -b / (2 * a)
        return f"Una única solución real: x = {x}"
    
    else:
        # Soluciones complejas (se usa la fórmula con números imaginarios)
        parte_real = -b / (2 * a)
        parte_imaginaria = ((-discriminante) ** 0.5) / (2 * a)
        return f"Soluciones complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

# Verificar que 'a' no sea cero (para evitar división por 0)
if a == 0:
    print("No es una ecuación cuadrática (a ≠ 0).")
else:
    resultado = ecuacion_cuadratica(a, b, c)
    print(resultado)

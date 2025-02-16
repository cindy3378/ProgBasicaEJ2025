cadena = input("Ingresa una cadena: ")

# Función para contar vocales y consonantes en una cadena
def contar_vocales_consonantes(cadena):
    cadena = cadena.lower()
    
    vocales = "aeiou"
    
    num_vocales = 0
    num_consonantes = 0
    
    for letra in cadena:
        if letra.isalpha():  # Verificar que sea una letra
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
    
    return num_vocales, num_consonantes

# Obtener el número de vocales y consonantes
vocales, consonantes = contar_vocales_consonantes(cadena)

# Mostrar el resultado
print(f"La cadena tiene {vocales} vocales y {consonantes} consonantes.")

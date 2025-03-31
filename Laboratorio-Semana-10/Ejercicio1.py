# Solicitar texto al usuario
txt = input("Ingrese un texto: ")
analizar_texto(txt)


def analizar_texto(texto):
    palabras = texto.lower().split()          #Convertir el texto a minúsculas y dividir el texto en una lista de palabras
    total_palabras = len(palabras)            #Contar el número total de palabras
    palabras_unicas = set(palabras)           #Encontrar la cantidad de palabras únicas usando un conjunto
    
    #Contar la frecuencia de cada palabra usando un diccionario
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1 
    
    #Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    max_frecuencia = frecuencia_palabras[palabra_mas_frecuente]
    
    print(f"Número total de palabras: {total_palabras}")
    print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' con {max_frecuencia} apariciones.")


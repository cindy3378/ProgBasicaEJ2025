#Pedir al usuario una cadena
cadena = input("Ingresa una palabra o frase: ")

#Convertir la cadena a minúsculas y eliminar espacios
cadenamin = cadena.replace(" ", "").lower()

#Verificar si es igual a su reverso
if cadenamin == cadenamin[::-1]:
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')

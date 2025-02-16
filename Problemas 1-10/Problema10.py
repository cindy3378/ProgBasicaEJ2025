# 10. Leer, escribir y modificar un archivo de texto.

contenido_original = input("Escribe el contenido inicial del archivo: ")
with open("archivo.txt", "w") as archivo:                #Usa la función open para abrir un archivo llamado archivo.txt en modo escritura ("w").
    archivo.write(contenido_original + "\n")             #La función write() escribe el texto almacenado en contenido_original en el archivo, añadiendo un salto de línea (\n) al final.

with open("archivo.txt", "r") as archivo:                #Usa la función open para abrir el archivo en modo lectura ("r").
    contenido_leido = archivo.read()                     #La función read() lee todo el contenido del archivo y lo guarda en la variable contenido_leido.
print("\nContenido original del archivo:\n", contenido_leido)     #Se imprime el contenido que se acaba de leer.

contenido_extra = input("Escribe el contenido adicional que quieres agregar: ")
with open("archivo.txt", "a") as archivo:                #Abre el archivo en modo añadir  ("a").
    archivo.write(contenido_extra + "\n")

with open("archivo.txt", "r") as archivo:                #Vuelve a abrir el archivo en modo lectura ("r") para leer su contenido modificado.
    contenido_modificado = archivo.read()
print("\nContenido modificado del archivo:\n", contenido_modificado)   #Imprime el contenido modificado del archivo.
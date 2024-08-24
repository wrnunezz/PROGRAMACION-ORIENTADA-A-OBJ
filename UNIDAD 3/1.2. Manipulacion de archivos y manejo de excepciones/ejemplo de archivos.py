# Abre el archivo en modo lectura y lo cierra después de imprimir su contenido.
"""
archivo = open('ejemplo_lectura.txt', 'r')
print(archivo.read())  # Imprime el contenido del archivo
archivo.close()  # Cierra el archivo
"""

# Abre el archivo en modo escritura (creándolo si no existe), escribe en él y luego lo cierra.
archivo = open('ejemplo_escritura.txt', 'w')
archivo.write('Este es un nuevo archivo.')
archivo.write('Añado hoy clase encuentro 24/08/2024')# Escribe en el archivo
archivo.close()  # Cierra el archivo

# Abre el archivo en modo añadir, añade una nueva línea y luego lo cierra.
archivo = open('ejemplo_escritura.txt', 'a')
archivo.write('\nAñadiendo una segunda línea.')
archivo.write('\nEstamos en Tutoria del 22/28/2024 18:39') # Añade nueva línea de texto al archivo
archivo.close()
# Cierra el archivo

# Abre el archivo en modo lectura y lo cierra después de imprimir su contenido.
archivo = open('ejemplo_escritura.txt', 'r')
print(archivo.read())  # Imprime el contenido del archivo
archivo.close()  # Cierra el archivo



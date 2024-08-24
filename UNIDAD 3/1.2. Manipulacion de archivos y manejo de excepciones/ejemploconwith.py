"""# Usando 'with' para abrir el archivo en modo lectura.
with open('ejemplo_lectura.txt', 'r') as archivo:
    print(archivo.read())  # Imprime el contenido del archivo

# Usando 'with' para abrir el archivo en modo escritura (creándolo si no existe).
# Escribe en él y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'w') as archivo:
    archivo.write('Este es un nuevo archivo.')  # Escribe en el archivo

# Usando 'with' para abrir el archivo en modo añadir.
# Añade una nueva línea y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'a') as archivo:
    archivo.write('\nAñadiendo una segunda línea.')  # Añade nueva línea de texto
    archivo.write('\nhola chicos estamos en tutoria.')
# Usando 'with' para abrir el archivo en modo lectura.
with open('ejemplo_escritura.txt', 'r') as archivo:
    print(archivo.read())  # Imprime el contenido del archivo
"""

import csv
# Escribiendo en el archivo CSV
with open('ejemplo_escritura.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['Texto'])  # Escribiendo encabezado (opcional)
    escritor.writerow(['Este es un nuevo archivo.'])  # Escribe en el archivo

# Añadiendo nuevas líneas al archivo CSV
with open('ejemplo_escritura.csv', 'a', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['Añadiendo una segunda línea.'])  # Añade nueva línea de texto
    escritor.writerow(['hola chicos estamos en encunetro.'])  # Añade otra línea de texto

# Leyendo el contenido del archivo CSV
with open('ejemplo_escritura.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila[0])  # Imprime el contenido del archivo

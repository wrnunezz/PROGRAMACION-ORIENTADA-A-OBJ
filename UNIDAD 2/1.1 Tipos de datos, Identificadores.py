# calcular el area de un rectangulo
"""

"""

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# variables
base_rectangulo = 5
altura_rectangulo = 4.8

# llamado
area_rectangulo= calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

#print(area_rectangulo)

if isinstance(base_rectangulo, int) and isinstance(altura_rectangulo, float):
    print("el area es : ",area_rectangulo)
else:
    print("los tipos de datos no son corerrectos ")











#Ejemplo de Constructores y destructores

class Libro:
    def __init__(self, titulo, autor, numerohojas):
        self.titulo = titulo
        self.autor = autor
        self.numerohojas = numerohojas
        print(f"constructor '{self.titulo}' ")
    def __del__(self):
        print("Se destruye ")
# instanciar
mi_libro = Libro("Cien años de soledad ","Don Quijote ",450)

del mi_libro





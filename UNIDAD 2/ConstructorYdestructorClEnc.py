# ejemplo de contructor y destr...

class Mensaje:
    def __init__(self,texto):
        self.texto = texto
        print(f"Este es el contructor de: {self.texto}")

    def __del__(self):
        print("Se destruye ")
# crear una inst...
mi_texto = Mensaje("HOLA EST POO")

del mi_texto



#constructores y destructores

class Mensaje:
    def __init__(self,texto,imagen):
        self.texto = texto
        self.imagen = imagen
        print(f"Esta construyendo : {self.texto}")

    def __del__(self):

        print("Destruyendo ")
# inst
mi_mensaje = Mensaje("Hola..!!!","imgen")

del mi_mensaje
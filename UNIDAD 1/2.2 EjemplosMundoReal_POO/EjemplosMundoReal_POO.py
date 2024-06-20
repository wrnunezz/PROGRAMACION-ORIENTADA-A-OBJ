#Almacen Pedidos

class Pedidos:
    def __init__(self,identificador,cantidad):
        self.identificador = identificador
        self.cantidad=cantidad

    def agregar(self,cantidad):
        self.cantidad += cantidad

    def eliminar(self,cantidad):
        self.cantidad -= cantidad

#intanciar cada objeto
pedido=Pedidos("Juan",0)
pedido.agregar(20)
print(pedido.cantidad)

pedido.eliminar(2)
print(pedido.cantidad)


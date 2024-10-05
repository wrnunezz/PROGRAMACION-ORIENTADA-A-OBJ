# clase Producto
class Producto:
    def __init__(self,id, nombre,cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'{self.id} {self.nombre} {self.cantidad} {self.precio}'

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print('Producto agregado exitosamente')

    def eliminar_producto(self, id):

        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print("Se elimino un producto ")
    def actualizar_precio(self,id, precio):
        for producto in self.productos:
            if producto.id == id:
                producto.precio = precio
                print('Producto actualizado exitosamente')

    def buscar_producto_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)


mi_inventario = Inventario()

"""
producto = Producto(1,"Camiseta",2,25)
#print(producto.id, producto.nombre, producto.precio)

mi_inventario.agregar_producto(producto)
mi_inventario.mostrar_inventario()

####actualizacion del precio

mi_inventario.actualizar_precio(1,100)
mi_inventario.mostrar_inventario()
"""
def Menu():
    while True:
        print('Menu')
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar Inventario")
        print("4.2 Contenedores. buscar producto por nombre ")
        print("5. Mostrar Inventario")
        print('4.2 Contenedores - Salir')

        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            id = int(input("Ingrese id del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))

            mi_inventario.agregar_producto(Producto(id, nombre, precio, id))

            print("Producto agregado")

        elif opcion == 2:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            mi_inventario.eliminar_producto(id)
            print("Producto eliminado")

        elif opcion == 3:
            print("\nActaulizar ")
            id = int(input("Ingrese el ID del producto a actualizar: "))
            precio = float(input("Ingrese precio del producto: "))
            mi_inventario.actualizar_precio(id, precio)
            print("Precio actualizado")

        elif opcion == 4:
            print("\nBuscar Nombre")
            nombre = input("Ingrese el nombre del producto: ")
            producto = mi_inventario.buscar_producto_nombre(nombre)
            print("Nombre buscado")
            print(producto.id, producto.nombre, producto.precio)

        elif opcion == 5:
            print("\nInventario ")
            mi_inventario.mostrar_inventario()


if __name__ == '__main__':
    Menu()



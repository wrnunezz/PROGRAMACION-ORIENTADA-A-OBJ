# clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'{self.id} {self.nombre} {self.cantidad} {self.precio}'

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        with open('Inventario.txt', 'r') as file:
            for line in file:
                id, nombre, cantidad, precio = line.strip().split(',')
                self.productos.append(Producto(id, nombre, cantidad, float(precio)))

    def guardar_inventario(self):
        with open('Inventario.txt', 'w') as file:
            for producto in self.productos:
                file.write(f'{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n')

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()
        print('Producto agregado exitosamente')

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Se eliminó un producto")

    def actualizar_precio(self, id, precio):
        for producto in self.productos:
            if producto.id == id:
                producto.precio = precio
                self.guardar_inventario()
                print('Producto actualizado exitosamente')

    def buscar_producto_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

mi_inventario = Inventario()

def Menu():
    while True:
        print('Menu')
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar Precio")
        print("4.2 Contenedores. Buscar producto por nombre")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))

            mi_inventario.agregar_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == 2:
            id = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id)

        elif opcion == 3:
            id = input("Ingrese el ID del producto a actualizar: ")
            precio = float(input("Ingrese nuevo precio del producto: "))
            mi_inventario.actualizar_precio(id, precio)

        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto: ")
            producto = mi_inventario.buscar_producto_nombre(nombre)
            if producto:
                print(f'Producto encontrado: ID={producto.id}, Nombre={producto.nombre}, Cantidad={producto.cantidad}, Precio={producto.precio}')
            else:
                print("Producto no encontrado")

        elif opcion == 5:
            mi_inventario.mostrar_inventario()

        elif opcion == 6:
            print("Saliendo del menú...")
            break

if __name__ == '__main__':
    Menu()
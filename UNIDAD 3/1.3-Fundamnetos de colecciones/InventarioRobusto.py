import os
from os import path
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
        self.productos = {}
        self.cargar_inventario()
    def cargar_inventario(self):
        try:
            if not os.path.exists('Inventario_Mejorado.txt'):
                with open('Inventario_Mejorado.txt','w') as file:
                    file.write('ID,nombre,cantidad,precio\n')
            else:
               with open('Inventario_Mejorado.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    self.productos[id] = Producto(id, nombre, cantidad, precio)
        except FileNotFoundError:
            print('Inventario no encontrado')

    def guardar_inventario(self):
        with open('Inventario_Mejorado.txt', 'w', encoding='utf-8') as file:
            for producto in self.productos.values():
                file.write(f'{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n')

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f'Producto {producto.id} ya existe')
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print('Producto agregado exitosamente')

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print('Producto eliminado exitosamente')
        else:
            print('Producto no encontrado')
    def actualizar_precio(self,id, precio):
        if id in self.productos:
            self.productos[id].precio = precio
            self.guardar_inventario()
            print('Producto actualizado exitosamente')
        else:
            print('Producto no encontrado')

    def buscar_producto_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)


mi_inventario = Inventario()

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
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio del producto: "))

            mi_inventario.agregar_producto(Producto(id, nombre,cantidad,precio))
            print("Producto agregado")

        elif opcion == 2:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            mi_inventario.eliminar_producto(id)
            print("Producto eliminado")

        elif opcion == 3:
            print("\nActualizar ")
            id = int(input("Ingrese el ID del producto a actualizar: "))
            precio = float(input("Ingrese precio del producto: "))
            mi_inventario.actualizar_precio(id, precio)
            mi_inventario.guardar_inventario()
            print("Precio actualizado")

        elif opcion == 4:
            print("\nBuscar Nombre")
            nombre = input("Ingrese el nombre del producto: ")
            producto = mi_inventario.buscar_producto_nombre(nombre)
            if producto is not None:
                print(f'ID: {producto.id}, Nombre: {producto.nombre}')
            else:
                print("Producto no encontrado")
           # print(producto.id, producto.nombre, producto.precio)

        elif opcion == 5:
            print("\nInventario ")
            mi_inventario.mostrar_inventario()


if __name__ == '__main__':
    Menu()

class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # privada
        self.__modelo = modelo  # privado

    def descripcion(self):
        return f'{self.__marca} {self.__modelo}'


class Auto(Vehiculo):
    def __init__(self, marca, modelo, cantidad_llantas):
        super().__init__(marca, modelo)
        self.cantidad_llantas = cantidad_llantas

    def descripcion(self):
        return f'{self._Vehiculo__marca} {self._Vehiculo__modelo}'


class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        return f'{self._Vehiculo__marca} {self._Vehiculo__modelo}'


# Ejemplo del polimorfismo
def imprimir_descripcion(vehiculo):
    print(vehiculo.descripcion())


# Instanciar objetos
auto1 = Auto("Toyota", "Hilux", 2)
print(auto1.descripcion())
auto2 = Auto("Mazda", "CX3", 5)
print(auto2.descripcion())

# Llamada al polimorfismo
imprimir_descripcion(auto1)
imprimir_descripcion(auto2)




from abc import ABC, abstractmethod

# Definición de la clase abstracta Personaje
class Personaje(ABC):  # Se marca como clase abstracta heredando de ABC
    def __init__(self, nombre, fuerza, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Vida:", self.vida)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método abstracto para calcular el daño
    @abstractmethod
    def daño(self, enemigo):
        pass

    # Método abstracto para atacar
    @abstractmethod
    def atacar(self, enemigo):
        pass


# Subclase Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, vida, espada):
        super().__init__(nombre, fuerza, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.fuerza

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Subclase Mago
class Mago(Personaje):
    def __init__(self, nombre, fuerza, vida, inteligencia, libro):
        super().__init__(nombre, fuerza, vida)
        self.inteligencia = inteligencia
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Inteligencia:", self.inteligencia)
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.fuerza * self.libro - enemigo.fuerza

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Función para el combate
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Creación de instancias de personajes y combate
personaje_1 = Guerrero("Guts", 20, 100, 4)
personaje_2 = Mago("Vanessa", 5, 100, 15, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)


enemigo_temporal = Guerrero("Enemigo Temporal", 0, 0, 5)

# Mostrar el daño calculado por cada personaje contra el enemigo temporal
print("\nDaño calculado porxdxdxdxdx", personaje_1.nombre, ":", personaje_1.daño(enemigo_temporal))
print("Daño calculado por", personaje_2.nombre, ":", personaje_2.daño(enemigo_temporal))


#/////////////////////////////---
enemigo_temporal = Guerrero("Enemigo Temporal", 0, 0, 5)

# Crear una instancia de Guerrero para personaje_1
personaje_1 = Guerrero("Guts", 20, 100, 4)

# Crear una instancia de un enemigo temporal para simular el ataque
enemigo_temporal = Guerrero("Enemigo Temporal", 0, 100, 5)

# Mostrar el daño calculado por personaje_1 contra el enemigo temporal
print("\nDaño calculado por", personaje_1.nombre, ":", personaje_1.daño(enemigo_temporal))

# Simular el ataque de personaje_1 contra el enemigo temporal
personaje_1.atacar(enemigo_temporal)




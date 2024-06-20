class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self._fuerza = fuerza  # Privado
        self._inteligencia = inteligencia  # Privado
        self._defensa = defensa  # Privado
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self._fuerza)  # Acceso a través de getter (opcional)
        print("·Inteligencia:", self._inteligencia)  # Acceso a través de getter (opcional)
        print("·Defensa:", self._defensa)  # Acceso a través de getter (opcional)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self._fuerza - enemigo._defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._espada = espada  # Privado

    def atributos(self):
        super().atributos()
        print("·Espada:", self._espada)  # Acceso a través de getter (opcional)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro = libro  # Privado

    def atributos(self):
        super().atributos()
        print("·Libro:", self._libro)  # Acceso a través de getter (opcional)

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
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)

# Simular un enemigo temporal
enemigo_temporal = Guerrero("Enemigo Temporal", 0, 0, 5, 50, 5)

# Mostrar el daño calculado por cada personaje contra el enemigo temporal
print("\nDaño ccalculado Clase Tutoria ", personaje_1.nombre, ":", personaje_1.daño(enemigo_temporal))
print("Daño calculado por", personaje_2.nombre, ":", personaje_2.daño(enemigo_temporal))

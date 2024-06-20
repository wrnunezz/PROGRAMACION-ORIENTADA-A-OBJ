# Clase base Personaje
class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Inicializa los atributos básicos de un personaje
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # Muestra los atributos del personaje
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        # Incrementa los atributos del personaje
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        # Verifica si el personaje está vivo
        return self.vida > 0

    def morir(self):
        # Marca al personaje como muerto
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        # Calcula el daño infligido al enemigo
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        # Realiza un ataque al enemigo
        daño = self.daño(enemigo)  # Llama al método daño (polimorfismo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Inicializa los atributos del Guerrero
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        # Cambia el arma del Guerrero
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        # Muestra los atributos del Guerrero, incluyendo su espada
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        # Calcula el daño infligido por el Guerrero
        return self.fuerza * self.espada - enemigo.defensa


# Clase Mago que hereda de Personaje
class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        # Inicializa los atributos del Mago
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        # Muestra los atributos del Mago, incluyendo su libro
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        # Calcula el daño infligido por el Mago
        return self.inteligencia * self.libro - enemigo.defensa


# Función para simular un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)  # Llama al método atacar (polimorfismo)
        if not jugador_2.esta_vivo():
            break
        print(">>> Acción de", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)  # Llama al método atacar (polimorfismo)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Crear instancias de Guerrero y Mago
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

# Mostrar los atributos de los personajes
personaje_1.atributos()
personaje_2.atributos()

# Simular el combate entre los dos personajes
combate(personaje_1, personaje_2)




enemigo_temporal = Personaje("Enemigo Temporal", 0, 0, 5, 100)

# Mostrar el daño calculado por cada personaje contra el enemigo temporal
print("\nDaño calculado por xdxdxdxdxd", personaje_1.nombre, ":", personaje_1.daño(enemigo_temporal))
print("Daño calculado por", personaje_2.nombre, ":", personaje_2.daño(enemigo_temporal))
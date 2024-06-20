# Clase base Personaje
class Personaje:

    # Método constructor para inicializar los atributos del personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para imprimir los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para aumentar los atributos del personaje
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para comprobar si el personaje está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para hacer morir al personaje
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular el daño infligido al enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método para atacar a un enemigo
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):

    # Método constructor para inicializar los atributos del Guerrero
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de la clase base
        self.espada = espada  # Atributo adicional específico de Guerrero

    # Método para cambiar el arma del Guerrero
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    # Método para imprimir los atributos del Guerrero, incluyendo la espada
    def atributos(self):
        super().atributos()  # Llama al método atributos de la clase base
        print("·Espada:", self.espada)

    # Método para calcular el daño infligido al enemigo, sobrescribe el método de la clase base
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


# Clase Mago que hereda de Personaje
class Mago(Personaje):

    # Método constructor para inicializar los atributos del Mago
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de la clase base
        self.libro = libro  # Atributo adicional específico de Mago

    # Método para imprimir los atributos del Mago, incluyendo el libro
    def atributos(self):
        super().atributos()  # Llama al método atributos de la clase base
        print("·Libro:", self.libro)

    # Método para calcular el daño infligido al enemigo, sobrescribe el método de la clase base
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


# Función para simular un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():  # Si el jugador 2 muere, termina el combate
            break
        print(">>> Acción de", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
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

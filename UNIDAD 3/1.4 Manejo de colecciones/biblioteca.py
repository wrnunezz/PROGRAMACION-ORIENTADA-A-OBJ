# clase libro
class Libro:
    def __init__(self, titulo, autor,categoria,isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion =(autor,titulo)

    def __str__(self):
        return f'ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}'

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.lista_usuarios = []

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuario = set()

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f'El libro {libro.titulo} ya existe')
        else:
            self.libros[libro.isbn] = libro
            self.ids_usuario.add(libro.isbn)
            print(f'El libro {libro.titulo} fue añadido')

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            #self.id_usuario.remove(libro.isbn)
            print(f'El libro {isbn} fue eliminado')
        else:
            print(f'El libro no existe')

    def agregar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f'El usuario {usuario.id_usuario} ya existe')
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuario.add(usuario.id_usuario)
            print("usuario agregado")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuario:
            del self.usuarios[id_usuario]
            #self.ids_usuario.remove(id_usuario)
            print(f'El usuario {id_usuario} ya existe')
        else:
            print(f'El usuario {id_usuario} no existe')

    def prestar_libro(self, id_usuario,isbn):
        if id_usuario not in self.usuarios:
            print(f'El usuario {id_usuario} no existe')
        elif isbn not in self.libros:
            print(f'El libro {isbn} no existe')
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f'al usuario: {id_usuario} fue prestado el libro: {libro.titulo}')
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f'El libro fue prestado al : {usuario.nombre} ')
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f'El usuario {id_usuario} no existe')


def menu():
    mi_biblioteca = Biblioteca()
    while True:
        print('1. Agregar libro')
        print('2. Quitar libro')
        print('3. Prestar libro')
        print('4.2 Contenedores. Agregar usuario')
        print('5. Quitar usuario')
        print('6. Prestar libro')
        print('11. Prestar libro')
        print('7. SALIR')

        opcion = input('Seleccione una opcion: ')
        if opcion == '1':
            titulo = input('Ingrese el titulo del libro: ')
            autor = input('Ingrese el autor : ')
            categoria = input('Ingrese el categoria del libro: ')
            isbn = input('Ingrese el ISBN del libro: ')
            libro = Libro(titulo,autor,categoria,isbn)
            mi_biblioteca.agregar_libro(libro)
            print(libro)
            print("libro agregado")
        if opcion == '2':
            isbn = input('Ingrese el ISBN del libro: ')
            mi_biblioteca.quitar_libro(isbn)
            print(isbn)
        if opcion == '11':

            mi_biblioteca.listar_libros_prestados('1')


if __name__ == '__main__':
    menu()









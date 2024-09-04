
   # Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} de {self.titulo_autor[1]}, categoría {self.categoria}, ISBN {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar los libros disponibles, con ISBN como clave
        self.usuarios = set()  # Conjunto para manejar los IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario.id_usuario)

    def dar_de_baja_usuario(self, id_usuario):
        self.usuarios.remove(id_usuario)

    def prestar_libro(self, usuario, libro):
        if libro.isbn in self.libros:
            usuario.libros_prestados.append(libro)
            del self.libros[libro.isbn]

    def devolver_libro(self, usuario, libro):
        usuario.libros_prestados.remove(libro)
        self.libros[libro.isbn] = libro

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and libro.titulo_autor[0] == titulo) or \
               (autor and libro.titulo_autor[1] == autor) or \
               (categoria and libro.categoria == categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados

# Prueba del sistema
biblioteca = Biblioteca()

libro1 = Libro("Harry Potter", "J.K. Rowling", "Fantasía", "1234567890")
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "2345678901")
libro3 = Libro("La Iliada", "Homero", "Clásicos", "3456789012")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Sofía Gómez", 1)
usuario2 = Usuario("Luis Rodríguez", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro(usuario1, libro1)
biblioteca.prestar_libro(usuario2, libro2)

print("Libros prestados a Sofía Gómez:")
for libro in biblioteca.listar_libros_prestados(usuario1):
    print(libro)

print("\nBuscar libros de Fantasía:")
for libro in biblioteca.buscar_libro(categoria="Fantasía"):
    print(libro)

biblioteca.devolver_libro(usuario1, libro1)
print("\nLibros disponibles:")
for libro in biblioteca.libros.values():
    print(libro)
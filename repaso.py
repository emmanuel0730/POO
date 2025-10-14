# ------------------------------
# Clase base (Herencia)
# ------------------------------
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        return f"Hola, soy {self.nombre}"

# ------------------------------
# Clase que hereda de Persona (Herencia + Polimorfismo)
# ------------------------------
class Bibliotecario(Persona):
    def __init__(self, nombre, id_empleado):
        super().__init__(nombre)
        self.id_empleado = id_empleado

    # Polimorfismo: sobrescribimos el método presentarse
    def presentarse(self):
        return f"Soy el bibliotecario {self.nombre}, ID: {self.id_empleado}"

# ------------------------------
# Clase Libro (objeto que será usado en agregación y composición)
# ------------------------------
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def info(self):
        return f"'{self.titulo}' de {self.autor}"

# ------------------------------
# Agregación: La Biblioteca “tiene” libros, pero los libros
# pueden existir sin la biblioteca.
# ------------------------------
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # agregación

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        return [libro.info() for libro in self.libros]

# ------------------------------
# Composición: Un préstamo NO puede existir sin un Libro y sin un Usuario.
# Cuando el préstamo se destruye, los objetos creados dentro también.
# ------------------------------
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        # Composición: se crea una copia interna del libro
        self.libro_prestado = Libro(libro.titulo, libro.autor)

    def info(self):
        return f"{self.usuario.nombre} ha tomado prestado {self.libro_prestado.info()}"

# ------------------------------
# Clase Usuario (Herencia)
# ------------------------------
class Usuario(Persona):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre)
        self.id_usuario = id_usuario

    def presentarse(self):
        return f"Soy el usuario {self.nombre}, ID: {self.id_usuario}"

# ------------------------------
# Ejemplo de uso
# ------------------------------
if __name__ == "__main__":
    # Creamos un bibliotecario y un usuario
    bibliotecario = Bibliotecario("Carlos", 101)
    usuario = Usuario("Ana", 202)

    # Creamos algunos libros
    libro1 = Libro("Cien años de soledad", "")
    libro2 = Libro("1984", "")

    # Creamos una biblioteca (Agregación)
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Mostramos información
    print(bibliotecario.presentarse())
    print(usuario.presentarse())
    print("Libros disponibles en la biblioteca:")
    for info_libro in biblioteca.mostrar_libros():
        print(" -", info_libro)

    # Hacemos un préstamo (Composición)
    prestamo = Prestamo(usuario, libro1)
    print(prestamo.info())

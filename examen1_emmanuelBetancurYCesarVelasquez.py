class biblioteca:
    def __init__(self, titulo: str, autor: str ,año_publicacion: int, genero: str):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
        
        

    def agregar_libro(self):
        lista_libros.append(libro_nuevo)
        

            
        


    def consulta(self):
        for n in lista_libros:
            if nombre == n.titulo:
                print("El libro si existe")
            else:
                print("Libro no existe")

    def numeros_libros(self):
        print(f"El numero de libros guardados es: {len(lista_libros)}")

lista_libros = []  
print("Bienvenido a la biblioteca UdeM")
while True:
    print("\n menú")
    print("1.Registrar nuevo libro")
    print("2.Ver libros registrados")
    print("3.consultar si libro existe")
    print("4.Numero de libros guardados")
    print("0.salir")

    opcion = int(input("Ingrese la opcion que quiera: "))

    if opcion == 1:
        titulos = input("Ingrese el nombre del libro nuevo: ").lower()
        autores = input("Ingrese el nombre del autor del libro: ").lower()
        año = int(input("Ingrese el año de publiacion: "))
        generos = input("Ingrese el genero del libro: ").lower()

        libro_nuevo = biblioteca(titulos, autores, año, generos)
        libro_nuevo.agregar_libro()
        print("Libro registrado correctamente")

    elif opcion == 2:
        print("\nLibros registrados")
        contador = 0 
        for libro in lista_libros:
            print(f"{contador + 1}: nombre: {libro.titulo}--Autor: {libro.autor}--Año de publicacion: {libro.año_publicacion}---Genero: {libro.genero} ")
            contador += 1

    elif opcion == 3:
        nombre = input("Ingrese el nombre del libro que desea buscar: ").lower()
        biblioteca.consulta(nombre)

    elif opcion == 4:
        biblioteca.numeros_libros()

    elif opcion == 0:
        break

    else:
        print("ingrese opcion valida")



       

   




class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad 
        self.nota = nota 


class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad 
        self.expereriencia = experiencia
        

class GrupoAsignatura:
    def __init__(self,nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiantes(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado correctamente")      
    

    def promedio (self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio
    
    def mostrar_estudiantes (self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
           
    

profesor = Profesor("juan",35,5)
poo = GrupoAsignatura("Programacion orientada a objetos", "M-V 10-12", "62", profesor)
print(poo.horario)
print(poo.profesor.nombre)

estudiante1 = Estudiante("Emmanuel", 18, 5)
estudiante2 = Estudiante("Sexar", 18,3.8)
estudiante3 = Estudiante("Chirri", 19,2.1)

poo.agregar_estudiantes(estudiante1)
poo.agregar_estudiantes(estudiante2)
poo.agregar_estudiantes(estudiante3)
print(poo.promedio())

poo.mostrar_estudiantes()
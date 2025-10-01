import random
class Persona:
    def __init__(self, nombre , correo):
        self.nombre = nombre
        self.correo  = correo

    def Presentarse (self):
        print(f"Hola, soy {self.nombre}")

class Empleado (Persona):
    def __init__(self, nombre, correo,Salario):
        super().__init__(nombre, correo)
        self.salario = Salario


    def calcular_bono (self,salario):
        bono = salario *0.10

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, Salario, lenguajePrincipal):
        super().__init__(nombre, correo, Salario)
        self.lenguajePrincipal = lenguajePrincipal

class Analista(Empleado):
    def __init__(self, nombre, correo, Salario, seniority):
        super().__init__(nombre, correo, Salario)
        self.seniority = seniority


    def calcular_bono(self, salario):
        bono = salario *0.8
    

class Gerente (Empleado):
    def __init__(self, nombre, correo, Salario):
        super().__init__(nombre, correo, Salario)
        self.empleados_a_cargo = []

    def agregar_empleado (self,empleado):
        if empleado in self.empleados_a_cargo:
            print("Empleado ya existente")
        else:
            self.empleados_a_cargo.append(empleado)

    def remover_empleado(self, empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)

    def listar_equipos ():
        print("hola")



class Proyecto:
    def __init__(self,nombre,presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.lista_tarea = []
            
    def agregar_tarea(self,descripcion , horas_estimadas):
        tarea = Tarea(descripcion, horas_estimadas)
        self.lista_tarea.append(tarea)
        return tarea
        
        



class Tarea: 
    def __init__(self, descripcion, horas_estimadas= int ):
        self.id = random.randint(100, 999)
        self.descripcion = descripcion
        self.horas_estimadas = horas_estimadas
        self.asignacion = None


mico = Tarea("mico", -1)





        




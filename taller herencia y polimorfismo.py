import random
class Persona:
    def __init__(self, nombre , correo):
        self.nombre = nombre
        self.correo  = correo

    def Presentarse (self):
        print(f"Hola, soy {self.nombre}, mi correo es {self.correo}")

class Empleado (Persona):
    def __init__(self, nombre, correo,Salario):
        super().__init__(nombre, correo)
        self.salario = Salario
        self.proyectos = []


    def calcular_bono (self):
        return 0
        

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, Salario, lenguajePrincipal):
        super().__init__(nombre, correo, Salario)
        self.lenguajePrincipal = lenguajePrincipal

    def calcular_bono(self):
        bono = self.salario * 0.10
        for p in self.proyectos:
            if len(p.lista_tareas) > 5:
                bono += bono * 0.01
                break
        return bono
    
    def Presentarse (self):
        print(f"Hola, me llamo {self.nombre}, desarrolador en{self.lenguajePrincipal}")

class Analista(Empleado):
    def __init__(self, nombre, correo, Salario, seniority):
        super().__init__(nombre, correo, Salario)
        self.seniority = seniority


    def calcular_bono(self):
        bono = self.salario * 0.08
        if self.seniority.lower() == "senior":
                bono += bono * 0.03
                
        return bono

    def Presentarse (self):
         print(f"Hola, me llamo {self.nombre}, analista {self.lenguajePrincipal}")

    

class Gerente (Empleado):
    def __init__(self, nombre, correo, Salario):
        super().__init__(nombre, correo, Salario)
        self.empleados_a_cargo = []

    def calcular_bono(self):
        return self.salario * 0.2

    def agregar_empleado (self,empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.append(empleado)

    def remover_empleado(self, empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)

    def listar_equipos (self):
        return [empleado.nombre for empleado in self.empleados_a_cargo]
        



class Proyecto:
    def __init__(self,nombre,presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.lista_tarea = []
            
    def agregar_tarea(self, descripcion , horas_estimadas):
        tarea = Tarea(descripcion, horas_estimadas)
        self.lista_tarea.append(tarea)
        return tarea
        
    def asignar_a_un_empleado(self,tarea ,empleado):
        if tarea in self.lista_tarea:
            tarea.asignacion = empleado
            empleado.proyectos.append(self)


class Tarea: 
    def __init__(self, id ,descripcion, horas_estimadas ):
        while True:
            if horas_estimadas < 0:
                print("ingrese una hora estimada correcta")
            else:
                break
        self.id = id
        self.descripcion = descripcion
        self.horas_estimadas = horas_estimadas
        self.asignacion = None


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def crear_proyecto(self, nombre, presupuesto):
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_proyecto(self, proyecto, tarea, empleado):
        if proyecto in self.proyectos and empleado in self.empleados:
            proyecto.asignar_empleado(tarea, empleado)

empresa = Empresa("Primera linea")


desarrollador = Desarrollador("emma","emma@gmail.com", 7000,"python")
analista = Analista("Aristi","aristi@gmail.com", 5000, "senior")
gerente = Gerente("Cesar", "cesar@gmail.com", 9000)

empresa.agregar_empleado(desarrollador)
empresa.agregar_empleado(analista)
empresa.agregar_empleado(gerente)

gerente.agregar_empleado(desarrollador)
gerente.agregar_empleado(analista)

proyecto1 = empresa.crear_proyecto("Impresiones", 300000)
proyecto1.agregar_tarea("diseñar",10)
proyecto1.agregar_tarea("programar",20)
proyecto1.agregar_tarea("frontend",17)
proyecto1.agregar_tarea("testear",7)
proyecto1.agregar_tarea("documentacion",6)
proyecto1.agregar_tarea("optimizar",12)

empresa.asignar_empleado_a_proyecto(proyecto1,1, desarrollador)
empresa.asignar_empleado_a_proyecto(proyecto1,0,analista)

print(desarrollador.presentarse(), " Bono:", desarrollador.calcular_bono())
print(analista.presentarse(), " Bono:", analista.calcular_bono())
print(gerente.presentarse(), " Bono:", gerente.calcular_bono())
print("Equipo gerente:", gerente.listar_equipo())






        




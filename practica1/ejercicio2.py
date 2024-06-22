class Estudiante:
    def __init__(self, nombre, edad, fechaNacimiento, fechaIngreso, matricula, activo):
        self.nombre = nombre
        self.edad = edad
        self.fechaNacimiento = fechaNacimiento
        self.fechaIngreso = fechaIngreso
        self.matricula = matricula
        self.activo = activo    
        
        
    def __str__(self) -> str:
        return self.nombre, self.edad, self.fechaNacimiento, self.fechaIngreso, self.matricula ,self.activo

class Universidad:
    def __init__(self):
        self.listaEstudiante = []
        
    def mostrarEstudiantes(self,estudiante): 
        self.listaEstudiante.append(estudiante) 
        
        
    def imprime(self):
        print(self.listaEstudiante)
universidad = Universidad()
    
# listaEstudiante =[{"Juan",35,'22/09/1996','02-06-2024','04-3444',True}]
# for estudiante in listaEstudiante:
#     universidad.ingresarEstudiantes(estudiante)
universidad.mostrarEstudiantes({"Juan",35,'22/09/1996','02-06-2024','04-3444',True})
universidad.mostrarEstudiantes({"Pedro",35,'22/09/1996','02-06-2024','04-3444',True})
universidad.mostrarEstudiantes({"Santiago",35,'22/09/1996','02-06-2024','04-3444',True})
universidad.imprime()

  
     

    

    
    
    

        
        
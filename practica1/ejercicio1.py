class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
            
Hola = Persona("Pedro", 35)
Hola.saludar() #salida: Hola, mi nombre es Juan y tengo 12 años.
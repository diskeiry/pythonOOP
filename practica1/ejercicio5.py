#Getters y Setters en python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
persona = Persona("Juan", 30)



# uso de los getters y setters
print(persona.get_nombre()) #salidad: Juan
persona.set_nombre("Carlos")
print(persona.get_nombre()) #Salida: Carlos
print(persona.get_edad()) #salida: 30

persona.set_edad(31)
print(persona.get_edad()) #salida:31

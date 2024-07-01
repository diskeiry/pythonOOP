#Herencias en python

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar el metodo hablar()")

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: !Guau"
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice:!Miau"

mi_perro = Perro("Bobby") #uso de la clases derivadas
mi_gato = Gato("Minino") # uso de la clase derivadas

print(mi_perro.hablar()) #salida: Bobby dice: !Guau
print(mi_gato.hablar()) #salida: Minino dice:!Miau
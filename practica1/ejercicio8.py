class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Subclase debe implementar el metodo hablar()")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "!Guau"

mi_perro = Perro("Boddy", "Ladrador")
print(f"{mi_perro.nombre} es un {mi_perro.raza} y dice: {mi_perro.hacer_sonido()}")

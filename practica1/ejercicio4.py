class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
def imprimir_sonido(teteo):
    print(teteo.hacer_sonido())
perro = Perro()
gato = Gato()
imprimir_sonido(perro)
imprimir_sonido(gato)


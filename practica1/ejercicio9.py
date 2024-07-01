#Esta clase es una clase abstracta (hereda de ABC), lo que significa que no se puede instanciar directamente.
from abc import ABC, abstractmethod
class Figura(ABC):
    #Define un método abstracto llamado area(). Cualquier clase que herede de Figura debe implementar este método.
    @abstractmethod
    def area(self):
        pass
    
#Hereda de la clase Figura
class Circulo(Figura):
    #Tiene un constructor que inicializa el radio del círculo.
    def __init__(self, radio):
        self.radio = radio
    #Implementa el método area() para calcular el área del círculo utilizando la fórmula.(πr2)   
    def area(self):
        return 3.1416 * self.radio ** 2

#También hereda de la clase Figura.   
#Tiene un constructor que inicializa la base y la altura del rectángulo. 
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    #Implementa el método area() para calcular el área del rectángulo multiplicando la base por la altura.
    def area(self):
        return self.base * self.altura


# Crear objetos
circulo = Circulo(radio=5)
rectangulo = Rectangulo(base=4, altura=3)

# Calcular y mostrar áreas
print(f"Área del círculo: {circulo.area()}")
print(f"Área del rectángulo: {rectangulo.area()}")

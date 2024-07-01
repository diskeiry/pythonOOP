from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2
class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura



figura = Circulo()
print(figura.area())

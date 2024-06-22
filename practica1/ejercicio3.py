class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")
coche1.arrancar()
coche2.arrancar()
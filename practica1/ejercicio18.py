import csv

def leerArchivo(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

#Ejemplo de uso: deben tener un archivo creado
path = '/Users\PC\OneDrive\Escritorio\prueba/archivo1.csv'
dato = leerArchivo(path)
print("Datos leidos del archivo CSV:")
for elementos in dato:
    print(elementos)
import csv

def agregarData(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        
#Ejemplo de uso: deben tener un archivo creado
path = '/Users\PC\OneDrive\Escritorio\prueba/archivo1.csv'
data = [
    ["Juan", 30], 
    ["Pedro", 25],
    ["Carlos", 35],  
]   
agregarData(path, data)

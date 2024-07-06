import csv

def guardar_en_directorio(file_path, data):
    with open(file_path, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(data)
        
path = '/Users\PC\OneDrive\Escritorio\prueba/archivo3.csv'  
escribir = [
    ['nombre', 'edad'],
    ['Juan', 23],
    ['Aldo', 21],
    ['Maria', 25],
    ['Pedro', 22],
    ['Jose', 24]
]
guardar_en_directorio(path, escribir)

import zipfile
from pathlib import Path
#Definir la ruta usuando pathlib
ruta = Path("/Users\PC\OneDrive\Escritorio\prueba")

#Crear archivo si no existe
archivo1 = ruta / 'archivo1.txt'
archivo2 = ruta / 'archivo2.txt'
archivo3 = ruta / 'archivo3.txt'

if not archivo1.exists():
    archivo1.write_text("contenido de archivo2.txt")

if not archivo2.exists():
    archivo2.write_text("contenido de archivo2.txt")
    
if not archivo3.exists():
    archivo3.write_text("contenido de archivo3.txt")
    
#Crear un archivo ZIP y añadir archivos
with zipfile.ZipFile(ruta / 'archivo.zip', 'w') as myzip:
    myzip.write(archivo1, archivo1.name)
    myzip.write(archivo2, archivo2.name)

    
if not archivo3.exists():
   with zipfile.ZipFile(ruta / 'archivo.zip', 'a') as myzip:
       myzip.write(archivo3, archivo3.name)
       
with zipfile.ZipFile(ruta / 'archivo.zip', 'r') as myzip:
    print("contenido del archivo ZIP: ", myzip.namelist())
    
with zipfile.ZipFile(ruta / 'archivo.zip', 'r') as myzip:
    myzip.extractall(ruta / 'mi_carpeta')


#Leer el conte

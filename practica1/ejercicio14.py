from pathlib import Path

dir_path = Path('/Users\PC\OneDrive\Escritorio')

if dir_path.exists():
    print(f"El directorio {dir_path} existe")
else:
    print(f"El directorio {dir_path} no existe")
    
for file in dir_path.iterdir():
    print(file)
    
new_file = dir_path / 'nuevo_archivo.txt'
new_file.write_text('Contenido de ejemplo')
print(new_file.read_text())
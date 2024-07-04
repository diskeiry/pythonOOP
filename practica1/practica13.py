import bcrypt

class Usuario:
    def __init__(self) -> None:
        self.usuario = ''
        self.hash_contrasena = ''
        self.lista_usuario = []

    def agregar_usuario(self):
        self.usuario = input("Ingrese el nombre de usuario: ")
        self.hash_contrasena = input("Ingrese la contraseña: ")
        self.usuario = self.usuario
        self.hash_contrasena = self.hash_contrasena
        # Generar el hash de la contraseña
        self.hash_contrasena = bcrypt.hashpw(self.hash_contrasena.encode('utf-8'),bcrypt.gensalt())

        # Agregar usuario y hash de contraseña a la lista
        self.lista_usuario.append((self.usuario, self.hash_contrasena))
        
        print(f"Usuario '{self.usuario}' agregado correctamente con el hash de la contraseña.")

    def consultar_usuarios(self):
        print("\nUsuarios y hashes de contraseñas:")

        for usuario,contrasena in self.lista_usuario:
            print(f"Usuario: {usuario}, Hash de contraseña: {contrasena}")

usuario = Usuario()
# Ejecutar el programa
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios y hashes de contraseñas")
    print("3. Salir")  
  
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        usuario.agregar_usuario()
    elif opcion == '2':
        usuario.consultar_usuarios()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-3).")
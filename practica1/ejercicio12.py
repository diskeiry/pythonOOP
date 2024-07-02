# class Usuario:
#     def __init__(self, nombre_usuario, contrasena):
#         self.nombre_usuario = nombre_usuario
#         self.contrasena = contrasena
      
#     def autenticar(self,contrasena_ingresada):
#         if contrasena_ingresada == self.contrasena:
#                 return True
#         else:
#             return False
        
# usuario = Usuario("Usuario1", "1234") #Crear un usuario

# contrasena_ingresada = input("Ingrese Contraseña: ") #autenticacion

# if usuario.autenticar(contrasena_ingresada):
#     print("Autenticacion exitosa!")
# else:
#     print("Contraseña incorrecta. Autenticacion fallida!")

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
      
    def autenticar(self,contrasena_ingresada):
        if contrasena_ingresada == self.contrasena:
                return True
        else:
            return False
        
Lista = [{'nombre_usuario':"Juan",'contrasena_ingresada':"1234"}
        ,{'nombre_usuario':"marco", 'contrasena_ingresada':"12345"},
         {'nombre_usuario':"pedro", 'contrasena_ingresada':"123456"}] 

nombre_usuario = input("Ingresar usuario: ")
contrasena_ingresada = input("Ingrese Contraseña: ") #autenticacion

for usuario in Lista:
    if usuario['nombre_usuario'] == nombre_usuario:
        if usuario['contrasena_ingresada'] == contrasena_ingresada:
            print("Autenticacion exitosa!")
        else:
            print("Contraseña incorrecta. Autenticacion fallida!")
print("\n")
print("********************************")
print("           LIBROS"           )
print("********************************")
print("    <<<LIBROS DISPONIBLES>>>"    )
print()
class Libro:
    def __init__(self, titulo, autor, disponible, id):
        self._titulo = titulo
        self._autor = autor
        self._disponible = disponible
        self._id = id
    
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, titulo):
        self._titulo = titulo
        
    def get_autor(self):
        return self._autor
    
    def set_autor(self, autor):
        self._autor = autor
        
    def get_disponile(self):
        return self._disponible
    
    def set_disponible(self, disponible):
        self._disponible = disponible
        
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def __str__(self) -> str:
        return f"{self._titulo}, {self._autor}, {self._disponible}, {self._id}"

libro = Libro("Develomente","Chappman", True , 1.004)
print(libro)

#uso de los getters y setters
libro.set_titulo("JavaScript") #salidad: Juan
libro.set_autor("Carlos")
libro.set_disponible(True) #Salida: True
libro.set_id(1.003)
print(libro)

#usuario modificado
libro.set_titulo("Matematica") #salidad: Juan
libro.set_autor("Roberto")
libro.set_disponible(True) #Salida: True
libro.set_id(1.002)
print(libro)

print("\n")
print("********************************")
print("        REGISTRO DE USUARIOS")
print("********************************")
print("         <<<USUARIOS>>>"    )
print()
class Usuario:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._libro_prestados = []
        
    #metodo para obtener el construction
    def get_nombre(self):
        return self._nombre
    #metodo para modificar el constuctor
    def set_nombre(self, nombre):
        self._nombre = nombre
        
   #metodo para obtener el construction   
    def get_edad(self):
        return self._edad
    
    #metodo para modificar el constuctor
    def set_edad(self, edad):
        self._edad = edad   
    
    #Metodo para guardar libro y prestarlo  
    def tomar_libro(self, Libro):
        self._libro_prestados.append(Libro)
        
    def devolver_libro(self, libro):
        self._libro_prestados.remove
        print(f"El libro {libro} ha sido devuelto")
        
    def buscar_libro(self):
        return self._libro_prestados
        
#crear un usuario
usuario = Usuario("Juan", 30)

#obtener el nombre y la edad del usuario
nombre = usuario.get_nombre()
edad = usuario.get_edad()
print(nombre, edad)

#modificar el usuario
usuario.set_nombre("Raffy")
usuario.set_edad(21)

#Tomo un libro prestado este usuario
usuario.tomar_libro("La raiz en github")

#devolvio el libro
usuario.devolver_libro("La raiz en github")

#busca de libros que se emprestaron
libro_prestados = usuario.buscar_libro()
print(f"El libro prestado fue: {libro_prestados}")
print("\n")


print("            ***********************************")
print("                        BIBLIOTECA")
print("            ***********************************")
print("                 <<<LIBROS Y USUARIOS>>>" )
print()
class Biblioteca:
    def __init__(self):
        self._libros = []
        self._usuarios = []
        
    def agregar_libro(self, titulo, autor):
        libro = {'titulo': titulo, 'autor': autor}
        self._libros.append(libro)
        print(f"El Libro '{titulo}' de '{autor}' ha sido agregado a la biblioteca.")
    
    def eliminar_libro(self, titulo, autor):
        libro = {'titulo': titulo, 'autor': autor}
        if libro in self._libros:
            self._libros.remove(libro)
            print(f"El Libro '{titulo}' de {autor} fue eliminado de la biblioteca.")
        else:
            print(f"Libro '{titulo}' de {autor} no encontrado en la biblioteca.")
    
        
    def buscar_libros(self, titulo=None, autor=None):
        resultados = []
        for libro in self._libros:
            if (titulo and titulo.lower() in libro['titulo'].lower()) or (autor and autor.lower() in libro['autor'].lower()):
                resultados.append(libro)
        return resultados
    
    
    def registrar_usuario(self, nombre):
        if nombre not in self._usuarios:
            self._usuarios.append(nombre)
            print(f"Usuario '{nombre}' registrado en la biblioteca.")
        else:
            print(f"Usuario '{nombre}' ya está registrado en la biblioteca.")
    
    def buscar_usuarios(self, nombre):
        resultados = [usuario for usuario in self._usuarios if nombre.lower() in usuario.lower()]
        return resultados
                
    def listar_libros(self):
        return self._libros
    
    def listar_usuarios(self):
        return self._usuarios
    
    
#instance
biblioteca = Biblioteca()

#agregar libros
biblioteca.agregar_libro("Develomente","Chappman")
biblioteca.agregar_libro("Java","Chan")

#eliminar libro
biblioteca.eliminar_libro("Develomente","Chappman")

#buscar libros
print("El libro encontrado en biblioteca es:", biblioteca.buscar_libros(titulo="Java"))
print("El libro encontrado en biblioteca es:", biblioteca.buscar_libros(autor="Chan"))

#registo de usuarios
biblioteca.registrar_usuario("Jose Cazals")
biblioteca.registrar_usuario("Bryant Rodriguez")

#buscar usuarios
print("Busrcar usuarios por nombre 'Jose':",
biblioteca.buscar_usuarios("jose"))

# Listar todos los libros
print("Libros disponibles:", biblioteca.listar_libros())

# Listar todos los usuarios
print("Usuarios registrados:", biblioteca.listar_usuarios())
print()

print("            ***********************************")
print("                  SUBCLASES Y POLIMORFISMO")
print("            ***********************************")
print("                 <<<SUBCLASES DE LIBRO>>>" )
print()
class Libro():
    def __init__(self, titulo, autor, disponible, id):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        self.id = id
class LibroFisico(Libro):
    def __init__(self, titulo, autor, disponible, id, ubicacion):
        super().__init__(titulo, autor, disponible, id)
        self.ubicacion = ubicacion

class LibroDigital(Libro):
    def __init__(self, titulo, autor, disponible, id, url):
        super().__init__(titulo, autor, disponible, id)
        self.url = url
        
libro_fisico = LibroFisico("Develomente","Chappman", True , 1.004, "masachusset")

libro_digital = LibroDigital("Ciberseguridad",
    " José Manuel Ortega Candel",True,"12345","https://www.paraninfo.es/catalogo/9788413661162/ciberseguridad--manual-practico"
)

print(f"El libro: {libro_fisico.titulo}, es del autor: {libro_fisico.autor}, esta: {libro_fisico.disponible}, con su id: {libro_fisico.id}, su ubicacion es: {libro_fisico.ubicacion}")

print(f"El libro: {libro_digital.titulo}, el autor es: {libro_digital.autor}, esta: {libro_digital.disponible},con su id: {libro_digital.id}, la url es: {libro_digital.url}")
print()

print("            ***********************************")
print("                  INTERACCION DEL USUARIO")
print("            ***********************************")
print("                 <<<MENU PRINCIPAL>>>" )
print()
class Biblioteca:
    # inicializar dos atributos
    def __init__(self):
        self.libros = {}  # Un diccionario que almacena los libros disponibles y su estado (prestado o no).
        self.usuarios = []  # Una lista que registra los nombres de los usuarios.

    # Agrega un libro al diccionario libros si no existe previamente.
    # Si el libro ya existe, muestra un mensaje indicando que el libro ya está en la biblioteca.
    def agregar_libro(self, titulo):
        if titulo not in self.libros:
            self.libros[titulo] = {'disponible': True, 'usuario': None}
            print(f"Libro '{titulo}' añadido.")
        else:
            print(f"Libro '{titulo}' ya existe.")

    # Si el libro existe, muestra si está disponible o prestado.
    # Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def buscar_libro(self, titulo):
        if titulo in self.libros:
            estado = "disponible" if self.libros[titulo][
                'disponible'] else f"prestado a {self.libros[titulo]['usuario']}"
            print(f"'{titulo}' está {estado}.")
        else:
            print(f"Libro '{titulo}' no encontrado.")
            

    # Si el libro no está disponible, muestra un mensaje indicando que no se puede prestar.
    # Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def prestar_libro(self, titulo, usuario):
        if titulo in self.libros and self.libros[titulo]['disponible']:
            self.libros[titulo]['disponible'] = False
            self.libros[titulo]['usuario'] = usuario
            print(f"'{titulo}' prestado a {usuario}.")
        elif titulo in self.libros:
            print(f"'{titulo}' no disponible.")
        else:
            print(f"Libro '{titulo}' no encontrado.")

    # Si el libro ya está disponible, muestra un mensaje indicando que no se puede devolver.
    # Si el libro no existe, muestra un mensaje indicando que no se encontró.
    def devolver_libro(self, titulo):
        if titulo in self.libros and not self.libros[titulo]['disponible']:
            self.libros[titulo]['disponible'] = True
            usuario = self.libros[titulo]['usuario']
            self.libros[titulo]['usuario'] = None
            print(f"'{titulo}' devuelto por {usuario}.")
        elif titulo in self.libros:
            print(f"'{titulo}' ya está disponible.")
        else:
            print(f"Libro '{titulo}' no encontrado.")

    # Si el usuario ya está registrado, muestra un mensaje indicando que ya existe.
    def registrar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios.append(nombre)
            print(f"Usuario '{nombre}' registrado.")
        else:
            print(f"Usuario '{nombre}' ya está registrado.")



# Crea una instancia de la clase Biblioteca.
# Muestra un menú con opciones para buscar, prestar, devolver, registrar usuarios, agregar libros o salir.
# Lee la opción seleccionada por el usuario y ejecuta la función correspondiente.
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nOpciones:")
        print("1. Buscar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Registrar nuevo usuario")
        print("5. Agregar nuevo libro")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            titulo = input("Introduce el título del libro: ")
            biblioteca.buscar_libro(titulo)  # Busca un libro por título y muestra su estado.
        elif opcion == '2':
            titulo = input("Introduce el título del libro: ")
            usuario = input("Introduce el nombre del usuario: ")
            if usuario in biblioteca.usuarios:
                biblioteca.prestar_libro(titulo, usuario)  # Presta un libro a un usuario registrado.
            else:
                print(f"Usuario '{usuario}' no registrado.")
        elif opcion == '3':
            titulo = input("Introduce el título del libro: ")
            biblioteca.devolver_libro(titulo)  # Devuelve un libro previamente prestado
        elif opcion == '4':
            nombre = input("Introduce el nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)  # Registra un nuevo usuario.
        elif opcion == '5':
            titulo = input("Introduce el título del libro: ")
            biblioteca.agregar_libro(titulo)  # Agrega un nuevo libro a la biblioteca.
        elif opcion == '6':
            print("Saliendo del programa...")
            break  # Sale del bucle y finaliza el programa.
        else:
            print("Opción no válida.")


# En resumen, la función menu() proporciona una interfaz interactiva para interactuar con la biblioteca, permitiendo buscar, prestar, devolver, registrar usuarios y agregar libros.


# Ejecuta el menú cuando el script se ejecuta directamente (no cuando se importa como módulo).
if __name__ == "__main__":
    menu()

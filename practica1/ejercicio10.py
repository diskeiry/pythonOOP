import hashlib

#Data de entrada
mensaje = "Diskeiry"

#Crear un obje hash SHA-256
hash_object = hashlib.sha256()

#Actualizar el hash con los datos
hash_object.update(mensaje.encode())

#Obtener el hash en formato hexadecimal
hash_hex = hash_object.hexdigest()

#Imprimir el hash
print(f"Mensaje original: {mensaje}")
print(f"Hash SHA-256: {hash_hex}")
import secrets 

#Generar un token de autenticacion seguro
token = secrets.token_hex(16)

print(f"Token de autenticacion seguro: {token}")
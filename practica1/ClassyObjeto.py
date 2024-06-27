#clases y objeto 
class nombre:
    pass

victor = nombre()
maria = nombre()

#objeto.attributo = valor

victor.edad = 30
victor.sexo = 'masculino'
victor.pais = 'Red.Dom'

maria.edad = 30
maria.sexo = 'femenino'
maria.pais = 'Spain'

print(f"La edad de victor es: {victor.edad} años")
print(f"Victor vive en: {victor.pais}")
print(f"La edad de maria es: {maria.edad} años")
print(f"Maria vive en: {maria.pais}")

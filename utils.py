import re

#Validación ingreso solo letras y espacios
def validar_caracteres(texto):
    return re.match(r'^[A-Za-z ]+$', texto) is not None

#Validación ingreso solo números
def validar_numeros(texto):
    return re.match(r'^[0-9]+$', texto) is not None

#Validación dni entre 7 u 8 números
def validar_dni (dni):
    return validar_numeros(dni) and (len(dni) ==7 or len(dni)== 8)

#Validacion dni existente
def dni_existe(dni, lista_usuarios):
    for i in lista_usuarios:
        if i["dni"] == dni:
            return True
    return False
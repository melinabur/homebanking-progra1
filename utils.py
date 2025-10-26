"""
Funciones auxiliares de validación para el sistema.
"""
import re
import random

#Validación ingreso solo letras y espacios
def validar_caracteres(texto):
    """
    Valida que el texto contenga solo letras y espacios.
    """
    return re.match(r'^[A-Za-z ]+$', texto) is not None

#Validación ingreso solo números
def validar_numeros(texto):
    """
    Valida que el texto contenga únicamente números.
    """
    return re.match(r'^[0-9]+$', texto) is not None

#Validación dni entre 7 u 8 números
def validar_dni (dni):
    """
    Verifica que el dni tenga 7 u 8 dígitos numericos.
    """
    return validar_numeros(dni) and (len(dni) ==7 or len(dni)== 8)

#Validacion dni existente
def dni_existe(dni, lista_usuarios):
    """
    Comprueba si el DNI ya está registrado en la lista de usuarios.
    """
    for i in lista_usuarios:
        if i["dni"] == dni:
            return True
    return False

#Generar alias aleatorio
def generar_alias(usuarios):
    """
    Selecciona tres palabras al azar de una lista predefinida 
    y las combina con puntos. Utiliza validacion para asegurar que no se repita.
    """
    palabras_alias = [
        "silla", "cielo", "perro", "gato", "sol", "luna", "mar", "nube", "sopa", "rueda",
        "pluma", "cabra", "flor", "hoja", "vino", "cuerda", "piedra", "puerta", "rayo", "fuego"
    ]
    alias = ".".join(random.sample(palabras_alias, 3))

    while alias_existe(alias, usuarios):
        alias = ".".join(random.sample(palabras_alias, 3))
    return alias
   

def validar_alias_formato(alias):
    """
    Valida que el alias cumpla con el formato permitido:
    - Solo letras, numeros y puntos
    - Entre 6 y 20 caracteres
    Devuelve True o False
    """
    return re.match(r'^[a-zA-Z0-9.]{6,20}$', alias) is not None

def alias_existe(alias, usuarios):
    """
    Verifica si el alias ya existe en la lista de usuarios.
    Devuelve True si esta en uso o False si esta disponible.
    """
    for u in usuarios:
        if u["alias"] == alias.lower():
            return True
    return False
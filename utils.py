"""
Funciones auxiliares de validación para el sistema.
"""
import re

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
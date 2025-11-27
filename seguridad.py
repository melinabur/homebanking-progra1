"""
Contiene las validaciones y mecanismos de seguridad del sistema.
"""

import re
from utils import guardar_usuarios, validar_numeros
from historial import registrar_evento

def validar_password(password):
    """
    Valida que la contraseña tenga al menos 8 caracteres, una mayúscula,
    una minúscula y un número.
    """
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', password) is not None

def cambiar_pin(usuario, usuarios): 
    """
    Esta función cambia el pin de transferencia de los usuarios. 
    """
    print("\n--- Cambio de PIN ---")
    pin_actual = input("Ingrese su PIN actual: ")

    if pin_actual != usuario["pin"]:
        print("PIN incorrecto.")
        return

    pin_nuevo = input("Ingrese un nuevo PIN de 4 dígitos: ")
    while not (validar_numeros(pin_nuevo) and len(pin_nuevo) == 4):
        print("Error. El PIN debe tener 4 dígitos numéricos.")
        pin_nuevo = input("Ingrese un PIN válido: ")

    usuario["pin"] = pin_nuevo
    guardar_usuarios(usuarios)
    registrar_evento(usuario, "Cambio de PIN", "El usuario actualizó su PIN de transferencias.")

    print("Su PIN ha sido actualizado correctamente.")
"""
Contiene las validaciones y mecanismos de seguridad del sistema.
"""

import re

def validar_password(password):
    """
    Valida que la contraseña tenga al menos 8 caracteres, una mayúscula,
    una minúscula y un número.
    """
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', password) is not None

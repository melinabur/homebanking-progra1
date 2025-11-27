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

#CAMBIAR CONTRASEÑA
def cambiar_contrasenia(usuario, usuarios):
    """
    Permite al usuario modificar su contraseña actual.
    La valida.
    """
    print("\n--- Cambio de Contraseña ---")
    actual = input("Ingrese su contraseña actual: ")

    # Verificar que la contraseña actual sea correcta
    if actual != usuario["password"]:
        print("Contraseña incorrecta. No se pudo realizar el cambio.")
        return

    # Pedir nueva contraseña y validarla con la función de seguridad
    nueva = input("Ingrese la nueva contraseña (mínimo 8 caracteres, con una mayúscula, una minúscula y un número): ")
   
    #Validar formato y diferencia con la contraseña actual
    es_valida = validar_password(nueva)
    # Obtener historial de las contraseñas previas si existe
    historial = usuario.get("historial_claves", [])

    while es_valida == False or nueva == usuario["password"] or nueva in historial:
        if nueva == usuario["password"]:
            print("La nueva contraseña no puede ser igual a la actual.")
        elif nueva in historial:
            print("La nueva contraseña ya fue usada anteriorment. Ingrese una diferente.")    
        else:
            print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")
        nueva = input("Ingrese una nueva contraseña válida: ")
        es_valida = validar_password(nueva)


    # Confirmar nueva contraseña
    confirmar = input("Confirme la nueva contraseña: ")
    if confirmar != nueva:
        print("Las contraseñas no coinciden. Intente nuevamente.")
        return
    
    # Agregar la contraseña actual al historial antes de reemplazarla
    historial.append(usuario["password"])
    
    # Mantener solo las últimas 7 contraseñas
    if len(historial) > 7:
        historial = historial[-7:]

    # Actualizar campos
    usuario["historial_claves"] = historial
    usuario["password"] = nueva
    print("Contraseña actualizada correctamente.")

    # Guardar el cambio en el archivo JSON
    guardar_usuarios(usuarios)
    registrar_evento(usuario, "Cambio de contraseña", "El usuario cambió su contraseña.")


#CAMBIAMOS PIN DE TRANSFERENCIA
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
from utils import guardar_usuarios

def transferir_dinero(usuario_origen, usuarios):
    """
    Permite transferir dinero a otro usuario del sistema usando ALIAS o CBU.
    Valida saldo, monto y existencia del destinatario.
    """

    print("\n--- Transferencia de Dinero ---")
    print("¿Cómo desea buscar al destinatario?")
    print("1) Por alias")
    print("2) Por CBU")
    opcion = input("Seleccione una opción: ")

    # Variables iniciales
    encontrado = False
    usuario_destino = {} 

    # Busqueda por alias
    if opcion == "1":
        alias_destino = input("Ingrese el alias del destinatario: ").lower()

        # Evita que el usuario se transfiera a sí mismo
        if alias_destino == usuario_origen["alias"]:
            print("No podés transferirte dinero a vos mismo.")
            return

        # Recorre la lista de usuarios para buscar el alias
        for i in range(len(usuarios)):
            if usuarios[i]["alias"] == alias_destino:
                encontrado = True
                usuario_destino = usuarios[i]

    # Busqueda por cbu
    elif opcion == "2":
        cbu_destino = input("Ingrese el CBU del destinatario: ")

        # Evita transferencia a uno mismo
        if cbu_destino == usuario_origen["cbu"]:
            print("No podés transferirte dinero a vos mismo.")
            return

        # Recorre la lista de usuarios para buscar el CBU
        for i in range(len(usuarios)):
            if usuarios[i]["cbu"] == cbu_destino:
                encontrado = True
                usuario_destino = usuarios[i]
    else:
        print("Opción inválida.")
        return

    # Si no se encontró ningún usuario
    if encontrado == False:
        print("No se encontró un usuario con ese alias o CBU.")
        return

    # Ingreso de monto con validacion de errores
    try:
        monto = float(input("Ingrese el monto a transferir: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return

    # Validar saldo
    if usuario_origen["saldo"] < monto:
        print("Saldo insuficiente para realizar la transferencia.")
        return

    print(f"Transferir ${monto:.2f} a {usuario_destino['nombre']} ({usuario_destino['alias']})")
    confirmar = input("¿Desea continuar? (S/N): ").upper()
    if confirmar != "S":
        print("Operación cancelada.")
        return

    # Actualizar datos
    usuario_origen["saldo"] = usuario_origen["saldo"] - monto
    usuario_destino["saldo"] = usuario_destino["saldo"] + monto

    guardar_usuarios(usuarios)

    print(f"✅ Transferencia realizada con éxito. Nuevo saldo: ${usuario_origen['saldo']:.2f}")
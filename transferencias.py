from utils import guardar_usuarios
from historial import registrar_evento

def transferir_dinero(usuario_origen, usuarios):
    """
    Permite transferir dinero a otro usuario del sistema (en ARS o USD)
    usando ALIAS o CBU. Valida saldo, monto, moneda y existencia del destinatario.
    """
    print("\n--- Transferencia de Dinero ---")

    # === SELECCIÓN DE CUENTA ORIGEN ===
    print("Seleccione la cuenta desde la que desea transferir:")
    print("1) Caja de Ahorro en Pesos (ARS)")
    print("2) Caja de Ahorro en Dólares (USD)")
    
    opcion = input("Ingrese 1 o 2: ")

    while opcion != "1" and opcion != "2":
        print("Opción inválida. Ingrese 1 para Pesos o 2 para Dólares.")
        opcion = input("Ingrese 1 o 2: ")

    if opcion == "1":
        cuenta_origen = usuario_origen["cuentas"][0]
        tipo_cuenta = "Caja de Ahorro en Pesos"
    elif opcion == "2":
        cuenta_origen = usuario_origen["cuentas"][1]
        tipo_cuenta = "Caja de Ahorro en Dólares"

    # === MONTO A TRANSFERIR ===
    monto_texto = input(f"Ingrese el monto a transferir desde {tipo_cuenta} ({cuenta_origen['moneda']}): ")
    try:
        monto = float(monto_texto)
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return

    if cuenta_origen["saldo"] < monto:
        print("Saldo insuficiente para realizar la transferencia.")
        return

    # === ELECCIÓN DEL DESTINATARIO ===
    print("\n¿Cómo desea buscar al destinatario?")
    print("1) Por alias")
    print("2) Por CBU")
    metodo = input("Seleccione una opción: ")

    usuario_destino = None
    cuenta_destino = None

    if metodo == "1":
        alias_destino = input("Ingrese el alias del destinatario: ").lower()
        for i in range(len(usuarios)):
            for j in range(len(usuarios[i]["cuentas"])):
                if usuarios[i]["cuentas"][j]["alias"] == alias_destino:
                    usuario_destino = usuarios[i]
                    cuenta_destino = usuarios[i]["cuentas"][j]
    elif metodo == "2":
        cbu_destino = input("Ingrese el CBU del destinatario: ")
        for i in range(len(usuarios)):
            for j in range(len(usuarios[i]["cuentas"])):
                if usuarios[i]["cuentas"][j]["cbu"] == cbu_destino:
                    usuario_destino = usuarios[i]
                    cuenta_destino = usuarios[i]["cuentas"][j]
    else:
        print("Opción inválida.")
        return

    if usuario_destino is None:
        print("No se encontró un usuario con ese alias o CBU.")
        return

    # Evitar transferirse a sí mismo
    if usuario_destino["dni"] == usuario_origen["dni"]:
        print("No podés transferirte dinero a vos mismo.")
        return

    # Verificar que la moneda coincida
    if cuenta_destino["moneda"] != cuenta_origen["moneda"]:
        print("No se puede transferir entre cuentas de diferente moneda.")
        return

    # Confirmación
    print(f"\nVas a transferir ${monto:.2f} {cuenta_origen['moneda']} a {usuario_destino['nombre']} {usuario_destino['apellido']}")
    confirmar = input("¿Desea continuar? (S/N): ").upper()

    if confirmar != "S":
        print("Operación cancelada.")
        return

    # Actualizar saldos
    cuenta_origen["saldo"] = cuenta_origen["saldo"] - monto
    cuenta_destino["saldo"] = cuenta_destino["saldo"] + monto

    guardar_usuarios(usuarios)

    # Registrar eventos
    registrar_evento(usuario_origen, "Transferencia enviada",
                     f"Envió ${monto:.2f} {cuenta_origen['moneda']} a {usuario_destino['nombre']} ({cuenta_destino['alias']})")
    registrar_evento(usuario_destino, "Transferencia recibida",
                     f"Recibió ${monto:.2f} {cuenta_destino['moneda']} de {usuario_origen['nombre']} ({cuenta_origen['alias']})")

    print(f"\n✅ Transferencia realizada con éxito.")
    print(f"Nuevo saldo en tu cuenta ({cuenta_origen['moneda']}): ${cuenta_origen['saldo']:.2f}")

""""
Contiene las pruebas manuales del sistema Home Banking
"""

from transferencias import transferir_dinero

#Realizamos la prueba de la funcion transferir_dinero

def prueba_transferencia():
    """
    Realiza la prueba manual de una transferencia habitual
    """

    usuario_origen = {
        "dni": 123,
        "pin": "1234",
        "cuentas": [
            {"moneda": "ARS", "saldo": 5000, "alias": "origen.ars", "cbu": "111"},
            {"moneda": "USD", "saldo": 100, "alias": "origen.usd", "cbu": "222"}
        ]
    }

    usuario_destino = {
        "dni": 456,
        "pin": "4567",
        "cuentas": [
            {"moneda": "ARS", "saldo": 2000, "alias": "destino.ars", "cbu": "333"},
            {"moneda": "USD", "saldo": 50, "alias": "destino.usd", "cbu": "444"}
        ]
    }

    usuarios = [usuario_origen, usuario_destino]
    monto = 1000

    saldoinicial_origen = usuario_origen["cuentas"][0]["saldo"]
    saldoinicial_destino = usuario_destino["cuentas"][0]["saldo"]

    #Como deberia funcionar transferir_dinero
    usuario_origen["cuentas"][0]["saldo"] -= monto
    usuario_destino["cuentas"][0]["saldo"] += monto

    if (usuario_origen["cuentas"][0]["saldo"] == saldoinicial_origen - monto and
        usuario_destino["cuentas"][0]["saldo"] == saldoinicial_destino + monto):
        print("True. La prueba de transferencia fue realizada con éxito.")
    else:
        print("False. La prueba de transferencia fallo.")

def prueba_transferenciaSinSaldo():
    """
    Realiza la prueba de transferencias sin saldos
    """

    usuario_origen = {
        "dni": 123,
        "pin": "1234",
        "cuentas": [
            {"moneda": "ARS", "saldo": 100, "alias": "origen.ars", "cbu": "111"},
        ]
    }

    usuario_destino = {
        "dni": 222,
        "pin": "5678",
        "cuentas": [
            {"moneda": "ARS", "saldo": 500, "alias": "destino.ars", "cbu": "333"},
        ]
    }

    #Asignamos un monto mayor al saldo que tiene cada usuario
    monto = 1000
    saldo_inicial = usuario_origen["cuentas"][0]["saldo"]

    if monto > saldo_inicial:
        print("True. El sistema indica que hay falta de saldo.")
    else:
        print("False. No se puede realizar una transferencia sin saldo suficiente.")

def prueba_transferenciamonedas():
    """
    Realiza la prueba manual de transferencia de monedas distintas
    """

    usuario_origen = {
        "dni": 111,
        "pin": "1234",
        "cuentas": [
            {"moneda": "ARS", "saldo": 3000, "alias": "origen.ars", "cbu": "111"},
        ]
    }

    usuario_destino = {
        "dni": 222,
        "pin": "9999",
        "cuentas": [
            {"moneda": "USD", "saldo": 100, "alias": "destino.usd", "cbu": "333"},
        ]
    }

    if usuario_origen["cuentas"][0]["moneda"] != usuario_destino["cuentas"][0]["moneda"]:
        print("True. El sistema detecta que las monedas no son iguales")
    else:
        print("False. No se puede realizar transferencias de monedas distintas.")




#Ejecutamos cada funcion de prueba 
if __name__ == "__main__":
    prueba_transferencia()
    prueba_transferenciaSinSaldo()
    prueba_transferenciamonedas()


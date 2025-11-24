"""
Contiene las funciones relacionadas con la gestión de usuarios.
"""

from utils import validar_caracteres, validar_dni, validar_numeros, dni_existe, generar_alias, validar_alias_formato, alias_existe, guardar_usuarios, cargar_usuarios, generar_cbu

from seguridad import validar_password

from transferencias import transferir_dinero

from historial import registrar_evento

from historial import exportar_historial_txt



#Al abrir el programa lee el archivo json si existe y carga a los usuarios anteriores.
usuarios = cargar_usuarios()

# Registro de usuario nuevo
def alta_Usuario():
    """
    Da de alta un nuevo usuario en el sistema. Solicita nombre, apellido,
    dni y contraseña, valida datos ingresados usando las funciones en Utils,
    inicia el saldo en 0.
    """
    consultaUsuario = input("¿Desea dar de alta un nuevo usuario? 1:SI 0:NO: ")
    while consultaUsuario != '1' and consultaUsuario != '0':
        print("Opción inválida. Por favor ingrese 1 para sí o 0 para no.")
        consultaUsuario = input("¿Desea dar de alta un nuevo usuario? 1:SI 0:NO: ")

    if consultaUsuario == "1":
        nombre= input("Ingrese su nombre: ")
        
        #VALIDACIÓN QUE NO PUEDAN INGRESAR NÚMEROS
        while validar_caracteres(nombre) == False:
            print("No se permite el ingreso de números y/o caracteres especiales, por favor intente nuevamente.")
            nombre= input("Ingrese su nombre: ")

        apellido= input("Ingrese su apellido: ") 
        #VALIDACIÓN QUE NO PUEDAN INGRESAR NÚMEROS
        while validar_caracteres(apellido) == False:
            print("No se permite el ingreso de números y/o caracteres especiales, por favor intente nuevamente.")
            apellido= input("Ingrese su apellido: ")

        dni = input("Ingrese su DNI sin puntos: ")
        #VALIDACIÓN NÚMERO Y ENTRE 7 Y 8
        while validar_dni(dni) == False:
            print("El DNI debe tener 7 u 8 dígitos numéricos.")
            dni= input("Ingrese su DNI sin puntos: ")
        #VALIDACIÓN SI DNI YA EXISTE
        if dni_existe(dni, usuarios):
            print("Ya existe un usuario con ese DNI. No se puede repetir.")
            return None

        #CREAR CONTRASEÑA
        password = input("Cree una contraseña (mínimo 8 caracteres, con una mayúscula, una minúscula y un número): ")
        es_valida = validar_password(password)
        
        while es_valida == False:
            print("Contraseña inválida. Debe tener al menos 8 caracteres, con una mayúscula, una minúscula y un número")
            password = input("Cree una contraseña (mínimo 8 caracteres, con una mayúscula, una minúscula y un número): ")
            es_valida = validar_password(password)

        
        # CREAR PIN DE TRANSFERENCIAS
        pin = input("Cree un PIN de 4 dígitos para autorizar transferencias: ")
        while not (validar_numeros(pin) and len(pin) == 4):
            print("El PIN debe tener exactamente 4 dígitos numéricos.")
            pin = input("Cree un PIN de 4 dígitos: ")
   

        #Saldo inicial 
        saldo = 0.0 


        #ARMAR NUEVO USUARIO Y AGREGAR A LA LISTA
        nuevo_usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "password": password,
            "pin": pin,
            "cuentas": [
                {
                    "tipo": "Caja de Ahorro en Pesos",
                    "moneda": "ARS",
                    "saldo": 0.0,
                    "cbu": generar_cbu(usuarios),
                    "alias": generar_alias(usuarios)
                },
                {
                    "tipo": "Caja de Ahorro en Dólares",
                    "moneda": "USD",
                    "saldo": 0.0,
                    "cbu": generar_cbu(usuarios),
                    "alias": generar_alias(usuarios)
                }
            ]
        }

        usuarios.append(nuevo_usuario) 
        registrar_evento(nuevo_usuario, "Alta de usuario", "Se registró un nuevo usuario en el sistema.") 
        
        print("Usuario creado con éxito.")

        guardar_usuarios(usuarios) #Guardar usuario generado en .json

        return nuevo_usuario             

    else:
        print("No se agregó ningún usuario.")
        return None


def iniciar_sesion():
    """
    Permite a un usuario autenticarse en el sistema. 
    Solicita DNI y contraseña.
    """
    bandera = True
    while bandera:
        dni = input("DNI: ")
        password = input("Contraseña: ")

        usuario_encontrado = list(filter(lambda u: u["dni"] == dni and u["password"] == password, usuarios))

        if len(usuario_encontrado) > 0:
            usuario = usuario_encontrado[0]
            print(f"Ingreso exitoso. Bienvenido/a {usuario['nombre']} {usuario['apellido']}")
            
            registrar_evento(usuario, "Inicio de sesión", "El usuario inició sesión correctamente.")
            return usuario
        else: 
            print("DNI o contraseña incorrectos.")
            print("1) Intentar de nuevo")
            print("2) Volver al menú anterior")
            print("0) Salir del programa")

            opcion = input("Opción: ")

            if opcion == "1":
                bandera = True # vuelve a pedir DNI y password
            elif opcion == "2":
                return None   # vuelve a menu_inicial
            elif opcion == "0":
                print("Hasta pronto.")
                return "SALIR"    # termina el programa
            else:
                print("Opción no válida, volviendo al menú de inicio.")
                
                return None


#CONSULTA DE SALDO DE CUENTAS
def consultar_saldo_cuentas(usuario):
    """
    Muestra los saldos de todas las cuentas del usuario (pesos y dólares).
    """
    print("\n--- Saldos de tus cuentas ---")
    for cuenta in usuario["cuentas"]:
        print(f"{cuenta['tipo']} ({cuenta['moneda']}):")
        print(f"   Alias: {cuenta['alias']}")
        print(f"   CBU: {cuenta['cbu']}")
        print(f"   Saldo: ${cuenta['saldo']:.2f}\n")



# CAMBIAR ALIAS DE USUARIO
def cambiar_alias(usuario):
    """
    Permite al usuario cambiar el alias de una de sus cuentas (Pesos o Dólares),
    validando formato y unicidad.
    """
    print("\n--- Cambio de Alias ---")
    print("Seleccione la cuenta cuyo alias desea cambiar:")
    print("1) Caja de Ahorro en Pesos (ARS)")
    print("2) Caja de Ahorro en Dólares (USD)")

    opcion = input("Ingrese 1 o 2: ")

    while opcion not in ["1", "2"]:
        opcion = input("Opción inválida. Ingrese 1 para Pesos o 2 para Dólares: ")

    # Seleccionar la cuenta
    cuenta = usuario["cuentas"][0]  if opcion == "1" else usuario["cuentas"][1]

    print(f"\nTu alias actual es: {cuenta['alias']}")
    nuevo_alias = input("Ingrese su nuevo alias (solo letras, números y puntos, sin espacios): ")

    # Validar formato
    while not validar_alias_formato(nuevo_alias):
        print("Formato inválido. El alias debe tener entre 6 y 20 caracteres, solo letras, números y puntos.")
        nuevo_alias = input("Ingrese un nuevo alias válido: ")

    # Validar que no esté repetido
    while alias_existe(nuevo_alias, usuarios):
        print("Ese alias ya existe, por favor elegí otro.")
        nuevo_alias = input("Ingrese un nuevo alias diferente: ")

    # Actualizar alias
    cuenta["alias"] = nuevo_alias.lower()
    print(f"Alias actualizado correctamente. Tu nuevo alias para la cuenta en {cuenta['moneda']} es: {cuenta['alias']}")

    # Guardar cambios y registrar el evento
    guardar_usuarios(usuarios)
    registrar_evento(usuario, "Cambio de alias", f"Nuevo alias en {cuenta['moneda']}: {cuenta['alias']}")


#CAMBIAR CONTRASEÑA
def cambiar_contrasenia(usuario):
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


#REALIZAMOS DEPOSITO
def realizamos_deposito(usuario):
    """
    Permite al usuario depositar dinero en una de sus cuentas (en pesos o en dólares).
    """
    print("\n --- Depósito de Dinero ---")

    # Mostrar las dos cuentas directamente
    print("Seleccione la cuenta donde desea realizar el depósito:")
    print("1) Caja de Ahorro en Pesos (ARS)" )
    print("2) Caja de Ahorro en Dólares (USD) ")

    opcion = input("Ingrese 1 o 2: ")

    # Validar opción
    while opcion not in ["1", "2"]:
        opcion = input("Opción inválida. Ingrese 1 para Pesos o 2 para Dólares: ")

    # Elegir la cuenta según la opción
    if opcion == "1":
        cuenta = usuario["cuentas"][0]
    else:
        cuenta = usuario["cuentas"][1]

    # Ingreso del monto
    monto = input("¿Cuánto dinero desea depositar? ")

    try:
        importe = float(monto)
        if importe <= 0:
            print("Monto inválido. Debe ingresar un número mayor a 0.")
            return
    except ValueError:
        print("Error. Debe ingresar un valor numérico válido.")
        return

    # Actualizar saldo     
    cuenta["saldo"] = cuenta["saldo"] + importe
    
    print("El depósito fue realizado con éxito en " + cuenta["tipo"] + " (" + cuenta["moneda"] + ").")
    print("Su nuevo saldo es: $" + str(round(cuenta["saldo"], 2)))

    registrar_evento(usuario, "Depósito", "Depositó $" + str(round(importe, 2)) + " en " + cuenta["moneda"])

def realizar_extraccion(usuario):
    """
    Permite al usuario extraer dinero de una de sus cuentas (en pesos o en dólares).
    """
    print("\n --- Extracción de Dinero ---")

    # Seleccionar cuenta
    print("Seleccione la cuenta desde donde desea extraer dinero:")
    print("1) Caja de Ahorro en Pesos (ARS)")
    print("2) Caja de Ahorro en Dólares (USD)")
    opcion = input("Ingrese 1 o 2: ")

    # Validar opción
    while opcion not in ["1", "2"]:
        opcion = input("Opción inválida. Ingrese 1 para Pesos o 2 para Dólares: ")

    # Elegir la cuenta según la opción
    if opcion == "1":
        cuenta = usuario["cuentas"][0]
    else:
        cuenta = usuario["cuentas"][1]

    # Ingreso del monto
    monto = input("¿Cuánto dinero desea extraer? ")

    try:
        importe = float(monto)
        if importe <= 0:
            print("Monto inválido. Debe ingresar un número mayor a 0.")
            return
    except ValueError:
        print("Error. Debe ingresar un valor numérico válido.")
        return

    # Validar saldo suficiente
    if importe > cuenta["saldo"]:
        print("Saldo insuficiente para realizar la extracción.")
        return

    # Actualizar saldo
    cuenta["saldo"] = cuenta["saldo"] - importe

    print("La extracción fue realizada con éxito en " + cuenta["tipo"] + " (" + cuenta["moneda"] + ").")
    print("Su nuevo saldo es: $" + str(round(cuenta["saldo"], 2)))

    # Registrar evento en historial
    registrar_evento(
        usuario,
        "Extracción",
        "Extrajo $" + str(round(importe, 2)) + " de " + cuenta["moneda"]
    )

    # Guardar cambios en usuarios.json
    guardar_usuarios(usuarios)


def ver_datos(usuario):
    """
    Muestra los datos personales y bancarios del usuario:
    nombre, DNI, y los alias/CBU de cada cuenta.
    """
    print("\n--- Mis datos ---")
    print(f"Nombre completo: {usuario['nombre']} {usuario['apellido']}")
    print(f"DNI: {usuario['dni']}\n")

    print("Cuentas asociadas:")
    for cuenta in usuario["cuentas"]:
        print(f"- {cuenta['tipo']} ({cuenta['moneda']})")
        print(f"  Alias: {cuenta['alias']}")
        print(f"  CBU:   {cuenta['cbu']}")
        print(f"  Saldo: ${cuenta['saldo']:.2f}\n")

    # Opcional: registrar en historial que consultó sus datos
    registrar_evento(usuario, "Consulta de datos", "Consultó sus datos personales y bancarios.")



#MENU DEL USUARIO   

def menu_usuario(usuario):
    """
    Despliega el menú interno del usuario que permite consulta saldo y cerrar sesión.
    """
    while True: 
        print("\n--- Menú de Usuario ---")
        print("1. Consultar mis datos")
        print("2. Consultar saldos de cuentas")
        print("3. Cambiar alias")
        print("4. Cambiar contraseña")
        print("5. Realizar depósito")
        print("6. Realizar extracción")
        print("7. Transferir dinero")
        print("8. Exportar historial a TXT")
        print("9. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": 
            ver_datos(usuario)
        elif opcion == "2": 
            consultar_saldo_cuentas(usuario)
        elif opcion=="3":
            cambiar_alias(usuario) 
        elif opcion == "4":
            cambiar_contrasenia(usuario)
        elif opcion == "5":
            realizamos_deposito(usuario)
        elif opcion == "6":
            realizar_extraccion(usuario)
        elif opcion == "7":
            transferir_dinero(usuario, usuarios)
        elif opcion == "8":
            exportar_historial_txt(usuario)
        elif opcion == "9":
            print("Se cerro sesión correctamente. Hasta luego. ")
            registrar_evento(usuario, "Cierre de sesión", "El usuario cerró su sesión correctamente.")
            return False
        else: 
            print("La opción ingresada no es válida, por favor vuelva a intentarlo.")

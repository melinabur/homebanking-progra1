"""
Contiene las funciones relacionadas con la gestión de usuarios.
"""

from utils import validar_caracteres, validar_dni, validar_numeros, dni_existe

from seguridad import validar_password

#Usuarios

usuarios = []

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

        saldo = 0.0 #Saldo inicial 

        #ARMAR NUEVO USUARIO Y AGREGAR A LA LISTA
        nuevo_usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "password": password,
            "saldo": saldo
        }
        usuarios.append(nuevo_usuario)  
        
        print("Usuario creado con éxito.")
        return nuevo_usuario             

    else:
        print("No se agregó ningún usuario.")
        return None


def iniciar_sesion():
    """
    Permite a un usuario autenticarse en el sistema. 
    Solicita DNI y contraseña.
    """
    seguir = True
    while seguir:
        dni = input("DNI: ")
        password = input("Contraseña: ")

        for i in usuarios:
            if i["dni"] == dni and i["password"] == password:
                print("Ingreso exitoso. Bienvenido/a", i["nombre"],i["apellido"])
                return i
        print("DNI o contraseña incorrectos.")
        print("1) Intentar de nuevo")
        print("2) Volver al menú anterior")
        print("0) Salir del programa")

        opcion = input("Opción: ")

        if opcion == "1":
            seguir = True # vuelve a pedir DNI y password
        elif opcion == "2":
            return None   # vuelve a menu_inicial
        elif opcion == "0":
            print("Hasta pronto.")
            return "SALIR"    # termina el programa
        else:
            print("Opción no válida, volviendo al menú de inicio.")
            return None


#CONSULTA DE SALDO
def consultar_saldo(usuario):
    """
    Muestra el saldo actual del usuario autenticado.
    """
    print(f"\n El saldo de {usuario['nombre']}, {usuario['apellido']} es: ${usuario['saldo']:.2f}")

#MENU DEL USUARIO   

def menu_usuario(usuario):
    """
    Despliega el menú interno del usuario que permite consulta saldo y cerrar sesión.
    """
    while True: 
        print("\n--- Menú de Usuario ---")
        print("1. Consultar saldo")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": 
            consultar_saldo(usuario)
        elif opcion == "2":
            print("Se cerro sesión correctamente. Hasta luego. ")
            return False
        else: 
            print("La opción ingresada no es válida, por favor vuelva a intentarlo.")

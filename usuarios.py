#Usuarios

usuarios = []

# Registro de usuario nuevo
def alta_Usuario():
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
        if dni_existe(dni):
            print("Ya existe un usuario con ese DNI. No se puede repetir.")
            return None

        #CREAR CONTRASEÑA
        password = input("Cree una contraseña (mínimo 6 caracteres): ")
        while len(password)< 6:
            print("La contraseña debe tener al menos 6 caracteres.")
            password = input("Cree una contraseña (mínimo 6 caracteres): ")

        #ARMAR NUEVO USUARIO Y AGREGAR A LA LISTA
        nuevo_usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "password": password,
        }
        usuarios.append(nuevo_usuario)  
        
        print("Usuario creado con éxito.")
        return nuevo_usuario             

    else:
        print("No se agregó ningún usuario.")
        return None


def iniciar_sesion():
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

#Validación ingreso solo caracteres, devuelve TRUE
def validar_caracteres(texto):
    if not texto: 
        return False
    for i in (texto):
        if not (i.isalpha() or i.isspace()):
            return False
    return True

#Validación ingreso solo números, devuelve TRUE
def validar_numeros(texto):
    return texto.isdigit()

#Validación dni entre 7 u 8 números
def validar_dni (dni):
    return validar_numeros(dni) and (len(dni) ==7 or len(dni)== 8)

#Validacion dni existente
def dni_existe(dni):
    for i in usuarios:
        if i["dni"] == dni:
            return True
    return False
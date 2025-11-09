#Menu Principal

""" 
Este módulo contiene el menú principal del sistema.

"""

from usuarios import alta_Usuario, iniciar_sesion, menu_usuario


def menu_inicial ():

    """
    Muestra el menú principal del sistema. Permite al usuario registrarse, 
    iniciar sesión o salir del sistema.

    """
    while True:
        print("\n=== Bienvenida/o al Home Banking ===")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("0) Cancelar")
        opcion = input("Opción: ")
        
        if opcion == "1":
            alta_Usuario()
        
        elif opcion == "2":
            usuario = iniciar_sesion()
            
            if usuario == "SALIR":
                return "SALIR"

            if usuario is not None:
                print("\nBienvenido al sistema,", usuario["nombre"], usuario["apellido"])
                print(f"Tu alias es: {usuario['alias']}")
                print(f"Tu CBU es: {usuario["cbu"]}")
                print(f"Tu saldo actual es: ${usuario['saldo']:.2f}")
                return menu_usuario(usuario)              

        elif opcion == "0":
            print ("Hasta pronto.")
            return "SALIR"
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

#main principal (invocamos todas las funciones)
def main():
    """
    Llama al menú inicial del sistema.
    """
    usario = menu_inicial()

if __name__ == "__main__":
    main()

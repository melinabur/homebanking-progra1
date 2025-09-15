#Menu Principal

from usuarios import alta_Usuario, iniciar_sesion


def menu_inicial ():
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
        elif opcion == "0":
            print("Hasta pronto.")
            return False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


#main principal (invocamos todas las funciones)
def main():
    user = menu_inicial ()

if __name__ == "__main__":
    main()
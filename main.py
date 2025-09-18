from usuarios import alta_Usuario, iniciar_sesion

def menu_inicial():
    usuario_registrado = False   

    while True:
        print("\n=== Bienvenida/o al Home Banking ===")

        if not usuario_registrado:   
            print("1) Registrarse")
            print("2) Iniciar sesión")
            print("0) Cancelar")

            opcion = input("Opción: ")

            if opcion == "1":
                alta_Usuario()
                usuario_registrado = True   

            elif opcion == "2":
                usuario = iniciar_sesion()
                if usuario == "SALIR":
                    return "SALIR"
                if usuario is not None:
                    print("\nBienvenido al sistema,", usuario["nombre"], usuario["apellido"])

            elif opcion == "0":
                print("Hasta pronto.")
                return "SALIR"

            else:
                print("Opción no válida. Por favor, intente nuevamente.")

        else:   
            print("1) Iniciar sesión")
            print("2) Cancelar")

            opcion = input("Opción: ")

            if opcion == "1":
                usuario = iniciar_sesion()
                if usuario == "SALIR":
                    return "SALIR"
                if usuario is not None:
                    print("\nBienvenido al sistema,", usuario["nombre"], usuario["apellido"])

            elif opcion == "2":
                print("Hasta pronto.")
                return "SALIR"

            else:
                print("Opción no válida. Por favor, intente nuevamente.")


# main principal
def main():
    menu_inicial()

if __name__ == "__main__":
    main()

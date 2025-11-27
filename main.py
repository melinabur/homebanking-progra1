#Menu Principal

""" 
Este módulo contiene el menú principal del sistema.

"""

from usuarios import alta_Usuario, iniciar_sesion, menu_usuario
from utils import cargar_usuarios

def menu_inicial (usuarios):

    """
    Muestra el menú principal del sistema. Permite al usuario registrarse, 
    iniciar sesión o salir del sistema.
    """
    while True:
        print("\n=== Bienvenida/o al Home Banking ===")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("0) Salir del programa")
        opcion = input("Opción: ")
        
        if opcion == "1":
            alta_Usuario()
        
        elif opcion == "2":
            usuario = iniciar_sesion()
            
            if usuario == "SALIR":
                return

            if usuario is not None:
                print("\nBienvenido al sistema,", usuario["nombre"], usuario["apellido"])
                
                sesion_activa = menu_usuario(usuario, usuarios)
                if sesion_activa is False:
                    print("\n--- Sesión cerrada correctamente. Volviendo al menú principal... ---")
                    continue #vuelve al menu inicial        

        elif opcion == "0":
            print ("Hasta pronto.")
            return #termina el programa
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

#main principal (invocamos todas las funciones)
def main():
    """
    Llama al menú inicial del sistema.
    """
    usuarios = cargar_usuarios()
    menu_inicial(usuarios)

if __name__ == "__main__":
    main()

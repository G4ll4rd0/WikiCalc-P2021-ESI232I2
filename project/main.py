from lib import menus
print(" - BIENVENIDO A WIKICALC - ")
opc = menus.mainMenu()

while opc != 4:
    if opc < 1 or opc > 4:
        print("Esa no es una opción valida, intente de nuevo")
        print("---------------------------------------------\n")
        opc = menus.mainMenu()
    if opc == 1:
        print("1. Mostrar todas las Funciones")
        break
    if opc == 2:
        print("2. Agregar una nueva Funcion")
        break
    if opc == 3:
        print("3. Modificar una Función")
        break

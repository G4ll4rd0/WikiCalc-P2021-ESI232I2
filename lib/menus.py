def mainMenu():
    print("1. Mostrar todas las Funciones")
    print("2. Agregar una nueva Funcion")
    print("3. Modificar una Función")
    print("4. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    if opc > 0 or opc < 5:
        return opc
    else:
        print("Esa no es una opción valida, intente de nuevo")
        print("---------------------------------------------\n")
        mainMenu()
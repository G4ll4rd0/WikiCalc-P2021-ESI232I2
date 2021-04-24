from lib import menus
from lib import latexParser
from lib import data
from lib import utilities
from lib import procedures

opc = menus.mainMenu()

while opc != 4:
    if opc < 1 or opc > 4:
        utilities.clear()
        print("Esa no es una opción valida, intente de nuevo")
        print("---------------------------------------------\n")
        opc = menus.mainMenu()
    if opc == 1:
        utilities.clear()
        opc = procedures.calcularFormula()
    if opc == 2:
        print("2. Agregar una nueva Funcion")
        break
    if opc == 3:
        print("3. Modificar una Función")
        break

utilities.clear()
print("Gracias por usar Wikicalc\n")
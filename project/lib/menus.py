from tabulate import tabulate

#Imprime el menú prinicpal del programa
def mainMenu():
    print(" - BIENVENIDO A WIKICALC - ")
    print("1. Usar una Función")
    print("2. Agregar una Funcion")
    print("3. Modificar una Función")
    print("4. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc

#Recupera las formulas de la db y genera una tabla, la cual imprime
def menuFormulas(fDict):
    table = []
    for i in fDict:
        row = []
        row.append(i['formulaNombre'])
        row.append(i['formulaLatex'])
        row.append(i['formulaTema'])
        row.append(i['formulaId'])
        table.append(row)
    print(tabulate(table, headers=['', 'Nombre', 'LaTeX', 'Tema', 'ID'], showindex=True))

#Cuando se decide calcular/modificar una formula se recupera y se muestra en pantalla
def unaFormula(fDict):
    table = []
    row = []
    row.append(fDict['formulaId'])
    row.append(fDict['formulaNombre'])
    row.append(fDict['formulaLatex'])
    row.append(fDict['formulaTema'])
    table.append(row)
    print(tabulate(table, headers=['ID', 'Nombre', 'LaTeX', 'Tema']))

#Despues de calcular una formula pregunta que quiere hacer a continuacion el usuario
def repeatFormulas():
    print(" - OPCIONES - ")
    print("1. Calcular Otra Formula")
    print("2. Volver al Menu")
    print("3. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc

#Despues de ingresar una formula pregunat que quiere hacer a continuacion
def repeatInsert():
    print(" - OPCIONES - ")
    print("1. Ingresar Otra Formula")
    print("2. Volver al Menu")
    print("3. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc

#Despues de modificar una formula pregunat que quiere hacer a continuacion
def repeatModify():
    print(" - OPCIONES - ")
    print("1. Modificar Otra Formula")
    print("2. Volver al Menu")
    print("3. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc
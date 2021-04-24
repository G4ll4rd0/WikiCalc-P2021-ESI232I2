from tabulate import tabulate

def mainMenu():
    print(" - BIENVENIDO A WIKICALC - ")
    print("1. Usar una función")
    print("2. Agregar una Funcion")
    print("3. Modificar una Función")
    print("4. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc

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

def unaFormula(fDict):
    table = []
    row = []
    row.append(fDict['formulaId'])
    row.append(fDict['formulaNombre'])
    row.append(fDict['formulaLatex'])
    row.append(fDict['formulaTema'])
    table.append(row)
    print(tabulate(table, headers=['ID', 'Nombre', 'LaTeX', 'Tema']))

def repeatFormulas():
    print(" - OPCIONES - ")
    print("1. Calcular Otra Formula")
    print("2. Volver al Menu")
    print("3. Salir")
    opc = int(input("Ingrese el numero de opción: "))
    return opc
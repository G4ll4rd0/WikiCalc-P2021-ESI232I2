from lib import data, menus, latexParser, utilities
from time import sleep
import sys

#Esta funcion se utiliza para llenar variables y obtener resultados
def obtainResult(formula, variables):
    #Se mandan llenar las variables y luego a evualar la operación
    result = latexParser.evalFormula(formula, variables)
    return result

#Esta funcion se manda ejecutar cuando se quiere calcular una formula
def calcularFormula():
    #Se obtienen as formulas y se imprimen con ayuda del menu
    print(' -- FORMULAS -- \n\n')
    fDict = data.allFormulas()
    menus.menuFormulas(fDict)
    #Una vez que se sabe que formula se va a usar se manda solicitar el objeto de esa
    fId = int(input('\nInserte el ID de la formula que desea calcular: '))
    form = data.getFormula(fId)
    #Se limpia la pantalla y se imprime un nuevo menu, en esta ocasion con solo la formula necesaria
    utilities.clear()
    menus.unaFormula(form)
    variables = data.fillVariables(form)
    form1 = form["formulaLatex"]
    form2 = form["formulaLatex"]
    #! Este pedazo añade soporte para el caso de que exista un \pm en la formula
    if str(form["formulaLatex"]).find(r"\pm") != -1:
        form1 = form1.replace(r"\pm", "+")
        form2 = form2.replace(r"\pm", "-")
        #Se manda obtener el resultado 1
        result = obtainResult(form1, variables)
        #Ya que se obtiene el resultado, se imprime y se espera antes de pasar al siguiente paso
        print("\n\n El resultado 1 es: ", result)
        #Se manda obtener el resultado 2
        result = obtainResult(form2, variables)
        #Ya que se obtiene el resultado, se imprime y se espera antes de pasar al siguiente paso
        print("\n\n El resultado 2 es: ", result)
    else:
        #Se manda obtener el resultado
        result = obtainResult(form1, variables)
        #Ya que se obtiene el resultado, se imprime y se espera antes de pasar al siguiente paso
        print("\n\n El resultado es: ", result)
    sleep(2)
    #Se imprime un menu para saber que es lo siguiente que quiere hacer el usuario, ya sea calcular otra formula, pasar a otra parte del menú o salir del programa
    num = menus.repeatFormulas()
    while num < 1 or num >3:
        utilities.clear()
        print("Esa no es una opción valida, intente de nuevo")
        print("---------------------------------------------\n")
        num = menus.repeatFormulas()
    if num == 1:
        opc = 1
    elif num == 2:
        utilities.clear()
        opc = menus.mainMenu()
    elif num == 3:
        opc = 4
    return opc

#Esta funcion se manda llamar cuando se va a agregar una nueva función
def agregarFormula():
    print(" -- AGREGAR FORMULAS -- \n\n")
    #?Para la API se necesita poner 0 en el Id cuando se quiere ingresar una nueva
    formulaId = "0"
    #Se solicitan los datos necesarios para ingresar la funcion
    formulaNombre = input("Ingrese el nombre de la formula: ")
    formulaLatex = input("Ingrese la formula en formato LaTeX(recuerde poner las variables precedidas de apostrofes): ")
    formulaTema = input("Ingrese el tema al que pertenece la formula: ")
    formulaVariables = input("Ingrese las variables separadas por comas y precedidas por apostrofes: ")
    #Se manda llamar la funcion que inserta la nueva formula y se gurada el resultado
    checkBool = data.saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables)
    #Si el resultado de la funcion es verdadero se manda a llamar el menu para saber que quiere hacerel usuario a continuacion ya sea ingresar otra formula, pasar a otra parte del menú o salir del programa
    if checkBool:
        print("\n\nGracias por ingresar esa formula")
        num = menus.repeatInsert()
        while num < 1 or num >3:
            utilities.clear()
            print("Esa no es una opción valida, intente de nuevo")
            print("---------------------------------------------\n")
            num = menus.repeatInsert()
        if num == 1:
            opc = 2
        elif num == 2:
            utilities.clear()
            opc = menus.mainMenu()
        elif num == 3:
            opc = 4
    #Si el resultado es Falso significa que hubo un problema y se tiene que repetir el proceso
    else:
        print("\n\nHubo un error al intentar agregar la formula, revise los datos e intente de nuevo") 
        input("Presione la tecla ENTER para continuar  ")
        opc = 2
    return opc

#Esta función se manda llamar cuando se quiere modificar una función
def modificarFormula():
    print(" -- MODIFICAR FORMULAS -- \n\n")
    #Se imprimen las formulas para que el usuario vea cual quiere modificar
    fDict = data.allFormulas()
    menus.menuFormulas(fDict)
    #una vez que se sabe que formula se va a usar se manda solicitar el objeto de esa
    fId = int(input('\nInserte el ID de la formula que desea Modificar: '))
    form = data.getFormula(fId)
    #Se limpia la pantalla y se imprime un nuevo menu, en esta ocasion con solo la formula necesaria
    utilities.clear()
    menus.unaFormula(form)
    #Se solicitan los datos necesarios para modificar la funcion
    formulaId = str(fId)
    formulaNombre = input("Ingrese el nombre de la formula: ")
    formulaLatex = input("Ingrese la formula en formato LaTeX(recuerde poner las variables precedidas de apostrofes): ")
    formulaTema = input("Ingrese el tema al que pertenece la formula: ")
    formulaVariables = input("Ingrese las variables separadas por comas y precedidas por apostrofes: ")
    #Se manda llamar la funcion que inserta la nueva formula y se gurada el resultado
    checkBool = data.saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables)
    #Si el resultado de la funcion es verdadero se manda a llamar el menu para saber que quiere hacerel usuario a continuacion ya sea ingresar otra formula, pasar a otra parte del menú o salir del programa
    if checkBool:
        print("\n\nGracias por ingresar esa formula")
        num = menus.repeatModify()
        while num < 1 or num >3:
            utilities.clear()
            print("Esa no es una opción valida, intente de nuevo")
            print("---------------------------------------------\n")
            num = menus.repeatModify()
        if num == 1:
            opc = 3
        elif num == 2:
            utilities.clear()
            opc = menus.mainMenu()
        elif num == 3:
            opc = 4
    #Si el resultado es Falso significa que hubo un problema y se tiene que repetir el proceso
    else:
        print("\n\nHubo un error al intentar modificar la formula, revise los datos e intente de nuevo") 
        input("Presione la tecla ENTER para continuar  ")
        opc = 3
    return opc
from lib import data, menus, latexParser, utilities
from time import sleep
import sys

def calcularFormula():
    print(' -- FORMULAS -- \n\n')
    fDict = data.allFormulas()
    menus.menuFormulas(fDict)
    fId = int(input('\nInserte el ID de la formula que desea calcular: '))
    form = data.getFormula(fId)
    utilities.clear()
    menus.unaFormula(form)
    variables = data.fillVariables(form)
    result = latexParser.evalFormula(form['formulaLatex'], variables)
    print("\n\n El resultado es: ", result)
    sleep(2)
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

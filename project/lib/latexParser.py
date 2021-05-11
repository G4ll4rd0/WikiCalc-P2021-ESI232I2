from pylatexenc.latex2text import LatexNodes2Text
import math

constantes = [["'pi", "math.pi"], ["'e", "math.e"], ["'g", "9.81"]]

#Esta funcion recibe una string en latex y la convierte en una string en texto plano
def latexToPlainText(latex):
    text = LatexNodes2Text().latex_to_text(latex)
    return text

#Esta funcion es para convertir simbolos/operaciones antes de pasarlo a texto plano
def latexToLatexFormula(latex):
    text = latex
    #TODO: Hay que llenar todo este
    #? Esta lista reemplaza todos aquelos que no son operaciones basicas, por su correspondiente formula en python
    formulas = [[r"\sqrt", "math.sqrt"], ["^", "**"]]
    for i,j in formulas:
        text = text.replace(i, j)
    text = latexToPlainText(text)
    return text

# Esta funcion obtiene el texto en latex, usa las otras funciones para obtener la formula en texto y luego reemplaza los valores de las variables en la ecuación para finalmente evaluarla en int
def evalFormula(latex, variables):
    f2Eval = latexToLatexFormula(latex)
    for i, j in variables:
        #Teniendo la lista de variables la iteramos para ir cambiando de una por una
        f2Eval = f2Eval.replace(i, j)
    for i, j in constantes:
        #Teniendo las constantes conocidas se reemplazan
        f2Eval = f2Eval.replace(i, j)
    #Usamos el comando eval para obtener el numero de respuesta
    result = eval(f2Eval)
    return result

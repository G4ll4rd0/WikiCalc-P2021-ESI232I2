from pylatexenc.latex2text import LatexNodes2Text
import math

#Esta funcion recibe una string en latex y la convierte en una string en texto plano
def latexToPlainText(latex):
    text = LatexNodes2Text().latex_to_text(latex)
    return text

#Esta funcion es para convertir simbolos/operaciones antes de pasarlo a texto plano
def latexToLatexFormula(latex):
    text = latex
    #TODO: Hay que llenar todo este
    formulas = [[r"\sqrt", "math.sqrt"], ["^", "**"]]
    for i,j in formulas:
        text = text.replace(i, j)
    text = latexToPlainText(text)
    return text

# Esta funcion obtiene el texto en latex, usa las otras funciones para obtener la formual en texto y luego reemplaza los valores de las variables en la ecuación para finalmente evaluarla en int
def evalFormula(latex, variables):
    f2Eval = latexToLatexFormula(latex)
    for i, j in variables:
        f2Eval = f2Eval.replace(i, j)
    result = eval(f2Eval)
    return result

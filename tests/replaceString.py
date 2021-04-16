from pylatexenc.latex2text import LatexNodes2Text
import math

#Se usa la funcion de la libreria para parsearlo
#? Sera mejor la libreria de https://github.com/JelteF/PyLaTeX ???
latex = r"\frac {-b \pm \sqrt({b^2 - 4xc})}{2x}"
latex2 = latex.replace(r"\sqrt", "math.sqrt")

formula1 = latex2.replace(r"\pm", "+")
formula2 = latex2.replace(r"\pm", "-")


text1 = LatexNodes2Text().latex_to_text(formula1)

print(text1)

#Se reemplazan 
tx = str(text1).replace("b", "(2)")
tx = tx.replace("x", "(1)")
tx = tx.replace("c", "(3)")

print(tx)

textInt = eval(tx)

print(textInt)

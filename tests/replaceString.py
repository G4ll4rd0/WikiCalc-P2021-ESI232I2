from pylatexenc.latex2text import LatexNodes2Text
import math

#Se usa la funcion de la libreria para parsearlo
latex = r"\frac {(-b \pm \sqrt({b^2 - 4*x*c}))}{2*x}"

#TODO: Ya que se construya la funcion en la carperta de librerias se tiene que hacer un diccionario con las diversas funiones necesarias
#TODO: de math, o calculo para reemplazarlas con un ciclo, aqui se ejemplifica por fines practicos
latex2 = latex.replace(r"\sqrt", "math.sqrt")
latex2 = latex2.replace("^", "**")

#! Tambien se tiene que agregar simbolos como el \pm
formula1 = latex2.replace(r"\pm", "+")
formula2 = latex2.replace(r"\pm", "-")

#Se usa la funcion de la libreria para convertirlo en una cadena d etexto tipo: (-b + math.sqrt(b**2 - 4*x*c))/2*x
text1 = LatexNodes2Text().latex_to_text(formula1)
text2 = LatexNodes2Text().latex_to_text(formula2)

print(text1)
print(text2)

#Se usa un diccionario para las variables
#TODO: En las librerias se tiene que hacer una funcion para crear/llenar esta lista
variables = [["x", "(1)"], ["b", "(2)"], ["c", "(-3)"]]

#Se usa un ciclo de este tipo para reemplazar las variables por números
for i,j in variables:
    text1 = text1.replace(i,j)
    text2 = text2.replace(i,j)

print(text1)
print(text2)

#Con eval convertimos de nuestra string tipo: (-(2) + math.sqrt((2)**2 - 4*(1)*(-3)))/2*(1) a un entero
textInt1 = eval(text1)
textInt2 = eval(text2)

print("x1 = ", textInt1)
print("x2 = ", textInt2)

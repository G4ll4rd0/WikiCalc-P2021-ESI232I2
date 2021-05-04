import urllib.request 
import json
from lib import latexParser
import requests

#Esta es la url basica para acceder a la API
#! Todas las funciones obtienen un json, por lo que usamos la libreria nativa de python para convertirlo en un diccionario y poderlo manipular. 
#? Se regresan diccionarios al mandar ejecutarlas
ip = "http://localhost:8080/wikicalc/ws/formulas/"

#Esta funcion recupera las formulas ordenadas por Tema (en orden alfabetico)
def allFormulas():
    url = urllib.request.Request(ip + "byTheme")
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

#Esta funcion nos permite obtener una formula en especifico para manipularla/evaluarla
#? Se tiene que mandar llamar esta funcion con el valor de la propiedad "formulaId" de la formula que deseemos
def getFormula(id):
    url = (ip + "get?keyId=" + str(id))
    url = urllib.request.Request(url)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

#A esta funcion se le manda el diccionario que recuperamos de la funcion getFormula() para proceder a completar las variables, 
#obtendremos una nueva lista que tendra nuestros valores y nuestras variables, esta lista hay que enviarla al parser
def fillVariables(fDict):
    #Se recuperan la cadena de etxto que tiene los nombres de las variables
    variables = fDict["formulaVariables"]
    #Se separan por variables 
    listaVariables = variables.split(",")
    listaValores = []
    #Se usa el cilo para crear la lista 2D
    for i in listaVariables:
        n = input("Valor de " + i + ": ")
        listaValores.append([i, n])
    return listaValores

#Esta funcion sirve para guardar una nueva formula en la db, hay que mandarle los parametros que requiere.
def saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables):
    #Se crea un diccionario con las propiedades y se convierte en un json para mandarlo
    data = {}
    data['formulaId']         = formulaId
    data['formulaNombre']     = formulaNombre
    data['formulaLatex']      = formulaLatex
    data['formulaTema']       = formulaTema
    data['formulaVariables']  = formulaVariables
    url = ip + "insert"
    send = json.dumps(data)
    response = requests.post(url, send)
    resp = response.json()
    return resp

#print(allFormulas())
#print(saveFormula(r"\frac {(-b - \sqrt({b^2 - 4*x*c}))}{2*x}", "FGN", "ZZZ", "x,b,c"))
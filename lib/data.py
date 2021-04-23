import urllib.request 
import json
import latexParser
import requests

ip = "https://app.solucionesenjambre.com/ws/formulas/"

def allFormulas():
    url = urllib.request.Request(ip + "byTheme")
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def getFormula(id):
    url = (ip + "get?keyId=" + id)
    url = urllib.request.Request(ip + "get?keyId=" + id)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def fillVariables(fDict):
    variables = fDict["formula_Variables"]
    listaVariables = variables.split(",")
    listaValores = []
    for i in listaVariables:
        n = input("Valor de " + i + ": ")
        listaValores.append([i, n])
    return listaValores

def saveFormula(formulaLatex, formulaNombre, formulaTema, formulaVariables):
    answer = False
    data = {}
    data['formulaId']         = "0"
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
print(saveFormula(r"\frac {(-b - \sqrt({b^2 - 4*x*c}))}{2*x}", "Formula General N", "Algebra3", "x,b,c"))
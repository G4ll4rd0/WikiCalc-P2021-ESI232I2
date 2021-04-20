from urllib.request import urlopen, HTTPError, pathname2url
import json

ip = "solucionesenjambre.com/wikicalc/ws/"

def allFormulas():
    url = ip + "byTheme"
    response = urlopen(url)
    data = json.loads(response.read())
    return data

def getFormula(id):
    url = ip + "get?keyId=" + id
    response = urlopen(url)
    data = json.loads(response.read())
    data = json.loads(data)
    return data

def fillVariables(fDict):
    variables = fDict["formula_Variables"]
    listaVariables = variables.split(",")
    listaValores = []
    for i in listaVariables:
        n = input("Valor de " + i + ": ")
        listaValores.append([i, n])
    return listaValores
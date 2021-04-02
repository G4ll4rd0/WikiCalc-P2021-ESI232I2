#Funcion que sirve para separar la cadena de texto en un arreglo bidimensional en las que cada elemento sea un parentesis y los subelementos sean las operaciones a realizar
#TODO: Que sucede cuando hay multiples parentesis?
def separarParentesis():
    #En nuestra cadena de ejemplo: (\div\sum)\sum(\mult\res)
    cadena = input("Cadena: ")
    listaCadena = []

    #Este ciclo separa en unidades de parentesis para que quede de la forma: ['\\div\\sum', '\\sum', '\\mult\\res']
    for i in range(len(cadena)):
        #Selleciona el interior de un parentesis para asignarlo como un item: \div\sum
        if cadena[i] == "(":
            x = cadena[i+1:]
            #//print("1: ", x)
            j = x.find(")")
            x = x[:j]
            #//print("2: ", x)
            listaCadena.append(x)
        #Selecciona las partes externas de los parentesis para que quede como unidad: \sum
        elif cadena[i] == ")":
            x = cadena[i+1:]
            #//print("1: ", x)
            j = x.find("(")
            x = x[:j]
            #//print("2: ", x)
            listaCadena.append(x)

    listaCadena.remove("")

    #//print(listaCadena)

    listaCadena2 = []

    #Se separan los items en operaciones para que quede un arreglo bidimensional de la forma: [['div', 'sum'], ['sum'], ['mult', 'res']]
    for i in listaCadena:
        x = i.split("\\")
        x.remove("")
        listaCadena2.append(x)

    return listaCadena2

#se manda llamar la funcion para ejemplificar su uso
print(separarParentesis())
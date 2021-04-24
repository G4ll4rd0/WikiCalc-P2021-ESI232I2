#Se intenta dividir la cadena en listas por parentesis y luego por diagonales
cadena = input("ingrese cadena: ")

#Se eliminan los primeros parentesis y se vuelve a juntar todo en una sola cadena
listaCadena = cadena.split("(")
listaCadena.remove("")
print("Original: ", cadena)
print("Primera Separacion: ", listaCadena)

#Se junta todo en una nueva cadena y a partir de esta se genera otro split, para obtener en items separados parentesis separados
'''
cadena2 = "".join(listaCadena)
listaCadena2 = cadena2.split(")")
listaCadena2.remove("")
print("Segunda Cadena: ", cadena2)
print("Segunda Separacion: ", listaCadena2)
'''

listaCadena2 = []

for i in listaCadena:
    x = i.split(")")
    listaCadena2.append(x)

print("Segunda Separacion: ", listaCadena2)

#Se genera un arreglo bidimensional siendo cada item de la 1D un parentesis
listaCadena3 = []

for i,j in listaCadena2:
    print(i)
    x = j.split("\\")
    x.remove("")
    listaCadena3.append(x)

print("Tercera Separacion: ", listaCadena3)
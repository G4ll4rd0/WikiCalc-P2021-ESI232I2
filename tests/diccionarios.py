#Se solicitan dos numeros
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))

#Una lista bidfimensional que posee la operacion que se debe mandar a llamar, el nombre de la operacion y la sintaxis con la que se le ingresa
operaciones = [
    ["\div", "división", x1/x2],
    ["\mult", "multiplicación", x1*x2],
    ["\sum", "suma", x1+x2],
    ["\minus", "resta", x1-x2]
]

opcion = input("Que desea Realizar? ")

#Iteramos el arreglo 2D hasta dar con la opcion que cuadre con lo que hemos ingresado, una vez ahi imprimeremos el nombre de la funcion y el resultado de la misma
for x,i,j in operaciones:
    if (x) == opcion:
        print(i,j)

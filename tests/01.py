import operacionesBasicas.operaciones.division
import operacionesBasicas.operaciones.multiplicacion
import operacionesBasicas.operaciones.suma
import operacionesBasicas.operaciones.resta

x1 = int(input("x1 = "))
x2 = int(input("x2 = "))

operaciones = [
    ["\div", "división", operacionesBasicas.operaciones.division.division(x1,x2)],
    ["\mult", "multiplicación", operacionesBasicas.operaciones.multiplicacion.multiplicacion(x1,x2)],
    ["\sum", "suma", operacionesBasicas.operaciones.suma.suma(x1,x2)],
    ["\minus", "resta", operacionesBasicas.operaciones.resta.resta(x1,x2)]
]

opcion = input("Que desea Realizar? ")

for x,i,j in operaciones:
    if (x) == opcion:
        print(i,j)

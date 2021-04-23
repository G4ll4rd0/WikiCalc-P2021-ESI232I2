import asyncio

#Funcion para establecer el resultado de la operacion que deseamos
async def setAfter(r, x1, x2, opc):
    #Arreglo bidimensional con el nombre comun de la operacion y la funcion que la realiza
    operaciones = [
    ["\div", "división", x1/x2],
    ["\mult", "multiplicación", x1*x2],
    ["\sum", "suma", x1+x2],
    ["\minus", "resta", x1-x2]
]


    #Ciclo para obtener el resultado de la operacion que deseamos
    for i,j in operaciones:
        if i == opc:
            n = j

    #Se fija el resultado de lo que hemos solicitado
    r.set_result(n)

#Funcion Principal
async def main():
    #Se le solicita al usario las operaciones que desea realizar y en caso de que sea mas de una se separa en una lista que luego usaremos para ir resolviendo
    #TODO: FALTA AGREGAR SOPORTE PARA PARENTESIS Y O JERARQUIA DE OPERACIONES, AHORITA HACE TODO LINEAL
    #?Se esta trabajando con un ejemplo de parentesis en el archivo de doubleSplitting.py
    opcion = input("Que desea Realizar? ")

    opc = opcion.split("\\")
    opc.remove("")
    
    #Asignamos un contador para saber si tendremos que pedir mas de un valor 
    contador = 0

    #Se crea un looppara nuestra funcion asincronica
    loop = asyncio.get_running_loop()

    #Lista bidimensional con los nombres ocmunes de las operaciones y la sintaxis con la que queda separada
    operaciones = [
        ["div", "división"],
        ["mult", "multiplicación"],
        ["sum", "suma"],
        ["minus", "resta"]
    ]

    #Se itera primero la lista de operaciones que quiere realizar el usuario
    for h in opc:
        #Dentro de esta iteramos nuesro diccionario de operaciones
        for x,i in operaciones:
            #Si el item de la lista de operaciones a realizar concuerda con el item de la lista de operaciones posibles, se manda obtener ese resultado
            if x == h:
                #Solo la primera vez que se ejecute deberemos de solicitar el primer numeo, luego solo sera el segundo ya que el resultado anterior fungira como el primero
                if contador == 0:
                    x1 = int(input("x1: "))
                x2 = int(input("x2: "))
                #Creamos nuestro objeto que sera completado en un futuro
                r = loop.create_future()
                #Mandamos obtener el resultado con esta funcion, pasandole el nombre de la operacion a realizar, ambos números, y nuestro objeto futuro
                loop.create_task(setAfter(r, x1, x2, i))
                #imprimimos el nombre de la operacion que acabamos de realizar y esperamos el resultado de nuestro objeto futuro
                print(i, await r)
                #Asignamos nuesro resultado como el valor de la primera x y sumamos uno al contador para no tener que volver a pedir el primer numero
                x1 = await r
                contador += 1

#Se manda llamar la funcion principal
asyncio.run(main())
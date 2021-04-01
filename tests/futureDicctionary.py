import operacionesBasicas.operaciones.division
import operacionesBasicas.operaciones.multiplicacion
import operacionesBasicas.operaciones.suma
import operacionesBasicas.operaciones.resta
import asyncio

async def setAfter(r, x1, x2, opc):
    operaciones = [
        ["división", operacionesBasicas.operaciones.division.division( x1,  x2)],
        ["multiplicación", operacionesBasicas.operaciones.multiplicacion.multiplicacion( x1,  x2)],
        ["suma", operacionesBasicas.operaciones.suma.suma( x1,  x2)],
        ["resta", operacionesBasicas.operaciones.resta.resta( x1,  x2)]
    ]

    for i,j in operaciones:
        if i == opc:
            n = j

    r.set_result(n)

async def main():
    opcion = input("Que desea Realizar? ")

    opc = opcion.split("\\")
    opc.remove("")
    
    contador = 0

    loop = asyncio.get_running_loop()

    operaciones = [
        ["div", "división"],
        ["mult", "multiplicación"],
        ["sum", "suma"],
        ["minus", "resta"]
    ]

    for h in opc:
        for x,i in operaciones:
            if x == h:
                if contador == 0:
                    x1 = int(input("x1: "))
                x2 = int(input("x2: "))
                r = loop.create_future()
                loop.create_task(setAfter(r, x1, x2, i))
                print(i, await r, "     ", contador+1)
                x1 = await r
                contador += 1

asyncio.run(main())
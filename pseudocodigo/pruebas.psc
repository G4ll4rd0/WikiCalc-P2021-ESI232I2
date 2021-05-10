Funcion menuFormulas(fDict)
	Dimension table[2,5]
	table[1,1] = ["ID"]
	table[1,2] = ["Nombre"]
	table[1,3] = ["LaTeX"]
	table[1,4] = ["Tema"]
	table[1,5] = ["Variables"]
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		table[2,i] = fDict[i]
	Fin Para
	Para fila <- 1 Hasta 2 Con Paso 1 Hacer
		row = ""
		Para columna <-1 Hasta 5 Con Paso 1 Hacer
			row = row + table[fila,columna] + "    "
		Fin Para
		Escribir row
	Fin Para
FinFuncion

Algoritmo pruebas
	Dimension prueba[5]
	prueba[1] = "1"
	prueba[2] = "Prueba"
	prueba[3] = "\frac{a}{b}"
	prueba[4] = "Temazo"
	prueba[5] = "a,b"
	menuFormulas(prueba)
FinAlgoritmo	
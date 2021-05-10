Funcion python(nombre_funcion)
	Escribir 'Funcion de Python(',nombre_funcion,')'
FinFuncion

Funcion clear
	python('system(cls)')
FinFuncion

Funcion data <- allFormulas()
	url = "https://app.solucionesenjambre.com/ws/formulas/" + "byTheme"
	//Estas funciones encodean en formato url nuestra url y reciben el objeto json que esta escupe
	python("url = urllib.request.Request(" + url + ")")
	python("response = urllib.request.urlopen( url )")
	python("data = json.loads(response.read())")
	//Se devuelve un data falso para poder probar el resto de la funcionalidad
	Dimension data[5]
	data[1] = "1"
	data[2] = "Prueba"
	data[3] = "\frac{a}{b}"
	data[4] = "Tema Prueba"
	data[5] = "a,b"
FinFuncion

Funcion data <- getFormula(id)
	url = "https://app.solucionesenjambre.com/ws/formulas/" + "get?keyId=" + id
	//Estas funciones encodean en formato url nuestra url y reciben el objeto json que esta escupe
	python("url = urllib.request.Request(" + url + ")")
	python("response = urllib.request.urlopen( url )")
	python("data = json.loads(response.read())")
	//Se devuelve un data falso para poder probar el resto de la funcionalidad
	Dimension data[5]
	data[1] = "1"
	data[2] = "Prueba"
	data[3] = "\frac{a}{b}"
	data[4] = "Tema Prueba"
	data[5] = "a,b"
FinFuncion

Funcion listaValores <- fillVariables(fDict)
	variables = fDict[5]
	//En python se usa la siguiente funcion, aqui se va a crear uno para poder completar nuestra prueba
	python("listaVariables = variables.split(,)")
	Dimension listaVariables[2]
	listaVariables[1] = "a"
	listaVariables[2] = "b"
	//La lista de valores se crea dinamicamente en un arreglo 2D aqui se crea fija
	Dimension listaValores[2,2]
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Escribir "Valor de " + listaVariables[i] + ": "
		Leer n
		python("listaValores.append([i,n])")
		listaValores[i,1] = listaVariables[i]
		listaValores[i,2] = n
	Fin Para
FinFuncion

Funcion resp <- saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables)
	//En python esto se construye en un diciionario para luego convertirlo en un json que se postea ,aqui es una array para que exista
	Dimension data[5]
	data[1] = formulaId
	data[2] = formulaNombre
	data[3] = formulaLatex
	data[4] = formulaTema
	data[5] = formulaVariables
	url = "https://app.solucionesenjambre.com/ws/formulas/" + "insert"
	python("send = json.dumps(data)")
	python("response = requests.post(url, send)")
	python("resp = response.json()")
	//Esta funcion devuelve un booleano, aqui se devuelve uno verdadero para continuar
	resp = Verdadero
FinFuncion

Funcion text <- latexToPlainText(latex)
	python("text = LatexNodes2Text().latex_to_text(latex)")
	//Aqui se devolveria el texto ya parseado, como no se puede hacer se envia lo que se recibe
	text = latex
FinFuncion

Funcion text <- latexToLatexFormula(latex)
	text = latex
	Dimension formulas[2,2]
	formulas[1,1] = "\sqrt"
	formulas[1,2] = "math.sqrt"
	formulas[2,1] = "^"
	formulas[2,2] = "**"
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Para j<-1 Hasta 2 Con Paso 1 Hacer
			python("text = text.replace(i, j)")
		Fin Para
	Fin Para
	text = latexToPlainText(text)
FinFuncion

Funcion result <- evalFormula(latex, variables)
	f2Eval = latexToLatexFormula(latex)
	//En python se reemplazan las variables con los valores obtenidos
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		python("f2Eval = f2Eval.replace(i, j)")
	Fin Para
	python("result = eval(f2Eval)")
	result = f2Eval
FinFuncion

Funcion result <- obtainResult(form)
	variables = fillVariables(form)
	result = evalFormula(form[3], variables)
FinFuncion

Funcion opc <- mainMenu()
	Escribir (' - BIENVENIDO A WIKICALC - ')
	Escribir ('1. Usar una función')
	Escribir ('2. Agregar una Funcion')
	Escribir ('3. Modificar una Función')
	Escribir ('4. Salir')
	Escribir ('Ingrese el numero de opción: ')
	Leer opc
FinFuncion

//Aqui se pone nomas con una tabla de dos filas para ver como funciona en python se construye dependiendo de la cantidad de resultados que se tienen, aqui se usara la misma funcion para imprimir una o más funciones, en python se hacen 2 por la naturaleza del objeto que se recupera
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
	//SE USA ESTE TIPO DE PRINT PARA QUE SALGA COMO TABLA
	Para fila <- 1 Hasta 2 Con Paso 1 Hacer
		row = ""
		Para columna <-1 Hasta 5 Con Paso 1 Hacer
			row = row + table[fila,columna] + "    "
		Fin Para
		Escribir row
	Fin Para
FinFuncion

Funcion opc <- repeatFormulas()
	Escribir(" - OPCIONES - ")
	Escribir("1. Calcular Otra Formula")
	Escribir("2. Volver al Menu")
	Escribir("3. Salir")
	Escribir "Ingrese el numero de opción: "
	Leer opc
FinFuncion

Funcion opc <- repeatAgregarFormulas()
    Escribir (" - OPCIONES - ")
    Escribir ("1. Ingresar Otra Formula")
    Escribir ("2. Volver al Menu")
    Escribir ("3. Salir")
    Escribir ("Ingrese el numero de opción: ")
    Leer opc
FinFuncion

Funcion opc <- repeatModificarFormulas()
    Escribir (" - OPCIONES - ")
    Escribir ("1. Modificar Otra Formula")
    Escribir ("2. Volver al Menu")
    Escribir ("3. Salir")
    Escribir ("Ingrese el numero de opción: ")
    Leer opc
FinFuncion

Funcion opc <- calcularFormula()
	Escribir " -- FORMULAS -- "
	fDict = allFormulas()
	menuFormulas(fDict)
	Escribir "Inserte el ID de la formula que desea calcular"
	Leer fId
	form = getFormula(fId)
	clear()
	menuFormulas(form)
	result = obtainResult(form)
	Escribir "El resultado es: " + result
	python("sleep(2)")
	num = repeatFormulas()
	Mientras num < 1 o num > 3 Hacer
		clear()
		Escribir("Esa no es una opción valida, intente de nuevo")
		Escribir("---------------------------------------------\n")
		num = repeatFormulas()
	Fin Mientras
	Segun num Hacer
		1:
			opc = 1
		2:
			clear()
			opc = mainMenu()
		3:
			opc = 4
		De Otro Modo:
			
	Fin Segun
FinFuncion

Funcion opc <- agregarFormula()
	Escribir " -- AGREGAR FORMULAS -- "
	formulaId = 0
	Escribir "Ingrese el nombre de la formula: "  Sin Saltar
	Leer formulaNombre
	Escribir "Ingrese la formula en formato LaTeX: "  Sin Saltar
	Leer formulaLatex
	Escribir "Ingrese eltema de la formula: "  Sin Saltar
	Leer formulaTema
	Escribir "Ingrese las variables de la formula separadas por comas: "  Sin Saltar
	Leer formulaVariables
	checkBool = saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables)
	Si checkBool Entonces
		Escribir "Gracias por añadir esta formula"
		num = repeatAgregarFormulas()
		Mientras num < 1 o num > 3 Hacer
			clear()
			Escribir("Esa no es una opción valida, intente de nuevo")
			Escribir("---------------------------------------------\n")
			num = repeatAgregarFormulas()
		Fin Mientras
		Segun num Hacer
			1:
				opc = 2
			2:
				clear()
				opc = mainMenu()
			3:
				opc = 4
			De Otro Modo:
				
		Fin Segun
	SiNo
		Escribir "Hubo un error al intentar agregar la formula, revise los datos e intente de nuevo"
		Escribir "Presione la tecla ENTER para continuar"
		Leer x
		opc = 2
	Fin Si
FinFuncion

Funcion opc <- modificarFormula()
	Escribir " -- MODIFICAR FORMULAS -- "
	fDict = allFormulas()
	menuFormulas(fDict)
	Escribir "Inserte el ID de la formula que desea modificar"
	Leer fId
	form = getFormula(fId)
	clear()
	menuFormulas(form)
	formulaId = fId
	Escribir "Ingrese el nombre de la formula: "  Sin Saltar
	Leer formulaNombre
	Escribir "Ingrese la formula en formato LaTeX: "  Sin Saltar
	Leer formulaLatex
	Escribir "Ingrese eltema de la formula: "  Sin Saltar
	Leer formulaTema
	Escribir "Ingrese las variables de la formula separadas por comas: "  Sin Saltar
	Leer formulaVariables
	checkBool = saveFormula(formulaId, formulaLatex, formulaNombre, formulaTema, formulaVariables)
	Si checkBool Entonces
		Escribir "Gracias por modificar esta formula"
		num = repeatModificarFormulas()
		Mientras num < 1 o num > 3 Hacer
			clear()
			Escribir("Esa no es una opción valida, intente de nuevo")
			Escribir("---------------------------------------------\n")
			num = repeatModificarFormulas()
		Fin Mientras
		Segun num Hacer
			1:
				opc = 3
			2:
				clear()
				opc = mainMenu()
			3:
				opc = 4
			De Otro Modo:
				
		Fin Segun
	SiNo
		Escribir "Hubo un error al intentar modificar la formula, revise los datos e intente de nuevo"
		Escribir "Presione la tecla ENTER para continuar"
		Leer x
		opc = 3
	Fin Si
FinFuncion

Algoritmo main
	opc <- mainMenu()
	Mientras opc <> 4 Hacer
		Segun opc  Hacer
			1:
				clear()
				opc = calcularFormula()
			2:
				clear()
				opc = agregarFormula()
			3:
				clear()
				opc = modificarFormula()
			De Otro Modo:
				clear()
				Escribir ('Esa no es una opción valida, intente de nuevo')
				Escribir ('---------------------------------------------\n')
				opc <- mainMenu()
		FinSegun
	FinMientras
	clear()
	Escribir 'Gracias por usar WikiCalc\n'
FinAlgoritmo

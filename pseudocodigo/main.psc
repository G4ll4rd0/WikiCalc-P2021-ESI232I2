Funcion python(nombre_funcion)
	Escribir 'Funcion de Python(',nombre_funcion,')'
FinFuncion

Funcion clear
	python('system(cls)')
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

Funcion opc <- repeatFormulas()
	Escribir(" - OPCIONES - ")
	Escribir("1. Calcular Otra Formula")
	Escribir("2. Volver al Menu")
	Escribir("3. Salir")
	Escribir "Ingrese el numero de opción: "
	Leer opc
FinFuncion

Funcion opc <- calcularFormula()
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

Funcion agregarFormula()
	
FinFuncion

Funcion modificarFormula()
	
FinFuncion

Algoritmo main
	opc <- mainMenu()
	Mientras opc<>4 Hacer
		Segun opc  Hacer
			1:
				clear()
				calcularFormula()
			2:
				clear()
				agregarFormula()
			3:
				clear()
				modificarFormula()
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

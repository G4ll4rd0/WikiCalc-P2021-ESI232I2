Funcion python(nombre_funcion)
	Escribir 'Funcion de Python(',nombre_funcion,')'
FinFuncion

SubProceso  opc <- mainMenu()
    Escribir (" - BIENVENIDO A WIKICALC - ")
    Escribir ("1. Usar una funci�n")
    Escribir ("2. Agregar una Funcion")
    Escribir ("3. Modificar una Funci�n")
    Escribir ("4. Salir")
    Escribir ("Ingrese el numero de opci�n: ")
	Leer opc
FinSubProceso


Algoritmo main
	opc = mainMenu()
	Mientras opc <> 4 Hacer
		Segun opc Hacer
			1:
				Escribir "1"
			2:
				Escribir "3"
			3:
				Escribir "2"
			De Otro Modo:
				python('system(cls)')
				Escribir ("Esa no es una opci�n valida, intente de nuevo")
				Escribir ("---------------------------------------------\n")
				opc = mainMenu()
		Fin Segun
	Fin Mientras
	
	python('system(cls)')
	Escribir 'Gracias por usar WikiCalc\n'
FinAlgoritmo

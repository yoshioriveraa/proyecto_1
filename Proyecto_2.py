Iniciacion=input("¿Quieres que se inicia la calculadora?, escriba si o no:")

if Iniciacion == "si":
	a=int(input("Ingrese el primer número:"))
	b=int(input("Ingrese el segundo número:"))
	operacion = input("Elija una opcion: x, /, +, -   :")

	if operacion == "x":
		multiplicacion = a * b
		print("El resultado es :", multiplicacion)
	elif operacion == "/":
		division = a / b
		print("El resultado es :", division)
	elif operacion == "+":
		suma = a + b
		print("El resultado es :", suma)
	elif operacion == "-":
		resta = a - b
		print("El resultado es :", resta)
	else:
		print("Eligio la opcion equivocada")
else:
	print("Gracias")

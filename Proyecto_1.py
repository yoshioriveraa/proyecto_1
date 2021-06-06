import random
import time
start = str(input("Ingresa el operador para la practica: "))

if start == "suma":
	i=0
	while i<5: #Se repetirá por 5 veces
		i+=1
		numeros ="1234567890"
		digitos = 1
		a="".join(random.sample(numeros,digitos)) #Número aleatorio
		b="".join(random.sample(numeros,digitos))
		print(int(a), "+",int(b))
		time.sleep(5) # 5 segundos se demora
		print(int(a) + int(b))
		time.sleep(2)

if start == "multiplicacion":
	i=0
	while i<3: #Se repetirá por 3 veces
		i+=1
		numeros ="123456789"
		digitos = 1
		a="".join(random.sample(numeros,digitos)) #Número aleatorio
		b="".join(random.sample(numeros,digitos))
		print(int(a), "x",int(b))
		time.sleep(8) # 8 segundos se demora
		print(int(a) * int(b))
		time.sleep(2)



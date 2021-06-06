import random
import time
start = str(input("Ingresa el operador para la practica: "))

if start == "suma":
	i=0
	while i<5:
		i+=1
		numeros ="1234567890"
		digitos = 1
		a="".join(random.sample(numeros,digitos))
		b="".join(random.sample(numeros,digitos))
		print(int(a), "+",int(b))
		time.sleep(5)
		print(int(a) + int(b))
		time.sleep(2)

if start == "resta":
	i=0
	while i<5:
		i+=1
		numeros ="123456789"
		digitos = 1
		a="".join(random.sample(numeros,digitos))
		b="".join(random.sample(numeros,digitos))
		print(int(a), "-",int(b))
		time.sleep(5)
		print(int(a) - int(b))
		time.sleep(2)



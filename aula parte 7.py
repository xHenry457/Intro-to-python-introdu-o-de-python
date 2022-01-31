import random # numeros aleatorios

numero = random.randint(0,10)
print(numero)

lista = [6,45,9]
numero = random.choice(lista)
print(numero)


""" Exceções"""

a = 2
b = 0

try:
	print (a/b)

except:
	print("nao e permitida divisao por 0")

print(a/a)		





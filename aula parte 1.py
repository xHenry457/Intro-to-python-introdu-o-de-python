# isto é um comentário #

print ("olá mundo")
print ("Outra mensagem")
print ("mensagem 3")

# isto é um comentario #

print ("nova linha")

"""comentarios
de
muitas
linhas
"""
# -*- coding: utf-8 -*- comprender acentos #

# operaçoes matematicas #
print(2+2)
print (2-1)
print (3*5)
print (2 / 2)
print (2 ** 3) # exponencial
print (10 % 3) # modulo

# variáveis #

minha_variavel = "olá mundo"
print (minha_variavel)
print (minha_variavel)
print (minha_variavel)

var1 = 1 # variável inteira 
var2 = 1.1 # variável float 
var3 = "Eu sou uma string"  # variável textual(string) 
var4 = True # Verdadeiro
var4 = False # Falsa

print(var1)
print(var2)
print(var3)
print(var4)

# Operadores Lógicos e relacionais #

# == Igual
# !=  Diferente
# >  Maior
# <  Menor
# >=  Maior ou igual
# <= Divisão

x = 2
y = 3

x == y 
print(x == y)

soma = x + y 
print(soma == x)

# operadores lógicos

# and = duas condições sejam verdadeiras
# or = pelo menos uma condição é verdadeira
# not = inverte o valor

x = 3
y = 3
z = 4


print(x == y and x == z)
print(x == y or x == z)
print(x == y or x == z and z == y)

# Comandos Condicionais

# -*- coding: utf-8 -*-
x = 1
y = 1000000

"""if =  executa um bloco SE uma determinada condição for atendida, 
avalia se a condição é verdadeira ou não."""

if x > y:
	print("x é maior que y")

if y > x:
	print("y é maior que x")

""" ELSE = É EXECUTADO caso a condição
do comando if não seja atendida"""	

# -*- coding: utf-8 -*-

x = 1
y = 2

if x > y:
	print ("x maior que y")
else:
	print("x não é maior que y")

""" ELIF = Caso haja necessidade de mais condições
 entre o if e o else"""

 # -*- coding: utf-8 -*-

x = 1
y = 2

if x == y:
	print(" numeros iguais")
elif y > x:
	print("y maior que x")
else:
	print("numeros diferentes")	

# while = repetitivo
x = 1

while x < 10:
	print(x)
	x += 1  # x = x = 1


"""for = para fazer laços pre com condições pre determinadas para varrer
 o conjunto de elementos"""

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99,True]

for i in lista3:
	print(i)

""" Range ela retorna uma lista """

for i in range(10,20):
	print(i)	
































































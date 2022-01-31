""" strings é um tipo de dados em que se
 armazena coleções de caracteres(texto)

 # -*- coding: utf-8 -*-

 variavel_1 = "ola, "
 variavel_2 = "mundo"

 concatenacao = variavel_1 + variavel_2
 print concatenacao"""

a = "Diego"
b = "Mariano"

concatenar = a + " " + b
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print(concatenar[0:5]) #imprimi ate onde eu quiser a palavra


"""strings = em python, strings são objetos
pode-se aplicar métodos a strings
string = string.método() """

print(concatenar)
print(concatenar.lower()) # deixar em minisculo
print(concatenar.upper()) # maisculo

""" caracter especial "/n" para quebrar ele e só usar o .strip()"""


minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ")
print(minha_lista)

busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:]) #continua de onde fez a busca


minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)




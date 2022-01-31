""" Listas

Representam conjunto de dados 
pode ser

- numérica: [1,2,3,4,5]
-strings: ["bola","sapato","chuva"]"""

minha_lista = ["abacaxi", "melancia", "abacate"]
print(minha_lista)

minha_lista2 = [1,2,3,4,5]
print(minha_lista2)

minha_lista_3 = ["abacaxi", 2, 9.89, True]
print(minha_lista_3)

print(minha_lista[0]) 

for item in minha_lista: # item por item
	print(item)

tamanho = len(minha_lista) # saber o tamanho da lista
print(tamanho)	

minha_lista.append("limao") # adcionar a lista
print(minha_lista)

if 3 in minha_lista2: # ve se esta incluso na lista
	print("3 esta na lista")

del minha_lista[2:]
print(minha_lista)	

minha_lista_4 = []  # criar uma lista
minha_lista_4.append(57) #adciona item na lista
print(minha_lista_4)

"""-----------------------------------------------------"""

lista = [124,345,5,72,46,6,7,3,1,7,0] 
lista.sort() # ordenar a lista
print(lista)

lista_2 = [124,345,5,72,46,6,7,3,1,7,0] 
sorted(lista_2) 
print(lista_2)

lista.sort(reverse=True) # orderna decrescente
print(lista)

lista.reverse() # reversão da lista
print(lista)

lista3 = ["bola", "abacate", "dinheiro"]
lista3.sort()
print(lista3)

# list comprehernsion

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)


a = [1, 2, 3, 4, 5]
b = [i**2 for i in a]

print("usando list comprehension")
print(a)
print(b)

"""enumerate"""

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i,lista[i])

for i, nome in enumerate(lista):
    print(i, nome)

# Função map

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#zip

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista_3 = ["R$ 2,00", "R$ 5,00", "nao tem preco", "nao tem preco", "nao tem preco" ]

for numero, nome, valor in zip(lista_1, lista_2, lista_3):
    print(numero, nome, valor)

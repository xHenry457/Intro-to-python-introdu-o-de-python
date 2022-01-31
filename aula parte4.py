""" Manipulando Arquivos
Função Open
Variavel = Open(nome, modo)

R = somente leitura
W = escrita(caso o arquivo ja exista, sera aagado e um novo
arquivo vazio sera criado)
A = leitura e escrita (adciona o novo conteuúdo ao fim do arquivo)
r+ = leitura e escrita
w+ = escrita( o modo w_, assim como o w, também apaga o conteúdo
anterior do arquivo)
a+ = leitura e escrita(abre o arquivo para atualização)


Read() = Lê arquivo inteiro
Readline() = Lê uma linha
Readlines() = Lê o arquivo e armazena em uma lista"""

arquivo = open("arquivo.txt")

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
	print(linhas)
#                            


arquivo = open("arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)

w = open ("arquivo2.txt", "a")
w.write("esse eh o meu arquivo\n")
w.close()


 
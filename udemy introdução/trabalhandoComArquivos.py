# -*- coding: utf-8 -*-

# ABRINDO ARQUIVOS

# FUNÇÃO OPEN
# variavel = open(nome do arquivo, modo)

'''
MODOS
r - somente leitura (default)
w - escrita (caso o arquivoi já exista, ele será apagado e um novo arquivo vazio será criado)
a - leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
r+ - leitura e escrita
w+ - escrita (o modo w+, assim como o w, também apaga o conteudo anterior do arquivo)
a+ - leitura e escrita (abre o arquivo para atualização)
'''
arquivo = open("arquivo.txt") # arquivo já criado anteriormente

# LENDO ARQUIVOS JÁ CRIADOS
'''
read() - le arquivo inteiro
readline() - lê uma linha
readlines() - lê arquivo e o armazena em uma lista
'''
linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print(linha)

textoCompleto = arquivo.read()
print(textoCompleto)


# CRIANDO ARQUIVOS NOVOS
w = open("arquivo2.txt", "w") # cria um novo arquivo e se ja existir apaga o que tem nele

#ESCREVER NO ARQUIVO
w.write("Esse e o meu arquivo\n")
# Toda vez que abre o arquivo deve fecha-lo apos usar
w.close()

w = open("arquivo2.txt", "a") # a vai adicionar as informações no fim do arquivo
w.write("Esse e o meu arquivo\n")
w.close()
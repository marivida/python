# imprimir uma lista ao mesmo tempo que obtem os indices de cada elemento

lista = ["abacate", "bola", "cachorro"]

for i in lista:
    print(i) # imprime todos os nomes

for i in range(len(lista)):
    print(i, lista[i]) # imprime os nomes e os indices

# usando a função enumerate
for i, nome in enumerate(lista): # i vai ser o indice e nome o nome
    print(i, nome)


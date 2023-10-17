# concatena uma lista com outra, compacta duas ou mais listas juntas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 5,00", "Nao tem preço", "Depende", "Muito"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
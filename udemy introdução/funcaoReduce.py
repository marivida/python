# recebe uma lista e retorna apenas um unico valor pra essa lista, por exemplo o valor da soma dos itens de uma lista

from functools import reduce 

def soma(x, y):
    return x + y

lista = [1, 3, 5, 10, 20]

soma = reduce(soma, lista) # função desejada e lista a ser aplicada, no caso dessa função x seria cada elemento dal ista e y seria a soma ja feita
print(soma)

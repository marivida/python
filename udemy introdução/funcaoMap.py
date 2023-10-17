# pegar uma função e aplicar a todos os elementos de uma lista

def dobro(x):
    return x*2

valor = 2
print(dobro(valor), "\n")

valor = [1, 2, 3, 4, 5]

valorDobrado = map(dobro, valor) # recebe primeiro a função e depois a lista a ser aplicada

# for v in valorDobrado:
#     print(v)

valorDobrado = list(valorDobrado)
print("\n", valorDobrado)


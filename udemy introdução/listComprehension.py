x = [1, 2, 3, 4, 5]

# y = [] # quero na lista y todos os numeros de x elevado ao quadrado
# for i in x:
#     y.append(i**2)
# print(x)
# print(y)

# y = [valorAAdicionar laço condição]
y = [i**2 for i in x] # aqui nãoo houve condição (i** 2 = valor a add) (for i in x = laço)
print(x)
print(y)

z = [i for i in x if i%2 == 1] # adicionar a lista apenas numeros impares
print(z)

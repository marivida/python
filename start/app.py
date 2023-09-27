# print("Hello World")

# age = 20
# print("Age: ", age)

# age = 30
# print("Age: ", age)

# price = 19.95
# first_name = "Mariana"
# is_online = False

# # We check in a patient named John Smith
# # He is 20 years old
# # HE is a new pacient
# name = "John Smith"
# age = 20
# new_pacient = True

# if new_pacient:
#     word = 'novo'
# else: 
#     word = 'habitual'

# print("Este é um paciente ", word, ". Ele tem ", age, " anos e se chama ", name)


# #RECEBENDO INPUTS
# name = input("Whats is your name? ")
# print("Hello "+ name)


# #TYPE CONVERSION
# birth_year = input("Enter yourbirth year: ")
# age = 2023 - int(birth_year)
# print("Idade: ", age)
# #float()    bool()   int()   str()
# number1 = float(input("First number: "))
# number2 = float(input("Second number: "))
# sum = number1 + number2
# print("Sum: " + str(sum))


# #STRINGS
# course = "Python for Beginners"
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.find('y')) #acha o index da letra, case sensitive, então diferencia maiusculas de minusculas
# print(course.find('Y'))
# print(course.find('for'))
# print(course.replace('for', '4'))
# print('Python' in course) # checar se tem a palavara "Python" na variavel course


# #ARITHMETIC OPERATORS
# print(10 + 3) #adição
# print(10 - 3) #subtração
# print(10 * 3) #multiplicaçao
# print(10 / 3) #divisão pegando numeros após a virgula
# print(10 // 3) #divisão, resultado mostra apenas o numero inteiro
# print(10 % 3) #módulo, mostra o resto da divisão
# print(10 ** 3) #expoente, 10 elevado a 3
# x = 10
# x += 3 #-= | *= | /=
# print("x:", x)


# #OPERATOR PRECEDENCE
# 1. * e /
# 2. + e -


# #COMPARISON OPERATORS
# x = 3 > 2
# print(x)
# # < | >= | <= | != | ==


# #LOGICAL OPERATORS
# price = 5
# print(price > 10 and price < 30) #TRUE se ambas as condições forem verdadeiras
# print(price > 10 or price < 30) #TRUE se ao menos uma das condições forem verdadeiras
# print(price > 10 )
# print(not price > 10 ) #nega a condição


# #IF STATEMENTS
# temperature = 9
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20: # (20, 30], de 21 a 30
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")


# #EXERCISE
# weight = float(input("Weight: "))
# measure = input("(K)g or (L)bs: ")
# if measure.lower() == 'k':
#     weightLbs = weight / 0.45
#     print("Weight in Lbs: ", weightLbs)
# elif measure.lower() == 'l':
#     weightkg = weight * 0.45
#     print("Weight in Kgs: " + str(weightkg))
# else:
#     print("ERROR")


# # WHILE LOOPS
# i = 1
# while i <= 10:
#     print(i * '*') # multiplicar um numero por uma string, essa string aparecerá o tanto de vezes do numero que valer
#     i += 1


# # LISTS - definida entre []
# names = ["John", "Bob", "Dean", "Sam", "Mary"]
# print(names)
# print(names[0])
# print(names[-1]) # ultimo elemento da lista, numeros negativos vc começa a contar do fim
# print(names[-2])
# names[0] = "Jon"
# print(names)
# print(names[0:3]) # vc só quer ver alguns elementos da lista, vc coloca o primeiro e o ultimo index que quer ver, excluindo o ultimo index


# # LIST METHODS
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) # adiciona um item ao fim da lista
# print(numbers)
# numbers.insert(0, -1) # adiciona um item no idex 0 (<index>, <item a ser add>)
# print(numbers)
# numbers.remove(3) # remove um numero em especifico da lista
# print(numbers)
# # numbers.clear() # limpa a lista toda
# # print(numbers)
# print(1 in numbers) # verifica se o numero 1 esta nesta lista de numeros
# print(len(numbers)) # verifica quantos elementos tem na lista


# #FOR LOOPS
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# for item in numbers:
#     print(item)


# #THE RANGE() FUNCTION - para gerar uma sequencia de numeros
# numbers = range(5) #gera uma lista de numeros de 0 a 4
# print(numbers)
# for number in numbers:
#     print(number)
# numbers = range(5, 10) #gera uma lista de numeros de 5 a 9
# for number in numbers:
#     print(number)
# numbers = range(5, 10, 2) #gera uma lista de numeros de 5 a 9, pulando de 2 em 2
# for number in numbers:
#     print(number)
# for number in range(10, 21):
#     print(number)


# #TUPLES - não podem ser mudadas deposi de criadas, definidas entre ()
# numbers = (1, 2, 3)
# print(numbers)


word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print (paragraph)


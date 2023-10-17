# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
sinal = input("Digite a operação desejada (+ | - | * | /):")

match sinal:
    case "+":
        print("Soma: ", n1, " + ", n2, " = ", n1+n2)
    case "-":
        print("Subtração: ", n1, " - ", n2, " = ", n1-n2)
    case "*":
        print("Multiplicação: ", n1, " * ", n2, " = ", n1*n2)
    case "/":
        print("Divisão: ", n1, " / ", n2, " = ", n1/n2)
    case _:
        print("Operação inválida. Tente novamente!")
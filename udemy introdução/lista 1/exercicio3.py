# Escreva um programa que resolva uma equação de segundo grau.  

import math

def calcularDelta (a, b, c):
    return b**2 - (4*a*c)

def calcularX1(a, b, delta):
    raiz = math.sqrt(delta)
    return (-b - raiz)/(2*a)

def calcularX2(a, b, delta):
    raiz = math.sqrt(delta)
    return (-b + raiz)/(2*a)

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = calcularDelta(a, b, c)
x1 = calcularX1(a, b, delta)
x2 = calcularX2(a, b, delta)

print("Soluçoes da equação: ", x1, " e ", x2)


###Proyecto calculadora
###Margarita Giron Chanez
from math import sqrt
import math
def S(a, b):
    return a + b
def R(a, b):
    return a - b
def M(a, b):
    return a * b
def D(a, b):
    return a / b
def Z(a):
    return sqrt(n1)
while True:
    print("***Menú***")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz")
    print("6. Exponente")
    print("7. Seno")
    print("8. Salir")
    opc = input("Ingresa una opción: ")
    if opc == "1":
        n1 = float(input("Ingresa el número 1: "))
        n2 = float(input("Ingresa el número 2: "))
        print("La suma es: ", S(n1, n2))
    elif opc == "2":
        n1 = float(input("Ingresa el número 1: "))
        n2 = float(input("Ingresa el número 2: "))
        print("La resta es: ", R(n1, n2))
    elif opc == "3":
        n1 = float(input("Ingresa el número 1: "))
        n2 = float(input("Ingresa el número 2: "))
        print("La división es: ", M(n1, n2))
    elif opc == "4":
        n1 = float(input("Ingresa el número 1: "))
        n2 = float(input("Ingresa el número 2: "))
        print("La multiplicación es: ", D(n1, n2))
    elif opc == "5":
        num = float(input("Ingresa el número para obtener la raíz: "))
        raiz = sqrt(num)
        print("La raíz es: ", raiz)
    elif opc == "6":
        base = int(input("Ingresa la base: "))
        exponente = int(input("Ingresa el exponente: "))
        resultado = 1
        i = 0
        while True:
               if exponente == 0:
                 print("El resultado es 1: ")
                 break
               resultado = base * resultado
               i = i + 1
               if i >= abs(exponente):
                 if exponente < 0:
                   resultado = 1 / resultado
                 print("El resultado es: ", resultado)
                 break
    elif opc == "7":
        rad = input("Ingresa el número: ")
        s1 = float(rad)
        s2 = math.radians(s1)
        print("El seno del número es: ", math.sin(s2))
    elif opc == "8":
        print("¡Hasta luego!")
        break
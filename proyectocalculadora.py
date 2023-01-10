def S(a, b):
    return a + b
def R(a, b):
    return a - b
def M(a, b):
    return a * b
def D(a, b):
    return a / b
while True:
    print("Menú")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opc = input("Ingresa una opción: ")
    n1 = float(input("Ingresa el número 1: "))
    n2 = float(input("Ingresa el número 2: "))
    if opc == "1":
        print("La suma es: ", S(n1, n2))
    elif opc == "2":
        print("La resta es:", R(n1, n2))
    elif opc == "3":
        print("La división es:", M(n1, n2))
    elif opc == "4":
        print("La multiplicación es", D(n1, n2))
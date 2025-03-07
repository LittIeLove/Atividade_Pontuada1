import os
os.system("clear || cls")

#Entrada de dados

n1 = int(input("Digite o número A: "))
n2 = int(input("Digite o número B: "))
forma = str(input("Digite a forma de cálculo: "))

#saida de dados

if forma == "+":
    print(f"A soma de {n1} + {n2} é igual a {n1 + n2}")
elif forma == "-":
    print(f"A subtração de {n1} - {n2} é igual a {n1 - n2}")
elif forma == "*":
    print(f"A multiplicação de {n1} * {n2} é igual a {n1 * n2}")
elif forma == "/":
    print(f"A divisão de {n1} / {n2} é igual a {n1 / n2}")
else:
    print("Operação inválida")
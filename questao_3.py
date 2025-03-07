import os
os.system ("clear || cls")
n1 = int(input("Digite o numero A: "))
n2 = int(input("Digite o numero B: "))

if n1 == n2:
    s = n1 + n2
    print(f"A soma dos numeros é: {s} ")

else:
    s = n1 * n2
    print(f"A multiplicação dos numeros é: {s} ")


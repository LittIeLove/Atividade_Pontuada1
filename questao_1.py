import os
os.system ("clear || cls")

#Entrada de dados
n1 = float(input("Digite o número A : "))
n2 = float(input("Digite o número B : "))
n3 = float(input("Digite o número C : "))

s = n1 + n2

os.system ("clear || cls")
#Saida de dados
if s < n3:
    print(f"A soma dos numero A ({n1}) e B ({n2}) é menor que C ({n3})")

elif s == n3:
    print(f"A soma de A ({n1}) + B ({n2}) e igual a C ({n3}) ")

else:
    print(f"A soma dos números A ({n1}) e B ({n2}) é maior que C ({n3})")
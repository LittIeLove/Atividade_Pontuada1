import os
os.system("clear || cls")

#Entrada de dados

kgmo = float(input("Digite quantos KG de morangos você ira levar: "))
kgma = float(input("Digite quantos KG de maçãs você ira levar: "))
if kgmo <= 5:
    preco_mo = 2.50
else:
    preco_mo = 2.20

if kgma <= 5:
    preco_ma = 1.80
else:
    preco_ma = 1.50

valormo = kgmo * preco_mo
valorma = kgma * preco_ma
valorkgtotal = valormo + valorma
kgtotal = kgmo + kgma

#saida de dados

if valorkgtotal >= 50 or kgma >= 8:
    desconto = valorkgtotal * 0.10
    valorkgtotal = valorkgtotal - desconto
print(f"O valor total a ser pago é de R${valorkgtotal:.2f}")
print(f"Você comprou {kgtotal} KG de frutas")
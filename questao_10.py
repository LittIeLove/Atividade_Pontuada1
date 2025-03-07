import os
os.system ("clear || cls")
print(""" 
==========POSTO DE COMBUSTIVEL PREÇOS==========

A = Álcool  3.79R$
G = Gasolina 6.59R$ """)
#Entrada de dados
comb = input("Digite o tipo de combustivel que deseja abastecer: ").upper()
litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
os.system ("clear || cls")

if comb == "A":
    preço = 3.79
    tipo = "Álcool"

elif comb == "G":
    preço = 6.59
    tipo = "Gasolina"

match comb:
    case "A":
        if litros <= 25:
            desconto = preço *0.02
        else:
            desconto = preço * 0.04
    case "G":
        if litros <= 25:
            desconto = preço * 0.03
        else:
            desconto = preço * 0.05
    case _:
        print("Combustivel não encontrado")
        exit()
            
valor = preço * litros
valorfinal = valor - desconto
print(f"O valor total a ser pago é de {valorfinal:.2f} no(a) {tipo}")
print(f"Você abasteceu {litros}L")
         
import os
os.system("clear || cls")  #LIMPEZA DE TERMINAL

print("""    
==========TABELA DE PRODUTOS==========
1 = Placa de video generica 100U$
2 = Placa de video gamer 200U$
3 = Memoria de 4GB RAM 20U$
4 = Memoria de 8GB RAM 40U$
5 = HD de 1TB 50U$
""")

#Entrada de dados

produto = int(input("Digite o numero do produto que deseja comprar: "))
quantidade = int(input("Digite a quantidade que deseja comprar: "))

#PROCESSAMENTO

if produto == 1:
    preco = 100
    produto = "Placa de video generica"
elif produto == 2: 
    preco = 200
    produto = "Placa de video gamer"
elif produto == 3:
    preco = 20
    produto = "Memoria de 4GB RAM"
elif produto == 4:
    preco = 40
    produto = "Memoria de 8GB RAM"
elif produto == 5:
    preco = 50
    produto = "HD de 1TB"
else:
    print("Produto não encontrado")
    exit()
valortotal = preco * quantidade
if quantidade <= 5:
    desconto = valortotal * 0.02
    valortotal = valortotal - desconto
elif quantidade > 5 and quantidade <= 10:
    desconto = valortotal * 0.03
    valortotal = valortotal - desconto
elif quantidade > 10:
    desconto = valortotal * 0.05
    valortotal = valortotal - desconto

#Saida de dados

print(f"O valor total a ser pago é de {valortotal}U$")
print(f"Você comprou {quantidade} unidades do produto {produto}")
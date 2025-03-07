import os 
os.system ("clear || cls")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media >= 6:
    print(f"Parabéns, você foi aprovado! Media: {media} ")

elif media >= 4 and media < 6:
    print(f"Você ficou de recuperação! Media: {media} ")

elif media < 4:
    print(f"Você foi reprovado! Media: {media} ")


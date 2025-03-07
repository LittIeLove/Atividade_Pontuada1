import os
os.system ("clear")
nome = str(input("Digite o nome:"))
sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
estadoc = int(input("Digite 1 para casado(a) e 2 para solteiro(a): "))

if sexo == 2 and estadoc == 1:
    tempo = str(input("Digite o tempo de casada: "))
    sexo = "Feminino"
    estadoc = "Casada"
    print(f"Sexo: {sexo}\nEstado civil: {estadoc}\nTempo de casada: {tempo}")

elif sexo == 2 and estadoc == 2:
    sexo = "Feminino"
    estadoc = "Solteira"
    print(f"Nome: {nome}\nSexo: {sexo}\nEstado civil: {estadoc}")

elif sexo == 1 and estadoc == 1:
    tempo = str(input("Digite o tempo de casado: "))
    sexo = "Masculino"
    estadoc = "Casado"
    print(f"Sexo: {sexo}\nEstado civil: {estadoc}\nTempo de casado: {tempo}")

elif sexo == 1 and estadoc == 2:
    sexo = "Masculino"
    estadoc = "Solteiro"
    print(f"Nome: {nome}\nSexo: {sexo}\nEstado civil: {estadoc}")
    
    









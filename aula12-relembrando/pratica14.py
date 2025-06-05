'''
14 - Desenvolver um script em linguagem Python que leia nome, altura e peso
de 15 pessoas. Este programa deverá armazená-los em um Dicionário, bem
como calcular e mostrar:
a. A menor altura do grupo;
b. O peso médio do grupo;
c. Uma lista dos nomes das pessoas em ordem alfabética.
'''
nomes = []
alturas = []
pesos = []
for i in range(15):
    nome = input('Digite o nome: ')
    nomes.append(nome)
    altura = float(input('Digite a altura (em metros): '))
    alturas.append(altura)
    peso = float(input('Digite o peso (em kg): '))
    pesos.append(peso)
print(f'Menor altura do grupo: {min(alturas)} m')
print(f'Peso médio do grupo: {sum(pesos) / len(pesos):.2f} kg')
print('Nomes em ordem alfabética:',nomes.sort())
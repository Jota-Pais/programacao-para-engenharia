'''
Crie um script em linguagem Python que leia dois vetores (ou listas) com 5 elementos cada. Gere uma lista de 10 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores (listas). Exibir na tela todos as estruturas em linhas separadas
'''
lista1 = [] 
lista2 = []
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor da lista 1: '))
    lista1.append(valor)
for i in range(5):
    valor2 = int(input(f'Digite o {i+1}º valor da lista 2: '))
    lista2.append(valor2)
uniao = []
for i in range(5):
    uniao.append(lista1[i])
    uniao.append(lista2[i])
print (uniao)
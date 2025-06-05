'''
Crie um script em linguagem Python que leia duas listas com 5
elementos cada. Gere uma terceira lista de 10 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois
outros vetores. Exibir na tela todas as listas em linhas separadas.
'''
lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    elemento1 = input(f'Digite o {i + 1}º elemento da primeira lista: ')
    lista1.append(elemento1)
for i in range(5):
    elemento2 = input(f'Digite o {i + 1}º elemento da segunda lista: ')
    lista2.append(elemento2)
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print('listas juntas:', lista3)
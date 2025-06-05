'''
1 - Dada uma lista L de n valores inteiros, elabore um programa que remova todos os números pares da lista. Exemplo: 
Tamanho da lista L: 10
L:1 2 3 4 5 6 7 8 9 10 
Resposta: 1 3 5 7 9
'''
L= []
n = int(input('Tamanho da lista: '))
for i in range(n):
    valor = int(input(f'Digite o {i+1}º valor da lista: '))
    if valor % 2 != 0:
        L.append(valor)
print(L)
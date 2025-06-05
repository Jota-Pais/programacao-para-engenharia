'''
Em um Script Python com duas listas de seis elementos com números
inteiros informados pelo usuário, crie uma nova lista onde cada elemento é a
soma dos elementos de mesma posição nas duas primeiras listas.
Exemplo: Lista1 = [1, 4, 6, ...] Lista2 = [2, 4, 3, ...] Lista_resultante = [3, 8, 9, ...]
'''
lista1 = []
lista2 = []
listaResultante = []
for i in range(6):
    num1 = int(input(f'Digite o {i + 1}º número da Lista 1: '))
    lista1.append(num1)
for i in range(6):
    num2 = int(input(f'Digite o {i + 1}º número da Lista 2: '))
    lista2.append(num2)    
for i in range(6):
    listaResultante.append(lista1[i] + lista2[i])
print (f'Lista 1: {lista1}')
print (f'Lista 2: {lista2}')
print (f'Lista Resultante: {listaResultante}')
'''
Dada uma lista L de n valores inteiros, elabore um Script em linguagem
Python que remova todos os números ímpares da lista.
Exemplo:
Tamanho da lista L: 10
L:1 2 3 4 5 6 7 8 9 10
Resposta: 2 4 6 8 10
'''
L = [1,2,3,4,5,6,7,8,9,10]
LPares = []
for i in range(len(L)):  
    if L[i] % 2 == 0:
        LPares.append(L[i])    
print(f'A lista com os números pares é: {LPares}')
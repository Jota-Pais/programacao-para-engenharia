'''
Desenvolva um Script em linguagem Python que lê vários
números positivos via teclado. Quando o número lido for -1, o
script deve parar e exibir a soma de todos os números positivos
inseridos, a média desses números, o menor e o maior número
digitado. No entanto, utilize uma lista para armazenar os números.
'''
numeros = []
while True:
    numero = int(input('Digite um número positivo (-1 para sair): '))
    if numero == -1:
        break
    elif numero < 0:
        print('Por favor, digite apenas números positivos.')
    else:
        numeros.append(numero)
print(f'Você digitou {len(numeros)} números positivos.')
if numeros:
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    print(f'Soma: {soma}')
    print(f'Média: {media:.2f}')
    print(f'Menor número: {menor}')
    print(f'Maior número: {maior}')
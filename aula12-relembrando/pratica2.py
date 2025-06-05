'''
Elabore um script em linguagem Python que leia de 10 números
reais, inserindo-os numa lista e ao final, mostre-os na ordem inversa.
'''
numeros = []
for i in range(10):
    numero = float(input(f'digite o {i + 1}º número: '))
    numeros.append(numero)
print('Números na ordem inversa:')
print(numeros[::-1])  # Exibe a lista na ordem inversa
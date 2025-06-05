'''
Elabore um script em linguagem Python que leia 10 números reais, inserindo-os em uma lista e ao final, mostre-os na ordem inversa.
'''
numbers = []
for i in range(10):
    number = float(input('Digite um número: '))
    numbers.append(number)
print('Os números na ordem inversa são: ', numbers[::-1])
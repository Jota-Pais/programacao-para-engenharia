'''
- De acordo com a tupla Vendas apresentada abaixo. Desenvolva um
script em linguagem Python que calcule a média, a Variância, o Desvio
Padrão, o menor valor e o maior Valor deste conjunto.
Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
Media = Ʃi Vendasi
n
Variância = Ʃi (Vendasi - Média)²
n
Desvio Padrão = √Variância
'''
import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

media = sum(Vendas) / len(Vendas)
print(f'A média das vendas é de: {media}')

variancia = sum((venda - media) ** 2 for venda in Vendas) / len(Vendas)
print(f'A variância das vendas é de: {variancia}')

desvio_padrao = math.sqrt(variancia)
print(f'O desvio padrão das vendas é de: {desvio_padrao}')

menor = min(Vendas)
maior = max(Vendas)
print(f'O menor valor de vendas é: {menor}')
print(f'O maior valor de vendas é: {maior}')

'''
Você está desenvolvendo um programa para calcular a vazão de um fluido em um tubo com base no diâmetro interno do tubo e na velocidade do fluxo. A fórmula para calcular a vazão deve ser pesquisada. Os dados de entrada devem ser alimentados em metros e m/s.

'''
import math
velocidade =float(input("informe a velocidade do fluxo:"))
diametro =float(input("informe o diametro interno do tubo"))
area = math.pi * (diametro / 2) ** 2
vazão = velocidade * area
print("a vazão do fluido é de:",vazão)
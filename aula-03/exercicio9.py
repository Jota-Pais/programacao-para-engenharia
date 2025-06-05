'''
Você foi contratado para desenvolver um programa que calcule área de uma coroa circular com base em duas medidas de raio fornecido pelo usuário. 


'''
import math
raiop = float(input("informe o raio menor:"))
raiog = float(input("informe o raio maior:"))
areap = math.pi * raiop * raiop
areag = math.pi * raiog * raiog
areaC = areag - areap
print("tamanho da coroa:",areaC)
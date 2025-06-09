'''
Questão 1 - (2,25) (____)  Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. 
'''
from pprint import pprint
medias = {}
while True:
    distancias= []
    nome = input('informe o nome do atleta: ')
    if nome == '':
        break
    for i in range(5):  
        distancia = float(input(f"informe a distancia do salto numero {i+1}: "))
        distancias.append(distancia)
    media = sum(distancias)/ len(distancias)
    medias[nome] = media

pprint(medias) 

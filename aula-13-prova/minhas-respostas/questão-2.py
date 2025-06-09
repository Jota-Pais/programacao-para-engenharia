'''
Questão 2 - (2,25)(____) Faça um programa que peça ao usuário o modelo de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc) e armazene em uma Lista. Em uma outra Lista, armazene o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível (exemplo: 13km/l, 15km/l, 10km/l). Calcule e mostre:
a) O modelo do carro mais econômico;
b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe 6,25 o litro.

'''
modelos = []
consumos = []
economico = 0

for i in range (5):
    modelo = input(f"escreva o modelo do carro numero {i+1}: ")
    consumo = float(input(f"escreva quantos quilometros por litro o {modelo} faz: "))
    consumos.append(consumo)
    modelos.append(modelo)
    if consumo > economico:
        economico = consumo
        modeloEco = modelo

print (f"o modelo mais economico Ã© o: {modeloEco}, que faz {economico} km/L")
print("-------------------------------------------------------------------------------------------------")

for i in range(5):
    consumo1000 = 1000 / consumos[i] 
    gasto = consumo1000 * 6.25
    print(f"para o modelo {modelos[i]}, em 1000 km serÃ£o {consumo1000} de litro de asolina")
    print(f"resultando em um gasto de {gasto} R$") 
    print("-------------------------------------------------------------------------------------------------")


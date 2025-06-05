'''
Elabore um Script em linguagem Python que leia a temperatura média de
cada mês do ano e guarde em uma lista. Com isso, efetue a média anual das
temperaturas e mostre todas que estão acima da média anual e em que mês
elas ocorreram (Ex.: 1  Janeiro, 2  Fevereiro, etc).
'''
temperaturas = []
for i in range(1, 13):
    temperatura = float(input(f'Digite a temperatura média do mês {i}: '))
    temperaturas.append(temperatura)
media_anual = sum(temperaturas) / len(temperaturas)
print(f'Média anual das temperaturas: {media_anual}°C')
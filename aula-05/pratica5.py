'''
Crie um programa em Python para calcular a média de três notas inseridas pelo usuário e dar feedback baseado na média calculada.

Peça ao usuário para inserir as notas de três avaliações.
Calcule a média das notas e arredonde-a para duas casas decimais.
Exiba a média na tela.
Dê um dos seguintes feedbacks de acordo com a média:
Média maior ou igual a 7.0: "Parabéns! Sua média é alta."
Média maior ou igual a 5.0: "Sua média é razoável."
Média abaixo de 5.0: "Sua média é baixa. É uma boa oportunidade para melhorar.".
'''
av1 = float(input("nota na primeira prova: "))
av2 = float(input("nota na segunda prova: "))
av3 = float(input("nota na terceira prova: "))
media = (av1 + av2 + av3)/3
if media>=7:
    print(media,",parabéns! Sua média é alta.")
elif media>=5:
    print(media,",sua média é razoável.")
else:
    print(media,",sua média é baixa. É uma boa oportunidade para melhorar.")
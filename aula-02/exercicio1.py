'''
Elabore um Script em linguagem Python que solicite o valor do investimento (PV),
o número de meses (n) que irá permanecer aplicado e a
rentabilidade (i). Ao final,
o script deve mostrar o valor do montante total (FV).
'''
PV = float(input("digite aqui o seu montante inicial:"))
n = float(input("digite aqui a duração em messes do seu ivestimento:"))
i = 1/200
FV = PV * ((1+i) **n)
print("O valor do maontante final sera de:",FV)

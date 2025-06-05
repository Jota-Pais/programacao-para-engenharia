salarioH = float(input("quanto voce ganha por hora? "))
horas = float(input("quantas horas voce trabalha no mês? "))
sm = salarioH * horas
salarioFinal = (((sm - sm*0.11) - sm* 0.08)- sm*0.05)
print(salarioFinal)

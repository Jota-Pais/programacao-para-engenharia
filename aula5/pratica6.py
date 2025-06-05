'''
Um posto de abastecimento está comercializando combustíveis com a seguinte tabela de descontos:

Álcool: 		até 20 litros, desconto de 2% por litro;
	       	acima de 20 litros, desconto de 5% por litro;

Gasolina: 	até 20 litros, desconto de 4% por litro;
	       	acima de 20 litros, desconto de 6% por litro;

Desenvolva um programa em Python que leia o número de litros vendidos e o tipo de combustível (codificado com A – Álcool e G – Gasolina), 
calcule e imprima o valor a ser pago pelo cliente, sabendo que o litro da gasolina está em R$ 5,57 e do álcool R$ 4,98.
'''
litros = float(input("quantos litros de combustível deseja colocar: "))
combustível = input("deseja colocar àlcool ou gasolina(A ou G)? ")
alcool = 4.98
gasolina = 5.57
if litros>=20 and combustível=="A":
    print(alcool * litros * 0.95)
elif litros<20 and combustível=="A":
    print(alcool * litros * 0.98)
elif litros<20 and combustível=="G":
    print(gasolina * litros * 0.96)
elif litros>=20 and combustível=="G":
    print(gasolina * litros * 0.94)   
else:
    print("deu ruim aí, escreve direito")

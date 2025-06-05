'''
Desenvolva um script em linguagem Python que solicite o valor final,
o número de meses que retende deixar seu dinheiro aplicado,
bem como a rentabilidade. O script deve exibir o valor inicial
que ele deve investir para atingir tal objetivo.
'''
FV = float(input("Digite montante que deseja alcançar:"))
n = float(input("digite o numero de messes deduração da sua a aplicação:"))
i = float(input("Digite a rentabilidade da sua aplicação:"))
PV = FV/((1+i) **n)
print("O montante inicial que você deve aplicar é de:",PV)


'''
A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas, 10% em outras, nada em outros produtos e até 30% em alguns outros produtos. Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido. Ele deve mostrar a saída igual ao exercício anterior.
'''
ptotal = float(input("preço total do produto:"))
desconto = float(input("digite o desconto a ser aplicado:"))

descontoRS = ptotal * desconto/100 
pfinal = ptotal - descontoRS

print("Você ganhou",descontoRS,"R$ de desconto")
pfinal = ptotal - descontoRS
print("valor total a pagar",pfinal,"R$")
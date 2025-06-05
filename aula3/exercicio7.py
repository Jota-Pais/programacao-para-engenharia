'''
Sua tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto. Você deve mostrar:
	Preço original do produto
	Valor do desconto em R$ (tipo 'Você ganhou R$ xx,xx de desconto’)
	Valor do produto com o desconto

'''
preçoTotal = float(input("preço total do produto:"))
desconto = preçoTotal * 0.2
print("Você ganhou",desconto,"R$ de desconto")
preçoFinal = preçoTotal - desconto
print("valor total a pagar",preçoFinal,"R$")
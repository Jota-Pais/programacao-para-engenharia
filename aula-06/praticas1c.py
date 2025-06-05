compra = float(input("o valor da compra foi de: "))
desconto = float(input("o valor do desconto em porcentagem foi de: "))
porcentagem = desconto/100
valorFinal = compra /(1 + porcentagem) 
print(valorFinal)

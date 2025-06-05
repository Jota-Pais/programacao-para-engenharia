"""
Suponha que o preço de capa de um livro seja R$ 24,95,
mas as livrarias recebem um desconto de 35%.
O transporte custa R$ 3,00 para o primeiro exemplar
e 75 centavos para cada exemplar adicional.
Qual é o custo total de atacado para X cópias?
Solicite o valor de X. Crie um Script em linguagem Python para 
solicitar os dados necessários e exibir o custo total da compra.
"""
n = float(input("Número de livros comprados:"))
livro = 24.95
desconto = 35/100
transporte = 3
transporteAd = 0.75
total = ((livro * n) - (desconto * livro)) + transporte + transporteAd + (n - 1)
print("Preço total a pagar:",total)
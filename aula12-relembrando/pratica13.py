'''
Desenvolva um script em linguagem Python, utilizando Dicionários, que
solicite ao usuário inserir a descrição de três produtos de mercado e seus
respectivos preços. Em seguida, mostre na tela o nome do produto mais caro.
'''
produtos = {}
for i in range(3):
    nome = input(f'Digite o nome do produto {i + 1}: ')
    preco = float(input(f'Digite o preço do produto {nome}: '))
    produtos[nome] = preco
produto_mais_caro = max(produtos, key=produtos.get)
print(f'O produto mais caro é {produto_mais_caro} com o preço de R${produtos[produto_mais_caro]}')
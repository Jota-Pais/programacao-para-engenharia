'''
Construa um script em linguagem Python que utilize um dicionário
cujas chaves são os códigos do produto e os valores são o nome do
produto, o preço unitário e a quantidade comprada. A partir do
dicionário, o programa deve imprimir os itens da compra e calcular o
subtotal de cada um deles, ou seja, quantidade * preço unitário. Por fim,
o Script deve apresentar o valor total da compra.

'''

D = {
    101: {'nome': 'Arroz', 'preco': 5.50, 'quantidade': 2},
    102: {'nome': 'Feijão', 'preco': 4.00, 'quantidade': 3},
    103: {'nome': 'Macarrão', 'preco': 3.00, 'quantidade': 1},
    104: {'nome': 'Óleo', 'preco': 6.00, 'quantidade': 1}
}
subtotais = []
for i in range(len(D)):
    codigo = list(D.keys())[i]
    produto = D[codigo]
    subtotal = produto['preco'] * produto['quantidade']    
    subtotais.append(subtotal)
    print(f'Produto: {produto["nome"]}: {subtotais[i]} ')        
print(f'o valor total a pagar é: {sum(subtotais)}')

'''
Construa um script em linguagem Python que utilize um dicionário cujas chaves são os códigos do produto e os valores são o nome do produto, o preço unitário e a quantidade comprada. A partir do dicionário, o programa deve imprimir os itens da compra e calcular o subtotal de cada um deles, ou seja, quantidade * preço unitário. Por fim, o programa deve apresentar o valor total da compra.
'''
produtos = {}

while True:
    cod = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("R$: "))
    qtde = int(input("Qtde: "))
    
    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    
    produtos.update({cod: prod})
    
    resp = input("Deseja continuar [S/N]? ")
    if resp == "N" or resp == "n":
        break
print("\nItens da compra:")
print("-" * 40)
total = 0
for codigo, dados in produtos.items():
    nome, preco, qtde = dados
    subtotal = preco * qtde
    total += subtotal
    print(f"Cód: {codigo} | {nome} | R$ {preco:.2f} x {qtde} = R$ {subtotal:.2f}")

print("-" * 40)
print(f"TOTAL DA COMPRA: R$ {total:.2f}")
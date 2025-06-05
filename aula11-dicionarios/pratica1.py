'''
1 - Desenvolva um código em Python que adicione em um dicionário “d” os seguintes campos: nome, idade, endereço e telefone e mostre os dados no final.
'''
d = {}
d['nome'] = input("Nome: ")
d['idade'] = int(input("Idade: "))
d['endereço'] = input("Endereço: ")
d['telefone'] = input("Telefone: ")
print("Dados do dicionário: ", d)
'''
Desenvolva um Script em linguagem Python que adicione em um
dicionário “d” os seguintes campos: nome, idade, endereço e telefone e
mostre os dados no final
'''
dados = []

n = int(input('Quantas pessoas deseja adicionar? '))

for i in range(n):
    pessoa = {
        'nome': input(f'Digite o nome da pessoa {i + 1}: '),
        'idade': int(input('Digite a idade: ')),
        'endereco': input('Digite o endereço: '),
        'telefone': input('Digite o telefone: ')
    }
    dados.append(pessoa)

print('\n--- Dados cadastrados ---')
for i, pessoa in enumerate(dados, start=1):
    print(f'\nPessoa {i}:')
    for chave, valor in pessoa.items():
        print(f'{chave.capitalize()}: {valor}')
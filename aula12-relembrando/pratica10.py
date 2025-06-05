'''
Elabore um script em linguagem Python, utilizando Dicionários, que
contenha 4 funcionários, com o índice numérico, seu nome, sua função e
tempo de serviço em anos. Em seguida, solicite do usuário demitir um dos
funcionários conforme o número de cadastro e mostre na tela os
funcionários restantes. O Script não deve permitir que um funcionário com a
função “Programador” e com 3 anos ou mais seja demitido.
'''
from pprint import pprint
D = {
    1: {'nome': 'Alice', 'funcao': 'Gerente', 'tempo_servico': 5},
    2: {'nome': 'Bob', 'funcao': 'Programador', 'tempo_servico': 4},
    3: {'nome': 'Carlos', 'funcao': 'Analista', 'tempo_servico': 2},
    4: {'nome': 'Diana', 'funcao': 'Programador', 'tempo_servico': 1}
}
pprint(D)
while True:
    demitido = int(input("Digite o número do funcionário que deseja demitir: "))
    
    if demitido in D:
        funcionario = D[demitido]
        if funcionario['funcao'] == 'Programador' and funcionario['tempo_servico'] >= 3:
            print(f"Não é possível demitir {funcionario['nome']}")
        else:
            D.pop(demitido)
            print(f"{funcionario['nome']} foi demitido.")
            pprint("Funcionários restantes:")
            pprint(D)
    continuar = input("Deseja demitir mais alguém? [S/N] ")
    if continuar == ('N' or 'n'):
        break
print("Funcionários restantes:")
pprint(D)
    
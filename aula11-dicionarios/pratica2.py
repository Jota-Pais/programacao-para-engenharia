'''
2 - Elabore um script em  linguagem Python, utilizando Dicionários, que contenha 4 funcionários, com o índice numérico e seu nome. Em seguida, solicite do usuário demitir um dos funcionários conforme o número de cadastro e mostre na tela os funcionários restantes.
'''
d = {'1': 'João',
     '2': 'Maria',
     '3': 'José',
     '4': 'Ana'}

print("Funcionários:", d)

while True:
    demitido = input("Digite o número do funcionário que deseja demitir: ")
    if demitido in d:
        d.pop(demitido)
    else:
        print("Funcionário não encontrado.")
    
    continuar = input("Deseja demitir mais alguém? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("Funcionários restantes:", d)

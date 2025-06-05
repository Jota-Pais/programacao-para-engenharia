'''
Em um script Python, crie uma lista vazia, que seja preenchida com notas de 3 alunos. Após a leitura das notas, mostrar a nota mais alta, a nota mais baixa, a média geral de notas, além de ordenar a lista de forma crescente.
'''
notas = []
for i in range(3):
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
print('A maior nota é: ', max(notas))
print('A menor nota é: ', min(notas))
print('A média geral é: ', sum(notas) / len(notas))
print('Notas em ordem crescente: ', sorted(notas))

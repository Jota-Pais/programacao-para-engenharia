'''
- Desenvolva um script em linguagem Python que peça as quatro
notas de 10 alunos, calcule e armazene em uma lista a média de cada
aluno, imprima o número de alunos com média maior ou igual a 7.
'''
passados = []
medias = []
for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f'Digite a nota {j + 1} do aluno {i + 1}: '))
        notas.append(nota)
        media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7:
        passados.append(media)
        
print(f'as medias médias dos alunos que passaram são {passados}')
        
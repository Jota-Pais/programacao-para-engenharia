medias = []
for i in range(10):
    aluno = []
    for j in range(4):
        nota = float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
        aluno.append(nota)
    media = sum(aluno) / len(aluno)
    medias.append(media)
print('As médias dos alunos são: ', medias)
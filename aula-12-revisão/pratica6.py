'''
- Dadas duas listas P1 e P2, ambas com n valores reais que representam as
notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um
script em linguagem Python que solicite o valor de n, leia as notas e calcule a
média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
obteve a melhor média. Exemplo:
Tamanho da turma: 5
P1: 7.0 8.3 10.0 6.5 9.3 P2: 8.5 6.9 5.0 7.5 9.8
Resposta:
Média da turma na prova 1: 8.22
Média da turma na prova 2: 7.54
A turma obteve a melhor média na prova 1.
'''
P1 = []
P2 = []
n = int(input('Digite o tamanho da turma: '))
for i in range(n):
    nota1 = float(input(f'Digite a nota da prova 1 do aluno {i + 1}: '))
    P1.append(nota1)
    nota2 = float(input(f'Digite a nota da prova 2 do aluno {i + 1}: '))
    P2.append(nota2)
media_P1 = sum(P1) / n
media_P2 = sum(P2) / n
print(f'Média da turma na prova 1: {media_P1}')
print(f'Média da turma na prova 2: {media_P2}')    
if media_P1 > media_P2:
    print('A turma obteve a melhor média na prova 1.')
elif media_P2 > media_P1:
    print('A turma obteve a melhor média na prova 2.')
else:
    print('A turma obteve a mesma média nas duas provas.')
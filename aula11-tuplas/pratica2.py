'''
2 - Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um script em linguagem Python que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média. 

Exemplo: 
Tamanho da turma: 5 
P1: 7.0   8.3   10.0   6.5   9.3        P2: 8.5   6.9   5.0   7.5   9.8 
Resposta: 
Média da turma na prova 1: 8.22 
Média da turma na prova 2: 7.54 
A turma obteve a melhor média na prova 1.

'''
P1= []
P2= []
for i in range(5):
    nota = float(input(f'Digite a nota do aluno {i+1} na prova 1: '))
    P1.append(nota)
    media1 = sum(P1) / len(P1)
for i in range(5):
    nota = float(input(f'Digite a nota do aluno {i+1} na prova 2: '))
    P2.append(nota)
    media2 = sum(P2) / len(P2)
print(f'Média da turma na prova 1: ',media1)
print(f'Média da turma na prova 2: ', media2)
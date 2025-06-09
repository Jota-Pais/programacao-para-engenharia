'''
Questão 3 - (2,25) (_____) Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões. O programa deve perguntar ao aluno a resposta de cada questão (usar uma Lista) e ao final comparar com o gabarito da prova (usar uma Tupla) e assim calcular o total de acertos e a nota do aluno (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema, deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a)  Maior e Menor Acerto;
b)  Total de Alunos que utilizaram o sistema;
c)  A Média das Notas da Turma.
Questão     Gabarito
01	             D
02		B
03		A
04		C
05		E
06		A
07		B
08		D
09		C
10		E

'''

gabarito = ("D","B","A","C","E","A","B","D","C","E")
notas = []
while True:
    nota = 0
    for i in range(10):
        resposta = input(f"a resposta de questÃ£o {i+1} Ã©: ")
        if gabarito[i] == resposta :
            nota= nota + 1
    notas.append(nota)
    continuar = input("deseja continuar? (S/N) ")
    if continuar == "N":
        break
print(f"o menor acerto foi: {min(notas)}")
print(f"o maior acerto foi: {max(notas)}")
print(f"o numero de alunos Ã©: {len(notas)}")
print(f"a mÃ©dia dos alunos Ã©: {sum(notas)/len(notas)}")

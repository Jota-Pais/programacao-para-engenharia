'''
Escreva um Script em linguagem Python que leia um número inteiro
positivo n e em seguida imprima n linhas chamado Triângulo de Floyd. Para n =
6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
'''
n = int(input("Digite um número inteiro positivo n: "))
for i in range(1,n + 1):
    for j in range(1, i + 1):
        print(j + (i * (i - 1)) // 2)
    print() 
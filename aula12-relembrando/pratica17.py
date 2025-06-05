'''
Escreva um Script em linguagem Python que leia um número inteiro entre
100 e 999 e imprima na saída cada um dos algarismo que compõem o número.
'''
numero = int(input("Digite um número inteiro entre 100 e 999: "))

centena = int(numero / 100)
dezena = int(numero  / 10) - (centena * 10)
unidade = numero - (centena * 100) - (dezena * 10)


print ('o numero na casa da centena é: ',centena)
print ('o numero na casa da dezena é: ',dezena)
print ('o numero na casa da unidade é: ',unidade)
'''
Faça um Script em linguagem Python que receba 6 números inteiros e
mostre:
- Os números pares digitados
- A soma dos números pares digitados
- Os números ímpares digitados
- A quantidade de números ímpares digitados
'''
numeros = []
pares = []
impares = []
soma_pares = 0
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
        soma_pares += num
    else:
        impares.append(num)
print("Números pares digitados:", pares)
print("Soma dos números pares:", soma_pares)
print("Números ímpares digitados:", impares)
print("Quantidade de números ímpares digitados:", len(impares))
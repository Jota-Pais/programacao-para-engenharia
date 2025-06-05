valor = int(input(" Entre com o valor desejado do saque: "))
notas = (100, 50, 20, 10, 5)
i = 0

while i < len(notas):
    quantidade = int(valor / notas[i])
    valor = valor % notas[i]
    if quantidade != 0:
        print(i + 1, " Entregar ", quantidade, " notas de ", notas[i])
    i = i + 1

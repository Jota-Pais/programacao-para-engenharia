valor = int(input(" Entre com o valor desejado do saque: "))
notas = (100, 50, 20, 10, 5)

for i in range(0, len(notas)):
    quantidade = int(valor / notas[i])
    valor = valor % notas[i]
    if quantidade != 0:
        print("Entregar ", quantidade, " notas de ", notas[i])
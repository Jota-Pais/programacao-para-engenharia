'''
Elabore um script em linguagem Python que, dados dois inteiros x e y,
retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]
'''
resultado = []
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if x > y:
    z = x - y
elif x < y:
    z = y - x
else:
    z = 0
for i in range(z + 1):
    if x < y:
        resultado.append(x + i)
    elif x > y:
        resultado.append(y + i)
    else:
        resultado.append(x)
print(f"Resultado: {resultado}")
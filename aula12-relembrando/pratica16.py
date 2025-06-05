'''
Elabore um Script em linguagem Python que crie um dicionário na qual
cada chave seja um caractere e seu valor seja o número de vezes que o
caractere aparece na frase.
'''
frase = input("Digite uma frase: ")
contagem_caracteres = {}


for caractere in frase:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

print("Contagem de caracteres:")
for caractere, contagem in contagem_caracteres.items():
    print(f"'{caractere}': {contagem}")

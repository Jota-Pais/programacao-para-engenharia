'''
Questão - 4 (2,25) (_____) Elabore um script que crie um dicionário na qual cada chave seja um caractere e seu valor seja o número de vezes que o caractere aparece na frase. 
Exemplo: 
"Digite uma frase para contar as letras:”–  fui aprovado
Resposta  {'f': 1, 'u': 1', 'i': 1, ' ': 1, 'a': 2, 'p': 1, 'r': 1, 'o': 2, 'v': 1, 'd': 1}

'''
dicionario = {}
frase = input('digite uma frase para contar as letras: ')
frase_ordem = sorted(frase)

for i in range(len(frase)):
    if frase_ordem[i] in dicionario:
        contagem= contagem + 1
    else:
        contagem = 1
    dicionario[frase_ordem[i]] = contagem 

print(dicionario)


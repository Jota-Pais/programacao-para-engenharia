'''
Agora, ao invés de apenas exibir o nome de cada um de seus amigos,  adicione um mensagem para eles. A mensagem deve ser a mesma, no entanto será personalizado com o nome de cada um deles.
'''
listaNome = ['antonio', 'thigas',  'maite', 'diego', 'goma']
i = 0
while i < len(listaNome):
    if i == 0:
        print('Oi, ' + listaNome[i] + ', tudo bem?')
    elif i == 1:
        print('salve, ' + listaNome[i] + ',beleza?')
    elif i == 2:
        print('partiu devassa ' + listaNome[i] + '?')
    elif i == 3:
        print('suave ' + listaNome[i])
    elif i == 4:
        print('Nao se mata ' + listaNome[i])
    else:
        print('--------------------------------')
    i += 1
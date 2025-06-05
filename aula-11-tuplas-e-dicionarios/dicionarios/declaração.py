sla = 'sla'
dicionário = {'chave1': 'valor1', 
              'chave2': 327,
              'chave3': sla,
              'chave4': [1,2,3,4,5],
              'chave5': True}
#print(dicionário) # !!! O dicionário do Python não fornece garantia de que as chaves estarão ordenadas !!!

dicionário.update({'chave6': 'valorAdicionado'}) # Adiciona uma nova chave e valor ao dicionário
#print(dicionário)

del dicionário['chave1'] # Remove a chave e o valor do dicionário
#print(dicionário)
print(dicionário.keys()) # Mostra as chaves do dicionário
print(dicionário.values()) # Mostra os valores do dicionário
print(dicionário.items()) # Mostra as chaves e valores do dicionário

copia = dicionário.copy() # Faz uma cópia do dicionário
#print('esse é a copia: ',copia)
copia.clear() # Limpa o dicionário

sorted(dicionário, reverse= True)  # Ordena as chaves do dicionário em ordem decrescente
sorted(dicionário, reverse= False)  # Ordena as chaves do dicionário em ordem crescent4

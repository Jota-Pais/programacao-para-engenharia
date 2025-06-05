amigos = []

while len(amigos) < 5:
    response = input('Digite o nome do amigo: ')
    amigos.append(response)
    
    
print(amigos[::-1])

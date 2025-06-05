'''
Construa um programa que receba do usuário a variação do deslocamento
de um objeto (em metros) e a variação do tempo percorrido (em segundo).
Ao fim, o programa deve calcular a velocidade média, em m/s, do objeto.
Mostrar os dados fornecidos e o valor calculado. 
'''
metros = int(input("digite a sua distancia percorrida em metros:"))
segundos = int(input("digite o seu tempo em segundos:"))
ms = metros/segundos
print("a sua velocidade foi de:",ms,"m/s")
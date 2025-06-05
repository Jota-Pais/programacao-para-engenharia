'''
Você está desenvolvendo um programa para calcular a área de um hexágono regular com base no raio fornecido pelo usuário. Um hexágono regular tem seis lados de igual comprimento e seis ângulos internos de 120 graus. Assim, para determinar a área desse hexágono, basta determinar a área de um dos triângulos e, em seguida, multiplicar o resultado por 6.
'''
raio = float(input("digite o raio do hexagono:"))
areaTriangulo = (raio * raio)/2
areaHexagono = areaTriangulo * 6
print("a área do hexágono é:",areaHexagono,"m")

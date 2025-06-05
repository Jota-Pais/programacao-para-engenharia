# Elabore um código fonte que calcule a hipotenusa de um triângulo retângulo, cujos catetos serão fornecidos pelo usuário.
import math
a = float(input("insira um cateto: "))  
b = float(input("insira outro cateto: "))  
c = math.sqrt(a** 2+ b**2)
print("a hipotenusa é igual a: ",c) 
'''
Você está no Brasil, e para temperatura usamos o grau Celsius.
Porém, quando você for contrato para trabalhar como programador
Python no exterior, deverá usar graus Fahrenheit.
Ou seja, você fornece a temperatura em graus Celsius,
e seu script faz a conversão para graus Fahrenheit.
'''
celcius = float(input("informe a temperatura:"))
fahrenheit = (celcius * 9/5) + 32
print(fahrenheit,"f")
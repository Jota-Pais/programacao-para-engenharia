maxima = float(input("maxima: "))
velocidade = float(input("velocidade: "))
if velocidade >= maxima + 30:
    multa = "574,69R$"
    pontos = 7
elif velocidade >= maxima + 11:
    multa = "127,69R$"
    pontos = 5
elif velocidade > maxima:
    multa = "85,15R$"
    pontos = 3
else:
      print("velocidade normal")

if velocidade > maxima:
    print("voces estava acima do limite de velocidade, sua multa é de: ",multa)
    print("além disso voce receberá:",pontos,"na sua carteira!")
    

    


 

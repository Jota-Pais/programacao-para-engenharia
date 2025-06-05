peso = float(input("informe o peso do peixe: "))


if peso >50:
    print("excesso:",peso-50)
    print("preço da multa:",(peso-50)*4,"R$")
else:
    print("tudo certo meu rei")


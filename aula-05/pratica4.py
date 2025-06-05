letra = input("Digite uma letra: ").strip().lower()
if letra in "aeiou":
    print("A letra digitada é uma vogal.")
elif letra.isalpha():
    print("A letra digitada é uma consoante.")
else:
    print("O caractere digitado não é uma letra.")

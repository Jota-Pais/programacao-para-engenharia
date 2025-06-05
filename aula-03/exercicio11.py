'''
Você foi contratado para desenvolver um programa que calcule o Índice de Massa Corporal (IMC) com base nos dados de altura e peso fornecidos pelo usuário. O IMC é uma medida que relaciona o peso e a altura de uma pessoa para avaliar se ela está abaixo do peso, com peso normal, com sobrepeso ou obesa.
A fórmula para calcular o IMC é: IMC = peso / (altura^2), onde o peso é em quilogramas e a altura é em metros.
'''
peso =float(input("informe seu peso:"))
altura =float(input("informe sua altura em metros:"))
imc = peso/(altura * altura)
print("seu IMC é:",imc)
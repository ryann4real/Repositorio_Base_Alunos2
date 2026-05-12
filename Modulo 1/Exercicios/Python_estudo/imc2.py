Nome = input("digite seu nome: ")
Peso = float(input("digite seu peso em kg: "))
Altura = float(input("digite sua altura em cm: "))

imc = Peso / (Altura * Altura)

print("seu imc é: ", imc)

if imc >= 18.5:
    print("abaixo do peso")

elif imc >= 24.9:
    print("peso normal")

elif imc >= 29.9:
    print("sobrepeso")

elif imc >= 34.9:
    print("obesidade Grau 1")

elif imc >= 39.9:
    print("obesidade grau 2")

elif imc >= 40.0:
    print("obesidade grau 3 (mórbida)")
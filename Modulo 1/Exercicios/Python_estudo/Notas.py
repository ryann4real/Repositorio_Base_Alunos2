nome = input("Qual o seu nome? ")

nota1 = float(input("Digite sua primeira nota: "))
print("----------------------------")
nota2 = float(input("Digite sua segunda nota: "))
print("----------------------------")
nota3 = float(input("Digite sua terceira nota: "))
print("----------------------------")

média = (nota1 + nota2 + nota3) / 3
print("Sua média é:", média)

if média >= 7:
    print("Aprovado!")
elif média >= 4:
    print("Em recuperação!")
else:
    print("Reprovado!")

média = ("Sua média é: ")


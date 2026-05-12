nota = float(input("Digite a sua nota (Notas Válidas de 0 até 10): "))

while nota < 0 or nota > 10:
    nota = float(input("inválido, digite uma nota entre 0 e 10"))

print(f"Sua nota foi:{nota}")
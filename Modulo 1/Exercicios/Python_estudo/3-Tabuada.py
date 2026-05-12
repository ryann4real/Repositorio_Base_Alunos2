numero = int(input("Digite o numero da tabuada: "))
inicio = int(input("Digite a partir de qual número a tabuada deve começar: "))
fim = int(input("digite onde deseja terminar a tabuada: "))

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
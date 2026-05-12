TAXA_SERVIÇO = 0.004
PERCENTUAL_IMPOSTO_RENDA_4 = 0.25
PERCENTUAL_IMPOSTO_RENDA_3 = 0.2
PERCENTUAL_IMPOSTO_RENDA_2 = 0.15
PERCENTUAL_IMPOSTO_RENDA_1 = 0.1

FAIXA_SALARIAL_4 = 10000

FAIXA_SALARIAL_3 = 7500

FAIXA_SALARIAL_2 = 5000

FAIXA_SALARIAL_1 = 2500

print("Calculadora de imposto")

salario_base = float(input("Digite o quanto você ganha"))

if salario_base > 10000:
    imposto = salario_base  (PERCENTUAL_IMPOSTO_RENDA_4 + TAXA_SERVIÇO)
elif salario_base > 7500:
    imposto = salario_base  (PERCENTUAL_IMPOSTO_RENDA_3 + TAXA_SERVIÇO
elif salario_base > 5000:
    imposto = salario_base  (PERCENTUAL_IMPOSTO_RENDA_2 + TAXA_SERVIÇO)
elif salario_base > 2500:
    imposto = salario_base (PERCENTUAL_IMPOSTO_RENDA_1 + TAXA_SERVIÇO)
else:
    imposto = 0

 
print(f"Para a sua faixa salarial o imposto é: {imposto} ")
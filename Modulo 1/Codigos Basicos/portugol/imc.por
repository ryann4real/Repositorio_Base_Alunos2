programa {
  funcao inicio() {

	
		// Declaração de variáveis
		real peso, altura, imc

		// Entrada de dados
		escreva("Digite o seu peso (kg): ")
		leia(peso)
		escreva("Digite a sua altura (m): ")
		leia(altura)

		// Cálculo do IMC
		imc = peso / (altura * altura)

		// Exibição do resultado
		escreva("Seu IMC é: ", imc, "\n")

		// Classificação do IMC
		se (imc < 18.5) {
			escreva("Classificação: Abaixo do peso")
		}
		senao se (imc >= 18.5 e imc < 25) {
			escreva("Classificação: Peso normal")
		}
		senao se (imc >= 25 e imc < 30) {
			escreva("Classificação: Sobrepeso")
		}
		senao {
			escreva("Classificação: Obesidade")
		}
	}
}

  }
}

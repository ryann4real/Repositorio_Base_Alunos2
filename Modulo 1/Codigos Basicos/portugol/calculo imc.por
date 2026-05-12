programa {
  funcao inicio() {
    
    real peso
    real altura
    real imc

    escreva("digite o peso em kg: ")
    leia(peso)

    escreva("digite a altura em m: ")
    leia(altura)

    imc = peso / (altura * altura)


    escreva("seu imc é: ", imc)
  }
}

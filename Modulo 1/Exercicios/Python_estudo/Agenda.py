import os

def limpar_tela():
    os.system("cls")



def adicionar_nome(lista_nomes, nome):
    lista_nomes.append(nome) #adiciona nome na lista_nomes.


def remover_nome(lista_nomes, nome):
    if nome in lista_nomes:
        lista_nomes.remove(nome)
        print(f"{nome} foi removido com sucesso!")
    else:
        print("Nome não encontrado.")


def mostrar_nomes(listas_nomes):
    for nome in listas_nomes:
        print(nome)

limpar_tela()

nomes = []
 
while True:
    limpar_tela()
    menu = input("Escolha sua opção:\n[1] - listar nomes \n[2] - Adicionar nomes\n[3] - remover nomes\n[0] - sair\nSua opção: ")
    if menu == "0":
        break
    elif menu == "1":
        mostrar_nomes(nomes)
        input("Aperte enter para continuar")
    elif menu == "2":
        nome_salvar = input("Digite o nome que deseja adicionar: ")
        adicionar_nome(nomes, nome_salvar)
    elif menu == "3":
        nome_remover = input("Digite o nome que deseja remover: ")
        remover_nome(nomes, nome_remover)
        input("Aperte enter para continuar")
    


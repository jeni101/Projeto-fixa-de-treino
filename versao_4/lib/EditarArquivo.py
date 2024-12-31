import os
from lib.Listar_Buscar import *
from lib.CarregarExercicios import *
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def editar_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def editar_exercicio():
    
    exercicios = carregar_exercicios()

    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    nomes_disponiveis = listar_nome_exercicio() 
    if not nomes_disponiveis:
        return
    
    nome_editar = input("\nDigite o nome do exercício que deseja editar: ").capitalize()
    limpar_tela()

    indice = encontrar_indice_exercicio(exercicios, nome_editar)

    if indice != -1:
        print("""
|==================================|
|-=-= OQUER GOSTARIA DE EDITAR =-=-|
|==================================|
|- Nome  . . . . . . . . . . . | 1 |
|- Tipo. . . . . . . . . . . . | 2 |
|- Repetições  . . . . . . . . | 3 |
|==================================|    
""" )
        escolha = input("Digite o número da opção que deseja editar (1, 2 ou 3): ")

        if escolha == '1':
            novo_nome = input("Digite o novo nome do exercício: ").capitalize()
            exercicios[indice]['Nome'] = novo_nome
        elif escolha == '2':
            novo_tipo = input("Digite o novo tipo do exercício: ")
            exercicios[indice]['Tipo'] = novo_tipo
        elif escolha == '3':
            novas_repeticoes = input("Digite o novo número de repetições: ")
            exercicios[indice]['Repeticoes'] = (novas_repeticoes)
        else:
            print("Opção inválida.")

        salvar_exercicios(exercicios)
        limpar_tela()
        print(f"Exercício '{nome_editar}' foi atualizado com sucesso.")
    else:
        print(f"Nenhum exercício encontrado com o nome '{nome_editar}'.")
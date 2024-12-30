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





# def editar_exercicio():
#     exercicios = carregar_exercicios()

#     if not exercicios:
#         print("Nenhum exercício encontrado.")
#         return

#     categorias = listar_tipos_exercicio()
#     if not categorias:
#         print("Nenhuma categoria disponível.")
#         return

#     print("|==================================|")
#     print("|-=-=-= TIPOS DE EXERCÍCIOS =-=-=-|")
#     print("|==================================|")

#     for i, categoria in enumerate(categorias, start=1):
#         print(f"| {i} | {categoria:<30}|")

#     print("|==================================|")

#     opcao_categoria = int(input(f"Escolha a categoria de exercícios (1-{len(categorias)}): "))
    
#     if opcao_categoria < 1 or opcao_categoria > len(categorias):
#         print("Opção inválida.")
#         return

#     categoria_escolhida = categorias[opcao_categoria - 1].strip() 
#     limpar_tela()

#     print(f"|=-=-=-=-=-= EXERCÍCIOS DE {categoria_escolhida.upper()} =-=-=-=-=-=|")
#     print("| EXERCÍCIO:             |   REPETIÇÕES:    |")
#     print("|========================|==================|")

#     lista_exercicios = exercicios.get(categoria_escolhida, [])

#     if not lista_exercicios:
#         print(f"Nenhum exercício encontrado para a categoria '{categoria_escolhida}'.")
#         return

#     for ex in lista_exercicios:
#         print(f"| {ex['Nome']:<23} | {ex['Repeticoes']:<16} |")

#     print("|========================|==================|")
    
#     nome_editar = input("\nDigite o nome do exercício que deseja editar: ").capitalize()
#     limpar_tela()

#     encontrado = False
#     indice_encontrado = -1

#     for indice, ex in enumerate(lista_exercicios):
#         if ex['Nome'] == nome_editar:
#             encontrado = True
#             indice_encontrado = indice
#             break

#     if encontrado:
#         print(""" 
# |==================================| 
# |-=-= O QUE GOSTARIA DE EDITAR =-=-| 
# |==================================| 
# |- Nome  . . . . . . . . . . . | 1 | 
# |- Tipo. . . . . . . . . . . . | 2 | 
# |- Repetições  . . . . . . . . | 3 | 
# |==================================| 
# """)
        
#         escolha = input("Digite o número da opção que deseja editar (1, 2 ou 3): ")

#         if escolha == '1':
#             novo_nome = input("Digite o novo nome do exercício: ").capitalize()
#             exercicios[categoria_escolhida][indice_encontrado]['Nome'] = novo_nome
#         elif escolha == '2':
#             print("|==================================|")
#             print("|-=-=-= TIPOS DE EXERCÍCIOS =-=-=-|")
#             print("|==================================|")
            
#             for i, tipo in enumerate(categorias, start=1):
#                 print(f"| {i} | {tipo:<30}|")
            
#             print("|==================================|")

#             opcao_tipo = int(input(f"\nEscolha a nova categoria de exercícios (1-{len(categorias)}): "))
#             if opcao_tipo < 1 or opcao_tipo > len(categorias):
#                 print("Opção inválida.")
#                 return
            
#             novo_tipo = categorias[opcao_tipo - 1].strip() 
#             exercicios[categoria_escolhida][indice_encontrado]['Tipo'] = novo_tipo  
#         elif escolha == '3':
#             novas_repeticoes = input("Digite o novo número de repetições: ")
#             exercicios[categoria_escolhida][indice_encontrado]['Repeticoes'] = novas_repeticoes
#         else:
#             print("Opção inválida.")

#         salvar_exercicios(exercicios)
#         limpar_tela()
#         print(f"Exercício '{nome_editar}' foi atualizado com sucesso.")
#     else:
#         print(f"Nenhum exercício encontrado com o nome '{nome_editar}' na categoria '{categoria_escolhida}'.")

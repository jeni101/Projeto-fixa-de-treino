from lib import *

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def escolhas() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def escolhas(): # Seleciona a opção desejada para a execução do código.

    limpar_tela()
    while True:
        print("""
|==================================|
|-=-=-= ESCOLHA UMA OPÇÃO: =-=-=-=-|
|==================================|
|- Adicionar exercicios  . . . | 1 |
|- Buscar exercicios . . . . . | 2 |
|- Atualizar arquivo . . . . . | 3 |
|- Sair. . . . . . . . . . . . | 4 |
|==================================|    
"""
        )
        opcao = input('Digite sua escolha: ')
        if opcao == '1':
            certeza = input("Deseja Realmente Adicionar algum Exercicio? (sim ou nao): ")
            if certeza == "sim":
                limpar_tela()
                salvar_dados()
            else:
                limpar_tela()
        elif opcao == '2':
            limpar_tela()
            buscar_por_tipo()
            
        elif opcao == '3':
            limpar_tela()
            print("Função Indisponível no Momento!")
        elif opcao == '4': 
            limpar_tela()
            print('''Saindo...                    
⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
     ⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
  ''')
            break
        else:
            limpar_tela()
            print('Opção invalida criatura, Tente Novamente...')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
escolhas()
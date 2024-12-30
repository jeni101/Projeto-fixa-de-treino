import os
from lib.CarregarExercicios import *
from lib.Listar_Buscar import *
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def limpar_tela() -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def salvar_dados() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def salvar_dados():
    exercicios = carregar_exercicios()

    print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-= NOVO EXERCICIOS =-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIO:              |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |
|                         |              |                  |
|=========================|==============|==================|""")
    
    nome_exercicio = input("Defina o Nome do Exercicio: ").capitalize()
    limpar_tela()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-= NOVO EXERCICIOS =-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIO:              |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")
    print(f"| {str(nome_exercicio):<23} |              |                  |")
    print("|=========================|==============|==================|")
    print("")
    listar_tipos_exercicio()
    tipo_exercicio = input("Defina o Tipo de Exercicio: ").capitalize()
    limpar_tela()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    limpar_tela()
    print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-= NOVO EXERCICIOS =-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIO:              |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")

    print(f"| {str(nome_exercicio):<23} | {str(tipo_exercicio):<12} |                  |")
    print("|=========================|==============|==================|")

    repeticoes_exercicio = input("Defina Quantas Repetições: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    limpar_tela()
    print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-= NOVO EXERCICIOS =-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIO:              |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")

    print(f"| {str(nome_exercicio):<23} | {str(tipo_exercicio):<12} | {str(repeticoes_exercicio):<16} |")
    print("|=========================|==============|==================|")

    decisao02 = input("Deseja realmente salvar esse exercício? (S/N): ")

    if decisao02.lower() == 's':
        novo_exercicio = {
            "Nome": nome_exercicio,
            "Repeticoes": repeticoes_exercicio
        }

        if tipo_exercicio not in exercicios:
            exercicios[tipo_exercicio] = []

        exercicios[tipo_exercicio].append(novo_exercicio)
        salvar_exercicios(exercicios)

        limpar_tela()
        print(f"Exercício salvo com sucesso!")
    else:
        limpar_tela()
        print("Operação cancelada.")
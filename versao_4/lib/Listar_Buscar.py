import os
from lib import *
from lib.CarregarExercicios import *
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def limpar_tela() -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_tipos_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# def listar_tipos_exercicio():
#     exercicios = carregar_exercicios()
#     if not exercicios:
#         print("Nenhum exercício encontrado.")
#         return []

#     categorias = exercicios.keys()

#     print("|==================================|")
#     print("|-=-=-= TIPOS DE EXERCÍCIOS =-=-=-=|")
#     print("|==================================|")

#     for categoria in categorias:
#         print(f"|  {categoria:<31} |")

#     espacos_vazios = 1 - len(categorias)
#     for _ in range(espacos_vazios):
#         print("|                                  |")

#     print("|==================================|")

#     return categoria


def listar_tipos_exercicio():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return []

    categorias = list(exercicios.keys())

    print("|==================================|")
    print("|-=-=-= TIPOS DE EXERCÍCIOS =-=-=-=|")
    print("|==================================|")
    
    contador = 1
    for categoria in categorias:
        print(f"|  {categoria:<28}| {contador:<2}|")
        contador += 1 
    print("|  Outro                       | 0 |")
    
    espacos_vazios = 5 - len(categorias)
    for _ in range(espacos_vazios):
        print("|                                  |")

    print("|==================================|")

    return categorias

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_nomes_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def listar_nome_exercicio():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    categorias = listar_tipos_exercicio()
    if not categorias:
        print("Nenhuma categoria disponível.")
        return

    opcao_categoria = int(input(f"\nEscolha a categoria de exercícios (1-{len(categorias)}): "))

    if opcao_categoria < 1 or opcao_categoria > len(categorias):
        print("Opção inválida.")
        return

    categoria_escolhida = categorias[opcao_categoria - 1]

    limpar_tela()

    print(f"|=-=-=-=-=-= EXERCÍCIOS DE {categoria_escolhida.upper()} =-=-=-=-=-=|")
    print("| EXERCÍCIO:             |   REPETIÇÕES:    |")
    print("|========================|==================|")

    lista_exercicios = exercicios[categoria_escolhida]
    
    if not lista_exercicios:
        print(f"Nenhum exercício encontrado para a categoria '{categoria_escolhida}'.")
    else:
        for ex in lista_exercicios:
            print(f"| {ex['Nome']:<23} | {ex['Repeticoes']:<16} |")
    
    print("|========================|==================|")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def buscar_por_tipo() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_por_tipo():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    tipos_disponiveis = listar_tipos_exercicio()
    if not tipos_disponiveis:
        return

    try:
        tipo_desejado = int(input("\nDigite o número do tipo de exercício que deseja buscar (0 = Sair): "))
        if tipo_desejado == 0:
            print("Operação cancelada.")
            return
        elif 1 <= tipo_desejado <= len(tipos_disponiveis):
            tipo_escolhido = tipos_disponiveis[tipo_desejado - 1] 

            print(f"""\n|===========================================|
|=-=-=-=-=-=-=- EXERCICIOS =-=-=-=-=-=-=-=-=|
|===========================================|
| EXERCÍCIO:              |   REPETIÇÕES:   |
|                         |                 |""")
            for ex in exercicios[tipo_escolhido]:
                print(f"| {ex['Nome']:<23} | {ex['Repeticoes']:<15} |")
            print("|===========================================|")
        else:
            print("Número inválido.")
            
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def encontrar_indices() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def encontrar_indice_exercicio(exercicios, nome_exercicio):
    for index, exercicio in enumerate(exercicios):
        if exercicio['Nome'].capitalize() == nome_exercicio.capitalize():
            return index
    return -1




import os
from lib import *
from lib.CarregarExercicios import *
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def limpar_tela() -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_tipos_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def listar_tipos_exercicio():
    exercicios = carregar_exercicios() 
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return []

    tipos = list(exercicios.keys())
    
    print("|==================================|")
    print("|-=-=-= TIPOS DE EXERCÍCIOS =-=-=-=|")
    print("|==================================|")
    
    for i, tipo in enumerate(tipos, start=1):
        print(f"| {i} | {tipo:<29}|")  

    print("|==================================|")
    return tipos 

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_nomes_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def listar_nome_exercicio():
    exercicios = carregar_exercicios() 
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return []

    categorias = listar_tipos_exercicio()
    if not categorias:
        print("Nenhuma categoria disponível.")
        return []

    print("Tipos disponíveis:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    opcao_categoria = int(input(f"\nEscolha a categoria de exercícios (1-{len(categorias)}): "))

    if opcao_categoria < 1 or opcao_categoria > len(categorias):
        print("Opção inválida.")
        return []

    categoria_escolhida = categorias[opcao_categoria - 1].strip()  
    limpar_tela()

    print(f"|=-=-=-=-=-= EXERCÍCIOS DE {categoria_escolhida.upper()} =-=-=-=-=-=|")
    print("| EXERCÍCIO:             |   REPETIÇÕES:    |")
    print("|========================|==================|")

    if categoria_escolhida in exercicios:
        lista_exercicios = exercicios[categoria_escolhida]
        
        if not lista_exercicios:
            print(f"Nenhum exercício encontrado para a categoria '{categoria_escolhida}'.")
        else:
            for ex in lista_exercicios:
                print(f"| {ex['Nome']:<23} | {ex['Repeticoes']:<16} |")
    else:
        print(f"Nenhum exercício encontrado para a categoria '{categoria_escolhida}'.")

    print("|========================|==================|")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def buscar_por_tipo() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_por_tipo():
    exercicios = carregar_exercicios() 
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    tipos_disponiveis = listar_tipos_exercicio() 
    if not tipos_disponiveis:
        print("Nenhum tipo disponível.")
        return

    print("Tipos disponíveis:")
    for tipo in tipos_disponiveis:
        print(f"- {tipo}")

    tipo_desejado = input("\nDigite o tipo de exercício que deseja buscar (0 = Sair): ").capitalize().strip()
    limpar_tela()

    if tipo_desejado == "0":
        print("Operação cancelada.")
        return

    if tipo_desejado in exercicios:
        print("""        
|===========================================|
|=-=-=-=-=-=-=- EXERCICIOS =-=-=-=-=-=-=-=-=|
|===========================================|
| EXERCÍCIO:              |   REPETIÇÕES:   |
|                         |                 |""")
        for ex in exercicios[tipo_desejado]:
            print(f"| {ex['Nome']:<23} | {ex['Repeticoes']:<15} |")
        print("|===========================================|")
    else:
        print(f"Nenhum exercício encontrado para o tipo '{tipo_desejado}'.")



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def encontrar_indices() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def encontrar_indice_exercicio(exercicios, nome_exercicio):
    for index, exercicio in enumerate(exercicios):
        if exercicio['Nome'].capitalize() == nome_exercicio.capitalize():
            return index
    return -1

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

    tipos = {ex['Tipo'].capitalize() for ex in exercicios}  
    
    print("|==================================|")
    print("|-=-=-= ESCOLHA UMA OPÇÃO: =-=-=-=-|")
    print("|==================================|")

    for tipo in tipos:
        print(f"|  {tipo:<31} |")
    
    espacos_vazios = 5 - len(tipos) 
    for _ in range(espacos_vazios):
        print("|                                  |")

    print("|==================================|")

    return tipos

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_nomes_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def listar_nome_exercicio():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return []

    nomes = {ex['Nome'].capitalize() for ex in exercicios}  

    print("|==================================|")
    print("|-=-=-= ESCOLHA UMA OPÇÃO: =-=-=-=-|")
    print("|==================================|")

    for nome in nomes:
        print(f"|  {nome:<31} |")

    espacos_vazios = 5 - len(nomes)
    for _ in range(espacos_vazios):
        print("|                                  |")

    print("|==================================|")

    return nomes

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def buscar_por_tipo() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_por_tipo():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    tipos_disponiveis = listar_tipos_exercicio() 
    if not tipos_disponiveis:
        return

    tipo_desejado = input("\nDigite o tipo de exercício que deseja buscar? (0 = Sair): ").capitalize()
    while True:
        if tipo_desejado == "0":
            limpar_tela()
            print("Operação cancelada.")
            break
        else:
            encontrados = [ex for ex in exercicios if ex['Tipo'].capitalize() == tipo_desejado]
            limpar_tela()
            if encontrados:
                print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-=-= EXERCICIOS -=-=-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIOS:             |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")
                for ex in encontrados:
                    print(f"| {ex['Nome']:<23} | {ex['Tipo']:<12} | {ex['Repeticoes']:<16} |")
                print("|=========================|==============|==================|")
                break
            else:
                print(f"Nenhum exercício encontrado para o tipo '{tipo_desejado}'.")
                break

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def encontrar_indices() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def encontrar_indice_exercicio(exercicios, nome_exercicio):
    for index, exercicio in enumerate(exercicios):
        if exercicio['Nome'].capitalize() == nome_exercicio.capitalize():
            return index
    return -1

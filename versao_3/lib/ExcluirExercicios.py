import os
from lib.Listar_Buscar import *
from lib.CarregarExercicios import *
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def limpar_tela() -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def excluir() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
def excluir():
    exercicios = carregar_exercicios()

    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    nomes_disponiveis = listar_nome_exercicio() 
    if not nomes_disponiveis:
        return
    
    nome_excluir = input("\nDigite o nome do exercício que deseja excluir: ").capitalize()
    limpar_tela()

    encontrado = False
    for tipo, lista in exercicios.items():
        encontrados = [ex for ex in lista if ex['Nome'].capitalize() == nome_excluir]
        if encontrados:
            encontrado = True
            break

    if encontrado:
        print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-=-= EXERCICIOS -=-=-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIOS:             |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")
        for ex in encontrados:
            print(f"| {ex['Nome']:<23} | {ex['Tipo']:<12} | {ex['Repeticoes']:<16} |")
        print("|=========================|==============|==================|")
        confirmacao = input("Você tem certeza que deseja excluir este exercício? (S/N): ").lower()
        
        if confirmacao == 's':
            exercicios[tipo].remove(encontrados[0])  
            salvar_exercicios(exercicios)
            limpar_tela()
            print(f"Exercício '{nome_excluir}' foi excluído com sucesso.")
        else:
            print("Exclusão cancelada.")
    else:
        print(f"Nenhum exercício encontrado com o nome '{nome_excluir}'.")



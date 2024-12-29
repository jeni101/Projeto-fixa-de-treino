import os
import json

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def carregar_dados() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def carregar_exercicios():
    
    try:
        with open("database/dados.json", "r") as file: # Verifica se o arquivo "dados.json" está vazio ou corrompido
            content = file.read().strip()
            if content:
                return json.loads(content)
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Deu Erro Parceiro")
        return []

def salvar_exercicios(exercicios): # Salva os exercícios no arquivo "dados.json"
    if not os.path.exists("database"):
        os.makedirs("database")
    
    with open("database/dados.json", "w") as file:
        json.dump(exercicios, file, indent=4)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def salvar_dados() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def salvar_dados():

    exercicios = carregar_exercicios()
    print("-=-=-=- Adicionar Exercicíos -=-=-=-")
    nome_exercicio = input("Defina o Nome do Exercicio: ")


    tipo_exercicio = input("Defina o Tipo de Exercicio: ")

    repeticoes_exercicio = input("Defina Quantas Repetições: ")

    novo_id = len(exercicios) + 1
    novo_exercicio = {
        "ID": f"EXERCICIO {novo_id}",
        "Nome": nome_exercicio,
        "Tipo": tipo_exercicio,
        "Repeticoes": repeticoes_exercicio
    }
    exercicios.append(novo_exercicio)
    salvar_exercicios(exercicios)

    limpar_tela()

    print(f"Exercício salvo com sucesso!")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def corrigir_texto(texto) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def limpar_tela():
    #Limpa a tela do terminal.
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def listar_tipos_exercicio() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def listar_tipos_exercicio():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return []

    tipos = {ex['Tipo'].capitalize() for ex in exercicios}  # Mostra os exercicios que tem no banco de dados.
    print("Tipos de exercício disponíveis:")
    print("-=" * 10)
    for tipo in tipos:
        print(f"- {tipo}")
    print("-=" * 10)
    return tipos

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def buscar_por_tipo() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_por_tipo():
    exercicios = carregar_exercicios()
    if not exercicios:
        print("Nenhum exercício encontrado.")
        return

    tipos_disponiveis = listar_tipos_exercicio() 
    if not tipos_disponiveis:
        return

    tipo_desejado = input("\nDigite o tipo de exercício que deseja buscar: ").capitalize()
    encontrados = [ex for ex in exercicios if ex['Tipo'].capitalize() == tipo_desejado]
    limpar_tela()
    if encontrados:
        print("""
|===========================================================|
|-=-=-=-=-=-=-=-=-=-= TREINOS DO DIA -=-=-=-=-=-=-=-=-=-=-=-|
|===========================================================|
| EXERCÍCIOS:             |     TIPO:    |   REPETIÇÕES:    |
|                         |              |                  |""")
        for ex in encontrados:
            print(f"| {ex['Nome']:<23} | {ex['Tipo']:<12} | {ex['Repeticoes']:<16} |")
        print("|=========================|==============|==================|")

    else:
        print(f"Nenhum exercício encontrado para o tipo '{tipo_desejado}'.")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

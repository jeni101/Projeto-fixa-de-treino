import os
import json
DATAPATH = "database/dados.json"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- def carregar_dados() =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def carregar_exercicios():
    
    try:
        with open(DATAPATH, "r") as file: 
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

def salvar_exercicios(exercicios):
    if not os.path.exists("database"):
        os.makedirs("database")
    
    with open(DATAPATH, "w") as file:
        json.dump(exercicios, file, indent=4)

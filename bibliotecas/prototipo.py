import os
import time
DATAPATH = "database/dados.txt"
   
def banco_de_dados():
    dicionarios = {}
    if os.path.exists(DATAPATH):
        with open(DATAPATH, 'r', encoding='utf-8') as file:
            for linha in file:
                tipo, nome, valor = linha.strip().split('|', 2)
                if tipo not in dicionarios:
                    dicionarios[tipo] = {}
                dicionarios[tipo][nome] = valor
    return dicionarios

def salvar_dados(dicionarios):
    with open(DATAPATH, 'w', encoding='utf-8') as file:
        for tipo, exercicios in dicionarios.items():
            for nome, valor in exercicios.items():
                file.write(f"{tipo}|{nome}|{valor}\n")
    
    
def adicionar_exercicio(tipo, nome, valor):
    dicionarios = banco_de_dados()
    if tipo not in dicionarios:
        dicionarios[tipo] = {}  
        dicionarios[tipo][nome] = valor 
        salvar_dados(dicionarios)
        
def mostrar_exercicios(tipo):
     """Mostra os exercícios de um tipo específico."""
     dicionarios = banco_de_dados()
     exercicios = dicionarios.get(tipo, {})
     if exercicios:
         print(f"Exercícios do tipo '{tipo}':")
         for nome, valor in exercicios.items():
             print(f"{nome}: {valor}")
     else:
         print(f"Não há exercícios cadastrados para o tipo '{tipo}'.")
         

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
from spellchecker import SpellChecker

def corrigir_texto(texto):
    spell = SpellChecker(language= 'pt')
    palavras = texto.split()
    palavras_corrigidas = [spell.candidates(palavra).pop() for palavra in palavras]
    texto_corrigido = ' '.join(palavras_corrigidas)
    return texto_corrigido
 
def dados():
    limpar_tela()
    nome = input('nome do exercicio por obséquio: ') 
    nome_corrigido = corrigir_texto(nome)
    limpar_tela()
    repeticoes = input('repeticoes desejadas do exercicio: ') 
    limpar_tela()
    tipo = input('qual o tipo do exercicio estamos a hablar: ')
    tipo_corrigido = corrigir_texto(tipo)
    limpar_tela()
    time.sleep(5) # TEMPO DE VISUALIZACAO DA PERGUNTA
    return nome_corrigido, repeticoes , tipo_corrigido 



def confirmacao():
    confirmacao = banco_de_dados()
    while True:
       
        nome_corrigido, repeticoes, tipo_corrigido = dados()
        
       
        print(f"Você confirmou: Nome = {nome_corrigido}, Repetições = {repeticoes}, Tipo = {tipo_corrigido}")
        confia = input('Voz mecê tem plena certeza de teus atos? (s ou n): ')
        
        if confia.lower() == 's':
            adicionar_exercicio(tipo_corrigido, nome_corrigido, repeticoes) 
            print(f"Exercício '{nome_corrigido}' adicionado com sucesso ao tipo '{tipo_corrigido}'.")
        else:
            print(f"Exercício '{nome_corrigido}' não foi adicionado ao tipo '{tipo_corrigido}'.")
        
        algo_mais = input('Deseja adicionar mais algum exercício? (s ou n): ')
        if algo_mais.lower() == 'n':
            limpar_tela()  
            ver = input('Deseja ver os exercícios adicionados? (s ou n): ')
            if ver.lower() == 's':
                for chaves, dicionario_interno in banco_de_dados.items():
                    print( f'{chaves}')
                    for chaves, dicionario_interno in banco_de_dados.keys():
                        print( f'suas opcoes sao{chaves}' )
                
                    
                opcoes = print(banco_de_dados([1]))
                
                tipo_exibicao = input('Qual o tipo de exercício deseja ver? ') 
                exercicios = mostrar_exercicios(tipo_exibicao)
                if exercicios:
                    print(f"Exercícios do tipo '{tipo_exibicao}':") 
                    for nome, valor in exercicios.items():
                        print(f"{nome}: {valor}") 
                else:
                    print(f"Não há exercícios cadastrados para o tipo '{tipo_exibicao}'.")
            break  
                
        
confirmacao()
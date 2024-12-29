import os
import time

def banco_de_dados():
    dicionarios = {}
    
    def adicionar_exercicio(tipo, nome, valor):
        if tipo not in dicionarios:
            dicionarios[tipo] = {} 
        dicionarios[tipo][nome] = valor 
        
    def mostrar_exercicios(tipo):
         return dicionarios.get(tipo, {}) 
    return adicionar_exercicio, mostrar_exercicios 

adicionar_exercicio, mostrar_exercicios = banco_de_dados()


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
    tipo = input('qual o tipo do exercicio? ')
    tipo_corrigido = corrigir_texto(tipo)
    limpar_tela()
    time.sleep(5) 
    return nome_corrigido, repeticoes , tipo_corrigido 



def confirmacao():
    while True:
        nome_corrigido, repeticoes, tipo_corrigido = dados()
    
        print(f"Você confirmou: Nome = {nome_corrigido}, Repetições = {repeticoes}, Tipo = {tipo_corrigido}")
        confia = input('Tem certeza que deseja salvar esse exercicio? (s ou n): ')
        
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
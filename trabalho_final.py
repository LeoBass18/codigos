#!/usr/bin/env python
# coding: utf-8


import os
import pyodbc

pasta_dados = r"C:\Users\leonardo.mello\OneDrive - Programmers Beyond IT\Área de Trabalho\Léo\UNIFOR\PYTHON\dados_ibge-20240323T140953Z-001\dados_ibge"

# Função para ler um arquivo e retornar como uma lista de linhas
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()[1:]  # Ignora a primeira linha (cabeçalho)
    return linhas

# Função para juntar todos os arquivos em um único conjunto de dados
def juntar_dados(pasta_dados):
    dados_completos = []
    for arquivo in os.listdir(pasta_dados):
        caminho_arquivo = os.path.join(pasta_dados, arquivo)
        dados_arquivo = ler_arquivo(caminho_arquivo)
        dados_completos.extend(dados_arquivo)
    return dados_completos

# Executar a função para juntar todos os dados
dados_juntos = juntar_dados(pasta_dados)

import pyodbc

# Parâmetros de conexão com o SQL Server
server = 'NTB-G0ZQMS3\SQLEXPRESS' 
database = 'desafio_final'  
username = 'PROGRAMMERS\\leonardo.mello' 
# Não forneci a senha, pois estamos usando autenticação do Windows

# String de conexão
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};Trusted_Connection=yes'

# Estabelecendo a conexão com o banco de dados
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Inserindo os dados na tabela
for linha in dados_juntos:
    valores = linha.strip().split(';')  # Dividir cada linha em valores individuais
    cursor.execute("INSERT INTO IBGE_2 (COD_UF, COD_MUN, COD_ESPECIE, LATITUDE, LONGITUDE, NV_GEO_COORD) VALUES (?, ?, ?, ?, ?, ?)", valores)

# Confirmar a transação e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso na tabela.")



# Confirmar a transação e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso no SQL Server.")


""" 4. Escrever quais pontos de dificuldade e quais os pontos a favor da técnica usada. 
Indique soluções de mercado através de uma pesquisa, quais ferramentas facilitariam essa jornada? (1 ponto)"""

#Resposta

"""Por conta do volume de dados, a performance foi uma questão nesse desafio, puramente baseado em Python,  
talvez com Pandas ou Spark teria tido uma performance melhor. 
Também pode ser difícil manter e escalar a solução de manipulação de dados sem o uso de estruturas e ferramentas mais robustas.
Considerando que nesse caso tinhamos 100Mi de linhas."""


#ALUNO: Leonardo da Rocha Mello






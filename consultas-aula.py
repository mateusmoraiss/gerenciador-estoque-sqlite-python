import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Filtrar produtos com preço entre 100 e 1000
cursor.execute("SELECT * FROM estoque WHERE preco BETWEEN 100 AND 1000")
produtos = cursor.fetchall()

# Exibir dados dos produtos
for produto in produtos:
    print("ID: ", produto[0])
    print("Nome: ", produto[1])
    print("Descrição: ", produto[2])
    print("Preço: ", produto[3])
    print("Quantidade em Estoque: ", produto[4])
    print("----------------------")

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")


## Fica abaixo mais exemplos para estudar de consutlas sqlite com python

'''
## APAGAR UMA COLUNA -----------------------------------------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Remover a coluna 'descricao' da tabela 'estoque'
cursor.execute("ALTER TABLE estoque DROP COLUMN descricao")
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")


#APAGAR UM DADO ESPECÍFICO PELO NOME ------------------------------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Nome do produto a ser apagado
nome_produto = "Produto A"

# Apagar o produto com o nome especificado
cursor.execute("DELETE FROM estoque WHERE nome = ?", (nome_produto,))
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")



## CRIAR NOVA COLUNA ---------------------------------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Adicionar uma nova coluna 'cor' à tabela 'estoque'
cursor.execute("ALTER TABLE estoque ADD COLUMN cor TEXT")
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")

-----

# APAGAR PELO ID  ------------------------------------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# ID do item a ser apagado
item_id = 1

# Apagar o item com o ID especificado
cursor.execute("DELETE FROM estoque WHERE id = ?", (item_id,))
conexao.commit()

# Verificar se algum registro foi afetado
if cursor.rowcount > 0:
    print("Item apagado com sucesso!")
else:
    print("Nenhum item encontrado com o ID especificado.")

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()



# ALTERAR ID DE UM PRODUTO --------------------------------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# ID do produto a ser alterado
produto_id = 1

# Novo ID para o produto
novo_id = 10

# Alterar o ID do produto
cursor.execute("UPDATE estoque SET id = ? WHERE id = ?", (novo_id, produto_id))
conexao.commit()

# Verificar se algum registro foi afetado
if cursor.rowcount > 0:
    print("ID do produto alterado com sucesso!")
else:
    print("Nenhum produto encontrado com o ID especificado.")

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()



# CONSULTAR PRODUTOS COM FILTROS ----------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Filtrar produtos com preço entre 3000 e 9000
cursor.execute("SELECT * FROM estoque WHERE preco BETWEEN 3000 AND 9000")
produtos = cursor.fetchall()

# Exibir dados dos produtos
for produto in produtos:
    print("ID: ", produto[0])
    print("Nome: ", produto[1])
    print("Descrição: ", produto[2])
    print("Preço: ", produto[3])
    print("Quantidade em Estoque: ", produto[4])
    print("----------------------")

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")



# APAGAR PRODUTOS COM FILTROS -----------------------------------
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Apagar produtos com preço entre 3000 e 9000
cursor.execute("DELETE FROM estoque WHERE preco BETWEEN 3000 AND 9000")
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")




# CONSULTAR POR FILTROS ESPECÍFICOS -------------------------------------

import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Filtro: preço acima de 5000
filtro_preco_min = 5000

# Filtro: quantidade em estoque abaixo de 5
filtro_quantidade_max = 5

# Consultar produtos com base nos filtros
cursor.execute("SELECT * FROM estoque WHERE preco > ? AND quantidade < ?",
               (filtro_preco_min, filtro_quantidade_max))
produtos = cursor.fetchall()

# Exibir dados dos produtos
for produto in produtos:
    print("ID: ", produto[0])
    print("Nome: ", produto[1])
    print("Descrição: ", produto[2])
    print("Preço: ", produto[3])
    print("Quantidade em Estoque: ", produto[4])
    print("----------------------")

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fechar a conexão com o banco de dados
conexao.close()

input("Pressione Enter para encerrar o programa...")





'''


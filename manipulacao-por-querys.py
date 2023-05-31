import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

cursor.execute("UPDATE estoque SET nome = 'Camisa do flamengo', descricao = 'A mais linda do mundo', preco = 1 WHERE id = 76")
conexao.commit()

conexao.close()
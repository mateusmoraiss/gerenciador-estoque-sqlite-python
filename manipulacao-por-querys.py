import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

cursor.execute("UPDATE estoque SET nome = 'Camisa do flamengo', descricao = 'A mais linda do mundo', preco = 1 WHERE id = 74")

conexao.commit()
conexao.close() 


































''' COMANDO PARA MOSTRAR O TAMANHO DA TABELA estoque 
import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()


cursor.execute("SELECT COUNT(*) FROM estoque")
result = cursor.fetchone()
count = result[0]
print("Número de registros na tabela: ", count)

conexao.close()

input("pressione enter para sair")
'''
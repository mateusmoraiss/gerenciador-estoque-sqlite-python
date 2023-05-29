import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Inserir dados fictícios na tabela
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('iPhone 12', 'Smartphone da Apple', 7999.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Samsung Galaxy S21', 'Smartphone da Samsung', 5999.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('MacBook Pro', 'Notebook da Apple', 12999.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sony PlayStation 5', 'Console de videogame', 4499.00, 10))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Samsung QLED 4K TV', 'Televisor Samsung 4K', 3999.00, 6))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Canon EOS R6', 'Câmera Mirrorless', 8399.00, 2))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Apple AirPods Pro', 'Fones de ouvido sem fio', 1899.00, 7))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Dell XPS 13', 'Notebook Dell', 6499.00, 4))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Samsung Galaxy Watch 4', 'Smartwatch Samsung', 1799.00, 9))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('LG OLED 4K TV', 'Televisor LG 4K', 3799.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Nintendo Switch', 'Console de videogame', 1999.00, 12))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Bose QuietComfort 35 II', 'Fones de ouvido sem fio', 1399.00, 6)),
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('LG UltraWide Monitor', 'Monitor LG UltraWide', 2499.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Microsoft Surface Pro 7', 'Tablet e Laptop Híbrido', 7999.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('GoPro Hero 9 Black', 'Câmera de Ação', 2499.00, 6))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sony WH-1000XM4', 'Fones de ouvido sem fio', 1899.00, 4))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Xbox Series X', 'Console de videogame', 4499.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Samsung Galaxy Tab S7', 'Tablet Samsung', 3499.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Amazon Echo Dot', 'Smart Speaker com Alexa', 349.00, 10))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('HP Envy 15', 'Notebook HP', 5499.00, 2))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sony Bravia 4K TV', 'Televisor Sony 4K', 2999.00, 7))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Apple Watch Series 6', 'Smartwatch Apple', 2499.00, 5)),
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Lenovo ThinkPad X1 Carbon', 'Notebook Lenovo', 8499.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sony Alpha a7 III', 'Câmera Mirrorless', 6299.00, 4))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Bose SoundLink Revolve+', 'Caixa de Som Bluetooth', 999.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Google Pixel 5', 'Smartphone Google', 3999.00, 6))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('ASUS ROG Strix G15', 'Notebook Gamer ASUS', 6499.00, 2))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Fitbit Versa 3', 'Smartwatch Fitbit', 899.00, 7))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('JBL Flip 5', 'Caixa de Som Bluetooth', 399.00, 9))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Microsoft Xbox Elite Wireless Controller Series 2', 'Controle Xbox', 699.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('HP Spectre x360', 'Notebook HP', 6999.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sony WH-1000XM3', 'Fones de ouvido sem fio', 1599.00, 6))

# Confirmar a inserção dos dados no banco de dados
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fecha a conexão
conexao.close()

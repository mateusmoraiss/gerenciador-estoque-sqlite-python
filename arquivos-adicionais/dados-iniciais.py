import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Inserir dados fictícios na tabela
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('iPhone 12', 'Smartphone da Apple', 7999.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Samsung Galaxy S21', 'Smartphone da Samsung', 5999.00, 8)) # ----------------------------
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
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",###### PRODUTOS PARA O LAR
               ('Sofá', 'Sofá confortável para sala de estar', 1500.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Geladeira', 'Geladeira com freezer', 2500.00, 2))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Mesa de Jantar', 'Mesa de jantar para 6 pessoas', 800.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Cama de Casal', 'Cama de casal com colchão', 1200.00, 4))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Máquina de Lavar', 'Máquina de lavar roupas', 1800.00, 3))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Televisão', 'Televisão LED 55 polegadas', 2000.00, 2))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Armário de Cozinha', 'Armário para utensílios de cozinha', 900.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Mesa de Centro', 'Mesa de centro para sala de estar', 400.00, 6))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Cadeira', 'Cadeira confortável para escritório', 250.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Estante', 'Estante para livros e decoração', 700.00, 3)) ################ PRODUTOS BARATOS
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Caneta Esferográfica', 'Caneta de tinta azul', 1.99, 50))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Caderno Universitário', 'Caderno com 200 folhas', 4.99, 30))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Pilha AA', 'Pacote com 4 pilhas alcalinas', 3.99, 100))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Barbeador Descartável', 'Pacote com 5 unidades', 7.99, 20))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Pasta Suspensa', 'Caixa com 10 pastas', 9.99, 40))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Cabo USB', 'Cabo USB para carregamento', 5.99, 50))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Pincel Marcador', 'Pacote com 6 marcadores coloridos', 3.49, 60))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Fone de Ouvido', 'Fone de ouvido com fio', 9.99, 100))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Tapete de Banheiro', 'Tapete antiderrapante para banheiro', 6.99, 25))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Caneca de Porcelana', 'Caneca para chá ou café', 4.49, 80)) ############### MAIS PRODUTOS DE TECNOLOGIA 
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Smart TV LED 32"', 'TV HD com Wi-Fi integrado', 999.00, 10))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Notebook Lenovo Ideapad', 'Processador Intel Core i5, 8GB RAM, 256GB SSD', 3499.00, 5))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Smartphone Xiaomi Redmi Note 10', 'Tela 6.43", 4GB RAM, 64GB', 1299.00, 15))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Headphone Bluetooth JBL', 'Fones de ouvido sem fio com microfone integrado', 249.00, 30))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Câmera DSLR Canon EOS Rebel', 'Sensor de 24.1MP, gravação de vídeo em Full HD', 2999.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Monitor Gamer LG 27"', 'Resolução QHD, tempo de resposta de 1ms', 1999.00, 12))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Impressora Multifuncional HP', 'Imprime, copia e digitaliza, conexão Wi-Fi', 399.00, 20))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Mouse Gamer Razer', 'Sensor óptico de 16000 DPI, iluminação RGB', 199.00, 25))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Roteador Wi-Fi TP-Link', 'Dual band, velocidade de até 1200Mbps', 99.00, 30))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Caixa de Som Bluetooth JBL', 'Potência de 20W, resistente à água', 199.00, 15)) # ALEATÓRIOS
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Sofá Retrátil', 'Sofá de 3 lugares com assentos retráteis', 1999.00, 20))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Geladeira Frost Free', 'Geladeira duplex com capacidade de 400L', 2599.00, 15))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Panela Elétrica de Arroz', 'Capacidade de 10 xícaras, função de aquecimento', 129.90, 30))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Máquina de Café Expresso', 'Preparo de café expresso e cappuccino', 399.00, 25))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Churrasqueira Elétrica', 'Churrasqueira portátil para uso em ambientes internos', 299.00, 10))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Bicicleta Dobrável', 'Bicicleta de aro 20" dobrável para facilitar o transporte', 799.00, 8))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Aspirador de Pó Robô', 'Limpeza automatizada com sistema de mapeamento', 999.00, 12))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Máquina de Lavar Roupas', 'Capacidade de 10kg, diversas programações', 1899.00, 15))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Violão Acústico', 'Violão clássico com cordas de nylon', 349.00, 30))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Kit de Maquiagem', 'Conjunto com variedade de produtos e cores', 199.90, 20))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Bola de Futebol', 'Bola oficial de futebol em tamanho padrão', 59.90, 40))
cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
               ('Jogo de Panelas', 'Conjunto com panelas antiaderentes de diferentes tamanhos', 299.90, 10))


# Confirmar a inserção dos dados no banco de dados
conexao.commit()

# Fechar o cursor, mas manter a conexão aberta
cursor.close()

# Fecha a conexão
conexao.close()

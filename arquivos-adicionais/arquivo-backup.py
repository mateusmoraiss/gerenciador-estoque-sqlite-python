import sqlite3
# Conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Criar tabela do estoque
cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    descricao TEXT,
                    preco REAL,
                    quantidade INTEGER
                )''')
conexao.commit()
# Função para adicionar um produto ao estoque
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    # Inserir produto no banco de dados
    cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
                   (nome, descricao, preco, quantidade))
    conexao.commit()
    print("Produto adicionado ao estoque com sucesso!")


# Função para atualizar as informações de um produto no estoque
def atualizar_produto():
    produto_id = int(input("Digite o ID do produto que deseja atualizar: "))

    cursor.execute("SELECT * FROM estoque WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto:
        descricao = input("Digite a nova descrição do produto: ")
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))

        # Atualizar informações do produto no banco de dados
        cursor.execute("UPDATE estoque SET descricao = ?, preco = ?, quantidade = ? WHERE id = ?",
                       (descricao, preco, quantidade, produto[0]))
        conexao.commit()
        print("Produto atualizado com sucesso!")


# Função para gerar o relatório de estoque
def gerar_relatorio():
    print("Relatório de Estoque:")

    # Selecionar todos os produtos do banco de dados
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()

    for produto in produtos:
        print("ID: ", produto[0])
        print("Nome: ", produto[1])
        print("Descrição: ", produto[2])
        print("Preço: ", produto[3])
        print("Quantidade em Estoque: ", produto[4])
        print("----------------------")


# Função para fechar a conexão com o banco de dados
def fechar_programa():
    conexao.close()
    print("Programa encerrado. Banco de dados salvo.")


while True:
    print("=== Sistema de Gerenciamento de Estoque ===")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Gerar Relatório de Estoque")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        gerar_relatorio()
    elif opcao == "4":
        fechar_programa()
        break
    else:
        print("Opção inválida. Digite uma opção válida.")

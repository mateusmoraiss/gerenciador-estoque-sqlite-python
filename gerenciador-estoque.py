import sqlite3
#### inicia conexão com o banco de dados
conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()
                                            #tabela chamada estoque
#### Criar tabela do estoque   SE NÃO EXSITIR ESTOQUE
cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    descricao TEXT,
                    preco REAL,
                    quantidade INTEGER
                )''')
conexao.commit()

##### Função para adicionar um produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

   ##### Inserir um produto no dba
    cursor.execute("INSERT INTO estoque (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
                   (nome, descricao, preco, quantidade))
    conexao.commit()
    print("Produto adicionado ao estoque com sucesso!")


#### Função que atualiza as informações
def atualizar_produto():
    produto_id = int(input("Digite o ID do produto que deseja atualizar: "))

    cursor.execute("SELECT * FROM estoque WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto:
        print("Produto encontrado:")
        print("ID: ", produto[0])
        print("Nome: ", produto[1])
        print("Descrição: ", produto[2])
        print("Preço: ", produto[3])
        print("Quantidade em Estoque: ", produto[4])
        print("----------------------")

        opcao = input("Deseja atualizar este produto? (S/N): ")
        if opcao.lower() == "s":
            descricao = input("Digite a nova descrição do produto (ou deixe em branco para manter a atual): ")
            if not descricao:
                descricao = produto[2]

            preco = input("Digite o novo preço do produto (ou deixe em branco para manter o atual): ")
            if not preco:
                preco = produto[3]
            else:
                preco = float(preco)

            quantidade = input("Digite a nova quantidade em estoque (ou deixe em branco para manter a atual): ")
            if not quantidade:
                quantidade = produto[4]
            else:
                quantidade = int(quantidade)

            if quantidade == 0:
                opcao_apagar = input("A quantidade informada é zero. Deseja apagar o produto? (S/N): ")
                if opcao_apagar.lower() == "s":
                    cursor.execute("DELETE FROM estoque WHERE id = ?", (produto_id,))
                    conexao.commit()
                    print("Produto apagado com sucesso!")
                else:
                    print("Atualização cancelada.")
            else:
                cursor.execute("UPDATE estoque SET descricao = ?, preco = ?, quantidade = ? WHERE id = ?",
                               (descricao, preco, quantidade, produto_id))
                conexao.commit()
                print("Produto atualizado com sucesso!")
        else:
            print("Atualização cancelada.")
    else:
        print("Nenhum produto encontrado com o ID especificado.")

### Função que gera o relatório
def gerar_relatorio():
    print("Relatório de Estoque:")

    ##### Selecionar todos os produtos
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()

    for produto in produtos:
        print("ID: ", produto[0])
        print("Nome: ", produto[1])
        print("Descrição: ", produto[2])
        print("Preço: ", produto[3])
        print("Quantidade em Estoque: ", produto[4])
        print("----------------------")


##### Função para fechar a conexão com o banco de dados
def fechar_programa():
    conexao.close()
    print("Programa encerrado. Banco de dados salvo.")


while True:
    print("=== Sistema de Gerenciamento de Estoque by Mateus Morais ===")
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

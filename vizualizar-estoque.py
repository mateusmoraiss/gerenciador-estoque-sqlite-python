import sqlite3
from tkinter import Tk
from tkinter.ttk import Treeview

def exibir_dados():
    # Conectar ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # Executar a consulta para obter os dados do estoque
    cursor.execute('SELECT id, nome, descricao, preco, quantidade FROM estoque')
    dados = cursor.fetchall()

    # Criar uma janela do tkinter
    janela = Tk()
    janela.title('Visualização de Estoque')

    # Criar o Treeview para exibir os dados
    treeview = Treeview(janela, columns=('ID', 'Nome', 'Descrição', 'Preço', 'Quantidade'), show='headings')
    treeview.pack()

    # Definir os cabeçalhos das colunas
    treeview.heading('ID', text='ID')
    treeview.heading('Nome', text='Nome')
    treeview.heading('Descrição', text='Descrição')
    treeview.heading('Preço', text='Preço')
    treeview.heading('Quantidade', text='Quantidade')

    # Adicionar os dados do estoque no Treeview
    for dado in dados:
        treeview.insert('', 'end', values=dado)

    # Executar a janela do tkinter
    janela.mainloop()

exibir_dados()

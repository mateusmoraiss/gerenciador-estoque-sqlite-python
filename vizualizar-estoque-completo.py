import sqlite3
from tkinter import Tk
from tkinter.ttk import Treeview

def exibir_dados():
    # Conectar ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # CONSULTA
    cursor.execute('SELECT id, nome, descricao, preco, quantidade FROM estoque')
    dados = cursor.fetchall()

    # CRIAÇÃO DE JANELA
    janela = Tk()
    janela.title('Visualização de Estoque')

    # EXIBIR OS DADOS NO TREEVIEW
    treeview = Treeview(janela, columns=('ID', 'Nome', 'Descrição', 'Preço', 'Quantidade'), show='headings')
    treeview.pack()

## NOME DAS COLUNAS NA TABELA
    treeview.heading('ID', text='ID')
    treeview.heading('Nome', text='Nome')
    treeview.heading('Descrição', text='Descrição')
    treeview.heading('Preço', text='Preço')
    treeview.heading('Quantidade', text='Quantidade')

    #####COLOCAR DADOS  no Treeview
    for dado in dados:
        treeview.insert('', 'end', values=dado)

    # EXIBIR A TABELA
    janela.mainloop()

exibir_dados()

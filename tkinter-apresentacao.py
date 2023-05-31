import sqlite3
from tkinter import Tk
from tkinter.ttk import Treeview

def exibir_dados():
  ######### CONEXÃO AO SQLITE
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # CONSULTA SQL
    query = "SELECT * FROM estoque"



    cursor.execute(query)
    dados = cursor.fetchall()

    janela = Tk()
    janela.title('Visualização de Estoque')

   ##### INSERÇÃO DOS DADOS NO DATAFRAME 
    treeview = Treeview(janela, columns=('ID', 'Nome', 'Descrição', 'Preço', 'Quantidade'), show='headings')
    treeview.pack()

    ###### NOME DAS COLUNAS QUE FICARÃO TABELA
    treeview.heading('ID', text='ID')
    treeview.heading('Nome', text='Nome')
    treeview.heading('Descrição', text='Descrição')
    treeview.heading('Preço', text='Preço')
    treeview.heading('Quantidade', text='Quantidade')

    # COLOCAR DADOS no Treeview
    for dado in dados:
        treeview.insert('', 'end', values=dado)

    # EXIBIR A TABELA
    janela.mainloop()

exibir_dados()

import os.path
from tkinter import *
from tkinter import ttk
from mundial_bot import *
from os import *

janela = Tk()
mundial_bot = Mundial()
pastaApp = os.path.dirname(__file__)

class Tela:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.entrada()
        self.lista_frame2()
        self.get_database()
        self.atualizar = mundial_bot.database_inserir()

        janela.mainloop()

    def tela(self):
        self.janela.title("www.mundialcalcados.com.br")
        self.janela.configure(background="#fff")
        self.janela.resizable(True, True)
        self.imagem_logo()

    def frames(self):
        self.frame_1 = Frame(self.janela, bg='grey', highlightthickness=0.5, highlightbackground="#fff")
        self.frame_1.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.40)

        self.frame_2 = Frame(self.janela, bg='grey', highlightthickness=0.5, highlightbackground="#fff")
        self.frame_2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.botao_atualizar = Button(self.frame_1, font=("GothamPro", 13), background="#fff", text="Atualizar", command= self.database_atualizar)
        self.botao_atualizar.place(relx=0.63, rely=0.56, relwidth=0.1, relheight=0.13)

        self.botao_pesquisar = Button(self.frame_1, font=("GothamPro", 13), background="#fff", text="Pesquisar", command= self.database_pesquisar)
        self.botao_pesquisar.place(relx=0.27, rely=0.56, relwidth=0.1, relheight=0.13)

    def labels(self):
        self.lb_input = Label(self.frame_1, font=("GothamPro", 15), text='Fabricante', bg='grey', fg="#fff")
        self.lb_input.place(relx=0.40, rely=0.40, relwidth=0.20, relheight=0.15)

        self.lbStatus = Label(self.frame_1, image=self.logo)
        self.lbStatus.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.21)

    def entrada(self):
        self.entrada_usuario = Entry(self.frame_1)
        self.entrada_usuario.place(relx=0.40, rely=0.57, relwidth=0.2, relheight=0.13)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col0', 'col1', 'col2','col3'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Marca')
        self.listaCli.heading('#2', text='Modelo')
        self.listaCli.heading('#3', text='Valor')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=35)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=188)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def database_pesquisar(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for marcas in database.cur.execute(f"SELECT * FROM tenis WHERE marca LIKE '%{self.entrada_usuario.get()}%'"):
            self.listaCli.insert(parent="", index=0, values=marcas)
        database.var.commit()

    def get_database(self):
        for coluna in database.cur.execute(f"SELECT * FROM tenis"):
            self.listaCli.insert(parent="", index=0, values=coluna)
        database.var.commit()

    def database_atualizar(self):
        Mundial()
        mundial_bot.database_inserir()
        mundial_bot.database_delete()
        mundial_bot.database_inserir()

    def imagem_logo(self):
        self.logo = PhotoImage(file=pastaApp+"//logo.png")

Tela()

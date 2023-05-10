from tkinter import *
from tkinter import ttk
from bot import Bot
##teste##

telinha = Tk()


class Tela():
    def __init__(self):
        self.telinha = telinha
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.lista_frame2()
        self.entrada()
        self.insert()
        telinha.mainloop()

    def tela(self):
        self.telinha.title("Cara a Cara")
        self.telinha.configure(background="#FFFFFF")
        self.telinha.resizable(True, True)

    def frames(self):
        self.frame = Frame(self.telinha, bg="#612a92", highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_2 = Frame(self.telinha, bg='#612a92', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_2.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.25)

        self.frame_3 = Frame(self.telinha, bg='#612a92', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_3.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.botao_grafico = Button(self.frame_2, font=("Arial", 13), background="#8ae287", text="Gráfico")
        self.botao_grafico.place(relx=0.51, rely=0.41, relwidth=0.1, relheight=0.15)

        self.botao_confirma = Button(self.frame_2, font=("Arial", 13), background="#8ae287", text="Confirmar")
        self.botao_confirma.place(relx=0.40, rely=0.41, relwidth=0.1, relheight=0.15)

    def labels(self):
        self.lb_input = Label(self.frame_2, font=("Arial", 15), text='Escreva qual a marca:  ', bg='#612a92')
        self.lb_input.place(relx=0.005, rely=0.40, relwidth=0.20, relheight=0.15)

        self.lbStatus = Label(self.frame, font=("Arial", 25), text='-=-=-=-=CELULARES-=-=-=-', fg='black', bg='#612a92')
        self.lbStatus.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.21)


    def entrada(self):
        self.entrada_usuario = Entry(self.frame_2)
        self.entrada_usuario.place(relx=0.18, rely=0.41, relwidth=0.20, relheight=0.15)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_3, height=3, columns=('col0', 'col1', 'col2','col3'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Marca')
        self.listaCli.heading('#2', text='Modelo')
        self.listaCli.heading('#3', text='Valor')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=35)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=188)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_3, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def insert(self):

        bot = Bot()
        for samsung in bot.lista_samsung:
            self.listaCli.insert(parent="", index=0, values=samsung)

        for iphone in bot.lista_iphone:
            self.listaCli.insert(parent="", index=0, values=iphone)

        for motorola in bot.lista_motorola:
            self.listaCli.insert(parent="", index=0, values=motorola)


Tela()

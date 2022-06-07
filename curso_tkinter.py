from tkinter import *

tela = Tk()

class Application():
    def __init__ (self):
        self.raiz = tela
        self.config()
        self.frames()
        self.widgets_frame_1()
        tela.mainloop()

    def config(self):
        self.raiz.title("Aprendendo Tkinter")
        self.raiz.configure(background="gray")
        self.raiz.geometry("700x500+788+311")
        self.raiz.maxsize(width="900", height="700")
        self.raiz.minsize(width="500", height="300")

    def frames (self):
        self.frame_1 = Frame(self.raiz, bd=4, bg='lightgray',highlightbackground='#759fe6',highlightthickness=3 )
        self.frame_1.place(relx=0.1, rely=0.05, relwidth=0.8 ,relheight=0.4 )

        self.frame_2 = Frame(self.raiz, bd=4, bg='lightgray',highlightbackground='#759fe6',highlightthickness=3 )
        self.frame_2.place(relx=0.1, rely=0.5, relwidth=0.8 ,relheight=0.4 )

    def widgets_frame_1(self):
        #Cria botão limpar
        self.bt_limpar = Button(self.frame_1,text="Limpar")
        self.bt_limpar.place(relx=0.1,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão buscar
        self.bt_buscar = Button(self.frame_1,text="Buscar")
        self.bt_buscar.place(relx=0.22,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão novo
        self.bt_Novo = Button(self.frame_1,text="Novo")
        self.bt_Novo.place(relx=0.46,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão alterar
        self.bt_alterar = Button(self.frame_1,text="Alterar")
        self.bt_alterar.place(relx=0.58,rely=0.1, relwidth=0.1, relheight=0.1)

        #Cria botão apagar 
        self.bt_apagar = Button(self.frame_1,text="Apagar")
        self.bt_apagar.place(relx=0.70,rely=0.1, relwidth=0.1, relheight=0.1)
        
        #Cria label e entrada do codigo
        self.lb_codigo = Label(self.frame_1,text="Código")
        self.lb_codigo.place(relx= 0.86, rely=0.01,relwidth=0.1, relheight=0.08)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.86,rely=0.12,relwidth=0.1,relheight=0.08)

        #Cria label e entrada do nome
        self.lb_nome = Label(self.frame_1,text="Nome")
        self.lb_nome.place(relx= 0.05, rely=0.3,relwidth=0.1)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05,rely=0.4,relwidth=0.6)

        #Cria label e entrada do telefone
        self.lb_telefone = Label(self.frame_1,text="Telefone")
        self.lb_telefone.place(relx= 0.05, rely=0.6,relwidth=0.1)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05,rely=0.7,relwidth=0.35)

        #Cria label e entrada do cidade
        self.lb_cidade = Label(self.frame_1,text="Cidade")
        self.lb_cidade.place(relx= 0.5, rely=0.6,relwidth=0.1,)

        self.cidade_entry = Entry(self.frame_1,bd=0,background="lightgray")
        self.cidade_entry.place(relx=0.5,rely=0.7,relwidth=0.35)


Application()
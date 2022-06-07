from tkinter import *

telaURL = Tk()
url_Img = PhotoImage(file="url.png")

class Application():
    def __init__(self):
        self.raiz = telaURL
        self.config()
        self.label_url()
        self.widgets_t1()
        telaURL.mainloop()
    
    def config(self):
        self.raiz.title("Automação SureBet")
        self.raiz.iconbitmap(default="icone.ico")
        self.raiz.geometry("549x324+788+311")
        self.raiz.wm_resizable(False,False)

    def label_url(self):
        self.label_URL = Label(telaURL, image=url_Img)
        self.label_URL.place(x=0, y=0)
        

    def widgets_t1 (self):
        #Botão
        self.bt_Ok = Button (text="Confirmar",bd=0,bg='#fff',fg='#3CB371',font=('verdana',16,'bold'))
        self.bt_Ok.place(relx= 0.375,rely= 0.73,relwidth=0.25,relheight=0.10)

        #Caixa de Entrada de dados
        self.url_entrada = Entry(telaURL,fg='#3CB371', bd=0, font=("Calibri",15), justify=CENTER)
        self.url_entrada.place(width=360, height=40, x=95, y=142)
        


Application()

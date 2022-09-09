from cgitb import text
from xml.sax import xmlreader
from login import login
from usuario import Usuario
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from tkinter.ttk import Label
from ttkbootstrap import Colors
class MinhaUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Login Mauá Loja Online",
            size= (600,300),
            position= (0,0),
            minsize= (600,300),
            maxsize= (1920,1080),
            alpha=1
        )
        
        return janela
    def _construir_frame(self, sizex,sizey):
        frame = ttk.Frame(
            width = sizex,
            height = sizey,
        )
        return frame

    def _criar_botao(self, texto, acao):
        return ttk.Button(
            self.base,
            text=texto,
            bootstyle=(INFO, OUTLINE),
            command=acao
        )
    def _criar_label(self, label):
        return ttk.label(
            self.base,

        )
    def _criar_texto(self, guardar,senha):
        if(senha == True):
            return ttk.Entry(
                self.base,
                textvariable=guardar,
                show = "*"
            )
        else:
            return ttk.Entry(
                self.base,
                textvariable=guardar,
            )

    def __init__(self) -> None:
        self.base = self._construir_base()
        self.valor_digitado = ""
        self.base.config(bg ="#ffffff")


        self.frame1 = self._construir_frame(1380,880)
        self.frame1.bg = "#111140"
        self.login = self._criar_texto(guardar=self.valor_digitado, senha = False)
        label_email = Label(anchor = W, text='Email:')
        label_email.pack(side=TOP, padx=5, pady=5)
        #
        self.login.pack(side=TOP, padx=5, pady=5)
        self.senha = self._criar_texto(guardar=self.valor_digitado, senha = True)
        
        label_senha= Label(anchor = W, text='Senha:')
        label_senha.pack(side=TOP, padx=5, pady=5)  

        self.senha.pack(side=TOP, padx=5, pady=5)  
        self.bot = self._criar_botao(texto="Logar", acao=self.guardar_logar)
        self.bot.pack(side=TOP, padx=5, pady=5)  
        self.bot = self._criar_botao(texto="Registrar", acao=self.guardar_registrar)
        self.bot.pack(side=TOP, padx=5, pady=5,expand=True)  


    def run(self):
        self.base.mainloop()

    def guardar_logar(self):
        log = [self.login.get(), self.senha.get()]
        login(log[0],log[1])

    def guardar_registrar(self):
        log = [self.login.get(), self.senha.get()]
        user = Usuario(log[0], log[1])


if __name__ == "__main__":
    app = MinhaUI()
    app.run()
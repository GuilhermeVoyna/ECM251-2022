import imp
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage



base = ttk.Window(
    title="MEU TITULO",
    size=(1024,400),
    position=(100,100),
    minsize=(600,300),
    maxsize=(1800,900),
    alpha=0.75,
)

base.iconphoto(False,PhotoImage(file='calculator.png'))


def acao_botao():
    print("CLICK!")
ttk.Button(
    base,
    text="Ola Mundo!",
    bootstyle="default",   
    command=acao_botao
).pack(side=LEFT,padx=10,pady=5)

#segundo botao

bot2=ttk.Button(
    base,
    text="Segundo Botão",
    bootstyle=(DANGER,OUTLINE),   
    command=acao_botao
)
bot2.pack(side=LEFT,padx=20,pady=5)


base.mainloop()


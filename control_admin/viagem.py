import tkinter as tk

from paho.mqtt import subscribe


class Viagem(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        # self.textLabel = tk.Label(text="Aguarde o motorista no local infomado")
        # self.textLabel.pack()

        master.msgVariable.set('Aguarde o motorista no local infomado')
        master.update()

        subscribe.simple('motorista')
        master.msgVariable.set('A Van já está no local informado.')

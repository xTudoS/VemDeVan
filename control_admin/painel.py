import tkinter as tk

class Painel(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.master = master

        self.master.title('Painel de Controle - Vem de Van')
        self['bg'] = 'black'

        button = tk.Button(text='Close', command=lambda : exit())
        button.pack()
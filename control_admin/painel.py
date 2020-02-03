import tkinter as tk
from .form_destino import FormDestino


class Painel(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.selectDestino = True

        self.msgVariable = tk.StringVar()
        self.msgVariable.set('Onde você está?')

        self.master = master

        self.master.title('Vem de Van')

        self['bg'] = '#9EC496'
  
        self.textLabel = tk.Label(self, textvariable=self.msgVariable, bg='#9EC496')
        self.textLabel.pack(fill=tk.X)

        self.formDestino = FormDestino(self)
        self.formDestino.pack()

        self.buttonAvancar = tk.Button(self, text='Avançar', command=self.next)
        self.buttonAvancar.pack()

    def next(self):
        if self.selectDestino:
            self.msgVariable.set('Para onde deseja ir?')
            for wid in self.formDestino.winfo_children():
                if 'entry' in str(wid):
                    wid.delete(0, 'end')
            self.selectDestino = False
            self.buttonAvancar['text'] = "Chamar Van"
        
        self.update()

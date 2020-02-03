import tkinter as tk

class FormDestino(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self['bg'] = '#9EC496'

        self.ruaLabel = tk.Label(self, text='Rua:', bg='#9EC496')
        self.ruaLabel.grid(column=0, row=0, sticky="EW", pady=10)

        self.ruaEntry = tk.Entry(self)
        self.ruaEntry.grid(column=1, row=0, pady=10)

        self.numLabel = tk.Label(self, text='N°:', bg='#9EC496')
        self.numLabel.grid(column=0, row=1, sticky="EW", pady=10)

        self.numEntry = tk.Entry(self)
        self.numEntry.grid(column=1, row=1, pady=10)

        self.cityLabel = tk.Label(self, text='Cidade:', bg='#9EC496')
        self.cityLabel.grid(column=0, row=2, sticky="EW", pady=10)

        self.cityEntry = tk.Entry(self)
        self.cityEntry.grid(column=1, row=2, pady=10)

        self.bairroLabel = tk.Label(self, text='Bairro:', bg='#9EC496')
        self.bairroLabel.grid(column=0, row=3, sticky="EW", pady=10)

        self.bairroEntry = tk.Entry(self)
        self.bairroEntry.grid(column=1, row=3, pady=10)

        self.estadoLabel = tk.Label(self, text='Estado:', bg='#9EC496')
        self.estadoLabel.grid(column=0, row=3, sticky="EW", pady=10)

        self.estadoEntry = tk.Entry(self)
        self.estadoEntry.grid(column=1, row=3, pady=10)

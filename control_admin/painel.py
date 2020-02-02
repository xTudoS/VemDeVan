import tkinter as tk


class Painel(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.master = master

        self.master.title('Painel de Controle - Vem de Van')

        
        self.saldoLabel = tk.Label(bg='#9EC496', textvariable=self.master.user.saldoStringVar)
        self.saldoLabel.config(font=("Courier", 15))
        self.saldoLabel.place(x=10, y=10)
        

        button = tk.Button(text='Close', command=self.aumentarSaldo)
        button.place(x=500, y=0)


    def aumentarSaldo(self):
        self.master.user.saldo += 1
        self.master.user.saldoStringVar.set(f"Seu Saldo: R${self.master.user.saldo:.2f}")
        self.master.update()
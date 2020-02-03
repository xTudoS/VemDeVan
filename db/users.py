import tkinter as tk

class Users:

    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
        self.motorista = False
        # self.saldo = 0
        # self.saldoStringVar = tk.StringVar()
        # self.saldoStringVar.set(f"Seu Saldo: R${self.saldo:.2f}")
        self.cpf = ''
        self.cnh = ''
        self.telefone = ''
        self.nome = ''
        self.data_nascimento = ''
        self.placa_veiculo = ''

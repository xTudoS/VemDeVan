import tkinter as tk

class Users:

    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
        self.motorista = False
        self.cpf = ''
        self.cnh = ''
        self.telefone = ''
        self.nome = ''
        self.data_nascimento = ''
        self.placa_veiculo = ''

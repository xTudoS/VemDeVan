import tkinter as tk


class RegisterForm(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.registerUser = tk.Checkbutton(self, text="Sou um passageiro", variable=master.passageiro, onvalue=1, offvalue=0, command=lambda : master.changeOption(True))
        self.registerMotorista = tk.Checkbutton(self, text="Sou um motorista", variable=master.motorista, onvalue=1, offvalue=0, command=master.changeOption)

        self.registerUser.grid(column=0, row=0)
        self.registerMotorista.grid(column=1, row=0)

        self.cpfLabel = tk.Label(self, text='CPF:')
        self.cpfEntry = tk.Entry(self, textvariable=master.cpf)

        self.cpfLabel.grid(column=0, row=1)
        self.cpfEntry.grid(column=1, row=1)

        self.nomeLabel = tk.Label(self, text="Nome:")
        self.nomeEntry = tk.Entry(self, textvariable=master.nome)

        self.nomeLabel.grid(row=2, column=0)
        self.nomeEntry.grid(row=2, column=1)

        self.telefoneLabel = tk.Label(self, text="Telefone:")
        self.telefoneEntry = tk.Entry(self, textvariable=master.telefone)

        self.telefoneLabel.grid(row=3, column=0)
        self.telefoneEntry.grid(row=3, column=1)

        self.data_nascLabel = tk.Label(self, text="Data de Nascimento:")

        self.data_nascLabel.grid(row=4, column=0)

        self.emailEntry = tk.Entry(self, textvariable=master.email)
        self.emailLabel = tk.Label(self, text="Email:")

        self.emailLabel.grid(column=0, row=5)
        self.emailEntry.grid(column=1, row=5)
    

        self.passwdEntry = tk.Entry(self, textvariable=master.passwd, show='*')
        self.passwdLabel = tk.Label(self, text="Senha:")

        self.passwdLabel.grid(column=0, row=6)
        self.passwdEntry.grid(column=1, row=6)

        


import tkinter as tk
from tkinter import messagebox
from .register_form import RegisterForm
from .date_entry import DateEntry
import psycopg2

import re

from PIL import ImageTk
from PIL import Image

class Register(tk.Toplevel):

    def __init__(self, master, *args, **kw):
        tk.Toplevel.__init__(self, master)

        self.cpf = tk.StringVar()
        self.email = tk.StringVar()
        self.passwd = tk.StringVar()
        self.telefone = tk.StringVar()
        self.nome = tk.StringVar()
        # self.data_nasc = True

        self.cnh = tk.StringVar()
        self.placa = tk.StringVar()

        self.resizable(width=False, height=False)
        self.title('Vem de Van')
        self.iconbitmap('img/favicon.ico')

        self.geometry(f"360x640+{master.width - 180}+{master.height - 350}")

        self.master = master

        self.imgBgOriginal = Image.open('img/bg.png')
        self.imgBgResize = self.imgBgOriginal.resize((360, 640), Image.ANTIALIAS)
        
        self.imgBg = ImageTk.PhotoImage(self.imgBgResize)

        self.imgBgLabel = tk.Label(self, image=self.imgBg)
        self.imgBgLabel.place(x=0, y=0)

        self.registerLabel = tk.Label(self, text="Preencha os dados abaixo para realizar o seu cadastro", bg='#9EC496')
        self.registerLabel.place(x=40, y=20)

        self.motorista = tk.IntVar()
        self.passageiro = tk.IntVar()
        self.passageiro.set(1)

        self.form = RegisterForm(self)
        self.form.place(x=60, y=50)

        self.data_nascDateEntry = DateEntry(self.form)
        self.data_nascDateEntry.grid(row=4, column=1)

        self.cnhLabel = tk.Label(self.form, text="CNH:")
        self.cnhEntry = tk.Entry(self.form, textvariable=self.cnh)

        
        self.placaLabel = tk.Label(self.form, text="Placa do veículo:")
        self.placaEntry = tk.Entry(self.form, textvariable=self.placa)
        
        


        self.buttonRegister = tk.Button(self, text="Registrar", command=self.register)
        self.buttonRegister.place(x=150, y=350)
    
    def changeOption(self, passageiro=False):
        if passageiro:
            self.passageiro.set(1)
            self.motorista.set(0)

            try:
                self.cnhLabel.grid_forget()
                self.cnhEntry.grid_forget()
                self.placaLabel.grid_forget()
                self.placaEntry.grid_forget()
            except:
                pass


           
        else:
            self.passageiro.set(0)
            self.motorista.set(1)

            # if master.motorista.get():
            # print('Motorista')
            # self.cnhLabel = tk.Label(self.form, text="CNH:")
            # self.cnhEntry = tk.Entry(self.form, textvariable=self.cnh)
            self.cnhLabel.grid(column=0, row=7)
            self.cnhEntry.grid(column=1, row=7)

            self.placaLabel.grid(column=0, row=8)
            self.placaEntry.grid(column=1, row=8)

        self.update()

    def register(self):
        cpf = self.cpf.get()
        email = self.email.get()
        passwd = self.passwd.get()
        telefone = self.telefone.get()
        nome = self.nome.get()
        cnh = None
        data_nasc = self.data_nascDateEntry.get()
        placa = self.placa.get()

        print(placa)
        
        error = False

        if self.motorista.get():
            cnh = self.cnh.get()
        
        emailValido = re.match(self.master.regexEmail, email)
        if emailValido == None or (0 == len(passwd) > 8):
            messagebox.showwarning('Warning', 'Erro ao se cadastrar!\nVerifique os dados informados e tente novamente.')
            return None

        if len(cpf) == 11 and len(telefone) == 11 and len(nome) <= 50 and len(data_nasc) == 10:
            if self.motorista.get():
                if len(cnh) == 11 and len(placa) == 7:
                    self.master.db.execute(f"insert into veiculo values ('{placa}')", insert=True)
                    error = self.master.db.execute(f"insert into usuario values ('{cpf}', '{telefone}', '{nome}', '{data_nasc}', '{email}', '{passwd}', '{cnh}', '{placa}')", insert=True)[1]
                else:
                    messagebox.showwarning('Warning', 'Erro ao se cadastrar!\nVerifique os dados informados e tente novamente.')
                    return None
        
            else:
                error = self.master.db.execute(f"insert into usuario values ('{cpf}', '{telefone}', '{nome}', '{data_nasc}', '{email}', '{passwd}')", insert=True)[1]
                

                    
        if error:
            messagebox.showwarning('Warning', 'Ops! Já existe um usuário com esses dados cadastrados')  
            return None 
        messagebox.showwarning('Warning', 'Usuário cadastrado com sucesso')

        self.destroy(exitApp=False)
                


    def destroy(self, exitApp=True, *args, **kw):
        super().destroy()
        if exitApp:
            exit(0)

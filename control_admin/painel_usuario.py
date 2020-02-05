import tkinter as tk
from .form_destino import FormDestino
from tkinter import messagebox


# from .viagem import Viagem

# import psycopg2.extras


from paho.mqtt import subscribe
import threading


class PainelUsuario(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.selectDestino = True

        self.msgVariable = tk.StringVar()
        self.msgVariable.set('Onde você está?')

        self.rua = tk.StringVar()
        self.num = tk.StringVar()
        self.city = tk.StringVar()
        self.estado = tk.StringVar()

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
        
        if len(self.rua.get()) == 0 or len(self.num.get()) == 0 or len(self.estado.get()) == 0:
            messagebox.showwarning('Warning', 'Nenhum campo pode ficar em branco')
            return None

        if self.selectDestino:
            self.msgVariable.set('Para onde deseja ir?')
            for wid in self.formDestino.winfo_children():
                if 'entry' in str(wid):
                    wid.delete(0, 'end')
            self.selectDestino = False
            self.buttonAvancar['text'] = "Chamar Van"
            self.update()

        else:
            if self.master.mqtt.is_connected() == False:
                self.master.mqtt.connect_broker()
            self.master.mqtt.publish("viagem", "passageiro")

            for wid in self.winfo_children():
                wid.pack_forget()

            self.msgVariable.set('Aguardando a confirmação de um motorista')
            self.textLabel.pack()

            self.update()
            
            m = subscribe.simple('motorista')
            cpf_motorista = m.payload.decode("utf-8") 
            
            self.master.cur.execute(f"""select nome, placa from usuario where usuario.cpf = '{cpf_motorista}'""")
            self.motorista = self.master.cur.fetchone()
            
            print(self.motorista)

            # self.viagem = Viagem(self)

            self.confirmacaoViagem = tk.Label(self, bg='#9EC496', text=f'O motorista {self.motorista[0]} confirmou a viagem. \nAguarde-o no local informado.\nPlaca do veículo {self.motorista[1]}')
            self.confirmacaoViagem.pack()
            self.update()

            subscribe.simple('motorista')


            self.confirmacaoMotorista = tk.Label(self, bg='#9EC496', text=f'O motorista {self.motorista[0]} já está no local informado')
            self.confirmacaoMotorista.pack()
            self.update()
            
            
            # self.textLabel.pack(fill=tk.X)

    def waitmsg(self):
        pass

    

import tkinter as tk
from .form_destino import FormDestino
# from .viagem import Viagem

from paho.mqtt import subscribe
import threading


class PainelUsuario(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.selectDestino = True

        self.msgVariable = tk.StringVar()
        self.msgVariable.set('Onde você está?')

        # self.confirmacaoViagem = True

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

        else:
            if self.master.mqtt.is_connected() == False:
                self.master.mqtt.connect_broker()
            self.master.mqtt.publish("viagem", "passageiro")

            for wid in self.winfo_children():
                wid.pack_forget()

            self.msgVariable.set('Aguardando a confirmação de um motorista')
            self.textLabel.pack()

            self.update()
            
            subscribe.simple('motorista')

            # self.viagem = Viagem(self)

            self.confirmacaoViagem = tk.Label(self, bg='#9EC496', text=f'O motorista {"jooj"} confirmou a viagem. \nAguarde-o no local informado.\nPlaca do veículo {"5asd"}')
            self.confirmacaoViagem.pack()
            self.update()

            subscribe.simple('motorista')


            self.confirmacaoMotorista = tk.Label(self, bg='#9EC496', text=f'O motorista {"jooj"} já está no local informado')
            self.confirmacaoMotorista.pack()
            self.update()
            
            
            # self.textLabel.pack(fill=tk.X)
        

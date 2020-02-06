import tkinter as tk
from .form_destino import FormDestino
from tkinter import messagebox

from paho.mqtt import subscribe


class PainelUsuario(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.selectDestino = True

        self.msgVariable = tk.StringVar()
        self.msgVariable.set('Onde você está?')

        self.rua = tk.StringVar()
        self.num = tk.IntVar()
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

        rua = self.rua.get()
        num = self.num.get()
        city = self.city.get()
        estado = self.estado.get()
        
        if len(rua) == 0 or num == 0 or len(city) == 0 or len(estado) == 0:
            messagebox.showwarning('Warning', 'Nenhum campo pode ficar em branco')
            return None

        local = self.master.db.execute(f"select id from local where local.rua = '{rua}' and local.numero = '{num}' and local.cidade = '{city}' and local.estado = '{estado}'")[0]
        if len(local) == 0:
            self.master.db.execute(f"insert into local(rua, numero, cidade, estado) values('{rua}', '{num}', '{city}', '{estado}')", insert=True)
            local = self.master.db.execute(f"select id from local where local.rua = '{rua}' and local.numero = '{num}' and local.cidade = '{city}' and local.estado = '{estado}'")[0]
        
        # print(local)
        self.master.trajetos.append(local[:])

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
            self.motorista = self.master.db.execute(f"""select nome, veiculo_placa from usuario where usuario.cpf = '{cpf_motorista}'""")[0]

            self.master.db.execute(f"insert into trajeto(local_chegada, local_saida, passageiro_cpf, motorista_cpf) values ({self.master.trajetos[1][0][0]}, {self.master.trajetos[0][0][0]}, '{self.master.user.cpf}', '{cpf_motorista}')", insert=True)


            self.confirmacaoViagem = tk.Label(self, bg='#9EC496', text=f'O motorista {self.motorista[0][0]} confirmou a viagem. \nAguarde-o no local informado.\nPlaca do veículo {self.motorista[0][1]}')
            self.confirmacaoViagem.pack()
            self.update()

            subscribe.simple('motorista')


            self.confirmacaoMotorista = tk.Label(self, bg='#9EC496', text=f'O motorista {self.motorista[0][0]} já está no local informado')
            self.confirmacaoMotorista.pack()
            self.update()
            
            


    

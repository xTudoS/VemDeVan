import tkinter as tk
import re
from PIL import ImageTk
from PIL import Image

import psycopg2
from psycopg2.extras import DictCursor


from home_page import HomePage
from db import Users
from control_admin import PainelUsuario
from mqtt import MQTT

class App(tk.Tk):
    def __init__(self, *args, **kw):
        
        tk.Tk.__init__(self)

        self.mqtt = MQTT()
        self.conn = psycopg2.connect("dbname='vemdevan' user='postgres' host='localhost' password='m249sopmod'")
        self.cur = self.conn.cursor(cursor_factory=DictCursor)
        self.regexEmail = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        # print(self.users)

        self.user = None
        
        self.email = tk.StringVar()
        self.passwd = tk.StringVar()
        
        self.iconbitmap('img/favicon.ico')
        self.resizable(width=False, height=False)
        
        self.width = self.winfo_screenwidth()//2
        self.height = self.winfo_screenheight()//2
        self.geometry(f"360x640+{self.width - 400}+{self.height - 350}")        
        # self.splashScreen = SplashScreen(self)

        self.imgBgOriginal = Image.open('img/bg.png')
        self.imgBgResize = self.imgBgOriginal.resize((360, 640), Image.ANTIALIAS)
        
        self.imgBg = ImageTk.PhotoImage(self.imgBgResize)

        self.imgBgLabel = tk.Label(self, image=self.imgBg)
        self.imgBgLabel.place(x=0, y=0)

        self.withdraw()
        self.screen = HomePage(self)

    def deiconify(self, *args, **kw):
        super().deiconify()
        if self.user.motorista:
            pass
        else:
            self.painelUsuario = PainelUsuario(self)
            self.painelUsuario.pack(pady=10)       

    def changeScreen(self, screen):
        self.screen.destroy()
        self.screen = screen
        self.update()

    def validarLogin(self):
        email = self.email.get().strip()
        passwd = self.passwd.get()

        emailValido = re.match(self.regexEmail, email)

        if emailValido == None or (0 == len(passwd) > 8):
            return None

        user = Users(email=email, passwd=passwd)

        self.cur.execute(f"""SELECT email, senha from usuario where email = '{user.email}' and senha = '{user.passwd}'""")

        self.users = self.cur.fetchall()

        if len(self.users) == 1:
            self.user = user

            return True
            

if __name__ == "__main__":
    # root = tk.Tk()
    app = App()
    app.mainloop()

import tkinter as tk

from PIL import ImageTk
from PIL import Image

class Login(tk.Toplevel):

    def __init__(self, master, *args, **kw):
        tk.Toplevel.__init__(self, master)

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

        self.imgLogoOriginal = Image.open('img/bglogo.png')
        self.imgLogoResize = self.imgLogoOriginal.resize((360, 640), Image.ANTIALIAS)
        self.imgLogo = ImageTk.PhotoImage(self.imgLogoResize)
        
        self.imgLogoLabel = tk.Label(self, image=self.imgLogo)
        self.imgLogoLabel.place(x=0, y=0)

        self.emailEntry = tk.Entry(self, textvariable=master.email)
        self.emailLabel = tk.Label(self, text="Email:", bg='#7DB871')
        

        self.emailLabel.place(x=90, y=260)   
        self.emailEntry.place(x=130, y=260)

        self.passwdEntry = tk.Entry(self, textvariable=master.passwd, show='*')
        self.passwdLabel = tk.Label(self, text="Senha:", bg='#7DB871')
        

        self.passwdLabel.place(x=90, y=290)   
        self.passwdEntry.place(x=130, y=290)

        self.button = tk.Button(self, text="Login", command=self.login)
        self.button.place(x=170, y=320)
    
    def destroy(self, exitApp=True, *args, **kw):
        super().destroy()
        if exitApp:
            exit(0)

    def login(self):

        userValido = self.master.validarLogin()

        if userValido:
            self.destroy(exitApp=False)
            self.master.deiconify()
import tkinter as tk
from control_admin import Login

from PIL import ImageTk
from PIL import Image

class HomePage(tk.Toplevel):

    def __init__(self, master, *args, **kw):
        tk.Toplevel.__init__(self, master)

        self.resizable(width=False, height=False)
        self.title('Vem de Van')
        self.iconbitmap('img/favicon.ico')

        self.geometry(f"360x640+{master.width - 180}+{master.height - 350}")

        self.master = master
        
        self.imgSplashScreenOriginal = Image.open('img/splash_screen.png')
        self.imgSplashScreenResize = self.imgSplashScreenOriginal.resize((360, 640), Image.ANTIALIAS)
        
        self.imgSplashScreen = ImageTk.PhotoImage(self.imgSplashScreenResize)

        self.imgSplashScreenLabel = tk.Label(self, image=self.imgSplashScreen)
        self.imgSplashScreenLabel.place(x=0, y=0)


        self.button = tk.Button(self, text="Abrir Painel de Controle", command=lambda : master.changeScreen(Login(master)))
        self.button.place(x=110, y=50)

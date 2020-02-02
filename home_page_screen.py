import tkinter as tk
from control_admin import Login

from PIL import ImageTk
from PIL import Image

class HomePageScreen(tk.Frame):

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)

        self.imgSplashScreenOriginal = Image.open('img/splash_screen.png')
        self.imgSplashScreenResize = self.imgSplashScreenOriginal.resize((360, 640), Image.ANTIALIAS)
        
        self.imgSplashScreen = ImageTk.PhotoImage(self.imgSplashScreenResize)

        self.imgSplashScreenLabel = tk.Label(self, image=self.imgSplashScreen)
        self.imgSplashScreenLabel.place(x=0, y=0)


        self.button = tk.Button(self, text="Abrir Painel de Controle", command=lambda : master.changeScreen(Login(master)))
        self.button.place(x=110, y=50)
import tkinter as tk
from home_page import HomePage
from db import Users

class App(tk.Tk):
    def __init__(self, *args, **kw):
        
        tk.Tk.__init__(self)

        self.users = [
            Users(email='a@a.com', passwd='1234'),
        ]
        
        self.email = tk.StringVar()
        self.passwd = tk.StringVar()
        
        self.iconbitmap('img/favicon.ico')
        self.resizable(width=False, height=False)
        
        self.width = self.winfo_screenwidth()//2
        self.height = self.winfo_screenheight()//2
        self.geometry(f"800x600+{self.width - 400}+{self.height - 350}")

        self.withdraw()
        # self.splashScreen = SplashScreen(self)
        self.screen = HomePage(self)

        self.title('Painel de Controle - Vem de Van')
        self['bg'] = 'black'

        button = tk.Button(text='Close', command=lambda : exit())
        button.pack()

    def changeScreen(self, screen):
        self.screen.destroy()
        self.screen = screen
        self.update()

    def validarLogin(self):
        email = self.email.get().strip()
        passwd = self.passwd.get()

        user = Users(email=email, passwd=passwd)

        for u in self.users:
            if u.email == user.email and u.passwd == user.passwd:
                return True


if __name__ == "__main__":
    # root = tk.Tk()
    app = App()
    app.mainloop()

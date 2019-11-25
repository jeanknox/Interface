from tkinter import *

class Interface:
    def __init__(self,master):
        self.master = master
        self.master.geometry('720x480')
        self.master.title('Tela de login')

        self.login_message = Label(self.master, text= 'Usuario', width = 30)
        # self.login_message.config(font=(, 20))
        self.login_message.grid(row=0,column=0)

        self.user = Entry(self.master, text='Usuario:', bd = 5, width= 30)
        self.user.grid(row=0,column=1)

        self.senha_message = Label(self.master, text='Senha')
        self.senha_message.grid(row=1,column=0)

        self.senha = Entry(self.master, text='Senha',bd = 5, width = 30 )
        self.senha.grid(row=1,column=1)

        self.logar = Button(self.master, text='Logar')
        self.logar.grid(row= 2, column = 1)


root = Tk()
Interface(root)
root.mainloop()

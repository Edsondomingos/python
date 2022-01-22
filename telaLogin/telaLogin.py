from tkinter import  *

def entrar():
    usuario = 'Edson'
    senha = '123'
    if entradaUser.get() == usuario and entradaPwd.get() == senha:
        i.destroy()
        s = Tk()
        s.geometry('100x100')
        s['bg'] = 'aqua'
        sucesso = Label(s,text=f'Bem vindo Sr. {usuario}')
        sucesso.pack()
        s.mainloop()
    else:
        print('usuario ou senha incorretos')

i = Tk()
i.geometry('200x100')

user = Label(i,text='Usuário')
user.pack()
entradaUser = Entry(i)
entradaUser.pack()

pwd = Label(i,text='Senha')
pwd.pack()
entradaPwd = Entry(i)
entradaPwd.pack()

btOk = Button(i,text='Entrar', command=entrar)
btOk.pack()


i.mainloop()

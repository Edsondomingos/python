from tkinter import  *

usuario = 'Edson'
senha = '123'

def entrar():
    '''Função que compara os dados digitados com as informações já salvas
        e abri uma nova tela, caso o login tenha sido bem sucedido no login.'''
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
        


#tela principal. Onde o usuário entra com os dados de login.
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

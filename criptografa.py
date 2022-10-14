from tkinter import *

alfabeto = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
alfabeto_criptografado = [
    '$1@','#3@','%76','*hh','&hy','!qd','Bnh','Asa','yuh','oi0','axa','Q3#','*uh','$EE',
    'Afw','87A','962','7as','24y','41a','11a','df5','74a','20j','74v','xyz'
]

def criptografar_senha(senha):
    senha_recebida = list(senha.upper().strip())
    cont_posicao = 0  
    for i in senha_recebida:
        for j in alfabeto:
            if i == j:
                senha_recebida[cont_posicao] = alfabeto_criptografado[alfabeto.index(j)]
        
        cont_posicao += 1
    # return "".join(senha_recebida)
    senha_cripto_label['text'] = senha_recebida
    return senha_recebida

def descriptografar_senha(senha):
    senha_recebida = senha
    cont_posicao = 0  
    for i in senha_recebida:
        for j in alfabeto_criptografado:
            if i == j:
                senha_recebida[cont_posicao] = alfabeto[alfabeto_criptografado.index(j)]
        
        cont_posicao += 1
    senha_desc_label['text'] = senha_recebida
    return "".join(senha_recebida)



i = Tk()
i.geometry('300x200')

senha_label = Label(i,text='Digite uma senha')
senha_label.pack()

senha_entry = Entry(i)
senha_entry.pack()

senha_btn = Button(i,text='Criptografar', command=lambda:criptografar_senha(senha_entry.get()))
senha_btn.pack()

senha_cripto_label = Label(i,text='')
senha_cripto_label.pack()

senha_desc_btn = Button(i,text='Descriptografar', command=lambda:descriptografar_senha(criptografar_senha(senha_entry.get())))
senha_desc_btn.pack()

senha_desc_label = Label(i,text='')
senha_desc_label.pack()


i.mainloop()
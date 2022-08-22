from tkinter import *
from random import randint


def escolha():
    maos = [0,0,0]    
    aleatorio = randint(0,2)
    maos[aleatorio] = 1
    resultado['text'] = maos
    global vezes_jogadas
    vezes_jogadas = vezes_jogadas + 1
    rodada['text'] = f'Rodada: {vezes_jogadas}'
    
vezes_jogadas = 0


tela = Tk()
tela.geometry('100x100')

jogar = Button(tela, text='Jogar', command=escolha)
jogar.pack()

resultado = Label(tela, text='')
resultado.pack()

rodada = Label(tela, text='Rodada: ')
rodada.pack()

tela.mainloop()



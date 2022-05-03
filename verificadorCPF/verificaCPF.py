from tkinter import *


 #Segundo digito verificador
def digito2(cpf):
    '''Verifica se o segundo digito verificado do cpf esta valido. Esta função só é executada se o primeiro digito estiver correto.'''
    try:    
        multiplicador = 0
        somador = 0
        resultado = 0
        for i in cpf:
            if multiplicador <= 9:
                resultado = multiplicador * int(i)
                somador += resultado
                multiplicador += 1            
        segundoDigito = somador % 11
        if segundoDigito == 10:
            segundoDigito = 0
        if segundoDigito == int(cpf[10]):
            cpfFormatado = f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}'
            resposta['text'] = f'{cpfFormatado}\nNumero  VÁLIDO'
        else:
            resposta['text'] = 'Verifique se os numeros estão corretos'
    except:
        resposta['text'] = 'Verifique se os numeros estão corretos'


def digito1(cpf):
    '''Verifica se o primeiro digito verificado do cpf esta valido.'''
    try:
        multiplicador = 1
        somador = 0
        #Multiplica os 9 digitos inicias e soma o resultado das multiplicações
        for i in cpf:
            if multiplicador <= 9:
                resultado = multiplicador * int(i)
                somador += resultado
                multiplicador += 1
        #Pega o resto da divisão da soma por 11 e verifica se o digito verificador é 10
        primeiroDigito = somador % 11
        if primeiroDigito == 10:
            primeiroDigito = 0
        if primeiroDigito == int(cpf[9]):
            digito2(cpf)
        else:
            resposta['text'] = 'Verifique se os numeros estão corretos'        
    except:
        if entradaCPF.get() == '':
            resposta['text'] = 'Digite um CPF'
        



i = Tk()
i.title('Verificador CPF')
i.geometry('300x150')

dica = Label(i, text='Digite seu cpf')
dica.pack()

entradaCPF = Entry(i)
entradaCPF.pack()

btVerificar = Button(i, text='Verificar', command=lambda:digito1(entradaCPF.get()), pady='5px',padx='5px',fg='green',font='Arial')
btVerificar.pack()

resposta = Label(i, text = '',fg='blue',font='Arial')
resposta.pack()

i.mainloop()

 

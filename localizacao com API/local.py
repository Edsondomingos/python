from requests import get
from time import sleep
from tkinter import *

def consultar():
    cidade = consulta.get()
    if cidade:
        url = f'http://api.weatherstack.com/forecast?access_key=6364bf509fa67af0af09e53280ccd974&query={cidade}'
        req = get(url)
        api = req.json()
        try:
            if  api['location']:
                res = (f"{api['location']['name']}, {api['location']['region']}, {api['location']['country']}\n"+
                        f"Temperatura: {api['current']['temperature']}°\n"+
                        f"Velocidade do vento: {api['current']['wind_speed']}\n"+
                        f"Direção do vento: {api['current']['wind_dir']}")
                resultado['text'] = res
        except:
            resultado['text'] = 'Sem Dados para informar'
    else:
        resultado['text'] = 'Digite uma cidade'

i = Tk()
i.title('Consultar Cidade')
i.geometry('400x200')
i['bg']='#555'

dica = Label(i,text='Digite uma Cidade', font='impact',bg='#555',fg='white')
dica.pack()
consulta = Entry(i)
consulta.pack()
btconsulta = Button(i, text='Consultar',command=consultar,font='arial',bg='#ff0000',fg='white')
btconsulta.pack()
resultado = Label(i,bg='#555',fg='white', font='Arial')
resultado.pack()

i.mainloop()

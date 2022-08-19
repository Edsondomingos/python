from requests import get

print('''
°Considere letras maiusculas e minusculas
°Digite "fim" para finalizar as consultas
°Não coloque espaços
''')
usuario = input('Digite o nome do usuário do github: ').strip()
while usuario != 'fim':
    try:
        req = get(f'https://api.github.com/users/{usuario}/repos')
        api = req.json()
        tamanho = 0
        print('*'*50)  
        for i in range(len(api)):
            repo = api[i]['html_url'].replace(f'https://github.com/{usuario}/', '')
            #print(api[i]['html_url'])
            print(repo)
            tamanho += 1

        print('*'*50)    
        print('Total de repositorios públicos: ',tamanho)
        print('*'*50) 
        
    except:
        print('Não coloque espaços entre as palavras')
        print('*'*50) 
    usuario = input('Digite o nome do usuário do github: ').strip()
print('Volte a consultar depois. Tchau!')

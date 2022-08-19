from random import randint

opcoes = ['Pedra','Papel','Tesoura']

while True:
    try:
        com = opcoes[randint(0,2)]
        escolha = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura5\nEscolha: '))
        j1 = opcoes[escolha-1]
        print('¨¨'*20)
        print(f'Computador -> {com} X Eu -> {j1}')
        print('¨¨'*20)
        
        if com == j1:
            print('EMPATE')
        elif com == 'Pedra' and j1 == 'Tesoura':
            print('COMPUTADOR GANHOU')
        elif com == 'Papel' and j1 == 'Pedra':
            print('COMPUTADOR GANHOU')
        elif com == 'Tesoura' and j1 == 'Papel':
            print('COMPUTADOR GANHOU')
        else:
            print('VOCÊ VENCEU')

        print('¨¨'*20)
        continuar = input('Continuar: ').lower()[0]
        print('¨¨'*20)
        if continuar == 'n':
            print('ATÉ MAIS')
            break
    except:
        print('XX'*20)
        print('opções Apenas numeros de 1 a 3')
        print('XX'*20)

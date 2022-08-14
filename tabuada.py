while True:
    
    print('ZERO termina')
    numero = int(input('Digite um numero para ver a tabuada: '))
    if numero != 0:
        for i in range(1,10):
            print(f'{numero} x {i} = {numero*i}')
    else:
        print('Volte depois')
        break



'''Tabuada de 1 a 9
for i in range(1,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')

'''

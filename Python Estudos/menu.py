n1 = int(input('Primeiro valor: '))
n2 = int(input("Segundo valor: "))
n3 = 0
while n3 != 5:
    print('''
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR''')
    n3 = int(input('Digite o numero do Menu: '))
    if n3 == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif n3 == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif n3==3:
        if n1>n2:
            print(f'Maior é o {n1}')
        elif n1<n2:
            print(f' Maior é o {n2}')
        elif n1 == n2:
            print('Os dois numeros sao iguais')
    
    elif n3==4:
        print('===Novos numeros===')
        n1=int(input("digite um novo numero:"))
        n2 = int(input("Digite segundo valor"))
    
    elif n3==5:
        print('Finalizando...')
        
    else:
        print('opçao invalida')
print('Saindo do programa...')
        

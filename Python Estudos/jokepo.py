from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Qual opção 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
comp = randint(0,2)
joke= int(input('Qual opção voce escolhe: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
print('-='*11)
print(' O Computador escolheu {}'.format(itens[comp]))
print(' Voce2 escolheu {}'.format(itens[joke]))
print('-='*11)

if comp == 0:
    if joke == 0:
        print("Deu empate")
    
    elif joke == 1:
        print('Voce ganhou')
    
    elif joke == 2:
        print("Voce perdeu")
    
    else:
        print('Opçao invalida')
elif comp == 1:
    if joke == 0:
         print( ' voce perdeu')
    elif joke == 1:
        print(' voce empatou ')

    
    elif joke == 2:
        print (" voce ganhou")
    
    else:
        print('opçao invalida')

elif comp == 2:
    if joke == 0:
         print("voce ganhou")
    
    elif joke == 1:
        print("voce perdeu")
    
    elif joke == 2:
        print('voce empatou')
    
    else:
        print('opçao invalida')

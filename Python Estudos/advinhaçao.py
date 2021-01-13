from random import randint
comp = randint(0,10)
print("sou seu computaodor.. pensando em numero de 0 a 10")
print("Sera que consegue advinhar qual foi ? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual seu palpite: '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais... tente novamente')
        elif jogador > comp:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas.'.format(palpites))
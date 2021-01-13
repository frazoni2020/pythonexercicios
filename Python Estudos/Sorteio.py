import random
lista = []
while True:
    lista.append(str(input('Digite o nome do funcionário para confirmar sua inscrição no sorteio: ')))
    continuar = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Quem leva o par de ingressos é {}'.format(random.choice(lista)))
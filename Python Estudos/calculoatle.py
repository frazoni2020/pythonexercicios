from datetime import date
anoAtual = date.today().year
nasc = int(input("qual ano voce nasceu: "))
idade = anoAtual - nasc
if idade >= 19 and idade<25:
    print("voce é um atleta Senior")
elif idade >=9 and idade<14:
    print('Atleta INFANTIL')
elif idade>=14 and idade<19:
    print('Atleta JUNIOR')
elif idade <9:
    print("Mirim")
elif idade>25:
    print("Voce é um atleta MASTER")

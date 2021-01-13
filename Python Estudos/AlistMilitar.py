from datetime import date
atual = date.today().year
nasc = int(input('Qual ano voce nasceu: '))
idade = atual - nasc
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para seu alistamento')
    print(f' Voce nasceu em {nasc} e tem {idade} anos ainda não chegou o momento de voce se alistar')
elif idade == 18:
    print(f'voce tem {idade} anos , vá se alistar IMEDIATAMENTE!') 

elif idade>18:
    saldo = idade - 18
    print(f'ja passou {saldo} anos do seu alistamento')
    print(f'voce nasceu em {nasc} e tem {idade} anos')

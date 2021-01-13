nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1+nota2) / 2
if media>=5 and media<7:
    print(f"sua media foi {media} e voce esta em recuperação")
elif media<7.0:
    print(f'a sua media foi {media} voce esta reprovado!')
elif media>=7.0:
    print(f'A sua media foi {media} voce esta aprovado') 
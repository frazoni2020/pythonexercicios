tot18 = 0
sexm1 = 0
sexf1 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("SEXO [F/M]")).upper().strip()[0]
    if idade >=18:
        tot18+=1
    if sexo == "M":
        sexm1+=1
    if sexo == "F":
        sexf1+=1
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer Continuar [S/N]')).upper().strip()[0] 
    if resp == "N":
        print("Programa encerrado")
        break
print(f'''
QUANTIDADE DE USUARIOS MAIORES DE 18 FORAM : {tot18}
SEXO MASCULINO FORAM {sexm1}
SEXO FEMININO FORAM {sexf1}''')
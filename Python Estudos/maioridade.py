from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    ano = int(input(f"Em que ano a {pess}º pessoa nasceu"))
    idade =  atual - ano
    if idade >=21:
        totmaior +=1
    else:
        totmenor +=1
print(f'ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'ao todo tivemos {totmenor} pessoa menores de idade')
somaidade=0
mediaidade=0
maioridade = 0
nomevelho = 0
totmulher20 = 0
for p in range (1,5):
    print(f'----{p}ª PESSOA -----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade+=idade
    if p == 1 and sexo in "Mm":
        maioridade = idade 
        nomevelho = nome
    if sexo in "Mm" and idade >maioridade:
        maioridade=idade
        nomevelho=nome
    if sexo in "Ff" and idade<20:
        totmulher20+=1
mediaidade=somaidade/4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')
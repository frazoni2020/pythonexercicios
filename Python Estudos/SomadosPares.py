soma = 0
cont = 0
for c in range(0,6):
    n1=int(input('digite um numero:  '))
    if n1 % 2 == 0:
        cont = cont+1
        soma = soma+n1
print(f' voce informou {cont} numeros pares e a soma foi {soma}')
        
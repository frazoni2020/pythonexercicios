ValorCasa= float(input('Qual valor da Casa :R$ '))
Salario = float(input('Qual seu Salario :R$ '))
Financiamento = int(input('quantos anos pretende pagar: '))
prestacao = ValorCasa / (Financiamento*12)
minimo = Salario*30/100
print('para pagar uma casa de  R${:.2f} em {} anos'.format(ValorCasa,Financiamento),end='')
print(' A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('ESTA APROVADO SEU FINANCIAMENTO')
else:
    print("Desculpe mas o financiamento será negado")
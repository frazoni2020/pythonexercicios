from datetime import date
atual = date.today().year
SalarioBruto = float(input('Qual seu salário: R$ '))
NumMeses = int(input(f'quantos meses trabalhados em {atual}: '))
PrimParcela = (NumMeses/12) * SalarioBruto/2
print(f'O valor da primeira parcela é R${PrimParcela}')
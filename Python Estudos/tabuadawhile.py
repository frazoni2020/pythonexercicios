while True:
    n= int(input('Que ver tabuada de qual valor: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c}x{n} = {c*n}')
print('Programa de Tabuada encerrado')
   
times = ('São Paulo','Internacional','Atlético-MG','Flamengo','Grêmio','Palmeiras','Fluminense','Santos','Corinthians','Athletico')
opçao = int(input('''
Escolha a sua opção
[1]Os 5 PRIMEIROS DA TABELA
[2]O ULTIMO DA TABELA
[3] EM ORDEM ALFABETICA
RESPOSTA : ''' ))
if opçao == 1:
    print('Os 5 primeiros são')
    for t in range (0,len(times[0:5])):
        print(times[t])
elif opçao == 2:
    for t in range (0,len(times[-2])):
        print(times[t])







#    for t in range(0,len(times[0:5])):
#       print(times[t])
   


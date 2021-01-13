primeiro = int(input('O primeiro Termo: '))
razao = int(input('A razao: '))
decimo = primeiro + (10-1)*razao
for c in range (primeiro,decimo+razao,razao):
    print(f'{c}',end="-")
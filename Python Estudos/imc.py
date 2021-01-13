peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu imc é {:.1f} voce está abaixo do peso'.format(imc))
elif imc>=18.5 and imc<24.9:
    print('voce esta com o imc de {:.1f} esta com peso normal'.format(imc))  
elif imc>= 25 and imc<29.9:
    print("voce esta com imc{:.1f} esta com Sobrepeso".format(imc)) 
elif imc>30.0 and imc<34.9:
    print("seu imc é {:.1f}esta OBESIDADE GRAU 1".format(imc))
elif imc>35 and imc<39.9:
    print("Seu imc é {:.1f} e esta com OBESIDADE GRAU 2".format(imc))
else:
    print("Seu imc é {:.1f} esta com OBESIDADE GRAU 3".format(imc))
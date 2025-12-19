#coletar váriaveis de peso e altura
peso = int(input("Qual é o seu peso (em quilogramas)?"))
altura = float(input("Qual é a sua altura (em metros, ex: 1.73)?"))

#calculo do imc
imc = peso / (altura ** 2)

#diz o imc exato ao usúario
print("Seu IMC é de", round(imc, 1))

#classifica o imc
if imc < 18.5:
    print("Você está abaixo do peso saudável.")
elif imc < 25:
    print("Seu peso está saudável :)")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade de Grau 1.")
elif imc < 40:
    print("Você está com obesidade de Grau 2.")
else:
    print("Você está com obesidade de Grau 3.")
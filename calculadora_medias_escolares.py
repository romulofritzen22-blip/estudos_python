#entrada
while True:
    nota1 = float(input("Qual é a sua nota do 1° trimestre?"))
    nota2 = float(input("Qual é a sua nota do 2° trimestre?"))
    nota3 = float(input("Qual é a sua nota do 3° trimestre?"))

#validação
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        print("Erro, insira uma nota válida (entre 0 e 10).\n")
    else:
        break

#média
mediafinal = (nota1 + nota2 + nota3) / 3
print("Sua nota final é", round(mediafinal, 1))

#classificação
if mediafinal >= 6:
    print("Aprovado :D")
elif mediafinal >= 4 and mediafinal < 6:
    print("Recuperação :/")
else:
    print("Reprovado :C")
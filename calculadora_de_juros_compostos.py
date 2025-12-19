#coleta dados do usuário
valor_inicial = float(input("Valor inicial: "))
taxa_mensal = float(input("Taxa de juros (mensal): "))
meses = int(input("Tempo investido (meses): "))

#transforma a porcentagem em decimal
taxa_mensal = taxa_mensal / 100

#fórmula dos juros compostos
montante_final = valor_inicial * (1 + taxa_mensal) ** meses

#calcula os juros
juros = montante_final - valor_inicial

#imprime as informações ao usuário
print("Ao final de", meses, "meses você terá um valor total de", round(montante_final, 2),", sendo desse valor", round(juros, 2), "o rendimento de juros.")


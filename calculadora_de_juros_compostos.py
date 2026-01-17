#coleta dados do usuário
valor_inicial = float(input('Valor inicial: R$'))
taxa_mensal = float(input('Taxa de juros (mensal): '))
meses = int(input('Tempo investido (meses): '))

#transforma a porcentagem em um número decimal 
taxa_mensal = taxa_mensal / 100 + 1

#fórmula dos juros compostos
montante_final = valor_inicial * taxa_mensal ** meses

#imprime as informações ao usuário
print(f'Ao final de {meses} meses você terá um valor total de R${montante_final:.2f} sendo desse total R${montante_final - valor_inicial:.2f} o rendimento de juros.')

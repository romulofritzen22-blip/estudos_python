nome = input('Digite o seu nome: ')
print(f'Olá {nome}! Bem-vindo à BugBurger.')

lanche = int(input('Selecione o seu lanche digitando o código correspondente: \n' \
'[ 1 ] BugBurger Simples (R$15,00) \n' \
'[ 2 ] MegaBug com Bacon (R$25,00) \n' \
'[ 3 ] Smash Bug Duplo (R$30,00) \n' \
'Sua escolha: '))

totalpedido = 0 
if lanche == 1:
    totalpedido += 15
elif lanche == 2:
    totalpedido += 25
elif lanche == 3: 
    totalpedido += 30
else:
    print('Opção Inválida.')

adicional = input('Deseja adicionar Batata Frita por R$10,00? (Digite S para Sim ou N para Não) \n'
'Sua escolha: ')
if adicional == 'S' or adicional == 's':
    totalpedido += 10

print(f'O total do seu pedido é R${totalpedido}')

pagamento = float(input('Informe o valor em dinheiro fornecido para o pagamento: R$'))

if pagamento < totalpedido:
    print(f'Pagamento recusado. Faltam R${totalpedido - pagamento}')
elif pagamento == totalpedido:
    print('Pagamento aprovado. Sem troco. O seu pedido está em preparação.')
elif pagamento > totalpedido:
    print(f'Pagamento aprovado. O seu troco é de R${pagamento - totalpedido}. O seu pedido está em preparação.')
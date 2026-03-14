#Trabalho avaliativo do curso SENAI que meus amigos estão fazendo em JS e eu quis fazer em Python XD

#coleta váriaveis base
id = int(input('Digite seu ID: '))
senha = input('Digite a sua senha: ')
horario = int(input('Digite o horário atual (ex: 0, 7, 18, 22...): '))

#verificação
captcha = id * 2 - horario
resposta = int(input('Desafio de Segurança: Quanto é o seu (ID vezes 2) menos a hora atual? \nResposta: '))

if resposta != captcha:
    print('ERRO DE SEGURANÇA! INVASOR DETECTADO.')

elif id < 1000 or id > 9999:
    print('ERRO DE SEGURANÇA! INVASOR DETECTADO.')

#aluno
elif id >= 1000 and id <= 1999:
    if senha == 'aluno123':
        if horario >= 8 and horario <= 22:
            opcao = int(input('Acesso liberado, Aluno. Digite: \n[ 1 ] Calcular média \n[ 2 ] Simulador de mensalidade \nSua opção: '))
            if opcao == 1:
                n1 = float(input('Primeira nota: '))
                n2 = float(input('Segunda nota: '))
                n3 = float(input('Terceira nota: '))
                media = (n1 + n2 + n3) / 3
                if media >= 7:
                    print(f'Sua média é {media:.2f}, você foi aprovado.')
                elif media >= 5:
                    print(f'Sua média é {media:.2f}, você ficou de recuperação!')
                else:
                    print(f'Sua média é {media:.2f}, você foi reprovado.')
            elif opcao == 2:
                mensalidade = float(input('Digite o valor da mensalidade: R$'))
                adiantamento = input('Vai pagar adiantado? (S/N) \nSua opção: ')
                if adiantamento == 's' or adiantamento == 'S': 
                    print(f'O valor da sua mensalidade é de R${mensalidade * 0.9}')
                else:
                    print(f'O valor da sua mensalidade é de R${mensalidade}')
            else:
                print('ERRO! Opção inválida.')
        else:
            print('Horário Inválido!')
    else:
        print('Acesso negado! Credencias inválidas.')

#professor
elif id >= 2000 and id <= 2999:
    if senha == 'prof2026':
        opcao = int(input('Acesso Liberado, Professor. Digite: \n[ 1 ] Adicional Noturno \n[ 2 ] Classificar Turma \nSua opção: '))
        if opcao == 1:
            salario = float(input('Salário: R$'))
            aulas_noturnas = int(input('Aulas noturnas dadas: '))
            print(f'Seu salário total é de R${salario + aulas_noturnas * 50:.2f}')
        elif opcao == 2:
            nota_turma = float(input('Nota geral da turma: '))
            if nota_turma >= 8:
                print('Turma excelente!')
            else:
                print('Turma em atenção!')
        else:
            print('Opção Inválida.')
    else:
        print('Acesso negado! Credencias inválidas.')

#diretor
elif id == 9999:
    if senha == 'adminSENAI':
        opcao = int(input('Acesso VIP, Diretoria. Escolha: \n[ 1 ] Balanço Financeiro \nSua opção: '))
        if opcao == 1: 
            receita = float(input('Qual é o total de receitas? R$'))
            despesa = float(input('Qual é o total de despesas? R$'))
            lucro = receita - despesa
            if lucro > 0:
                print(f'Lucro de R${lucro}')
            elif lucro < 0:
                print(f'Prejuízo de R${lucro}')
            else:
                print('Saldo Zero')
    else:
        print('Acesso negado! Credencias inválidas.')
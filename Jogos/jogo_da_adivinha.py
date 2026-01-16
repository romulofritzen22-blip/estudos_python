from random import randint
decoline = 22
computer_num = randint(1, 10)

print('\033[33m-=' * decoline * 2)

print('\033[4;34mJogo da Sorte!\033[m')

print('\033[33m-=' * decoline)

print('\033[34mEstou pensando em um número entre 1 e 10...')
user_num = int(input('\033[34mVocê consegue adivinhar qual é? \033[33m '))

print('\033[33m-=' * decoline)

while True:
    user_num = int(input('\033[34mVocê \033[1;31mERROU \033[34mTente novamente: \033[33m'))
    if computer_num != user_num:
        print('\033[33m-=' * decoline)
    else:
        break

print('\033[33m-=' * decoline)       

print(f'\033[34mVocê \033[1;32mACERTOU\033[34m! Eu pensei no {user_num}!')

print('\033[33m-=' * decoline)
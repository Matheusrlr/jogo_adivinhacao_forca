import random


def jogar_adivinhacao():

    rodada = 0

    pontos = 100

    numero_secreto =  random.randrange(1,101)

    # print ('O número secreto é o {}'.format(numero_secreto))
    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    print('Escolha o nível de dificuldade \n(1) fácil, (2) médio ou (3) difícil')

    nivel = int(input())

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 6    
    elif(nivel == 3):
        tentativas = 3
    else:
        print('o valor digitado não é válido')



    for i in range (tentativas):

        rodada = rodada + 1

        print('Tentativa {} de {}'.format(rodada, tentativas))

        chute = input('Digite um número entre 1 e 100: ')

        numero = int(chute)

        print('Você digitou:', numero)

        subtracao = abs(numero_secreto - numero)

        pontos = pontos - subtracao

        if(numero < 1 or numero > 100):
            print('O número deve ser um inteiro maior que 1 e menor que 100')
            continue

        menor = numero < numero_secreto

        if (numero == numero_secreto):
            print('Você acertou')
            print('Você tem {} pontos'.format(pontos) )
            break
        else :
            if(numero > numero_secreto):
                print('Errrou pra cima')
                print('Você tem {} pontos'.format(pontos) )
                if(rodada == tentativas):
                    print('Você errou e o número secreto era o {} e você fez {} pontos'.format(numero_secreto, pontos))
            elif (menor):
                print('Errrou pra baixo')
                print('Você tem {} pontos'.format(pontos) )
                if(rodada == tentativas):
                    print('Você errou e o número secreto era o {} e você fez {} pontos'.format(numero_secreto, pontos))

    print('Fim de jogo')                 

if (__name__ == "__main__"):

    jogar_adivinhacao()

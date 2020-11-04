import random



def jogar_forca():

    imprime_abertura()

    palavra_secreta = carregar_arquivo('linguagens.txt')


    letras_corretas = ['_' for letra in palavra_secreta]

    enforcou = False

    acertou = False

    erros = 0

    while(not enforcou and not acertou):

        chute = palpite()

        print(chute)
        if(chute in palavra_secreta):
            preenche_forca(palavra_secreta, chute, letras_corretas)
        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou =  '_' not in letras_corretas
            

    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)  




def imprime_abertura():
    print('**************************')
    print('Bem vindo ao jogo da Forca')
    print('**************************')    


def carregar_arquivo(nome_arquivo = 'palavras.txt'):
    arquivo = open(nome_arquivo, 'r')
    palavras = []

    for i in arquivo:
        i = i.strip()
        palavras.append(i)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero_aleatorio].upper() 

    return palavra_secreta 

def palpite():
    chute = input('Qual a próxima letra? ')
    chute = chute.upper().strip()

    return chute      

def preenche_forca(palavra_secreta, chute, letras_corretas):
    index = 0
    for letra in palavra_secreta :
        if(chute == letra):
            letras_corretas[index] = letra
        index += 1   

    print('Letra encontrada nas posições {}, {}'.format(index,letras_corretas))

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()        



if (__name__ == "__main__"):
    jogar_forca()    

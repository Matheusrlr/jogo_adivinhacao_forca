import adivinhacao
import forca



print('*******************')
print('Escolha o seu jogo!')
print('*******************')

print('(1) Adivinhação (2) Forca')

escolha = int(input())


if(escolha == 1):
    print('Você escolheu Adivinhação')
    adivinhacao.jogar_adivinhacao()

elif(escolha == 2):    
    print('Você escolheu Forca')
    forca.jogar_forca()
else:
    print('Digite um número válido')    
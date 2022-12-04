import jogadas
from jogadas import calcularJogada
from cliente import cliente
from servidor import servidor

escolha = int(input("Você deseja jogar como? 1-Cliente / 2-Servidor: "))

if(escolha == 1):
    cliente()

if(escolha == 2):
    servidor()

from random import randrange
import enum

def avaliarJogadas(jogada1,jogada2):
    if(jogada1 == jogada2):
        return True
    if(jogada1 == jogada.pedra.value):
        return jogada2 == jogada.tesoura.value or jogada2 == jogada.lagarto.value
    if(jogada1 == jogada.tesoura.value):
        return jogada2 == jogada.papel.value or jogada2 == jogada.lagarto.value
    if(jogada1 == jogada.spock.value):
        return jogada2 == jogada.tesoura.value or jogada2 == jogada.pedra.value
    if(jogada1 == jogada.lagarto.value):
        return jogada2 == jogada.papel.value or jogada2 == jogada.spock.value
    if(jogada1 == jogada.papel.value):
        return jogada2 == jogada.pedra.value or jogada2 == jogada.spock.value
    return 0

def calcularJogada():
    return randrange(5)

class jogada(enum.Enum):
    pedra = 0
    spock = 1
    papel = 2
    tesoura = 3
    lagarto = 4


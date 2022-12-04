import socket
from jogadas import *

import jpysocket as jpy

def cliente():
    HOST = '127.0.0.1'
    PORT = 5000
    contador = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vitoriasCliente = 0
    vitoriasServidor = 0
    sock.connect((HOST, PORT))

    while True:
        contador +=1
        jogadaCliente = calcularJogada()
        sock.sendall(jpy.jpyencode(str(jogadaCliente)))

        data = sock.recv(1024)

        jogadaServidor = int(data.decode().upper())

        vencedor = avaliarJogadas(jogadaCliente, jogadaServidor)
        if(vencedor):
            vitoriasCliente +=1
            jogVencedor = "Cliente"
        else:
            vitoriasServidor +=1
            jogVencedor = "Servidor"

        resultado = str(contador) + " - " + "Servidor: " + jogada(jogadaServidor).name + " / " + "Cliente: " + jogada(jogadaCliente).name + " - " + "Vencedor " + jogVencedor
        print(resultado)

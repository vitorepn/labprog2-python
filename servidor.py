import socket
import random
from jogadas import jogada
from jogadas import avaliarJogadas
from jogadas import calcularJogada

def servidor():
    HOST = 'localhost'
    PORT = 5000
    addr = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    sock.bind(addr)

    sock.listen(5)

    print("Aguardando conexão de um cliente:")

    conn, ender = sock.accept()

    print('Connectado com', ender)
    print("\nOs palpites do servidor são ALEATÓRIOS!\n")
    contador = 0

    while contador<15:
        contador+=1
        data = conn.recv(1024)

        print("Resposta do cliente:", data.decode())

        if not data:
            print("\nConexão encerrada!\n")
            conn.close()
            break

        palpiteClient = data.decode()
        palpiteServ = calcularJogada()

        print("* O Servidor respondeu:", palpiteServ)

        vencedor = avaliarJogadas(palpiteServ,palpiteClient)

        if(vencedor == True):
            ganhador = 'Servidor'
        else:
            ganhador = 'Cliente'

        if (palpiteClient == palpiteServ):
            ganhador = 'Empate'

        result = '- Cliente: ' + str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> GANHADOR: ' + str(ganhador) + '\n'
        conn.sendall(bytes(str(result), 'utf8'))
    sock.close()
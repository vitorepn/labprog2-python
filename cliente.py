import socket
from jogadas import calcularJogada

def cliente():
    HOST = '127.0.0.1'
    PORT = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOST, PORT))

    while True:

        mensagemEnvioClient = calcularJogada()

        sock.sendall(str.encode(str(mensagemEnvioClient)))

        print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient)

        data = sock.recv(1024)

        print('\n*** Resultado final do jogo: \n', data.decode().upper())
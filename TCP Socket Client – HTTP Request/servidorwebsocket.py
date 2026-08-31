import socket

HOST = '127.0.0.1'
PORT = 6789

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f'Servidor rodando em {HOST}:{PORT}')

    conn, addr = s.accept()

    with conn:
        print('Conectado por:', addr)

        data = conn.recv(1024)
        print('Recebido:', data)

        conn.sendall(b'Hello!')

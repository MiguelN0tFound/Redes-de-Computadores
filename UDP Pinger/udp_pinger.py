import socket, time
HOST = '127.0.0.1'
PORT = 6789

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(1)
    message = b'Ping'
    for i in range(10):
        start = time.time()
        s.sendto(message, (HOST, PORT))
        try:
            data, server = s.recvfrom(1024)
            
            end = time.time()
            rtt = end - start
            print('RTT: ', rtt, 'seconds')
        except socket.timeout:
            print('Request timed out')
    


    


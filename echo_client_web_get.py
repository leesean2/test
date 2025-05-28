import socket

HOST = '220.149.232.226'
PORT = 10022

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    request = (
            "GET /greet?username=lee HTTP/1.1\r\n"
            f"HOST: {HOST}:{PORT}\r\n"
            "Connection: closer\r\n"
            "\r\n"
        )
    s.sendall(request.encode('utf-8'))

    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    print(response.decode('utf-8'))


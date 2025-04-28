import socket

ports = [22, 80, 9999]
host = "127.0.0.1"

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

    sock.close()

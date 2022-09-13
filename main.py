import socket
with open('hostname.txt', 'w') as f:
    f.write(f'Hello from {socket.gethostname()}')
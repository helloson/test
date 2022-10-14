import socket
with open('hostname2.txt', 'w') as f:
    f.write(f'Hello from {socket.gethostname()}')
    
  Good

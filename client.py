import socket

HOST = '192.168.43.88'    # The remote host
PORT = 8443              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('12345')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

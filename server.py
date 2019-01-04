import socket
import time
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
qrValues = {"54321","12345","1234"}
#print 'Connected by', addr
while 1:

    conn, addr = s.accept()
    data = conn.recv(1024)
    #if not data: break
    if data in qrValues:
    #time.sleep(5)
        conn.sendall("good")
    else:
        conn.sendall("bad")
conn.close()

from socket import *
import sys

s = socket(AF_INET,SOCK_STREAM)
port = int(sys.argv[2])
s.connect((sys.argv[1],port))
s.send("GET /hello.html HTTP/1.0\n\n")
data = s.recv(4096)
print(data)

s.close()
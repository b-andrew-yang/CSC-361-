import socket
import sys
from datetime import datetime
from time import time

main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('',12000))
        
    except socket error:
        print "failed to connect to socket"
        sys.exit()

    host = "localhost"
    port = args[2]

    counter = 10
    i = 0

    while(1):
        message = "ping "
        msg = raw_input(message + str(i))
        i+=1

        try:
            s.sendto(msg, (host, port))

            a = datetime.now()
            
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]

            print("Reply from " + str(addr) + " " + str(reply) + "date")

        except socket.error, msg:
            print("Error code: " + str(msg[0]) + " Message " + msg[1])
            sys.exit()


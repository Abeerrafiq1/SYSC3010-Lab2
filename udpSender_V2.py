# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
message = "Message"

while 1:
#    print ("Enter data to transmit: ENTER to quit")
#    data = sys.stdin.readline().strip()
    for i in range(1, n):
        data = message + i
        if not len(data):
            break
    #    s.sendall(data.encode('utf-8'))
        s.sendto(data.encode('utf-8'), server_address)

s.shutdown(1)


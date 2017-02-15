import socket
import sys
import datetime

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    s_time = datetime.datetime.now()
    s_time = s_time.strftime('%y/%b/%a %I:%M:%S:%f')
    print ("request sent at  {}".format(s_time))
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data
    r_time = datetime.datetime.now()
    r_time = r_time.strftime('%y/%b/%a %I:%M:%S:%f')
    print ("reply  recieved at  {}".format(r_time))

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

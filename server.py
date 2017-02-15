import socket
import sys
import datetime
import argparse

def run_server(server_ip):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Bind the socket to the port
	server_address = (server_ip, 10000)
	print ('starting up on %s port %s' % server_address)
	sock.bind(server_address)

	while True:
		print ('\nwaiting to receive message')
		data, address = sock.recvfrom(4096)
		recieve_time = datetime.datetime.now()
		recieve_time = recieve_time.strftime('%y/%b/%a %I:%M:%S:%f')
		print(recieve_time)
		
		print ( 'received {} bytes from {}'.format(len(data), address))
		msg = datetime.datetime.now()
		msg = msg.strftime('%y/%b/%a %I:%M:%S:%f')
		msg =  'recieve_time ' + recieve_time + ' ' + 'send_time ' + msg
		print ("{}".format(msg))
		if msg:
			sent = sock.sendto(msg, address)
			print ('sent {0} bytes back to {1}'.format(sent, address))

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--ip", help="ip of the server",
                           type=str, default='localhost', required=False)
    args = argparser.parse_args()
    run_server(args.ip)

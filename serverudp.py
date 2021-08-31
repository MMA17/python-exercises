from client import MESSAGE
import socket
  
UDP_IP = "::" # = 0.0.0.0 u IPv4
UDP_PORT = 6006

sock = socket.socket(socket.AF_INET6, # Internet
						socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print ("IP: " + str(addr) + "    message:" + str(data))
    MESSAGE = "Hello " + str(addr)
    sock.sendto(MESSAGE.encode(), addr)
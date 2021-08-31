import socket

HOST = '::1' # <= IPv6 máy chạy file servertcp.py
PORT = 6006  # <= Port máy chạy file servertcp.py
message = input("Nhap thong diep: ")
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    data = s.recv(1024)

print(repr(data))
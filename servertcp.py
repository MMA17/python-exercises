import socket

HOST = '::' # <= IPv6 máy chạy file servertcp.py
PORT = 6006 # <= Port máy chạy file servertcp.py

f = open("ThongDiepTuClient.txt", "a")

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        # print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(str(data))
            f.write("\n")
            MESSAGE = "Xin chao, " + str(addr)
            conn.sendall(MESSAGE.encode())

f.close()
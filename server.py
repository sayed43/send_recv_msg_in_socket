import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=7634

s.bind((host,port))
s.listen(1)

con,addr=s.accept()
print("connected with",addr)
while True:
    messg=input("send message to client: ")
    con.send(messg.encode())
    print("waiting for response")
    c_messg=con.recv(1024)
    print("message from client: ",c_messg.decode())



import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=7634

s.connect((host,port))
while True:
    print("wating for response")
    s_messg=s.recv(1024)
    print("message from server: ",s_messg.decode())
    c_messg=input("send message to server: ")
    s.send(c_messg.encode())
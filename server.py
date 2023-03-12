import threading
import socket
import to
HEADER=64
PORT=5045
SERVER=socket.gethostbyname(socket.gethostname())
#SERVER="localhost"
#SERVER="127.0.0.1"
#print(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="dISCONNECTED"
print(SERVER)
#C:\Users\Sebin\OneDrive\program\python\pyhton machine learning\socket_programming
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class seb(object):
    def __init__(self):
        self.x=34
    def f(self):
        print(self.x)


e="hfghghfghgh"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    
    #conn.send(f"yoooo000000oooooooooooooooooooooooooooooooooooooo {e}".encode(FORMAT))
    
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            
            
            if msg == DISCONNECT_MESSAGE:
                connected=False
        
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            #conn.send(d.decode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(F"[LISTINING] server is listing on {SERVER}")
    while True:
        conn, addr=server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STRARTING] server is starting...")
start()

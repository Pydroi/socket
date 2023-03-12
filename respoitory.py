"""import threading
import socket
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
#SERVER="127.0.0.1"
#print(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="dISCONNECTED"


server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print("[NEW CONNECTION] {}")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected=False
        
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(F"[LISTINING] server is liting on {SERVER}")
    while True:
        conn, addr=server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STRARTING] server is starting...")
start()


from ctypes import addressof
import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#s.bind((socket.gethostbyname(socket.gethostname()),135))

#SERVER = socket.gethostbyname(socket.gethostname())
import threading
import socket
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
#SERVER="127.0.0.1"
#print(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="dISCONNECTED"


server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected=False
        
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTINING] server is liting on {SERVER}")
    while True:
        conn, addr=server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STRARTING] server is starting...")
start()
s.listen()

print("Listening.....")

while True:
    client,address=s.accept()
    print("connected to {}".format(address))
    message="hello client"
    client.send(message.encode("ascii"))
    client.close()



import threading
import socket





import threading
import socket
HEADER=64
PORT = 5050
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER="192.168.0.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    #print(client.recv(2048).decode(FORMAT))

send("hello world")




PORT = 5050
SERVER =socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{addr}] {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print('[SERVER STARTED]!')
    server.listen()
    while True:
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
"""
#client

"""
import socket

HEADER = 64
PORT=5050

FORMAT="utf-8"

DISCONNECT_MESSAGE="DISCONNECT00"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b" " *(HEADER -len(send_length))
    client.send(send_length)
    client.send(message)


send("hello world")
send("hello everyone")
send("hi")


#send(DISCONNECT_MESSAGE)
import socket
import time

PORT = 5050
SERVER = "192.168.0.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect()
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()

SERVER="192.168.0.6"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            
            
            if msg ==DISCONNECT_MESSAGE:
                CONNECTED=False
            print(f"[{addr}]  {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr =server.accept()
        thread=threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
    


print("[SARTING]server is starting")
start()"""

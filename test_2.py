import socket			

# 1. Create socket
# socket parameter socket.AF_INET(IPv4),socket.SOCK_STREAM(TCP)<->socket.SOCK_DGRAM(UDP)
# socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)-default

s = socket.socket()	
print ("Socket successfully created")

# 2. for binding, assign port
port = 1500		

# 3. To bind ip,port
s.bind(('', port))		
print ("Socket binded to %s" %(port))

# 4. lisen status with waiting parameter
s.listen(10)	
print ("socket is listening")		

# 5. Start accept 
while True:

    # Establish connection with client.
    # accept() -> (conn,address)
    # conn->데이터를 보내고 받을 수 있는 새로운 소켓 객체, addr->연결의 다른 끝에 있는 소켓에 바인드 된 주소.
    c, addr = s.accept()	
    print ('Got connection from', addr )

    # send data
    # sendall -> send data until all data sending or error occur 
    # if success return none
    c.send('Thank you for connecting server'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
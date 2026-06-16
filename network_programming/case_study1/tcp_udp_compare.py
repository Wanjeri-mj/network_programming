# File: tcp_udp_compare.py
import socket
import sys

# Get tothe mode from the terminal argument (defaults to 'tcpclient')
mode = sys.argv[1] if len(sys.argv) > 1 else "tcpclient"

# TCP VERSION (Connection-Oriented)
if mode == "tcpserver":
    # SOCK_STREAM specifies TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 6000))
    s.listen(1)
    print("TCP Server listening on port 6000...")
    
    conn, addr = s.accept() # Establishes a dedicated connection line
    print(f"Received from TCP client: {conn.recv(1024).decode()}")
    conn.sendall(b"TCP ACK: Connection stable and verified.")
    conn.close()

elif mode == "tcpclient":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 6000)) # Handshakes with the server first
    s.sendall(b"Hello through TCP")
    print(f"Server Response: {s.recv(1024).decode()}")
    s.close()

#UDP VERSION (Connectionless)
elif mode == "udpserver":
    # SOCK_DGRAM specifies UDP (Datagrams)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 6001))
    print("UDP Server listening on port 6001...")
    
    # Notice: No s.accept() here! It just grabs the packet out of the air.
    data, addr = s.recvfrom(1024) 
    print(f"Received from UDP client: {data.decode()}")
    s.sendto(b"UDP ACK: Packet caught.", addr)

elif mode == "udpclient":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Notice: No s.connect()! We just fire the message directly to the target address.
    s.sendto(b"Hello through UDP", ("127.0.0.1", 6001))
    
    data, addr = s.recvfrom(1024)
    print(f"Server Response: {data.decode()}")
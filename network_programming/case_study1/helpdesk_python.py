# File: helpdesk_python.py
import socket
import sys

HOST = "127.0.0.1"  # Localhost (your own computer)
PORT = 5000         # The port number the server listens on

def run_server():
    ticket = 1
    # AF_INET = IPv4, SOCK_STREAM = TCP protocol
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Allows reusing the port quickly after closing the server
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Helpdesk server running on {HOST}:{PORT}")
        
        while True:
            # server.accept() blocks and waits for a client to connect
            conn, addr = server.accept()       
            with conn:
                # Receive data (up to 1024 bytes) and decode from bytes to string
                request = conn.recv(1024).decode()
                print(f"Received from {addr}: {request}")
                
                # Format response and increment ticket number
                response = f"Request received. Ticket number: HD{ticket:03d}"
                conn.sendall(response.encode())  # Convert string to bytes and send
                ticket += 1

def run_client():
    reg = input("Registration number: ").strip()
    issue = input("Issue: ").strip()
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            # Send data as bytes
            client.sendall(f"{reg}: {issue}".encode())
            # Receive and print the server's reply
            reply = client.recv(1024).decode()
            print(f"Server response: {reply}")
    except ConnectionRefusedError:
        print("Server is not running or is unreachable.")

if __name__ == "__main__":
    # Check command-line arguments to see whether to run server or client
    if len(sys.argv) > 1 and sys.argv[1].lower() == "server":
        run_server()
    else:
        run_client()
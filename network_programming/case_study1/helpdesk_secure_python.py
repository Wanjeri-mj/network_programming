import socket
import threading
import datetime

HOST, PORT = "127.0.0.1", 5001
TOKEN = "NET123|"
ticket = 1
lock = threading.Lock()

def handle_client(conn, addr):
    global ticket
    print(f"[CONNECTED] Client connected from {addr}")
    with conn:
        line = conn.recv(1024).decode().strip()
        if not line.startswith(TOKEN):
            conn.sendall(b"Rejected: invalid token")
            return
        request = line[len(TOKEN):].strip()
        if len(request) < 5:
            conn.sendall(b"Rejected: message too short")
            return
        with lock:
            no = f"HD{ticket:03d}"
            ticket += 1
        with open("helpdesk_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} {no} {request}\n")
        conn.sendall(f"Accepted. Ticket: {no}".encode())
        print(f"[DISCONNECTED] Handled client {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Secure helpdesk server running on port 5001...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
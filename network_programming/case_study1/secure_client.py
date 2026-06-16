import socket

HOST, PORT = "127.0.0.1", 5001

print("--- Secure Helpdesk Client ---")
reg = input("Enter Registration Number: ").strip()
issue = input("Enter your Issue: ").strip()

# We manually glue the TOKEN to the front of the message so the server accepts it!
full_message = f"NET123|{reg}: {issue}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
        client.sendall(full_message.encode())
        
        # Read what the server says back
        response = client.recv(1024).decode()
        print(f"\nServer Response: {response}")
    except ConnectionRefusedError:
        print("\nError: Could not connect. Is the server running?")
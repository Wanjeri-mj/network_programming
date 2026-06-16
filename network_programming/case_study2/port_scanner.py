# File: port_scanner.py
import socket

# Dictionary matching common ports to their standard networking services
ports = {
    21: "FTP (File Transfer)",
    22: "SSH (Secure Shell)",
    25: "SMTP (Email)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Unsecure Web)",
    443: "HTTPS (Secure Web)"
}

host = input("Enter host or IP to scan: ").strip()

print(f"\nScanning host: {host}...")
print("-" * 40)

try:
    # Validate hostname up front by checking if it resolves
    target_ip = socket.gethostbyname(host)
except socket.gaierror:
    print(f"Error: Host '{host}' could not be resolved. Check your spelling.")
    exit()

# Loop through our dictionary and knock on each port door
for port, service in ports.items():
    # SOCK_STREAM establishes a temporary TCP socket for scanning
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.5)  # Don't wait forever—1.5 seconds per port is enough
        
        # connect_ex() returns an error code instead of throwing a full crash exception
        # 0 means connection succeeded (Port is open!)
        result = s.connect_ex((target_ip, port))
        
        status = "OPEN" if result == 0 else "closed"
        print(f"Port {port:3d} [{service:20s}]: {status}")

print("-" * 40)
print("Scan complete.")
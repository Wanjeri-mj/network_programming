# File: local_host_info.py
import socket
import os
import sys

# Step 1: Display basic local hostname and default IP address
hostname = socket.gethostname()
try:
    default_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    default_ip = "127.0.0.1"

print("=" * 50)
print(f"Local Host Name:       {hostname}")
print(f"Primary Local IP:      {default_ip}")
print("=" * 50)

# Step 2: Extract deeper network interface details programmatically
print("\nScanning Local Active Network Interfaces...")
print("-" * 50)

# socket.getifaddrs() gives a comprehensive list of system interfaces (Linux/Mac)
# Fallback structure used for universal cross-platform tracking
if hasattr(socket, "getifaddrs"):
    if_records = socket.getifaddrs()
    interfaces_mapped = {}
    
    for record in if_records:
        name = record.name
        if name not in interfaces_mapped:
            interfaces_mapped[name] = {"IPv4": [], "IPv6": []}
            
        # Classify the network address family
        if record.family == socket.AF_INET: # IPv4
            interfaces_mapped[name]["IPv4"].append(record.addr[0])
        elif record.family == socket.AF_INET6: # IPv6
            interfaces_mapped[name]["IPv6"].append(record.addr[0])
            
    for if_name, info in interfaces_mapped.items():
        print(f"\nInterface Name: {if_name}")
        print(f"  -> IPv4 Addresses: {', '.join(info['IPv4']) or 'None'}")
        print(f"  -> IPv6 Addresses: {', '.join(info['IPv6']) or 'None'}")
else:
    # Fallback message for environments with stricter sandboxed socket configurations
    print(f"Detailed tracking requires OS shell execution queries.")
    print(f"Windows system check fallback: run 'ipconfig /all' in terminal.")
    print(f"Linux/Mac system check fallback: run 'ifconfig' or 'ip addr' in terminal.")

print("-" * 50)
# File: host_resolver.py
import socket
import ipaddress

domain = input("Enter domain name (e.g., google.com): ").strip()

print(f"\nResolving DNS records for '{domain}'...")
print("-" * 50)

try:
    # 1. Query DNS records for BOTH IPv4 and IPv6 streams
    # Passing None for the port returns every address structure tied to the host
    infos = socket.getaddrinfo(domain, None)       
    
    # Use a set to filter out duplicate address returns
    seen_ips = set()
    
    for info in infos:
        # Extract the raw IP address string from the address tuple structure
        ip = info[4][0]
        
        if ip in seen_ips:
            continue
        seen_ips.add(ip)
        
        # 2. Leverage Python's ipaddress library to instantly check the IP version
        ip_obj = ipaddress.ip_address(ip)
        version = f"IPv{ip_obj.version}"
        
        print(f"Host: {domain:<15s} | IP Address: {ip:<30s} | Type: {version}")

except socket.gaierror:
    # Captures cases where the domain name is completely unmapped or misspelled
    print("Error: Host name cannot be resolved by DNS.")

print("-" * 50)
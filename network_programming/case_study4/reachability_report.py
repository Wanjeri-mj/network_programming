# File: reachability_report.py
import socket
import time

print("--- Bulk Reachability Report Utility ---")
print("Enter hostnames/IPs one by one. Press ENTER on a blank line when done.")
print("-" * 55)

hosts = []
while True:
    h = input("Add Host: ").strip()
    if not h: 
        break
    hosts.append(h)

# If the user immediately hit enter without adding hosts, exit gracefully
if not hosts:
    print("No hosts entered. Exiting.")
    exit()

print(f"\nProcessing {len(hosts)} targets. Please wait...")
lines = []

# Iterate and evaluate each collected target address sequentially
for host in hosts:
    start_time = time.time()
    status = "Unreachable"
    ip_resolved = "Unknown"
    
    try:
        # 1. Resolve host domain pattern
        ip_resolved = socket.gethostbyname(host)
        
        # 2. Try an active TCP Handshake connection on port 80 with a 2-second timeout
        socket.create_connection((ip_resolved, 80), timeout=2).close()
        status = "Reachable"
    except Exception:
        # If any step fails, leave status as Unreachable
        if ip_resolved == "Unknown":
            ip_resolved = "Resolution Failed"

    # Calculate time taken in milliseconds
    elapsed_time = int((time.time() - start_time) * 1000)
    
    # Format the block for this host
    report_entry = (
        f"Host:          {host}\n"
        f"IP Address:    {ip_resolved}\n"
        f"Status:        {status}\n"
        f"Response Time: {elapsed_time} ms\n"
        f"{'-' * 40}\n"
    )
    lines.append(report_entry)

# Write out our collected report strings to a text file
with open("reachability_report.txt", "w") as report_file:
    report_file.write("=== BULK NETWORK REACHABILITY REPORT ===\n\n")
    report_file.write("".join(lines))

print("\nTask complete! Report saved as 'reachability_report.txt'.")
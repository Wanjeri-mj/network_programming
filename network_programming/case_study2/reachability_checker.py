# File: reachability_checker.py
import socket
import time
# Get target from user (e.g., "google.com" or "127.0.0.1")
host = input("Enter hostname or IP: ").strip()

# Start the stopwatch
start_time = time.time()

try:
    # 1. Resolve host name (converts "google.com" -> IP address)
    ip = socket.gethostbyname(host)
    
    # 2. Attempt a quick TCP connection on port 80 (HTTP) with a 3-second timeout
    # create_connection handles both socket creation and connecting in one step
    socket.create_connection((ip, 80), timeout=3).close()
    status = True

except socket.gaierror:
    # This specific error triggers if the name doesn't exist (e.g., "fakewebsite123.xyz")
    ip, status = "Could not resolve hostname", False

except Exception:
    # This triggers if the hostname is real, but the connection timed out/failed
    status = False

# Stop the stopwatch and calculate milliseconds
elapsed_time = int((time.time() - start_time) * 1000)

# Display diagnostic results
print("-" * 30)
print(f"Host:         {host}")
print(f"IP Address:   {ip}")
print(f"Reachable:    {status}")
print(f"Time taken:   {elapsed_time} ms")
print("-" * 30)
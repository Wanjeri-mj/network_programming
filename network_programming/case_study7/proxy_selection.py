# File: proxy_selection.py
from urllib.parse import urlparse

# Define our routing policy tables using sets for optimal lookup speed
LOCAL_DOMAINS = {"localhost", "127.0.0.1", "portal.kcau.ac.ke"}
BLOCKED_DOMAINS = {"blockedsite.com", "malware.example", "socialmedia.com"}

print("=" * 60)
print("     CAMPUS GATEWAY PROXY ROUTING SIMULATOR")
print("=" * 60)

url_input = input("Enter Target URL: ").strip()

# Safely catch basic schema errors if user didn't type http/https prefix
if not (url_input.startswith("http://") or url_input.startswith("https://")):
    url_input = "https://" + url_input

# Parse out the hostname component
host = urlparse(url_input).hostname

print("-" * 60)

if not host:
    print("Decision: [INVALID URL] -> Unable to resolve target hostname.")
    
# 1. Firewall Policy Check: Is the host flagged in our blacklist?
elif any(blocked in host for blocked in BLOCKED_DOMAINS):
    print(f"Decision: [ACCESS DENIED] -> Content security policy blocks '{host}'")
    
# 2. Local Policy Check: Is it an internal campus server or local loopback?
elif host in LOCAL_DOMAINS or host.endswith(".local"):
    print(f"Decision: [DIRECT CONNECTION] -> Bypassing proxy for internal asset.")
    
# 3. External Traffic Policy: Route all other safe outbound requests through the campus proxy
else:
    print(f"Decision: [USE PROXY] -> Routing traffic to Web Proxy on Port 8080.")

print("=" * 60)
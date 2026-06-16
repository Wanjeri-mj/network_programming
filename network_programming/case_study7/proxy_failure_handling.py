# File: proxy_failure_handling.py

print("=" * 60)
print("     ENTERPRISE PROXY COMPLIANCE VALIDATOR")
print("=" * 60)

# 1. Gather configuration data safely
host = input("Proxy Host IP/Domain: ").strip()

try:
    port = int(input("Proxy Port Number:    ").strip())
except ValueError:
    # If the user types characters or leaves it blank, assign an out-of-bounds error state flag
    port = -1 

url = input("Destination URL:       ").strip()

print("-" * 60)
print("VALIDATION ANALYSIS:")

# 2. Sequential Validation Check Filter Pipeline
if not host:
    print(" -> CONFIGURATION REJECTED: Proxy host string cannot be blank.")

elif port <= 0 or port > 65535:
    # 65535 is the absolute mathematical threshold limit for physical hardware TCP/UDP ports
    print(f" -> CONFIGURATION REJECTED: Port '{port}' is out of valid network range (1 - 65535).")

elif not (url.startswith("http://") or url.startswith("https://")):
    print(" -> CONFIGURATION REJECTED: Invalid schema. URL must begin with 'http://' or 'https://'.")

elif "blockedsite.com" in url:
    print(" -> SECURITY VIOLATION: Access to 'blockedsite.com' is explicitly blacklisted by network policy.")

else:
    print(" ✅ STATUS APPROVED: Proxy settings successfully validated and deployed.")

print("=" * 60)
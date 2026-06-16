# File: proxy_configuration.py

print("=" * 60)
print("     NETWORK APPLICATION PROXY BOUNDARY SETUP")
print("=" * 60)

try:
    # 1. Collect intermediate proxy server parameters
    proxy_host = input("Enter Proxy Server IP/Host (e.g., 10.0.0.1): ").strip()
    proxy_port = int(input("Enter Proxy Port Number (e.g., 8080):    ").strip())
    
    # 2. Collect final external web destination 
    target_url = input("Enter Intended Destination URL (e.g., google.com): ").strip()
    
    print("-" * 60)
    print("APPLICATION LOGS:")
    
    # 3. Output the exact network transmission layout structure
    print(f" [Initial Socket Initialization]: Target set to Proxy gateway.")
    print(f" [Encapsulating Header Request]: Appending destination target '{target_url}'")
    print(f" -> STATUS: Connecting to {target_url} via gateway proxy at {proxy_host}:{proxy_port}")

except ValueError:
    print("\n[Configuration Error]: Proxy Port must be a valid numerical integer.")
except Exception as e:
    print(f"\n[Unexpected Error]: {str(e)}")

print("=" * 60)
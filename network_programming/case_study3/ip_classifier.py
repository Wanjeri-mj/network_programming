# File: ip_classifier.py
import ipaddress

print("--- IP Address Classification Utility ---")
print("Enter an IP address to classify (or press Enter on a blank line to exit):")
print("-" * 50)

while True:
    value = input("IP: ").strip()
    
    # Exit condition if the user hits Enter without typing anything
    if not value: 
        print("Exiting utility.")
        break
        
    try:
        # 1. Parse and validate using Python's built-in ipaddress module
        # This single engine checks structural syntax, range values, and formatting rules
        ip = ipaddress.ip_address(value)         
        
        # 2. Extract and print the version property (returns integer 4 or 6)
        print(f" -> Result: SUCCESS | {value} is a valid IPv{ip.version} address\n")
        
    except ValueError:
        # If the address fails syntax rules (e.g., characters out of bounds, wrong separators)
        print(f" -> Result: INVALID | '{value}' is not a valid IP address\n")
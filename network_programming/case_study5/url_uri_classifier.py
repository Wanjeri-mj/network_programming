# File: url_uri_classifier.py
from urllib.parse import urlparse

print("--- URL / URI Structural Classifier ---")
print("Enter an identifier to evaluate (or press Enter on a blank line to exit):")
print("-" * 65)

while True:
    value = input("Input string: ").strip()
    
    if not value:
        print("Exiting utility.")
        break
        
    # Parse the string structure
    p = urlparse(value)
    
    # 1. A URL must have a protocol scheme AND a network location/host (netloc)
    if p.scheme and p.netloc:
        print(f" -> Result: https://my.clevelandclinic.org/health/diseases/14248-overactive-bladder (Points to a network resource)")
        print(f"    Scheme: {p.scheme} | Host: {p.netloc}\n")
        
    # 2. A generic URI only needs a scheme (like 'urn' or 'mailto'), no host location required
    elif p.scheme:
        print(f" -> Result: [URI but NOT a URL] (Identifies, but does not locate)")
        print(f"    Scheme: {p.scheme} | Path/ID: {p.path}\n")
        
    # 3. If it doesn't even have a scheme structure, it's malformed
    else:
        print(" -> Result: [Invalid Identifier]\n")
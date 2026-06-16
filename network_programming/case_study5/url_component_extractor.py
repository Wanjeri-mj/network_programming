# File: url_component_extractor.py
from urllib.parse import urlparse

print("--- URL Component Extractor Utility ---")
url_input = input("Enter a full URL: ").strip()

# 1. Parse the text string into structured components
# urlparse recognizes standard RFC web standards out of the box
parsed_url = urlparse(url_input)

# Display the extracted layout properties
print("\n" + "=" * 45)
print("EXTRACTED URL ARCHITECTURE COMPONENTS")
print("=" * 45)
print(f"Protocol/Scheme: {parsed_url.scheme}")
print(f"Host/Domain:     {parsed_url.hostname}")

# 2. Extract port details (Defaults to standard port 80/443 if not specified)
port_val = parsed_url.port if parsed_url.port else "Default (Standard)"
print(f"Port Number:     {port_val}")

# 3. Extract sub-routing flags
print(f"Resource Path:   {parsed_url.path or '/'}")
print(f"Query String:    {parsed_url.query or 'None'}")
print(f"Fragment Identifier: #{parsed_url.fragment or 'None'}")
print("=" * 45)
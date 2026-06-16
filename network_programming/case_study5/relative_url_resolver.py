# File: relative_url_resolver.py
from urllib.parse import urljoin

print("--- Relative URL Resolver Utility ---")
print("Enter the foundational Base URL and the target Relative Path:")
print("-" * 65)

# Example Base: https://example.com/students/index.html
base_url = input("Base URL:         ").strip()

# Example Relative: ../images/avatar.jpg
relative_path = input("Relative URL/Path: ").strip()

# 1. Resolve the path combinations using Python's native RFC-compliant engine
# urljoin automatically computes folder steps (like '../') and directory limits
absolute_url = urljoin(base_url, relative_path)

print("-" * 65)
print(f"Resulting Absolute Destination:\n -> {absolute_url}")
print("=" * 65)
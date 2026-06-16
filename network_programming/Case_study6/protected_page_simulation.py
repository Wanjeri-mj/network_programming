# File: protected_page_simulation.py

# Credential Database Store
users = {
    "admin": "admin123", 
    "student": "net2026", 
    "lecturer": "teach456"
}

print("=" * 55)
print("     UNIVERSITY DEPARTMENT SECURE INTERNAL PORTAL")
print("=" * 55)

# Gather user inputs
username = input("Username: ").strip()
password = input("Password: ").strip()

print("-" * 55)

# Gatekeeper conditional validation block
if users.get(username) == password:
    # Protected content is strictly contained inside the successful block scope
    print("🔓 ACCESS GRANTED: Welcome to the Internal Portal.\n")
    print("Available Student Resources:")
    print("  [1] Lecture Notes & Slides (PDF)")
    print("  [2] Lab Sandbox Setup Exercises")
    print("  [3] Final Assignment Git Submission Portals")
else:
    # If the check fails, the resource strings are never read or processed
    print("🔒 ACCESS DENIED: Invalid credentials. This incident has been logged.")

print("=" * 55)
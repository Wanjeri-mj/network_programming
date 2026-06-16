# File: simple_authenticator.py

# Step 1: Create a secure local database mapping usernames (keys) to passwords (values)
users = {
    "admin": "admin123", 
    "student": "net2026", 
    "lecturer": "teach456"
}

print("=" * 45)
print("     COMPANY INTERNAL LOGIN GATEWAY")
print("=" * 45)

# Step 2: Prompt the user for input credentials
username_input = input("Enter Username: ").strip()
password_input = input("Enter Password: ").strip()

print("-" * 45)

# Step 3: Validate credentials securely using a single-step dictionary lookup
# .get() safely returns None if the username doesn't exist, preventing KeyErrors
if users.get(username_input) == password_input:
    print(">>> ACCESS GRANTED: Authentication Successful. <<<")
else:
    print(">>> ACCESS DENIED: Invalid Username or Password. <<<")

print("=" * 45)
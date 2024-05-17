import hashlib

def login(username, password):
    # Hardcoded password for demonstration purposes (vulnerable)
    hardcoded_password = "secretpassword"

    # Hash the user-provided password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username exists and the passwords match (vulnerable)
    if username == "admin" and hashed_password == hashlib.sha256(hardcoded_password.encode()).hexdigest():
        print("Login successful! Welcome admin.")
    else:
        print("Login failed. Invalid username or password.")

# Get user input for username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Authenticate user
login(username, password)

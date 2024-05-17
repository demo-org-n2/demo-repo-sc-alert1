import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable code
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user

username = input("Enter your username: ")
password = input("Enter your password: ")

user = login(username, password)
if user:
    print("Login successful!")
else:
    print("Invalid username or password!")

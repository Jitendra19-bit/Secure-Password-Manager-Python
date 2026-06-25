import sqlite3

website = input("Enter Website: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT,
    username TEXT,
    password TEXT
)
""")

cursor.execute(
    "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
    (website, username, password)
)

conn.commit()
conn.close()

print("Password Saved Successfully!")
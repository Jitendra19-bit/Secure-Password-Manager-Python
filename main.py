import sqlite3

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

conn.commit()
conn.close()

print("Database Created Successfully")
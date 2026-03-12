import csv
import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT
)
""")

# Read CSV and insert into database
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

conn.commit()

# Display inserted data
cursor.execute("SELECT * FROM users")
print("Users Table:")
for row in cursor.fetchall():
    print(row)

conn.close()

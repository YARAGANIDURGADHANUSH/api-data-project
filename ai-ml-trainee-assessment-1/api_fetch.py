import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER,
    title TEXT,
    body TEXT
)
""")

for item in data:
    cursor.execute(
        "INSERT INTO posts (id, title, body) VALUES (?, ?, ?)",
        (item["id"], item["title"], item["body"])
    )

conn.commit()

cursor.execute("SELECT * FROM posts LIMIT 5")
rows = cursor.fetchall()

print("Sample Data from Database:")
for row in rows:
    print(row)

conn.close()

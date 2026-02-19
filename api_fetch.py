import requests
import sqlite3

# Step 1: Fetch data from API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Step 2: Connect to SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Step 3: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER,
    title TEXT,
    body TEXT
)
""")

# Step 4: Insert API data
for item in data:
    cursor.execute(
        "INSERT INTO posts (id, title, body) VALUES (?, ?, ?)",
        (item["id"], item["title"], item["body"])
    )

conn.commit()

# Step 5: Display data
cursor.execute("SELECT * FROM posts LIMIT 5")
rows = cursor.fetchall()

print("Sample Data from Database:")
for row in rows:
    print(row)

conn.close()

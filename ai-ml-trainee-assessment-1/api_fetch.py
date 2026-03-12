import requests
import sqlite3

API_URL = "https://jsonplaceholder.typicode.com/posts"
DB_NAME = "database.db"


# Fetch data from API
def fetch_api_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("API data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching API data:", e)
        return []


# Create SQLite database and table
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT
    )
    """)

    conn.commit()
    return conn, cursor


# Insert API data into database
def insert_data(cursor, data):
    for item in data:
        cursor.execute(
            "INSERT OR IGNORE INTO posts (id, title, body) VALUES (?, ?, ?)",
            (item["id"], item["title"], item["body"])
        )


# Display sample records
def display_data(cursor):
    cursor.execute("SELECT * FROM posts LIMIT 5")
    rows = cursor.fetchall()

    print("\nSample Data from Database:")
    for row in rows:
        print(row)


# Main pipeline
def main():
    data = fetch_api_data()

    if not data:
        print("No data to process.")
        return

    conn, cursor = create_database()

    insert_data(cursor, data)
    conn.commit()

    display_data(cursor)

    conn.close()
    print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()

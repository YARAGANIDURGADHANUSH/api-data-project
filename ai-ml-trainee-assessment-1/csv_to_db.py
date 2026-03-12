import csv
import sqlite3

DB_NAME = "database.db"
CSV_FILE = "users.csv"


# Create database and table
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    conn.commit()
    return conn, cursor


# Read CSV file
def read_csv():
    users = []
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append((row["name"], row["email"]))
        print("CSV data loaded successfully.")
    except Exception as e:
        print("Error reading CSV file:", e)

    return users


# Insert CSV data into database
def insert_users(cursor, users):
    for user in users:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            user
        )


# Display inserted data
def display_users(cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("\nUsers Table:")
    for row in rows:
        print(row)


# Main workflow
def main():
    conn, cursor = create_database()

    users = read_csv()
    if not users:
        print("No data found in CSV.")
        return

    insert_users(cursor, users)
    conn.commit()

    display_users(cursor)

    conn.close()
    print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()

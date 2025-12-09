import sqlite3

def create_db():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()

    # Clean setup
    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        year INTEGER NOT NULL,
        auth INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Database 'people.db' and table 'users' created successfully.")

if __name__ == "__main__":
    create_db()

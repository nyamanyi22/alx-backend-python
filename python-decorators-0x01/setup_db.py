import sqlite3

def setup():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Insert sample users
    cursor.executemany('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', [
        ('Alice Smith', 'alice@example.com'),
        ('Bob Johnson', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com')
    ])

    conn.commit()
    conn.close()
    print("✅ users.db setup complete.")

if __name__ == "__main__":
    setup()

import sqlite3


def create_database():
    # Connect to SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Create the 'vocabulary' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY,
            english_word TEXT NOT NULL,
            chinese_word TEXT NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database with vocabulary created successfully.")

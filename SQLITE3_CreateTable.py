import sqlite3

def create_database_without_data():         #this script now creates an empty table. The output should be: No entries found in the vocabulary table.
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

def print_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Print the entire vocabulary table
    cursor.execute('SELECT * FROM vocabulary')
    rows = cursor.fetchall()

    if not rows:
        print("No entries found in the vocabulary table.")
    else:
        print("Entries in the vocabulary table:")
        for row in rows:
            print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    create_database_without_data()
    print_database()


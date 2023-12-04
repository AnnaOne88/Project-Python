import sqlite3
import random

def create_database_with_data():
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

    # Insert some sample data into the table THE FIRST TIME YOU RUN THE CODE, UNCOMMENT THIS TO ADD ENTRIES. THE SECOND TIME YOU RUN IT, THIS NEEDS TO BE DEACTIVATED.
    '''sample_data = [
        ('hello', '你好'),
        ('world', '世界'),
        ('english word', 'chinese word'),
    ]

    cursor.executemany('INSERT INTO vocabulary (english_word, chinese_word) VALUES (?, ?)', sample_data)'''

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

def select_random_entry():
    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Use SELECT with ORDER BY RANDOM() in a subquery to get a random entry
    cursor.execute('''
        SELECT * FROM vocabulary
        WHERE id = (
            SELECT id FROM vocabulary
            ORDER BY RANDOM()
            LIMIT 1
        )
    ''')

    # Fetch the result
    random_entry = cursor.fetchone()

    # Print the result
    if random_entry:
        print("Random entry:", random_entry)
    else:
        print("No entries found in the vocabulary table.")

    # Close the connection
    conn.close()

def delete_extra_rows():
    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Delete all rows except for the first three
    cursor.execute('DELETE FROM vocabulary WHERE id > 3')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == "__main__":
    create_database_with_data()
    print_database()

    delete_extra_rows()

    print()
    select_random_entry()

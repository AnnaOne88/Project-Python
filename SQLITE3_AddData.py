import sqlite3

def add_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Insert data into the 'vocabulary' table
    data_to_insert = [
        ('apple', '苹果'),
        ('book', '书'),
        ('cat', '猫'),
        # Add more data as needed
    ]

    cursor.executemany('INSERT INTO vocabulary (english_word, chinese_word) VALUES (?, ?)', data_to_insert)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

'''def delete_extra_rows():     #this is here just in case you need it after running the script more times, like me!!!!!!
    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Delete all rows except for the first three
    cursor.execute('DELETE FROM vocabulary WHERE id > 3')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()'''

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

if __name__ == "__main__":
    add_data()
    print_database()
    print()
    select_random_entry()
    #delete_extra_rows()

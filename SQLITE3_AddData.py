import sqlite3
import openpyxl

#this adds data from our external XLS file. RUN ONLY ONCE.

def read_and_insert_data(xlsx_file_path):
    # Load the workbook using openpyxl
    wb = openpyxl.load_workbook(xlsx_file_path)
    sheet = wb.active
    word_dictionary = {}

    # Connect to the SQLite database
    conn = sqlite3.connect('vocabulary.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Iterate through rows in the sheet and insert data into the 'vocabulary' table. This structure from our other script... Debugging prints added.
    for row in sheet.iter_rows(min_row=2, values_only=True):
        english_word, chinese_words_str = row

        # Skip the row if english_word is None
        if english_word is None:
            print("Skipping row with None for english_word.")
            continue

        # Add a check for None before splitting
        if chinese_words_str is not None:
            chinese_words = [word.strip() for word in chinese_words_str.split(',')]
        else:
            chinese_words = []

        # Add debug prints
        print(f"Inserting: english_word={english_word}, chinese_words={chinese_words}")

        # Insert data into the 'vocabulary' table
        cursor.execute('INSERT INTO vocabulary (english_word, chinese_word) VALUES (?, ?)',
                       (english_word, chinese_words_str))

        # Commit the changes
    conn.commit()

        # Close the connection
    conn.close()
    return word_dictionary

if __name__ == "__main__":
    xlsx_file_path = './vocabulary-list-extended.xlsx'  # Replace with the actual path to your XLSX file
    word_dict = read_and_insert_data(xlsx_file_path)

'''def delete_extra_rows():     # this is here just in case you need it after running the script more times, like me!!!!!!
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

if __name__ == "__main__":
    print_database()
    #delete_extra_rows()

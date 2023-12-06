import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_item(conn,tableName,columns,values):
    print(f"values={values}")
    sql = f''' INSERT INTO {tableName} ({str(columns)})
              VALUES {str(values)} '''
    print(f"sql={sql}")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid    

def fetchOneByRandom(db_file,tableName):
    # create a database connection
    conn = create_connection(db_file)
    cur = conn.cursor()
    # Use SELECT with ORDER BY RANDOM() in a subquery to get a random entry
    cur.execute('''
                SELECT * FROM englishWithChinese
                WHERE id = (
                SELECT id FROM englishWithChinese
                ORDER BY RANDOM()
                LIMIT 1
                )
    ''')

    # Fetch the result
    random_entry = cur.fetchone()

    # Print the result
    if random_entry:
        print("Random entry:", random_entry)
    else:
        print("No entries found in the vocabulary table.")
    cur.close
    conn.close

def main():
    database = "pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
        cur = conn.cursor()
        cur.execute("""
    INSERT INTO projects(name,begin_date,end_date) VALUES
        ('Monty Python and the Holy Grail', 1975, "None"),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
        conn.commit()
        cur.close
        conn.close
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
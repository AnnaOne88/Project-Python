import Sqlite3Tool

database = "vocabulary.db"
tableName_englishWithChinese = "tableName_englishWithChinese"
def initData():
    # create database ,init data.
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS tableName_englishWithChinese(
                                        id integer PRIMARY KEY,
                                        EnglishWord text NOT NULL,
                                        translation1 text,
                                        translation2 text,
                                        translation3 text,
                                        translation4 text,
                                        translation5 text
                                    ); """
    # create a database connection
    conn = Sqlite3Tool.create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        Sqlite3Tool.create_table(conn, sql_create_projects_table)
        cursor = conn.cursor()
        res = cursor.execute("SELECT EnglishWord FROM tableName_englishWithChinese")
        if res.fetchone() is None:
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3,translation4",
                                ( 'hello','你好','您好','nihao','ni hao' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'cat','猫','mao','mao1' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'tree','树','shù','shu' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'Computer','电脑','diànnǎo','diannao' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'Adventure','冒险','màoxiǎn','maoxian'))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'Decision','决定','jieding','juédìng' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'Challenge','挑战','tiaozhan','tiǎozhàn' ))
            Sqlite3Tool.insert_item(conn,tableName_englishWithChinese,
                                "EnglishWord,translation1,translation2,translation3",
                                ( 'Friendship','友谊','youyi','yǒuyì' ))
        cursor.close
        conn.close    
        
    else:
        print("Error! cannot create the database connection.")

def main():
    initData()
    sum =0 
    correctNum = 0
    wrongNum = 0
    wrong_answers = [] #this list will record which word the user didnt answer correctly
    # create a database connection
    conn = Sqlite3Tool.create_connection(database)
    cursor = conn.cursor()
    #Sqlite3Tool.fetchOneByRandom(database,tableName_englishWithChinese)
    cursor.execute(f"SELECT * FROM {tableName_englishWithChinese}")
    for row in cursor: #这样，每次循环迭代时，只会将一行结果从数据库读取到内存中，而不是将整个结果集都读取到内存中
        print(row)
        print(f"What is '{row[1]}' in Chinese?")
        user_input = input("Your answer: ").strip()
        if user_input in row:
            correctNum += 1
            sum += 1
            print(f"Correct! ✔️ Correct: {correctNum}, Wrong: {wrongNum}, Total revised: {sum}\n")
        else:
            wrongNum += 1
            sum += 1
            print(f"Wrong. The correct answers are: {', '.join(row[2])}. ❌, Correct: {correctNum}, Wrong: {wrongNum}, Total revised: {sum}\n")
            wrong_answers.append((row[1], row[2]))
    
    percentage_correct = correctNum/sum*100
    print(f"Your success rate is: {percentage_correct:.2f}% correct ({correctNum} out of {sum}) ") #formatting this to 2 decimal places
    print('Wrong answers:', wrong_answers)
    cursor.close
    conn.close

if __name__ == "__main__":
    main()
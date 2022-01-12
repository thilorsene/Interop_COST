import sqlite3

def updateSqliteTable(id,status):
    try:
        sqliteConnection = sqlite3.connect('aust_db.sqlite')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update order set status = ? where id = ?"""
        cursor.execute(sql_update_query,(status,id))
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def save_bon(bon):
    try:
        sqliteConnection = sqlite3.connect('aust_db.sqlite')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """INSERT INTO bon Values (?,?,?,?)"""
        cursor.execute(sql_update_query,(bon['article_id'],bon['qte'],bon['date ']))
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
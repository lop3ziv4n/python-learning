import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

sql = """CREATE TABLE PERSON ( 
    name TEXT,
    surname TEXT,
    surname2 TEXT,
    age INTEGER
      )"""

cursor.execute(sql)

connection.commit()
connection.close()

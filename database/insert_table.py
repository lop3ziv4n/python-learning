import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

sql = """INSERT INTO PERSON VALUES ( 
    'Jorge',
    'Cas',
    'Perez',
    35
      )"""

cursor.execute(sql)

connection.commit()
connection.close()

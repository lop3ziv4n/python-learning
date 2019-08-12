import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

sql = """UPDATE PERSON SET
         age = 46  
         WHERE name = 'Sofia'"""

cursor.execute(sql)

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

sql = """DELETE FROM PERSON WHERE name = 'Luis' """

cursor.execute(sql)

connection.commit()
connection.close()

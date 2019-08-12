import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

persons = [('Pedro', 'Rodriguez', 'Perez', 26),
           ('Maria', 'Lopez', 'Gomez', 45),
           ('Luis', 'Gonzalez', 'Perez', 46),
           ('Sofia', 'Lopez', '', 45)]

sql = """INSERT INTO PERSON VALUES (?,?,?,?)"""

cursor.executemany(sql, persons)

connection.commit()
connection.close()

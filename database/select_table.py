import sqlite3

connection = sqlite3.connect("database_test.db")
cursor = connection.cursor()

sql = """SELECT * FROM PERSON WHERE age > 40 """

cursor.execute(sql)

persons = cursor.fetchall()
print(persons)

for person in persons:
    print(person)

connection.close()

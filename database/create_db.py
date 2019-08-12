# SQLite - Relational database management system
# https://es.wikipedia.org/wiki/SQLite
# https://sqlitebrowser.org/

import sqlite3

connection = sqlite3.connect("database_test.db")
connection.close()

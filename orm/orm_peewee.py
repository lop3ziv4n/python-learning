# pip3 install peewee

import datetime

import peewee

database = peewee.MySQLDatabase('peewee_test', host='localhost', port=3306, user='root', password='root')


#
class User(peewee.Model):
    username = peewee.CharField(unique=True)
    email = peewee.CharField(index=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'User'


if __name__ == '__main__':
    if not User.table_exists():
        User.create_table()

    username = input("Input Username")
    email = input("Input Email")

    # Select
    if not User.select().where(User.username == username).exists():
        # Insert
        new_user = User.create(username=username, email=email)
        new_user.save()
    else:
        print('User exists')

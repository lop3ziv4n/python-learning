from sqlobject import StringCol, SQLObject, ForeignKey, sqlhub, connectionForURI

sqlhub.processConnection = connectionForURI('sqlite:/:memory:')


class Person(SQLObject):
    name = StringCol()


class Address(SQLObject):
    address = StringCol()
    person = ForeignKey('Person')


Person.createTable()

Address.createTable()

person = Person(name='person')
address = Address(address='address', person=person)

print(person)
print(address)

persons = Person.select(Person.q.name == 'person')
print(persons)

person1 = persons[0]

print(person1 == person)
# True

addresses = Address.select(Address.q.person == person1)
print(addresses)

address1 = addresses[0]
print(address1 == address)
# True

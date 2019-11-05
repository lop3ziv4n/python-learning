from storm.locals import Int, Reference, Unicode, create_database, Store

db = create_database('sqlite:')
store = Store(db)


class Person(object):
    __storm_table__ = 'person'
    id = Int(primary=True)
    name = Unicode()


class Address(object):
    __storm_table__ = 'address'
    id = Int(primary=True)
    address = Unicode()
    person_id = Int()
    person = Reference(person_id, Person.id)


store.execute("CREATE TABLE person (id INTEGER PRIMARY KEY, name VARCHAR)")
store.execute(
    "CREATE TABLE address (id INTEGER PRIMARY KEY, address VARCHAR, person_id INTEGER, "
    "FOREIGN KEY(person_id) REFERENCES person(id))")

person = Person()
person.name = u'person'
print(person)

print("%r, %r" % (person.id, person.name))
# None, u'person'
# Notice that person.id is None since the Person instance is not attached to a valid database store yet.
store.add(person)

print("%r, %r" % (person.id, person.name))
# None, u'person'
# Since the store hasn't flushed the Person instance into the sqlite database yet, person.id is still None.
store.flush()

print("%r, %r" % (person.id, person.name))
# 1, u'person'
# Now the store has flushed the Person instance, we got an id value for person.

address = Address()
address.person = person
address.address = 'address'

print("%r, %r, %r" % (address.id, address.person, address.address))
# None,, 'address'

print(address.person == person)
# True
store.add(address)
store.flush()

print("%r, %r, %r" % (address.id, address.person, address.address))
# 1,, 'address'

person = store.find(Person, Person.name == u'person').one()
print("%r, %r" % (person.id, person.name))
# 1, u'person'
store.find(Address, Address.person == person).one()

address = store.find(Address, Address.person == person).one()
print("%r, %r" % (address.id, address.address))
# 1, u'address'

# Functions generators
range(0, 11)
print(range(0, 11))
for value in range(0, 11):
    print(value)


# range(0, 11) = range(11)

def range_par(maximum):
    for value in range(maximum):
        if value % 2 == 0:
            yield value


for value in range_par(11):
    print(value)

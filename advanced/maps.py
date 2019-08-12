# Functions Map
def multi(value):
    return value * 2


print(multi(4))

numbers = [2, 4, 6, 8]

# execute function in list
maps = map(multi, numbers)

print(list(maps))

# execute function in list. one line
results = list(map(lambda number: number * 2, numbers))
print(results)

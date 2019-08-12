# Functions Filters
def positive(value):
    if value > 0:
        return True
    else:
        return False


print(positive(5))
print(positive(-3))

numbers = [4, -2, 8, -3, -5, -7, 1, 9]

# execute filter in list
filters = filter(positive, numbers)

print(list(filters))

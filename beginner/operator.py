# operator {+,-,*,/,%,**,//}

number1 = 10
number2 = 5
# add
print(number1 + number2)
# subtract
print(number1 - number2)
# multiply
print(number1 * number2)
# divide
print(number1 / number2)
# rest
print(number1 % number2)
# quotient
print(number1 // number2)
# exponent
print(number1 ** number2)

# operator assignment {=, +=, -=, +=, /=, **=}
number = 5
# number = number + 4
number += 4
print(number)

# number = number - 4
number -= 4
print(number)

# number = number * 4
number *= 4
print(number)

# number = number / 4
number /= 4
print(number)

# number = number ** 4
number **= 4
print(number)

# operator comparison {==, !=, >, <, >=, <=}
number1 = 5
number2 = 3
print(number1 == number2)
print(number1 != number2)
print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)
print(number1 <= number2)

string1 = "hola"
string2 = "hola"
print(string1 == string2)
print(string1 != string2)
print(string1 > string2)
print(string1 < string2)
print(string1 >= string2)
print(string1 <= string2)

# operator logical {and, or, not}
number1 = 10
number2 = 5
number3 = 7
number4 = 8
print((number1 > number2) and (number3 < number4))
print((number1 > number2) and (number3 > number4))
print((number1 > number2) or (number3 > number4))
print(not (number3 > number4))

# operator identity {is, is not}
string1 = ["manzana", "pera"]
string2 = ["manzana", "pera"]
string3 = string1
print(string3 is string1)

string3.append("naranja")
print(string1)

print(string3 is not string2)

# operator membership {in, not in}
string1 = ["manzana", "pera", "naranja"]
string2 = "pera"
print(string2 in string1)

print(string2 not in string1)

string3 = "melocoton"
print(string3 not in string1)

def timesTwo(num: int): return num * 2

# List of numbers that we'll use for multiple operations.
sequence = list(range(1, 6))

# Multiplies all the numbers in the sequence using the timesTwo function.
output = list(map(timesTwo, sequence))
print(output)


# Multiplies all numbers in the sequence by three.
output = list(map(lambda num: num * 3, sequence))
print(output)


# Filters out the odd numbers
output = list(filter(lambda num: num % 2 == 0, sequence))
print(output)


string = "Hello my name is Chris"
print(string.lower())
print(string.upper())
print(string.split())


tweet = "Go sports! #Sports"
print(tweet.split("#"))


dictionary = {'k1': 1, 'k2': 2}
print(dictionary.keys())
print(dictionary.items())
print(dictionary.values())


numbers = [1, 2, 3, 4, 5]
item = numbers.pop()
print(item)

item = numbers.pop(1)
print(item)

print('x' in [1, 2, 3, 4, 5])
print(3 in [1, 2, 3, 4, 5])

tuplie = [(1, 2), (3, 4), (5, 6)]
print(tuplie[0][1])

for item in tuplie:
    print(item)

for a, b in tuplie:
    print("A: %d" % a)
    print("B: %d" % b)


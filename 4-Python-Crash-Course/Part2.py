dictionary = {'key': 'value', 'second': 123}
print(dictionary['second'])


dictionary = {'k1': [1, 2, 3]}
print(dictionary['k1'])
print(dictionary['k1'][0])


dictionary = {'k1': {'innerkey': [1, 2, 3]}}
print(dictionary['k1']['innerkey'])
print(dictionary['k1']['innerkey'][1])


boolean = True
print(boolean)


boolean = False
print(boolean)


tuple = (1, 2, 3)
print(tuple[0])

# Tuples cannot be re-assigned, the following throws an error:
# tuple[0] = 5


s = {1, 2, 3}
print(s)


s = {1, 1, 1, 2, 2, 3, 2, 1, 2, 3}
print(s)


s = set([1, 1, 2, 2, 6, 6, 5, 5, 4, 4, 3, 3])
print(s)


print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 != 2)
print('hi' == 'bye')
print('hi' != 'bye')

print((1 < 2) and (2 < 3))
print((1 < 2) and (2 > 3))
print((1 < 2) or (2 < 3))
print((1 < 2) or (2 > 3))
print((1 > 2) or (2 > 3))


if 1 < 2:
    print("Yes, 1 is less than 2")

if 1 > 2:
    print("This will not show")

if (1 < 2) and (2 < 3):
    print("Perform this code")

if 1 == 2:
    print('You should not see this.')
else:
    print('First condition failed.')

if 1 == 2:
    print('First')
elif 3 == 3:
    print('Middle')
else:
    print('Last')

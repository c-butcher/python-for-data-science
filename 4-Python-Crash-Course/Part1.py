question = "1 + 1 = %d"
answer = 1 + 1
print(question % answer)


question = "1 * 3 = %d"
print(question % answer)


question = "1 / 2 = %f"
answer = 1 / 2
print(question % answer)


question = "2^4 = %d"
answer = 2 ** 4
print(question % answer)


question = "5 modulus 2 = %d"
answer = 5 % 2
print(question % answer)


x = 2
y = 3
question = "x * y = %d"
answer = x * y
print(question % answer)


single = 'single quote'
double = "double quotes"
mixed = "mixed 'quote' string"
print(single)
print(double)
print(mixed)


num = 12
name = 'Sam'
string = 'My number is {} and my name is {}'.format(num, name)
print(string)


string = 'My number is {one} and my name is {two}, more {one}'.format(one=num, two=name)
print(string)


string = "hello"
print(string[4])


string = 'abcdefghijk'
print(string[0:])
print(string[:3])
print(string[3:6])


list = [1, 2, 3]
list.append(4)
print(list[1:3])


nested = [1, 2, [3, 4]]
print(nested[2][1])


nested = [1, 2, 3, [4, 5, ['target']]]
print(nested[3][2][0])


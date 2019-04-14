sequence = [1, 2, 3, 4, 5]
for number in sequence:
    print("Number - %d" % number)


i = 1
while i <= 5:
    print("Number is %d" % i)
    i += 1


for number in range(1, 6):
    print("Number %d in range" % number)


inputs = list(range(1, 5))
output = []

for number in inputs:
    output.append(number ** 2)

print(output)


output = [num ** 2 for num in inputs]
print(output)


def my_function(name='Nobody'):
    print("Hello %s" % name)


my_function("Chris")
my_function()


def square(num: int):
    """
    This function squares the supplied number.
    :param num:
    :return:
    """
    return num ** 2


output = square(2)
print(output)



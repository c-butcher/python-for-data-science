print('-- What is 7 to the power of 4?')
print(7**4)
print()

print('-- Split this string into a list ... "Hi there Sam!"')
str = "Hi there Sam!"
print(str.split())
print()

print("-- Given the variables, use .format() to print a string \"The diameter of Earth is 12742 kilometers.\"")
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))
print()

print("-- Given this nested list, use indexing to grab the word \"hello\"")
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2])
print()

print("-- Given this nested dictionary grab the word \"hello\".")
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
print()

print("-- What is the main difference between a tuple and a list?")
print("Tuples are immutable (can't be modified)")
print()


print('-- Create a function that grabs the email website domain from a string in the form')


# user@domain.com
def domainGet(email):
    return email.split('@')[1]


print(domainGet('user@domain.com'))
print()


print('-- Create a basic function that returns True if the word \'dog\' is contained in the input string.')


def findDog(sentence: str):
    return sentence.lower().count('dog') > 0


print(findDog('Is there a dog here?'))
print()


print('-- Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.')


def countDog(sentence: str):
    return sentence.lower().count('dog')


print(countDog('This dog runs faster than the other dog dude!'))
print()


print("-- Use lambda expressions and the filter() function to filter out words from a list that")
print("-- don't start with the letter 's'")
sequence = ['soup', 'dog', 'salad', 'cat', 'great']
print(list(filter(lambda word: word.lower()[0] == 's', sequence)))
print()

print('-- You are driving a little too fast, and a police officer stops you.')
print('-- Write a function to return one of 3 possible results: "No ticket",')
print('-- "Small ticket", or "Big Ticket". If your speed is 60 or less, the result')
print('-- is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket"')
print('-- If speed is 81 or more, the result is "Big Ticket".')
print('-- On your birthday, your speed can be 5 higher in all cases')


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed >= 81:
        return "Big Ticket"
    elif speed >= 61:
        return "Small Ticket"
    else:
        return "No Ticket"


print(caught_speeding(81, True))
print(caught_speeding(81, False))
print(caught_speeding(61, True))
print(caught_speeding(61, False))

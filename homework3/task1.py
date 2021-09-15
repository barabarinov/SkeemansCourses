#1
number = str(input("Input number: "))
rev_number = number[::-1]
print(rev_number)

#2
mystr = str(input("Please write something: "))
print(mystr[::-1])

#3
my_int = int(input("Input number: "))
my_str = 'somestring'
if my_int % 2 == 0:
    print(my_str[::-1])
else:
    print(my_str.upper())

# for i in l:
#     print(i)
# height = 3
# for i in range(height):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(height - i):
#         print("*", end=" ")
#     print()

# start, end, step = 3, -1, -1
# i = start
# while i != end - 1:
#     for j in range(i):
#         print("*", end=" ")
#     print()
#     i += step

# height = int(input("Input height of triangle: "))
# for i in range(height):
#     print(" " * (height - i - 1), end="")
#     print("* " * (i + 1))

# height = 3
# for i in range(height):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# height = 3
# for i in range(height, -1, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(4):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()

#4
# Quiz
points = 0
print("""Let's start!
Solve the equation:""")
print()
answer_one = int(input('2 * 4 = '))
if answer_one == 8:
    print("That's right")
    points = points + 1
else:
    print('This is the wrong result. Result is 8.')

answer_two = int(input('100 / 20 = '))
if answer_two == 5:
    print("Awesome")
    points = points + 1
else:
    print('This is the wrong result. Result is 5.')

answer_three = float(input('9 / 4 = '))
if answer_three == 2.25:
    print("You are a Genious!!!")
    points = points + 1
else:
    print('Sorry man, but this is the wrong result. Result is 2.25.')

answer_four = int(input('7 * 8 = '))
if answer_four == 56:
    print("Great! You are smart guy!!!")
    points = points + 1
else:
    print('No no no. Result is .')

answer_five = int(input('8 * 9 = '))
if answer_five == 72:
    print('Correct')
    points = points + 1
else:
    print('Wrong answer')

print(f'Correct answers = {points}')
wrong_answers = 5 - points
print(f'Wrong answers = {wrong_answers}')

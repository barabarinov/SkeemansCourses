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
    print('No no no. Result is 56.')

answer_five = int(input('8 * 9 = '))
if answer_five == 72:
    print('Correct')
    points = points + 1
else:
    print('Wrong answer')

print(f'Correct answers = {points}')
wrong_answers = 5 - points
print(f'Wrong answers = {wrong_answers}')
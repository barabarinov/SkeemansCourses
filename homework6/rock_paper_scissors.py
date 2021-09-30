import random

# rock paper scissors
value = ['ROCK', 'SCISSORS', 'PAPER']
a, b, c = 'ROCK', 'PAPER', 'SCISSORS'
print('ROCK, PAPER & SCISSORS')
while True:
    choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ')
    choice = choice.upper()
    if choice not in value:
        print('Wrong value!')
        continue
    else:
        print('\nYOU: ' + choice)
        new_value = random.choice(value)
        print(f'COMPUTER: ' + new_value)
    # WINBLOCK
    if choice == 'PAPER':
        if new_value == 'ROCK':
            print('You won! Congrats')
        elif new_value == 'SCISSORS':
            print('You lose! But that\'s okay!')

    if choice == 'ROCK':
        if new_value == 'SCISSORS':
            print('You won! Congrats')
        elif new_value == 'PAPER':
            print('You lose! Sorry bro!')

    if choice == 'SCISSORS':
        if new_value == 'PAPER':
            print('You won! Congrats')
        elif new_value == 'ROCK':
            print('Oops! You lose! Well, don\'t be discouraged!')

    if choice == new_value:
        print('Tie, try again')
        continue
    else:
        ask = input('Would you like to play again?')
        ask = ask.upper()
        if ask == 'YES':
            continue
        elif ask == 'NO':
            print('See ya!')
            break
        else:
            print('Wrong value')
            break

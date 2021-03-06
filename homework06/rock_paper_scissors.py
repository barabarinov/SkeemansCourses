import random
# ROCK, PAPER & SCISSORS
game_values = ['rock', 'scissors', 'paper']
print('ROCK, PAPER & SCISSORS')
while True:
    players_choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ').lower()
    if players_choice not in game_values:
        print('Wrong value!')
        continue
    else:
        print('\nYOU: ' + players_choice)
        computer_choice = random.choice(game_values)
        print(f'COMPUTER: ' + computer_choice)

    if players_choice == computer_choice:
        print('Tie, try again')
        continue

    if players_choice == 'paper':
        if computer_choice == 'rock':
            print('You won! Congrats')
        elif computer_choice == 'scissors':
            print('You lose! But that\'s okay!')

    elif players_choice == 'rock':
        if computer_choice == 'scissors':
            print('You won! Congrats')
        elif computer_choice == 'paper':
            print('You lose! Sorry bro!')

    elif players_choice == 'scissors':
        if computer_choice == 'paper':
            print('You won! Congrats')
        elif computer_choice == 'rock':
            print('Oops! You lose! Well, don\'t be discouraged!')

    ask = input('Would you like to play again? ').lower()
    if ask == 'yes':
        continue
    else:
        print('See ya!')
        break

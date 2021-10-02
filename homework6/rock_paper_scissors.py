import random

# rock paper scissors
game_values = ['ROCK', 'SCISSORS', 'PAPER']
print('ROCK, PAPER & SCISSORS')
while True:
    players_choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ').upper()
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

    if players_choice == 'PAPER':
        if computer_choice == 'ROCK':
            print('You won! Congrats')
        elif computer_choice == 'SCISSORS':
            print('You lose! But that\'s okay!')

    if players_choice == 'ROCK':
        if computer_choice == 'SCISSORS':
            print('You won! Congrats')
        elif computer_choice == 'PAPER':
            print('You lose! Sorry bro!')

    if players_choice == 'SCISSORS':
        if computer_choice == 'PAPER':
            print('You won! Congrats')
        elif computer_choice == 'ROCK':
            print('Oops! You lose! Well, don\'t be discouraged!')

    ask = input('Would you like to play again? ').upper()
    if ask == 'YES':
        continue
    else:
        print('See ya!')
        break

#ВАРИАНТ КОНЦОВКИ С ЦИКЛОМ
# ask = input('Would you like to play again? ').upper()
# while (ask != 'YES') and (ask != 'NO'):
#     print('Wrong value')
#     ask = input('Would you like to play again? ').upper()
# if ask == 'YES':
#     continue
# elif ask == 'NO':
#     print('See ya!')
#     break
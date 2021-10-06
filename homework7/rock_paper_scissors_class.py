import my_random

class Rock_Paper_Scissors:

    def __init__(self, game_values,):
        self.game_values = game_values ['rock', 'scissors', 'paper']

        # print('ROCK, PAPER & SCISSORS')
    def choices_of_players(self):
        while True:
            players_choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ').lower()
            if players_choice not in game_values:
                print('Wrong value!')
                continue
            else:
                print('\nYOU: ' + players_choice)
                computer_choice = my_random.choice(game_values)
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


#ВАРИАНТ КОНЦОВКИ С ЦИКЛОМ1
# ask = input('Would you like to play again? ').lower()
# while (ask != 'yes') and (ask != 'no'):
#     print('Wrong value')
#     ask = input('Would you like to play again? ').lower()
# if ask == 'yes':
#     continue
# elif ask == 'no':
#     print('See ya!')
#     break

#ВАРИАНТ КОНЦОВКИ С ЦИКЛОМ2
# is_exit = False
# while True:
#     inp = input('Do you want to play again?').lower()
#     if inp in ['yes', 'no']:
#         is_exit = inp == 'no'
#         break
# if is_exit:
#     break
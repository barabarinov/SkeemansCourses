import random

def choices_of_players():
    game_values = ['rock', 'scissors', 'paper']
    while True:
        players_choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ').lower()
        if players_choice not in game_values:
            print('Wrong value!')
            continue
        else:
            print('\nYOU: ' + players_choice)
            computers_choice = random.choice(game_values)
            print(f'COMPUTER: ' + computers_choice)
        return players_choice, computers_choice

def dead_heat(players_choice, computers_choice):
    while True:
        if players_choice == computers_choice:
            print('Tie, try again')
            players_choice, computers_choice = choices_of_players()
        else:
            return players_choice, computers_choice

def game_progress(players_choice, computers_choice):
    if players_choice == 'paper':
        if computers_choice == 'rock':
            return 'You won! Congrats'
        elif computers_choice == 'scissors':
            return 'You lose! But that\'s okay!'

    elif players_choice == 'rock':
        if computers_choice == 'scissors':
            return 'You won! Congrats'
        elif computers_choice == 'paper':
            return 'You lose! Sorry bro!'

    elif players_choice == 'scissors':
        if computers_choice == 'paper':
            return 'You won! Congrats'
        elif computers_choice == 'rock':
            return 'Oops! You lose! Well, don\'t be discouraged!'

def repeat_or_end():
    while True:
        inp = input('Do you want to play again?').lower()
        if inp in 'yes':
            return 'yes'
        elif inp in 'no':
            print('See ya!')
            exit()
    # ask = input('Would you like to play again? ').lower()
    # if ask == 'yes':
    #     choices_of_players()
    # else:
    #     print('See ya!')
    #     exit()

def main():
    print('ROCK, PAPER & SCISSORS')
    while True:
        players_selection, computers_selection = choices_of_players()
        players_selection, computers_selection = dead_heat(players_selection, computers_selection)
        result = game_progress(players_selection, computers_selection)
        print(result)
        repeat_or_end()


if __name__ == '__main__':
    main()

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
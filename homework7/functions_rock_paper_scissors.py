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

def is_won(players_choice, computers_choice):
    if players_choice == 'paper':
        if computers_choice == 'rock':
            return True
        elif computers_choice == 'scissors':
            return False

    elif players_choice == 'rock':
        if computers_choice == 'scissors':
            return True
        elif computers_choice == 'paper':
            return False

    elif players_choice == 'scissors':
        if computers_choice == 'paper':
            return True
        elif computers_choice == 'rock':
            return False

def is_repeat():
    while True:
        inp = input('Do you want to play again? ').lower()
        return inp == 'yes'

def main():
    print('ROCK, PAPER & SCISSORS')
    while True:
        players_selection, computers_selection = choices_of_players()
        players_selection, computers_selection = dead_heat(players_selection, computers_selection)
        if is_won(players_selection, computers_selection):
            print('You won! Congrats')
        else:
            print('Oops! You lose! Well, don\'t be discouraged!')
        if is_repeat():
            continue
        else:
            exit('See ya!')

if __name__ == '__main__':
    main()
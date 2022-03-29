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


def dead_heat():
    while True:
        players_choice, computers_choice = choices_of_players()
        if players_choice != computers_choice:
            break
        print('Tie, try again')
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
    return input('Do you want to play again? ').lower() == 'yes'


def main():
    print('ROCK, PAPER & SCISSORS')
    while True:
        players_selection, computers_selection = dead_heat()
        if is_won(players_selection, computers_selection):
            print('You won! Congrats')
        else:
            print('Oops! You lose! Well, don\'t be discouraged!')
        if is_repeat():
            continue
        else:
            return print('See ya!')


if __name__ == '__main__':
    main()

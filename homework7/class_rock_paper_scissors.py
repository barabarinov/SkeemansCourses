import random

class RockPaperScissors:
    game_values = ['rock', 'scissors', 'paper']

    def __init__(self, tie = 0):
        self.tie = tie

    def choices_of_players(self):
        while True:
            print(f'Ties: {self.tie}')
            players_choice = input('You can choose: Rock, Paper or Scissors. Make your choice!: ').lower()
            if players_choice not in self.game_values:
                print('Wrong value!')
                continue
            else:
                print('\nYOU: ' + players_choice)
                computers_choice = random.choice(self.game_values)
                print(f'COMPUTER: ' + computers_choice)
            return players_choice, computers_choice

    def dead_heat(self):
        while True:
            players_choice, computers_choice = self.choices_of_players()
            if players_choice != computers_choice:
                break
            print('Tie, try again')
            self.tie += 1
        return  players_choice, computers_choice

    def is_won(self, players_choice, computers_choice):
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

    def is_repeat(self):
        inp = input('Do you want to play again? ').lower()
        return inp == 'yes'

    def run(self):
        print('ROCK, PAPER & SCISSORS')
        while True:
            players_selection, computers_selection = self.dead_heat()
            if self.is_won(players_selection, computers_selection):
                print('You won! Congrats')
            else:
                print('Oops! You lose! Well, don\'t be discouraged!')
            if self.is_repeat():
                continue
            else:
                exit('See ya!')

if __name__ == '__main__':
    RockPaperScissors = RockPaperScissors()
    RockPaperScissors.run()
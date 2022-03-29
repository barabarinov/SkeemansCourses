import random


class Dice:
    def __init__(self):
        ...

    def get_target(self, amount_of_dices):
        while True:
            target = int(input("Choose your target: "))
            if amount_of_dices <= target <= amount_of_dices * 6:
                return target
            print("INCORRECT TARGET")

    def is_won(self, amount_of_dices, target):
        dices = [random.randrange(1, 7) for i in range(amount_of_dices)]
        print("ROLLED DICES:", dices)
        return sum(dices) == target

    def is_repeat(self):
        return input('Do you want to play again? ').lower() == 'yes'

    def run(self):
        amount_of_dices = int(input("Choose amount of dices: "))
        while True:
            target = self.get_target(amount_of_dices)
            if self.is_won(amount_of_dices, target):
                print("YOU WON")
            else:
                print("TRY AGAIN")
                continue
            if self.is_repeat():
                amount_of_dices = int(input("Choose amount of dices: "))
            else:
                print('GOODBYE')
                break


if __name__ == '__main__':
    Dice = Dice()
    Dice.run()

import random


def is_target(amount_of_dices):
    while True:
        target = int(input("Choose your target: "))
        if amount_of_dices <= target <= amount_of_dices * 6:
            return target
        print("INCORRECT TARGET")

def is_won(amount_of_dices, target):
        dices = [random.randrange(1, 7) for i in range(amount_of_dices)]
        # for i in range(amount_of_dices):
        #     dices.append(random.randrange(1, 7))
        print("ROLLED DICES:", dices)
        return sum(dices) == target

def is_repeat():
    return input('Do you want to play again? ').lower() == 'yes'

def main():
    amount_of_dices = int(input("Choose amount of dices: "))
    while True:
        target = is_target(amount_of_dices)
        if is_won(amount_of_dices, target):
            print("YOU WON")
        else:
            print("TRY AGAIN")
            continue
        if is_repeat():
            amount_of_dices = int(input("Choose amount of dices: "))
            continue
        else:
            print('GOODBYE')
            break

if __name__ == '__main__':
    RockPaperScissors = RockPaperScissors()
    RockPaperScissors.run()
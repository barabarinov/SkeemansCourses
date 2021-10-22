import random

def get_target(amount_of_dices):
    while True:
        target = int(input("Choose your target: "))
        if amount_of_dices <= target <= amount_of_dices * 6:
            return target
        print("INCORRECT TARGET")

def is_won(amount_of_dices, target):
        dices = [random.randrange(1, 7) for i in range(amount_of_dices)]
        print("ROLLED DICES:", dices)
        return sum(dices) == target

def is_repeat():
    return input('Do you want to play again? ').lower() == 'yes'

def main():
    amount_of_dices = int(input("Choose amount of dices: "))
    while True:
        target = get_target(amount_of_dices)
        if is_won(amount_of_dices, target):
            print("You won!")
            if is_repeat():
                main()
                break
            else:
                print('Goodbye!')
                break
        else:
            print("Try again!")

if __name__ == '__main__':
    main()
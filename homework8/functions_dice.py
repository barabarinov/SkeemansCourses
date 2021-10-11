import random

def is_amount_and_target():
    amount_of_dices = int(input("Choose amount of dices: "))
    while True:
        target = int(input("Choose your target: "))
        if amount_of_dices <= target <= amount_of_dices * 6:
            return amount_of_dices, target
        print("INCORRECT TARGET\n")

def is_won(amount_of_dices, target):
        dices = []
        for i in range(amount_of_dices):
            dices.append(random.randrange(1, 7))
        print("ROLLED DICES:", dices)
        if sum(dices) == target:
            return True
        else:
            return False

def is_repeat():
    answer = input('Do you want to play again? ').lower()
    return answer == 'yes'

def main():
    while True:
        amount_of_dices, target = is_amount_and_target()
        if is_won(amount_of_dices, target):
            print("YOU WON")
            break
        else:
            print("TRY AGAIN")
        if is_repeat():
            continue
        else:
            print('GOODBYE')
            break

if __name__ == '__main__':
    main()
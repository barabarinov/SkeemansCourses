import random
from termcolor import colored


def add_link(links):
    number = list(range(10))
    random.shuffle(number)
    original_url = input('Enter your url' + colored('> ', 'green'))
    short_name = None
    while not short_name or short_name in links:
        short_name = "https://short.com/{}".format(''.join(map(str, number[:6])))
        if short_name in links:
            print('This name already exist!')
    links[short_name] = original_url
    print(f"Your short link" + colored('> ', 'green') + short_name)


def get_link(links):
    name= input('Enter short link' + colored('> ', 'green'))
    url = links.get(name, None)

    if url:
        print(url)
    else:
        print('Link does not exist!')


def main():
    links = dict()

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input(colored('> ', 'green'))
        if choice == '1':
            add_link(links)
        elif choice == '2':
            get_link(links)
        elif choice == '3':
            break
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()

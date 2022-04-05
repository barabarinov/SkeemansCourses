import time
from termcolor import colored

phrases = ['Wake up, Neo...',
           'The Matrix has you',
           'Follow the white rabbit.',
           'Knock, knock, Neo.']
for phrase in phrases:
    time.sleep(3)
    for letter in phrase:
        print(colored(letter, 'green'), end='')
        time.sleep(0.2)
    time.sleep(4)
    print(end='\r')

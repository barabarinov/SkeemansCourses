def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        amount = len(names) - 2
        return f'{names[0]}, {names[1]} and {amount} others like this'


print(likes(['Jacob', 'Kate', 'Josh', 'Will', 'Ksyusha', 'Ded', 'Moroz']))


def likes_likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes_likes([]))
print(likes_likes(["Max", "John"]))
print(likes_likes(["Max", "John", "Mark"]))
print(likes_likes(["Max", "John", "Mark"]))
print(likes_likes(["Alex", "Jacob", "Mark", "Max"]))

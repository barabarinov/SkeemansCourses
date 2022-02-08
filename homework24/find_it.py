from collections import defaultdict


def find_it(seq):
    amounts = defaultdict(int)
    for i in seq:
        amounts[i] += 1
    return [k for k, v in amounts.items() if v % 2 == 1][0]


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


def find_if_two(seq):
    amounts = {}
    for i in seq:
        amounts[seq.count(i)] = i
    return [v for k, v in amounts.items() if k%2 == 1][0]


# print(find_if_two([7, 5, 7, 5, 7]))

def find_it_three(seq):
    seen = set()
    for i in seq:
        if i not in seen:
            seen.add(i)
        else:
            seen.remove(i)
    return seen.pop()


print(find_it_three([7, 5, 7, 5, 7]))

def fobonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = 6
for fib in fobonacci(count):
    print(fib)

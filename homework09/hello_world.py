def hello(name):
    return f'Hello, {name.capitalize()}!' if name.strip() else f'Hello, World!'

name = ' '
print(hello(name))

def hello_second(name):
    if name.strip(''):
        return f'Hello, {name.title().strip()}!'
    return f'Hello, World!'

print(hello_second('Justy smith'))
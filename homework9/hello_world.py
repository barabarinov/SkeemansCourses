def hello(name):
    return f'Hello, {name.capitalize()}!' if name.strip() else f'Hello, World!'

name = 'Justin'
print(hello(name))

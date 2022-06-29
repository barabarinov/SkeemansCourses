array = [[] for i in range(1000)]
key = 'kyiv'
value = 2000000

values = array[hash(key) % len(array)]
print(f'values {values}')
print(f'{array[hash(key) % len(array)]}')

array[hash(key) % len(array)].append((key, value))

for k, v in values:
    if k == key:
        print(f'key={k}, value={v}')

print(array)

def string_clean(s):
    return ''.join(char for char in s if not char.isdigit())


print(string_clean("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"))
print('My "messy" data issues! Will they ever, ever be solved?')

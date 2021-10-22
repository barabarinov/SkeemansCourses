def abbrev_name(name):
    name = name.split()
    return f'{name[0][0]}.{name[1][0]}'.upper()

name = 'patrick feenan'
print(abbrev_name(name))

def abbrevName(name):
    return name.split()[0][0].upper() + '.' + name.split()[1][0].upper()

print(abbrevName('Jordan Rakei'))
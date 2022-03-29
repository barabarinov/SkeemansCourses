def bumps(road):
    counter = len([i for i in road if i == 'n'])
    return 'Car Dead' if counter > 15 else 'Whoohoo!'


print(bumps('_n_n_n_n_n_n_n_n_n_n_n_n_n'))


def bumps2(road):
    return 'Car Dead' if road.count('n') > 15 else 'Whoohoo!'


print(bumps2('_n_n_n_n_n_n_n_n_n_n_n_n_n_n_n'))

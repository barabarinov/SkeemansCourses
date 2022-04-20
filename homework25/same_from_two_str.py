def same_letters(string1, string2):
    return set(string1) & set(string2)

# & Вертає символи, що є в обох сетах.
# | Вертає усі унікальні символи з двох сетів.
# ^ Вертає різницю двох сетів. Тобто унікальні символи кожного сета.
# - Вертає усі символи які є у string1 і немає у string2


# print(same_letters('Programming', 'Drumming'))

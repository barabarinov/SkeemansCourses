class Book:
    def __init__(self, name, author, published_date, genre):
        self.name = name
        self.author = author
        self.published_date = published_date
        self.genre = genre

    def __repr__(self):
        return f'Book: {self.name}, Author: {self.author}, Published date: {self.published_date}, Genre: {self.genre}'

    def __str__(self):
        return f'Book: {self.name}, Author: {self.author}, Published date: {self.published_date}, Genre: {self.genre}'

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.published_date == other.published_date and self.genre == other.genre


def main():
    book1 = Book('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 'novel')
    book2 = Book('The Sea Wolf', 'Jack London', 1904, 'novel')
    book3 = Book('Кобзар', 'Тарас Шевченко', 1840, 'поезія')
    book4 = Book('Захар Беркут', 'Іван Франко', 1883, 'історична повість')

    print(book1)
    print(book2)
    print(book3)
    print(book4)


if __name__ == '__main__':
    main()

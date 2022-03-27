import datetime
from datetime import date
import enum


class Genres(enum.Enum):
    NOVEL = 'Novel'
    POETRY = 'Poetry'
    HISTORICAL_FICTION = 'Historical Fiction'


class Book:
    def __init__(self, name: str, author: str, published_year: date, genre: Genres):
        self.name = name
        self.author = author
        self.published_year = published_year
        self.genre = genre
        self.review_list = []

    def __repr__(self):
        return f'Book: {self.name}, Author: {self.author}, Published date: {self.published_year.isoformat()}, Genre: {self.genre.value}'

    def __str__(self):
        return f'Book: {self.name}, Author: {self.author}, Published date: {self.published_year.isoformat()}, Genre: {self.genre.value}'

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.published_year == other.published_year and self.genre == other.genre

    def add_review(self, user: str, text: str, time: datetime):
        self.review_list.append(Review(user, text, time))

    def book_info(self):
        for review in self.review_list:
            print(f'Review of "{self.name}" by: {review.user}. Text: {review.text} Time of Creation: {review.time}')


class Review:
    def __init__(self, user: str, text: str, time: datetime):
        self.user = user
        self.text = text
        self.time = time # datetime.datetime.strftime('%H:%M  %d/%m/%Y')

    def __str__(self):
        return f'Reviev by: {self.user}. Text: {self.text} time of creation: {self.time}'


def main():
    book1 = Book('Crime and Punishment', 'Fyodor Dostoevsky', datetime.date.fromisoformat('1866-01-07'), Genres.NOVEL)
    book2 = Book('The Sea Wolf', 'Jack London', datetime.date.fromisoformat('1904-12-02'), Genres.NOVEL)
    book3 = Book('Kobzar', 'Taras Shevchenko', datetime.date.fromisoformat('1840-09-28'), Genres.POETRY)
    book4 = Book('Zahar Berkut', 'Ivan Franko', datetime.date.fromisoformat('1883-06-17'), Genres.HISTORICAL_FICTION)
    book1.add_review('barinovman', 'This book is super great! I like it!', datetime.datetime.now())
    book3.add_review('VladLyt', 'My favorite poetry book! Love it! 🇺🇦', datetime.datetime.now())

    print(book1)
    print(book2)
    print(book3)
    print(book4)
    print(book1.book_info())


if __name__ == '__main__':
    main()

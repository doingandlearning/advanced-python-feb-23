from .bookshelf import Bookshelf
from .book import Book


def write_demo_file():
    # Write to file

    great_python_books_bookshelf = Bookshelf(
        Book("Automate the Boring Stuff with Python", "Al Sweigart", 592, 592),
        Book("Doing Math with Python", "Amit Saha", 264, 100),
        Book("Black Hat Python", "Justin Seitz", 192, 0),
        Book("Serious Python", "Julien Danjou", 240, 200),
        Book("Real-World Python", "Lee Vaughan", 370, 370),
    )

    with open('mybookshelf.shlf', 'bw') as file:
        great_python_books_bookshelf.write_to_stream(file)


def read_demo_file():
    with open('mybookshelf.shlf', 'br') as file:
        bookshelf = Bookshelf.from_stream(file)

    for book in bookshelf:
        print(book.title)


if __name__ == "__main__":
    # write_demo_file()
    read_demo_file()

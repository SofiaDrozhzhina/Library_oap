class Book:
    def __init__(self, title, author, genre,year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, Жанр: {self.genre},Год: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre,year):
        book = Book(title, author, genre,year)
        self.books.append(book)
        print("Книга добавлена в каталог.")

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Книга удалена из каталога.")
                return
        print("Книга не найдена.")

    def search_books(self, keyword):
        results = [book for book in self.books if
                   keyword.lower() in book.title.lower() or
                   keyword.lower() in book.author.lower() or
                   keyword.lower() in book.genre.lower() or
                   str(book.year).lower() in keyword.lower()]
        if results:
            print("Найденные книги:")
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")

    def view_books(self):
        if not self.books:
            print("Каталог пуст.")
        else:
            print("Каталог книг:")
            for book in self.books:
                print(book)

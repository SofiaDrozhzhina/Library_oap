from Classes import Library

def main():
    library = Library()
    print("Здравствуйте! Добро пожаловать в библиотеку!")
    while True:
        print("\nДоступные команды:")
        print("1 - Добавить книгу")
        print("2 - Удалить книгу")
        print("3 - Найти книгу")
        print("4 - Просмотреть все книги")
        print("5 - Выход")
        command = input("Введите номер команды: ")

        if command == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            genre = input("Введите жанр: ")
            year = input("Введите год: ")
            library.add_book(title, author, genre,year)
        elif command == "2":
            title = input("Введите название книги для удаления: ")
            library.delete_book(title)
        elif command == "3":
            keyword = input("Введите ключевое слово для поиска (название, автора, жанр или год): ")
            library.search_books(keyword)
        elif command == "4":
            library.view_books()
        elif command == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверная команда. Попробуйте снова.")


